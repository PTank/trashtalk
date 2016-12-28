from __future__ import print_function
from pathlib import Path
from datetime import datetime
from shutil import move

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
                if not i.exists():
                    raise IOError("File %s doesn't exist" % i.name)
                list_info_from_file = [i.name]
                if size:
                    list_info_from_file.append(i.lstat().st_size)
                yield list_info_from_file
                total += i.lstat().st_size
            except Exception as e:
                yield (None, e)
        if size:
            yield ["Total: ", total]

    def clean(self, list_files=None, path=None):
        """
        method to clean files from trash
        if file doesn't exist return 'error message'
        """
        error = []
        info = False
        if not path:
            info = True
            path = self.path + '/files/'
        if not list_files:
            l = Path(path).iterdir()
        else:
            l = map(lambda x: Path(path + x), list_files)
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
                error.append(str(e))
        return error

    def remove(self, list_files=[]):
        """
        move file in list_files to trash and built trashinfo
        """
        if type(list_files) is not list and type(list_files) is not tuple:
            # raise error
            return
        files = Path(self.path + '/files/')
        for f in list_files:
            old_path = Path(f)
            if not old_path.exists():
                continue
            info_path = Path(self.path+ '/info/' + old_path.name + '.trashinfo')
            info_path.touch()
            move(str(old_path.absolute()), str(files) + '/' + old_path.name)
            with info_path.open("w") as o:
                o.write('[Trash Info]\n')
                o.write('Path=%s\n' % str(old_path.absolute()))
                date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                o.write('DeletionDate=%s\n'% date)

    def __iter__(self):
        """
        Trash object iter on file in /files
        """
        return self.list_files()

    def __str__(self):
        return "%s" % (self.path)
