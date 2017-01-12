from __future__ import print_function, absolute_import
from os import getlogin
from trashtalk.core import parse_option
from trashtalk.generate_trashs import generate_trashs, get_media_trashs


def autocomplete(args=''):
    args = args.split()
    args = args[1:]
    if args:
        options, unknown = parse_option(args)
    else:
        options = parse_option(args)
    args.reverse()
    if (options.am or options.trash) and "home" not in options.trash:
        home = False
    else:
        home = True
    if options.a:
        options.am = True
    files = ""
    trashs, error = generate_trashs(options.u, options.trash,
                                  home, options.am)
    for trash in trashs:
        for f in trash.list_files():
            files += ' ' + f[0]

    for arg in args:
        if arg[0] in '-':
            if arg == "-f":
                print(files, end='')
            return
    string_media = ""
    for trash in get_media_trashs(getlogin())[0]:
        string_media += " " + trash.name
    print(string_media, end="")
