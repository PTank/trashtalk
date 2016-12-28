from tests.init_test import (generate_trash, list_files,
                             list_files_size, trash_with_dir_and_files,
                             trash_with_files)
from pathlib import Path
from datetime import datetime
from trashtalk.exception import WrongFormat
from trashtalk.trash import Trash
import pytest


def test_path_name(generate_trash):
    trash = generate_trash
    trash.select_path("/test", "test")
    assert str(trash) == "/test"
    assert trash.name == "test"
    assert trash.info == "/test/info"
    assert trash.files == "/test/files"
    t = Trash()
    assert t.name == ""


def test_iter(trash_with_files, list_files):
    """
    test list_files from trash
    """
    trash = trash_with_files
    # test all files in list_files
    for f in trash:
        assert f[0] in list_files


def test_list(trash_with_files, list_files):
    """
    test list_files from trash
    """
    trash = trash_with_files
    # test all files in list_files
    for f in trash.list_files():
        assert f[0] in list_files

    # test one select file
    f = trash.list_files([list_files[2]])
    assert list(f)[0][0] == list_files[2]

    # test wrong file
    f = trash.list_files(['error.txt'])
    assert list(f)[0][0] == None


def test_size(trash_with_files, list_files_size):
    """
    test list_files from trash with correct size in byte
    """
    trash = trash_with_files
    for f in trash.list_files(size=True):
        assert f in list_files_size


def test_clean(list_files, trash_with_dir_and_files):
    """
    test all files are removed: /files and /info
    """
    trash = trash_with_dir_and_files
    list_files = list_files
    files = Path(trash.path) / "files"
    info = Path(trash.path) / "info"

    # test for one delete file
    one_file = list_files.pop()
    error = trash.clean([one_file])
    one_file_path = files / one_file
    assert one_file_path.exists() == False
    one_file_info = info / (one_file + ".trashinfo")
    assert one_file_info.exists() == False

    #test error
    error = trash.clean(['error_file'])
    assert type(error[0]) == str
    assert len(error) == 1

    # test all cleaning
    trash.clean()
    for f in list_files:
        file_path = files / f
        assert file_path.exists() == False
        file_info = info / (f + ".trashinfo")
        assert file_info.exists() == False

    # test dir cleaning
    dir_path = files / 'testdir'
    assert dir_path.exists() == False
    dir_info_path = info / 'testdir.trashinfo'
    assert dir_info_path.exists() == False



def test_remove(list_files, generate_trash):
    """
    test file are restore with the correct path
    """
    trash = generate_trash
    desk = Path(trash.path + '/../desk')

    # create files and dir
    test_dir = desk / "dir"
    test_dir.mkdir()
    new_path = [str(test_dir.absolute())]
    for f in list_files:
        new_file = desk / f
        new_file.touch()
        new_path.append(str(new_file.absolute()))
        new_file = test_dir / f
        new_file.touch()
    # use remove method
    trash.remove(new_path)
    # test
    now = datetime.now()
    trash_path = Path(trash.path)
    for path in new_path:
        p = Path(path)
        assert p.exists() == False
        assert (trash_path / "files" / p.name).exists() == True
        if p.name is not "dir":
            assert (Path(trash.path) / "files/dir" / p.name).exists() == True
        info = trash_path / "info" / (p.name + ".trashinfo")
        assert info.exists() == True
        with info.open(encoding="utf-8") as f:
            info_str = [i for i in f]
            assert info_str[0] == "[Trash Info]\n"
            assert info_str[1].split("=")[1][:-1] == path
            date = datetime.strptime(info_str[2].split('=')[1][:-1], "%Y-%m-%dT%H:%M:%S")
            assert now.year == date.year
            assert now.month == date.month
            assert now.day == date.day

    # test false info
    trash.remove(["/tmp/fakepath/nohing/arg.fail"])
    assert (trash_path / "files" / "arg.fail").exists() == False
    assert (trash_path / "info" / "arg.fail.trashinfo").exists() == False
    with pytest.raises(WrongFormat):
        trash.remove("string is not accepted")
