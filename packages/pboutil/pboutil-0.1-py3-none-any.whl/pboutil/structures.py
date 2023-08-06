from construct import *
from datetime import datetime
import arrow
import hashlib

class TimestampAdapter(Adapter):
    def _decode(self, obj, context, path):
        return datetime.utcfromtimestamp(obj)

    def _encode(self, obj, context, path):
        if obj == datetime(1970, 1, 1, 0, 0):
            return 0
        else:
            return int(obj.timestamp())


# https://resources.bisimulations.com/wiki/PBO_File_Format

PBO_Header_Extended = RepeatUntil(lambda obj, lst, ctx: len(obj) == 0, CString("ascii"))

PBO_Header_Entry = Struct(
    "filename" / Default(CString("ascii"), ""),
    "method" / Enum(Int32ul, default=0, packed=0x43707273, extended=0x56657273) * "PackingMethod",
    "originalsize" / Int32ul * "OriginalSize",
    Const(0, Int32ul) * "Reserved",
    "timestamp" / Timestamp(Int32ul, 1, 1970) * "TimeStamp",  # or use TimestampAdapter(Int32ul) if you don't like Arrow,
    "datasize" / Int32ul * "DataSize",

    "i" / Computed(lambda ctx: ctx._index),
    "meta" / Computed(lambda ctx: len(ctx.filename) == 0),
    "final" / Computed(lambda ctx: ctx.i != 0 and len(ctx.filename) == 0),
    "extended" / Computed(lambda ctx: ctx.i == 0 and len(ctx.filename) == 0),

    "extension" / If(this.extended, PBO_Header_Extended),
)


class Files(Construct):
    def _parse(self, stream, context, path):
        obj = ListContainer()

        for header in context.header:
            if header.meta:
                continue
            if header.method.intvalue != 0:
                raise RuntimeError("can't extract files with method: 0x%x" % (header.method.intvalue,))
            e = Bytes(header.datasize)._parsereport(stream, context, path)
            obj.append(e)

        return obj

    def _build(self, obj, stream, context, path):
        retlist = ListContainer()
        i = 0
        for header in context.header:
            if header.meta:
                continue
            context._index = i
            buildret = Bytes(header.datasize)._build(obj[i], stream, context, path)
            retlist.append(buildret)
            i += 1
        return retlist


class PBOStruct(Struct):
    def _parse(self, stream, context, path):
        return super()._parse(stream, context, path)

    def _build(self, obj, stream, context, path):
        # adjust file sizes
        i = 0
        for header in obj.fields.value.header:
            if header.meta:
                continue
            header.datasize = len(obj.fields.value.files[i])
            i += 1

        filecount = len(obj.fields.value.files)

        if filecount != i:
            raise RuntimeError("not all files were processed, expected %d, processed %d" % (i, filecount))

        del(obj.fields['data'])

        return super()._build(obj, stream, context, path)


PBO = PBOStruct(
    "fields" / RawCopy(Struct(
        "header" / RepeatUntil(lambda obj, lst, ctx: obj.final is True, PBO_Header_Entry),
        "files" / Files(),
    )),
    "data_end" / Tell,
    Const(0, Byte) * "terminator",
    "sha1" / Checksum(Bytes(20), lambda data: hashlib.sha1(data).digest(), this.fields.data),
    Terminated,

    "header" / Computed(this.fields.value.header),
    "files" / Computed(this.fields.value.files),
)
