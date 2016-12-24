from __future__ import print_function
from pathlib import Path

__all__ = ["Trash"]


class Trash():

    def __init__(self, path=None, name=""):
        self.path = path
        self.name = name

    def list_files(self, list_file=None, size=False):
        """
        method to list files in trash
        can print size in byte
        if file doesn't exist return (None, 'error message')
        """
        total = 0
        if not list_file:
            l = Path(self.path + '/files').iterdir()
        else:
            l = map(lambda x: Path(self.path + '/files/' + x), list_file)
        for i in l:
            try:
                yield (i.name, ['', i.lstat().st_size][bool(size)])
                total += i.lstat().st_size
            except Exception as e:
                yield (None, e)
        if size:
            yield ("Total: ", total)

    def clean(self, list_file=None, path=None):
        """
        method to clean files from trash
        if file doesn't exist return 'error message'
        """
        info = False
        if not path:
            info = True
            path = self.path + '/files/'
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
                if info:
                    info = Path(self.path + "/info/" + i.name + ".trashinfo")
                    if info.exists():
                        info.unlink()
            except Exception as e:
                yield str(e)

    def __str__(self):
        return "%s" % (self.path)
