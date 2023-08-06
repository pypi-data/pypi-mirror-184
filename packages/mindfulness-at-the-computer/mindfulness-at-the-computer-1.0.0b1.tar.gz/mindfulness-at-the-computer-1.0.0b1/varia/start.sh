#!/bin/bash
# The reason for using a shellscript like this is that we then can use Python 3.7.
# (Other ways i have tried to use 3.7 have failed)
cd ~/PycharmProjects/mindfulness-at-the-computer/
source venv/bin/activate
./mindfulness-at-the-computer.py
