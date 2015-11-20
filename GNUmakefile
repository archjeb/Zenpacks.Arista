##############################################################################
#
# Copyright (C) Zenoss, Inc. 2015, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

PYTHON=$(shell which python)
HERE=$(PWD)
ZP_DIR=$(HERE)/ZenPacks/community/Arista


default: build

egg:
	python setup.py bdist_egg

build:
	python setup.py bdist_egg
	python setup.py build

clean:
	rm -rf build dist *.egg-info

analytics-bundle:
	rm -f ZenPacks/community/Arista/analytics/analytics-bundle.zip
	mkdir -p ZenPacks/community/Arista/analytics
	mkdir -p analytics/resources/public/Arista_ZenPack
	./create-analytics-bundle \
        --folder="Arista_ZenPack" \
        --domain="Arista Domain" \
        --device=Arista;
	cd analytics && \
	zip -r ../ZenPacks/community/Arista/analytics/analytics-bundle.zip * && \
	cd ..
