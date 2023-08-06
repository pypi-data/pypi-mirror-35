import os
import os.path as path
import zipfile
from .structures import PBO
from .utils import pbo_empty, pbo_files_add, find_files_index_by_filename

class PBOFile():
    def __init__(self, init_empty=True):
        if init_empty:
            self._pbo = pbo_empty()

    @classmethod
    def from_bytes(cls, data):
        """create PBOFile from data"""
        obj = PBOFile(init_empty=False)
        obj._pbo = PBO.parse(data)
        return obj

    @classmethod
    def from_file(cls, fn):
        """read .pbo file"""
        obj = PBOFile(init_empty=False)
        obj._pbo = PBO.parse_file(fn)
        return obj

    def to_file(self, fn):
        """write .pbo file"""
        open(fn, 'wb').write(self.as_bytes())

    def as_bytes(self):
        """build .pbo file bytes"""
        return PBO.build(self._pbo)

    @classmethod
    def from_zip(cls, fn):
        pbo = PBOFile()
        zf = zipfile.ZipFile(fn)
        # find all files and strip first component
        filelist = (('/'.join(fn.split('/')[1:]), fn) for fn in zf.namelist() if not fn.endswith('/'))
        for fn, zfn in filelist:
            pbo.add_file_data(fn, zf.read(zfn))
        return pbo

    def to_zip(self, fn):
        pass

    @classmethod
    def from_directory(cls, root):
        # maybe use .pboignore?
        os.chdir(root)
        fns = [os.path.join(dirpath, name)[2:] for dirpath, dirnames, filenames in os.walk('.') for name in filenames]
        fns.sort(key=lambda x:x.lower())

        obj = PBOFile()
        for fn in fns:
            obj.add_file(fn, fn)
        return obj

    def to_directory(self, root):
        for pbofn in self.filenames():
            *dirs, fn = pbofn.split('\\')
            os.makedirs(path.join(root, *dirs), exist_ok=True)
            fullfn = path.join(root, *dirs, fn)
            open(fullfn, 'wb').write(self.file_as_bytes(pbofn))

    def filenames(self):
        for h in self._pbo.header:
            if h.meta:
                continue
            yield(h.filename)

    def add_file(self, fn, data_fn):
        fn = fn.replace('/', '\\')
        pbo_files_add(self._pbo, fn, open(data_fn,'rb').read())

    def add_file_data(self, fn, data):
        fn = fn.replace('/', '\\')
        pbo_files_add(self._pbo, fn, data)

    def remove_file(self, fn):
        fn = fn.replace('/', '\\')
        pbo_remove_file(self._pbo, fn)

    def file_as_bytes(self, fn):
        fn = fn.replace('/', '\\')
        i = find_files_index_by_filename(self._pbo, fn)
        return self._pbo.files[i]
