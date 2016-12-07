# TRASHTALK


## concept

*script to simplify trash access*

# output

	# without trash user or name all option is for current home
	'path to home trash'
	-a; select all trash, home + media
	-au; select all home
	-am; select all trash in media
	-p; print path
	-l; list content in trash
	-s "file"; detail size of trash by file
	-cl or --clean "file"; clean trash without arg else clean "file"
	-rm "file"; move file to trash
	======================
	--verbose; verbose lol
	--help or -h; show help

### exemple

	$ trashtalk -a -p -cl *; clean all trash and print path
	/home/user/.local/share/Trash
	/media/user/yourmedia/.Trash-0000
