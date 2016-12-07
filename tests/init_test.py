import pytest
from trashtalk import Trash


@pytest.fixture()
def list_files():
    return ['file1.txt',
            'file2.txt',
            'file3.txt',
            'file4.txt',
            'file5.txt'
            ]
@pytest.fixture()
def list_files_size():
    return [('file1.txt', 4),
            ('file2.txt', 4),
            ('file3.txt', 4),
            ('file4.txt', 4),
            ('file5.txt', 4),
            ('Total: ', 20)
            ]

@pytest.fixture()
def generate_trash(tmpdir, list_files):
    d = tmpdir.mkdir('trash_test')
    files = tmpdir.mkdir('trash_test/files')
    for f in list_files:
        files.join(f).write('osef')
    trash = Trash(str(d))
    return trash
