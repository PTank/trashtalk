from __future__ import print_function
from collections import Iterable
try:
    from urllib.parse import quote, unquote
except:
    from urllib import quote, unquote
from pathlib import Path
from datetime import datetime
from shutil import move
from trashtalk.exception import WrongFormat

__all__ = ["Trash"]


class Trash():
    """This object is an implementation of posix trash

    Args:
        path: path to the trash
        name: name of this trash

    Example:
        >>> from trasktalk import Trash
        >>> trash = Trash("/path/to/trash", "mytrash")
        >>> for element in trash: # list all elements in this trash
        >>>     print(element)
            element1
            element2
    """

    def __init__(self, path=None, name=""):
        if path:
            self.select_path(path, name)
        else:
            self.name = name

    def select_path(self, path, name):
        """ Add path and name to this Trash

            Args:
                path: path to the trash
                name: name of this trash
        """
        self.path = path
        self.name = name
        self.info = str((Path(path) / 'info').absolute())
        self.files = str((Path(path) / 'files').absolute())

    def list_files(self, files=None, size=False, info=False):
        """Method to list files in trash

        can print size in byte with size
        if file doesn't exist return [None, 'error message']

        Args:
            files: list specific file, if param == None list all elements
            size: at true return size in byte with file name

        Returns:
            Generator list [filename], or [filename, size]
        """
        total = 0
        if not files:
            l = Path(self.files).iterdir()
        else:
            l = [(Path(self.files) / x) for x in files]
        for i in l:
            try:
                if not i.exists():
                    raise IOError("File: %s doesn't exist" % i.name)
                list_info_from_file = [i.name]
                if size:
                    list_info_from_file.append(i.lstat().st_size)
                    total += i.lstat().st_size
                if info:
                    i = (Path(self.info) / (i.name + ".trashinfo"))
                    if i.exists():
                        for line in list(i.open())[1:]:
                            try:
                                list_info_from_file.append(
                                    unquote(line.split('=')[1].strip()))
                            except:
                                list_info_from_file.append("unknow")
                yield list_info_from_file
            except Exception as e:
                yield [None, str(e)]
        if size:
            yield ["Total: ", total]

    def clean(self, list_files=None, path=None):
        """Method to clean files from trash

        :return: list of error message
        """
        error = []
        info = False
        if not path:
            info = True
            path = self.files
        if not list_files:
            l = Path(path).iterdir()
        else:
            l = [(Path(path) / x) for x in list_files]
        for i in l:
            try:
                if i.is_dir():
                    self.clean(path=(str(i)))
                    i.rmdir()
                else:
                    i.unlink()
                if info:
                    info = (Path(self.info) / (i.name + ".trashinfo"))
                    if info.exists():
                        info.unlink()
            except Exception as e:
                error.append(str(e))
        return error

    def remove(self, files_path=[]):
        """Move files in list_files to trash and built .trashinfo

           Returns:
               List of error

           Raises:
               WrongFormat: if files_path in args isn't iterable or is str
        """
        if type(files_path) == str or not isinstance(files_path, Iterable):
            raise WrongFormat('files_path must be an iterable')
        files = Path(self.files)
        files_in_trash = [x[0] for x in self.list_files()]
        error = []
        for file_path in files_path:
            old_path = Path(file_path)
            name = old_path.name
            while name in files_in_trash:
                i = 1
                name += str(i)
                i += 1
            if not old_path.exists():
                error.append("file %s doesn't exist" % old_path.name)
                continue
            info_path = (Path(self.info) / (name + '.trashinfo'))
            info_path.touch()
            move(str(old_path.absolute()), str(files) + '/' + name)
            with open(str(info_path.absolute()), "w") as o:
                o.write('[Trash Info]\n')
                o.write('Path=%s\n' % quote(str(old_path.absolute())))
                date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                o.write('DeletionDate=%s\n' % date)
        return error

    def restore(self, list_files):
        if type(list_files) is not list and type(list_files) is not tuple:
            raise WrongFormat()
        error = []
        files_dir = Path(self.files)
        info_dir = Path(self.info)
        for f in list_files:
            file_path = files_dir / f
            file_info = info_dir / (f + ".trashinfo")
            if not file_path.exists():
                error.append("file doesn't in %s trash" % self.name)
                continue
            if not file_info.exists():
                error.append(
                    "file doesn't have trahsinfo in %s trash" % self.name)
                continue
            with file_info.open() as o:
                i = list(o)
                old_path = i[1].split("Path=")[1][:-1]
                # move file to old path
                try:
                    move(unquote(str(file_path.absolute())), old_path)
                    file_info.unlink()
                except Exception as e:
                    error.append(str(e))
        return error

    def read_trashinfo(self, file_name):
        """Read from file_name.trashinfo in Trash/info

           Args:
                file_name: obviously name of the file from you want info

           Returns:
                Tuple : (path, datetime)

           Example:
                >>> trash.read_trashinfo("test.txt")
                ('/path/of/file/test.txt', '2016-12-29T00:37:15')
        """

    def __iter__(self):
        """Trash object iter on file in /files"""
        return self.list_files()

    def __str__(self):
        """Return path"""
        return "%s" % (self.path)
