# cd in Makefiles: https://stackoverflow.com/q/1789594/2525237
# General help with Makefiles: https://makefiletutorial.com/
# return (using print in python) from a python script: https://stackoverflow.com/q/60263526/2525237

# Each line in a recepie runs in it's own sub-shell

# Running dependencies in order:
# * Option A: target: | dep1 dep2 dep3
# * Option B: make dep1 (indented)

# If the platform is not specified (e.g. ___-windows the) commands should work on Linux
# and MacOS systems. (They may only have been tested on a Linux system though)

# "pip -V" can be used to determine if we are running inside a virtual environment

version:=$(shell cat matc/version.txt)

.PHONY: install
install:
	pip3 install -U -e .[dev]
	pip3 --version
# Using both the -U and the -e flags will make sure that the pypi version is uninstalled and the
# editable version is installed (assuming that the local/editable version is a later version)

.PHONY: run
run:
	python3 -m matc

.PHONY: trace
trace:
	python3 -m trace --trace matc/__main__.py
# --ignore-module=shiboken6

# Interesting options:
# --trace - this gives a lot of output!
# --listfuncs --trackcalls - this doesn't seem to show anything until after exit
# --report - has not been tested
# --coverdir - for code coverage
# --ignoredir
# More here:
# * https://docs.python.org/3/library/trace.html
# * http://pymotw.com/3/trace/

.PHONY: clean
clean:
	rm -rf dist/ build/ mindfulness_at_the_computer.egg-info/ .pytest_cache/

.PHONY: build-pypi-test
build-pypi-test:
	make clean
	make install
	python3 -m build
	python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	python3 -m webbrowser -t "https://test.pypi.org/project/mindfulness-at-the-computer/"
# git pull

.PHONY: build-pypi-live
build-pypi-live:
	make clean
	make install
	python3 -m build
	python3 -m twine upload dist/*
	python3 -m webbrowser -t "https://pypi.org/project/mindfulness-at-the-computer/"
	python3 -m webbrowser -t "https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer.gitlab.io/-/blob/master/application-version.txt"

.PHONY: analysis
analysis:
	pylint matc/
	prospector matc/ --without-tool pycodestyle --without-tool pylint --strictness high

# Pylint
# Uses the config in pyproject.toml
# One reason for running pylint directly instead of through Prospector is that we now have
# clickable links into the code


# Prospector
# https://prospector.landscape.io/en/master/supported_tools.html
# https://prospector.landscape.io/en/master/usage.html
#
# pycodestyle --- excluded because i use pycharm for checking code style
# pylint --- excluded because it is run separately
# pyflakes ---
# mccabe --- investigates code complexity
# dodgy --- looks for plain text passwords, tokens, etc
# pydocstyle ---
#
# Extras:
# --with-tool pyroma (setup.py) --- issue: https://github.com/PyCQA/prospector/issues/562
# -can be run separately using `pyroma .`
# --with-tool vulture (unused classes and functions)
# --with-tool mypy
# --with-tool bandit (security issues)
#
# prospector --tool pylint --strictness verylow matc/

.PHONY: test
test:
	pytest
# Runs the tests using the configuration in pyproject.toml. Please note that when running tests
# with Pycharm the configuration will not be used

# pytest -rA -vv test/
# -o log-cli=true can be used for debugging failing tests

.PHONY: coverage
coverage:
	coverage run -m pytest -rA -vv test/
	coverage report --omit="/usr/*,test/*,*/shibokensupport/*,*/signature_bootstrap.py" -m
# "-i" can be added to ignore warnings
# The problem "No source for code" can be solved by adding a pattern to --omit="" or by using "-i"

.PHONY: build-pyinstaller-linux
build-pyinstaller-linux:
	make clean
	pyinstaller mindfulness-at-the-computer-linux.spec
	cd dist && tar -czvf mindfulness-at-the-computer.tar.gz mindfulness-at-the-computer/
	mv dist/mindfulness-at-the-computer.tar.gz .
	echo ${version}
	mv -f mindfulness-at-the-computer.tar.gz mindfulness-at-the-computer_linux_${version}.tar.gz
	xdg-open build/mindfulness-at-the-computer-linux/warn-mindfulness-at-the-computer-linux.txt

# The following windows make commands have not been tested (make is difficult to run on windows)
# Instead of running make on windows we may want to simply copy and paste these commands, one
# by one.

.PHONY: ubuntu-complete-uninstall
ubuntu-complete-uninstall:
	pip3 uninstall -y mindfulness-at-the-computer
	pip3 uninstall -y PySide6
	pip3 uninstall -y shiboken6
	rm -f ~/.local/share/applications/mindfulness-at-the-computer.desktop
	rm -f ~/.config/autostart/mindfulness-at-the-computer.desktop
	rm -f ~/Desktop/mindfulness-at-the-computer.desktop

.PHONY: clean-windows
clean-windows:
	rmdir /s /q dist build mindfulness_at_the_computer.egg-info

.PHONY: build-pyinstaller-windows
build-pyinstaller-windows:
	make clean-windows
	pyinstaller mindfulness-at-the-computer-windows.spec
	# There is no easy way to create zipfiles from the windows command line, so instead we do this:
	cd dist && start .
	echo The file explorer has been opened in the dist dir. Please create the zipfile yourself.
