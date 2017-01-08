from __future__ import print_function, absolute_import
from pwd import getpwnam
from os import getlogin
from pathlib import Path
from trashtalk.trash import Trash
import sys

"""
Module who generate trash

:Todo
rename file: generate_trash.py
remove class and make function
change this in core.py and autocomplete_bash.py
add better way of searching media or trash
"""

MEDIA_DIR = ['/media']
TRASHS_PATH = []

class TrashFactory():
    """
    """

    def create_trash(self, users=[], medias=[], home=True, all_media=False, error=True):
        trashs = []
        if not users:
            users = [getlogin()]
        for user in users:
            if home:
                path = Path('/home/' + user + "/.local/share/Trash")
                if path.exists():
                    trashs.append(Trash(str(path), user))
                elif error:
                    print("can't find: " + path.name, file=sys.stderr)
            if all_media:
                medias = Path("/media/" + user).iterdir()
            elif medias:
                medias = map(lambda x: Path("/media/%s/%s" % (user, x)),
                             medias)
            for m in medias:
                if m.exists():
                    t = m / (".Trash-" + str(getpwnam(user)[2]))
                    if t.exists():
                        trashs.append((Trash(str(t), m.name)))
                    elif error:
                        print("media " + m.name + " have no trash", file=sys.stderr)
                elif error:
                    print("no media name: " + m.name, file=sys.stderr)
        return trashs

    def get_all_media(self, user):
        for m in Path('/media/' + user).iterdir():
            yield m.name
