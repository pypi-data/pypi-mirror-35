#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>
#

PREFIX=/usr/local

XMLPLAIN=$(abspath xmlplain.py)

all: all-local all-tests

all-local:
	./setup.py build

all-tests:
	$(MAKE) -C tests XMLPLAIN="$(XMLPLAIN)" all

check: check-local check-tests

check-local: all-local

check-tests:
	$(MAKE) -C tests XMLPLAIN="$(XMLPLAIN)" check

clean: clean-local clean-doc clean-tests

clean-local:
	rm -rf build xmlplain.pyc

clean-tests:
	$(MAKE) -C tests clean

distclean: distclean-local distclean-doc distclean-tests

distclean-local: clean
	rm -rf dist __pycache__ xmlplain.egg-info venv2 venv3

distclean-tests:
	$(MAKE) -C tests distclean

install:
	./setup.py install --prefix=$(PREFIX)

sdist:
	./setup.py sdist

bdist:
	./setup.py bdist_wheel

doc:
	sphinx-build doc gh-pages

upload:
	twine upload dist/xmlplain-*.tar.gz dist/xmlplain-*.whl

requirements:
	pip install -r requirements.txt

upload-requirements:
	pip install twine

doc-requirements:
	pip install sphinx

self-requirements:
	pip install xmlplain

release:
	$(MAKE) distclean
	$(MAKE) virtualenv2
	$(MAKE) venv2-requirements
	$(MAKE) venv2-check
	$(MAKE) venv2-bdist
	$(MAKE) virtualenv3
	$(MAKE) venv3-requirements
	$(MAKE) venv3-check
	$(MAKE) venv3-bdist
	$(MAKE) venv3-sdist
	$(MAKE) venv3-doc-requirements
	$(MAKE) venv3-doc

release-upload:
	$(MAKE) venv3-upload-requirements
	$(MAKE) venv3-upload

check-release:
	$(MAKE) distclean
	$(MAKE) virtualenv2
	$(MAKE) venv2-self-requirements
	$(MAKE) XMLPLAIN="python -m xmlplain" venv2-check
	$(MAKE) virtualenv3
	$(MAKE) venv3-self-requirements
	$(MAKE) XMLPLAIN="python -m xmlplain" venv3-check
	$(MAKE) distclean

venv2-%:
	env VIRTUAL_ENV="$$PWD/venv2/bin" \
	PATH="$$PWD/venv2/bin:$$PATH" \
	$(MAKE) $*

venv3-%:
	env VIRTUAL_ENV="$$PWD/venv3/bin" \
	PATH="$$PWD/venv3/bin:$$PATH" \
	$(MAKE) $*

virtualenv2:
	virtualenv -p python2 venv2
	venv2/bin/pip install --upgrade pip setuptools wheel

virtualenv3:
	virtualenv -p python3 venv3
	venv3/bin/pip install --upgrade pip setuptools wheel

clean-doc:
	rm -rf gh-pages/.buildinfo gh-pages/.doctrees gh-pages/_modules gh-pages/_sources gh-pages/_static gh-pages/objects.inv gh-pages/*.html gh-pages/*.js

distclean-doc: clean-doc

.PHONY: all check clean distclean install sdist bdist doc upload
.PHONY: all-local check-local clean-local distclean-local
.PHONY: doc clean-doc distclean-doc
.PHONY: all-tests check-tests clean-tests disclean-tests
.PHONY: release release-upload requirements upload-requirements doc-requirements self-requirements
.PHONY: virtualenv2 virtualenv3
.PHONY: venv2-% venv3-%
