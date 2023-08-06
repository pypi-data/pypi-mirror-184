# Manual testing

This document contains test cases for manual testing

For all the tests below: Please start the application in debug mode, or at least in such a way that you can see the debug output (from the logging)

Test Record: Please use [the wiki](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/wikis/home)

"TBD" in this document often means that the test case is yet to be written

## Installation and setup

PIP, PyInstaller

### Additional setup

GNU/Linux:

pip: check  done at install time
pyinstaller: done at first start

Creating an application shortcut
Adding the application to the start menu
Adding the application to autostart



Windows, Mac:
* Verify that the intro dialog show a message on the last page (automate this?)


## System Tray Menu

1. Click on the system tray icon.        
2. Click on "Breathing dialog".
3. Verify: Breathing dialog comes up.

## Breathing phrases

1. Select a phrase from the list to the left.
2. Verify: The breathing area text is changed.
3. Enable breathing reminders.
4. Click on "test" for the breathing reminders (or wait for the next reminder).
5. Verify: The text has been changed from before.

## Settings dialog

Settings file

## Breathing visualizations




## Stess/load testing

### Memory

*DRAFT*

`sudo apt install stress-ng`

1. `sudo swapoff -a` (may take a few seconds)
2. `stress-ng --brk 2 --stack 2 --bigheap 2 -t 15` (15 seconds). Reference: https://wiki.ubuntu.com/Kernel/Reference/stress-ng
3. test appl
4. `sudo swapon -a`

