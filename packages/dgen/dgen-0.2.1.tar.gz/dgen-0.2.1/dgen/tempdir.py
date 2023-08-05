import os
import shutil
from . import settings


class TempDir(object):
    def __init__(self, dirname):
        self.dirname = dirname
        self.parent = os.getcwd()
        self.path = os.path.join(self.parent, dirname)

    def make(self):
        self.remove()
        os.mkdir(self.path)

    def remove(self):
        if os.path.isfile(self.path):
            os.unlink(self.path)
        elif os.path.isdir(self.path):
            shutil.rmtree(self.path)

    def copy_files(self, filenames, dst_path):
        for filename in filenames:
            src_path = os.path.join(self.path, filename)

            if not os.path.exists(dst_path):
                os.makedirs(dst_path)

            shutil.copy(src_path, dst_path)


tempdir = TempDir(settings.TEMPDIR)
