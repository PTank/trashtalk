from __future__ import print_function
from pathlib import Path


class Trash():

    def __init__(self, path=None):
        self.path = path

    def list_files(self, list_file=None, size=False):
        total = 0
        if not list_file:
            l = Path(self.path + '/files').iterdir()
        else:
            l = map(lambda x: Path(self.path + '/files/' + x), list_file)
        for i in l:
            try:
                s = i.name + ['', '\t' + str(i.lstat().st_size)][bool(size)]
                total += i.lstat().st_size
                print(s)
            except Exception as e:
                print(e)
        if size:
            print("Total:\t%d" % total)

    def clean(self, list_file=None, path=None):
        if not path:
            path = self.path + '/files'
        if not list_file:
            l = Path(path).iterdir()
        else:
            l = map(lambda x: Path(path + x), list_file)
        for i in l:
            try:
                if i.is_dir():
                    self.clean(path=(str(i)))
                    i.rmdir()
                else:
                    i.unlink()
            except Exception as e:
                print(e)

    def __str__(self):
        return "%s" % (self.path)
