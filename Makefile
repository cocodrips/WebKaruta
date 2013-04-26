
APPCFG_PATH = $(shell readlink $(shell which appcfg.py))
SDK_DIR = $(shell dirname $(APPCFG_PATH))

test:
	python runtest.py $(SDK_DIR)
clean:
	-rm -r tests/.urlopen_cache/

.PHONY: test