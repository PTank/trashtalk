from __future__ import print_function, absolute_import
from os import getlogin
from trashtalk.core import parse_option
from trashtalk.trash_factory import TrashFactory


def autocomplete(args=''):
    args = args.split()
    args = args[1:]
    if args:
        options, unknown = parse_option(args)
        del(unknown)
    else:
        options = parse_option(args)
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
    for media in factory.get_all_media(getlogin()):
        print(media, end="")
