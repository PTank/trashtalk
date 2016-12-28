#! /usr/bin/env python3
"""
Option parser and the main function
"""
from __future__ import print_function, absolute_import
import argparse
from trashtalk.trash_factory import TrashFactory
import sys

__all__ = ["trashtalk"]


def parse_option(args=None):
    parser = argparse.ArgumentParser(
        description="Taking out your trash easily")
    # CLASSIC
    from trashtalk.__init__ import __version__
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s: ' + __version__)
    parser.add_argument('--verbose', action='store_true')
    # TRASH SELECTION
    selection = parser.add_argument_group('trash selections')
    option = parser.add_argument_group('trash options')
    selection.add_argument('trash', nargs='*', default=[],
                           help=("name where you want use trash, "
                                 "this is a list, you can write home or media,"
                                 " by default your home trash was selected"))
    selection.add_argument('-a', action='store_true', default=False,
                           help="select all trash (home + all your media)")
    selection.add_argument('-u', action='store', nargs='*',
                           help="select user")
    selection.add_argument('-au', action='store_true', default=False,
                           help="select all home")
    selection.add_argument('-am', action='store_true', default=False,
                           help="select all media, this can depend of user")
    # TRASH OPTION
    option.add_argument('-p', action='store_true', default=False,
                        help="print trash path")
    option.add_argument('-f', '--files', action='store', nargs='*',
                        help="select file in trash")
    option.add_argument('-l', action='store_true', default=False,
                        help="list file in trash")
    option.add_argument('-s', action='store_true',
                        help=("print size"))
    option.add_argument('-cl', '--clean', action='store_true',
                        help="clean file, or without file all")
    option.add_argument('-rm', action='store', nargs='*',
                        help="move file to selected trash")
    if args:
        return parser.parse_args(args)
    return parser.parse_args()


def print_files(list_files):
    line = ""
    for e, value in enumerate(list_files[0]):
        new_list = [x[e] for x in list_files]
        spaces = len(str(max(new_list, key=lambda x: len(str(x))))) + 1
        line += "{%d:%d}" % (e, spaces)
    for f in list_files:
        if f[0]:
            print(line.format(*f))
        else:
            print(f[1], file=sys.stderr)


def trashtalk():
    options = parse_option()
    factory = TrashFactory()
    if (options.am or options.trash) and "home" not in options.trash:
        home = False
    else:
        home = True
        if options.trash:
            options.trash.remove('home')
    if options.a:
        options.am = True
    trashs = factory.create_trash(options.u, options.trash, home, options.am)
    for trash in trashs:
        if not trash:
            continue
        if options.p or (
                not options.l and not
                options.s and not options.clean
                and not options.rm):
            if options.p:
                print('\033[34;1m%s: ' % trash.name, end='')
            print("%s\033[0m" % str(trash))
        if options.l or options.s:
            print_files(list(trash.list_files(options.files, options.s)))
        if options.clean:
            errors = trash.clean(options.files)
            if errors:
                for e in errors:
                    print("clean: " + e, file=sys.stderr)
        if options.rm:
            trash.remove(options.rm)
