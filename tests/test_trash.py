from tests.init_test import generate_trash, list_files, list_files_size

def test_list(generate_trash, list_files):
    trash = generate_trash
    for f in trash.list_files():
        assert f[0] in list_files
        print(f)
    assert trash == trash


def test_size(generate_trash, list_files_size):
    trash = generate_trash
    for f in trash.list_files(size=True):
        print(f)
        assert f in list_files_size
    assert trash == trash
