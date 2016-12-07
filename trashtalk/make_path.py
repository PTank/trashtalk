from __future__ import print_function, absolute_import
from trashtalk.trash import Trash
from pathlib import Path
from pwd import getpwnam
import sys


def get_home_trash(user):
    trashs = []
    path = Path("/home/" + user + "/.local/share/Trash")
    if path.exists():
        trashs.append((user, Trash(str(path))))
    else:
        print("can't find: " + path.name, file=sys.stderr)
    return trashs


def get_media_trash(user, media=[]):
    trashs = []
    if not media:
        media = Path("/media/" + user).iterdir()
    else:
        media = map(lambda x: Path("/media/%s/%s" % (user, x)), media)
    for m in media:
        if m.exists():
            t = m / (".Trash-" + str(getpwnam(user)[2]))
            if t.exists():
                trashs.append((m.name, Trash(str(t))))
            else:
                print("media " + m.name + "have no trash", file=sys.stderr)
        else:
            print("no media name: " + m.name, file=sys.stderr)
    return trashs

