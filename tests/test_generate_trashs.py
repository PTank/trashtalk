from pathlib import Path
from trashtalk import generate_trashs


def test_add_profil_info(tmpdir):
    test_file = tmpdir.join('.trashtalk')
    s = "MEDIA_PATH=/testmediapath\nTRASH_PATH=/testtrashpath , bob"
    test_file.write(s)
    f = Path(str(test_file))
    generate_trashs.MEDIA_DIR = ['/media']
    generate_trashs.TRASHS_PATH = []
    generate_trashs.add_profil_info(f.open())
    assert generate_trashs.MEDIA_DIR == ['/media', '/testmediapath']
    assert generate_trashs.TRASHS_PATH == [('bob', '/testtrashpath')]
