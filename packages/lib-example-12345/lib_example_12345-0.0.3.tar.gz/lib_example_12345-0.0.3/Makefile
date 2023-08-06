all:
	python pipfile_parse.py
	nbdev_read_nbs
	nbdev_clean_nbs
	nbdev_test_nbs
	nbdev_build_lib
	nbdev_bump_version
	git status