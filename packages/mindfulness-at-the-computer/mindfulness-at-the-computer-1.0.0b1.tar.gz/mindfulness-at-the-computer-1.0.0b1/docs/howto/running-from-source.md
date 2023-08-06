# Running from Source

If you don't see a download option for the platform of your choice, or you just prefer running from source for other reasons, you can follow these steps to start the application:

### Windows or GNU/Linux Systems

1. Download the Python 3.x installation package for your platform: https://www.python.org/downloads/
2. Install Python 3.x
3. On the command line: `pip install --upgrade pip` (On Ubuntu use `sudo -H` and `pip3` instead of `pip`)
4. On the command line: `pip install -r requirements.txt` (On Ubuntu use `pip3` instead of `pip`)
5. Download the latest code from the project main page on GitLab. Click the download icon (a small cloud with a down arrow inside it) and select "Download ZIP".
6. Unzip the downloaded file
7. Change directory to where the software files have been extracted
8. Type and run `python -m matc` on Windows or `python3 -m matc`on GNU/Linux systems

### MacOS

1. Install python: `brew install python3`
2. Download the latest code from the project main page on GitLab. Click the download icon (a small cloud with a down arrow inside it) and select "Download ZIP".
3. Change directory to where the software files have been extracted
4. create a virtual environment: `python3 -m venv ./venv`. You should now have a venv folder in your project
5. activate this venv: `source ./venv/bin/activate`. You can test whether you are using the right python now by doing: 
`which python` and `which pip`. You should be seeing the python and pip from the ./venv/bin folder
6. install dependencies in this environment: `pip install -r requirements.txt`
7. Type and run `python -m matc`

## Creating a shortcut (Optional)

### Windows

You can create a shortcut by right-clicking the `.exe` file for the application and choosing "Send to" and then "Desktop (create shortcut)"

### GNU/Linux Systems

For desktop systems that are compatible with the [freedesktop](https://www.freedesktop.org/) standard - such as Gnome and KDE - you can use the bwb.desktop file included in the source (If using a file manager, such as Gnome File Manager, you may see the name displayed as "Well-being Diary" rather than "bwb.desktop") to make the application visible in any start-menu-like menu. In Lubuntu, this is called the "main menu" and it's shown when the button in the lower left is clicked. "Vanilla" Ubuntu (ordinary) may not have a menu like this.

To use this file:

1. Edit the `mindfulness-at-the-computer.desktop` file (from the varia/ directory) and change the paths to match the path that you are using
2. Copy the `mindfulness-at-the-computer.desktop` file to your desktop or to any place from where you want to be able to start the application
3. To add the shortcut to the menu system ("start menu"): Copy the `mindfulness-at-the-computer.desktop` file to `/usr/share/applications/` using `sudo`
