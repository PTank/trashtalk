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

	$ trashtalk -ap -cl; clean all trash and print path
	user: /home/user/.local/share/Trash
	yourmedia: /media/user/yourmedia/.Trash-0000


## todo

* [x] add method move to trash option
* [x] add method to untrash file with trashinfo
* [x] human readable size standard
* [x] can take direct path in arg ? not yet
* [x] add error return in remove method
* [x] add media from /media without /user
* [x] add a .trashtalk in home who can personalise trash location
* [ ] complete test, trash restore, generatetrashs,  tools
* [ ] doc
