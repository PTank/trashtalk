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
    return [['file1.txt', 4],
            ['file2.txt', 4],
            ['file3.txt', 4],
            ['file4.txt', 4],
            ['file5.txt', 4],
            ['Total: ', 20]
            ]


@pytest.fixture()
def generate_trash(tmpdir, list_files):
    d = tmpdir.mkdir('trash_test')
    files = tmpdir.mkdir('trash_test/files')
    info = tmpdir.mkdir('trash_test/info')
    tmp_desk = tmpdir.mkdir('desk')
    trash = Trash(str(d), 'trash_test')
    for f in list_files:
        files.join(f).write('osef')
        infostring = ('[Trash Info]\nPath=%s/%s\n'
                      'DeletionDate=Unknow\n') % (str(tmp_desk), f)
        info.join(f + '.trashinfo').write(infostring)
    return trash


@pytest.fixture()
def trash_with_dir(tmpdir, generate_trash, list_files):
    trash = generate_trash
    dir_test = tmpdir.mkdir(trash.name + '/files/testdir')
    info = tmpdir.join(trash.name + '/info')
    tmp_desk = tmpdir.join('desk')
    infostring = '[Trash Info]\nPath=%s/%s\nDeletionDate=Unknow\n' % (str(tmp_desk), 'testdir')
    info.join('testdir.trashinfo').write(infostring)
    for f in list_files:
        dir_test.join(f).write('osef')
    return trash
