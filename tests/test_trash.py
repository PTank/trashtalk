from tests.init_test import generate_trash, list_files, list_files_size
from pathlib import Path


def test_path_name(generate_trash):
    trash = generate_trash
    trash.path = "test"
    assert str(trash) == "test"


def test_list(generate_trash, list_files):
    """
    test list_files from trash
    """
    trash = generate_trash
    # test all files in list_files
    for f in trash.list_files():
        assert f[0] in list_files

    # test one select file
    f = trash.list_files([list_files[2]])
    assert list(f)[0][0] == list_files[2]

    # test wrong file
    f = trash.list_files(['error.txt'])
    assert list(f)[0][0] == None


def test_size(generate_trash, list_files_size):
    """
    test list_files from trash with correct size in byte
    """
    trash = generate_trash
    for f in trash.list_files(size=True):
        assert f in list_files_size


def test_clean(generate_trash, list_files):
    """
    test all files are removed: /files and /info
    """
    trash = generate_trash
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



def test_restore():
    """
    test file are restore with the correct path
    """
    pass
