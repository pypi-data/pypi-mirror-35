import arrow
import zipfile
from .structures import PBO
from construct import Container

def find_files_index_by_filename(pbo, fn):
        i = 0
        for header in pbo.header:
                if header.meta:
                        continue
                if header.filename == fn:
                        return i
                i += 1
        raise RuntimeError("Can't locate target file within pbo")


def find_header_index_by_filename(pbo, fn):
        for i, header in enumerate(pbo.header):
                if header.meta:
                        continue
                if header.filename == fn:
                        return i
        raise RuntimeError("Can't locate target file within pbo")


def pbo_empty():
    arrow_z = arrow.Arrow(1970, 1, 1, 0, 0, 0)
    pbo = PBO.parse(PBO.build(Container(
        fields=Container(value=Container(
            header=[
                Container(filename=u'.', method=0, originalsize=0, timestamp=arrow_z, datasize=0, meta=False, final=False, extended=False, extension=None),
                Container(filename=u'', method=0, originalsize=0, timestamp=arrow_z, datasize=0, meta=True, final=True, extended=False, extension=None)
            ],
            files=[b''],
        ))
    )))
    del(pbo.files[0])
    del(pbo.header[0])

# extented header
#    pbo.header.insert(0, Container(filename=u'', method=0, originalsize=0, timestamp=arrow_z, datasize=0, meta=True, final=False, extended=True, extension=['foo','bar','']))

    return pbo


def pbo_files_add(pbo, fn, data):
    arrow_z = arrow.Arrow(1970, 1, 1, 0, 0, 0)
    f = 0
    h = 0
    for header in pbo.header:
        if header.final:
            break
        if header.extended:
            h += 1
            continue
        if fn.lower() == header.filename.lower():
            raise RuntimeError('file already exists in pbo')
        if fn.lower() < header.filename.lower():
            break
        f += 1
        h += 1
    pbo.header.insert(h, Container(filename=fn, method=0, originalsize=0, timestamp=arrow_z, datasize=len(data), meta=False, final=False, extended=False, extension=None))
    pbo.files.insert(f, data)


def find_indexes_by_filename(pbo, fn):
    i = 0
    for h, header in enumerate(pbo.header):
        if header.meta:
            continue
        if header.filename == fn:
            return i, h
        i += 1
    raise RuntimeError("Can't locate target file within pbo")

def pbo_remove_file(pbo, fn):
    fi, hi = find_indexes_by_filename(pbo, fn)
    del(pbo.files[fi])
    del(pbo.header[hi])

def pbo_by_zip(fn):
    import zipfile
    pbo = pbo_empty()
    zf = zipfile.ZipFile(fn)
    # find all files and strip first component
    filelist = (('/'.join(fn.split('/')[1:]).replace('/', '\\'), fn) for fn in zf.namelist() if not fn.endswith('/'))
    for fn, zfn in filelist:
        pbo_files_add(pbo, fn, zf.read(zfn))
    return pbo
