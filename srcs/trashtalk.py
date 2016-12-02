#! /usr/bin/env python3
from __future__ import print_function
import argparse
from trash import Trash


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
    option.add_argument('-l', action='store_true', default=False,
                        help="list file in trash")
    option.add_argument('-s', action='store', nargs='*',
                        help=("print size, if -du and "
                              "-cl was select du is run before -rm"))
    option.add_argument('-cl', '--clean', action='store', nargs='*',
                        help="clean file, or without file all")
    option.add_argument('-rm', action='store', nargs='*',
                        help="move file to selected trash")
    return parser.parse_args()


def main():
    options = parse_option()
    trash = Trash(options)
    print(trash.trash_list)

if __name__ == "__main__":
    main()
