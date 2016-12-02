from __future__ import print_function
from path import path
import os


class Trash():

    def __init__(self, options):
        self.options = options
        self.trash_list = []
        self.define_trash()

    def define_trash(self):
        if self.options.trash:
            pass
        elif self.options.a:
            pass
            if self.options.au:
                pass
            if self.option.am:
                pass
        else:
            self.trash_list.append(
                (os.getlogin(),
                 path('/home/%s/.locate/Trash/files' % os.getlogin()))
            )
