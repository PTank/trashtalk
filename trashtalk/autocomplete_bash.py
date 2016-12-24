from __future__ import print_function, absolute_import
from trashtalk.make_path import get_media_trash
from os import getlogin
from trashtalk.core import parse_option
from trashtalk.trash_factory import TrashFactory


def current_media():
    for media in get_media_trash(getlogin()):
        print(media[0], end='')


def autocomplete(args=''):
    args = args.split()
    args = args[1:]
    try:
        options = parse_option(args)
    except:
        return
    args.reverse()
    factory = TrashFactory()
    if (options.am or options.trash) and "home" not in options.trash:
        home = False
    else:
        home = True
    files = ""
    trashs = factory.create_trash(options.u, options.trash,
                                  home, options.am, error=False)
    for trash in trashs:
        for f in trash.list_files():
            files += ' ' + f[0]

    for arg in args:
        if arg[0] in '-':
            if arg == "-f":
                print(files, end='')
                return
            else:
                break
    return current_media()
