# TRASHTALK *beta*

[![Build Status](https://travis-ci.org/PTank/trashtalk.svg?branch=master)](https://travis-ci.org/PTank/trashtalk) 
[![Coverage Status](https://coveralls.io/repos/github/PTank/trashtalk/badge.svg?branch=master)](https://coveralls.io/github/PTank/trashtalk?branch=master) 
__master__

[![Build Status](https://travis-ci.org/PTank/trashtalk.svg?branch=dev)](https://travis-ci.org/PTank/trashtalk) 
[![Coverage Status](https://coveralls.io/repos/github/PTank/trashtalk/badge.svg?branch=dev)](https://coveralls.io/github/PTank/trashtalk?branch=dev) 
__dev__

## concept

*script to simplify trash access*

## install

	python setup.py install

### example

	$ trashtalk -ap -cl *; clean all trash and print path
	user: /home/user/.local/share/Trash
	yourmedia: /media/user/yourmedia/.Trash-0000


## todo

* [ ] add method move to trash option
* [ ] add method to untrash file with trashinfo
* [ ] add option -h human readable size
* [ ] can take direct path in arg
* [ ] add a .trashtalk in home who can personalise trash location
* [ ] complete test
* [ ] doc
