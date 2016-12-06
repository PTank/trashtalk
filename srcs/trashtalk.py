#! /usr/bin/env python3
from __future__ import print_function
import argparse
from os import getlogin
from pathlib import Path
from make_path import get_media_trash, get_home_trash


def parse_option():
    parser = argparse.ArgumentParser(
        description="Taking out your trash easily")
    # CLASSIC
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s: ' + "0.01")
    parser.add_argument('--verbose', action='store_true')
    # TRASH SELECTION
    selection = parser.add_argument_group('trash selection')
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
    return parser.parse_args()


def main():
    trashs = []
    options = parse_option()
    if not options.u and not options.au:
        options.u = [getlogin()]
    elif options.au:
        options.u = [i.name for i in Path('/home').iterdir()]
    if not options.trash:
        for user in options.u:
            if options.a or not options.am:
                trashs.append(get_home_trash(user))
            if options.am or options.a:
                trashs.append(get_media_trash(user))
    else:
        for media in options.trash:
            for user in options.u:
                t = get_media_trash(user, [media])
                if t:
                    trashs.append(t)
    for t in trashs:
        for trash in t:
            if not trash:
                continue
            if options.p or (
                    not options.l and not options.s and not options.clean):
                print("%s: %s" % (trash[0], str(trash[1])))
            if options.l or options.s:
                trash[1].list_files(options.files, options.s)
            if options.clean:
                trash[1].clean(options.files)

if __name__ == "__main__":
    main()
