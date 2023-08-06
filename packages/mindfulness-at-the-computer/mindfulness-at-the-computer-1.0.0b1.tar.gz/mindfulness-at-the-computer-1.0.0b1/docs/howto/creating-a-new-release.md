

## Before building

* `git checkout master`
* `git pull`
* Check if there are any open issues relating to the next release: https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/-/milestones
* Versioning: Update the versioning string which can be found here: `matc/version.txt`
  * Please note that PyPI only allows a single upload for each version number (no retries!), so it may be good to use a `dev.x` version for testing, alternatively using test.pypi with the real version (or even combining these two approaches)
* `make install` - this will install build requirements: pyinstaller and packages needed for building for PyPI (as well as all the dependencies for the application to run)
* Upgrade all packages: [Link](https://www.activestate.com/resources/quick-reads/how-to-update-all-python-packages/)
* Creating a [new release tag in GitLab](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/tags)
* Runnings auto-tests


## Building platform-specific binaries (using pyinstaller and py2app)

PyInstaller is used for building for GNU/Linux and Windows, it bundles almost everything into a distribution package. This includes Python and all dependencies (Qt and the PySide6 Qt bindings in our case). After having created a package using PyInstaller the user doesn't need to worry about dependencies, with the exception of [libc on Linux-based systems](https://pyinstaller.readthedocs.io/en/stable/usage.html#making-linux-apps-forward-compatible), which is why for Linux systems it's generally recommended build on older systems

Pyinstaller documentation:
* See latest info about what platforms are supported (Python version and OS version) [here](https://github.com/pyinstaller/pyinstaller)
  * Please note that the pyinstaller version may not be compatible with the latest python version. (At the time of writing this is not a problem, but it has been in the past)
* Command line: http://pyinstaller.readthedocs.io/en/stable/usage.html
* Spec files: http://pyinstaller.readthedocs.io/en/stable/spec-files.html


### Building on Ubuntu

Before first time building:
1. Install the *oldest supported (LTS) release* of Ubuntu (at the time of writing this is 20.04 LTS)
  * The reason is that pyinstaller does not bundle *glibc* into the resulting package so the resulting package may not (will not?) work with earlier versions of libc and Linux: [link](https://pyinstaller.org/en/stable/usage.html#making-gnu-linux-apps-forward-compatible)
  * glibc is also specific for 32 or 64 bit so builds will only work on that architecture. Because of how common 64 bit systems are nowadays this is the priority for us
1. Install Python: `sudo apt-get install python3`
1. `sudo apt-get install python3-pip`

To build:
1. Please run this from the base application directory: `make build-pyinstaller-linux` - this will use the [Makefile](../../Makefile)


### Building on Windows

Before first time building:
1. Install Windows
   * It seems to be better to build on Windows 7 than later versions. The Windows 10 build binary file has failed to start for us, but the Windows 7 has always worked once the build has been completed. More info [here](https://pyinstaller.org/en/stable/usage.html#windows)
   * If you build on Windows 7 please make sure that SP1 (service pack 1) is installed, as this is needed for the Python installer to run
   * It may alsos be needed to install a VS C++ redistributable file, please see the issues section at the end of this document
2. Install Python (PyInstaller works with 3.6 which is the latest Python version at the time of writing). *Please use these settings*:
   * Install Python *only for the current user* (otherwise there may be problems with permissions later on)
   * *Add the path* (you have to restart to get the path to work)
3. Start cmd.exe, or start Windows powershell
   * If we get permission denied for the PySide/PyQt files: Please run with admin privileges
4. Create an empty directory where you can unzip the files, preferably with a path without any spaces

To build:
1. Go to the base application directory
2. f you have tried to build previously: Remove the `build` and `dist` directories:
   * `rmdir /s build`
   * `rmdir /s dist`
3. `pyinstaller mindfulness-at-the-computer-windows.spec`

The resulting `.exe` and `.dll` files will be in the `./dist/mindfulness-at-the-computer` directory. (There will also be an executable in the `./build/mindfulness-at-the-computer` directory but this should not be used because it has the wrong references)

As the last step, you can create a zip file from all the contents of the `./dist/mindfulness-at-the-computer` directory. Please add the version number at the end of this file name, as well as "windows"

Please find and run the resulting `.exe` file (`mindfulness-at-the-computer.exe`)

We may want to upload the resulting .exe file to an analyzer like virustotal.com, this can tell us how many anti-virus applications will detect the application as a virus

### Building on macOS

1. Install Python (PyInstaller now works with version 3.6 of Python): `brew install python3`
2. Go to the base application directory
3. Create and activate a virtual environment: see [this article](using-virtual-environment.md)
4. Install py2app: `pip install py2app`
5. `git pull`
6. `python setup.py py2app
`. This will give you a `dist` folder with a subfolder:
    - mindfulness-at-the-computer.app
7. Manually remove any *.db files from `./dist/mindfulness-at-the-computer.app/Contents/Resources/user_files` --- TODO: This needs to be updated since we have changed the place (and type) of the storage file
8. Go to the `dist` folder and add a symlink to the /Applications folder: `ln -s /Applications Applications`. 
   PyCharm might not like this and start indexing the Applications folder as well.
   You might want to close PyCharm before doing this.
9. Open the disk utilities with spotlight `cmd-space utility`
10. Create a new dmg file: `cmd-shift-n`
11. Select the dist folder in your project. 
12. In the `Save As` field enter the name of the dmg file: `mindfulness-at-the-computer`
13. From the `Image Format` drop-down select `read only` then click `Save`

You will now have a `mindfulness-at-the-computer.dmg` file at the selected location.


## After building

TODO: Move more of the documentation from the OS-specific sections into this section

You may want to reduce the size of the archive/zip file by removing unnecessary lib (.dll, .so) files. This script can help with that: [/varia/so_files.py](/varia/so_files.py)

### Uploading

1. Go to [sourceforge](https://sourceforge.net/projects/mindfulness-at-the-computer/files/)
2. Create a dir for the new version
3. Upload the archive files (`.tar.gz`, `.zip` and `.dmg`, for the different platforms) to sourceforge
4. For each file: Press the "i" (info) icon and set it as the default download for the related Operating system. This will make sure that we can give [this link](https://sourceforge.net/projects/mindfulness-at-the-computer/files/latest/download) to a user and it will lead directly to the correct file (the website detects the OS)


## Building a test version for PyPI

*This must be done by SunyataZero* since he has the login credentials for PyPI

On a GNU/Linux computer: `make build-pypi-test`

### To try it out

In dev environment:
```
make build-pypi-test
```

In test environment:
```
make ubuntu-complete-uninstall
cd
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ mindfulness-at-the-computer==[version] -v --upgrade
```
(Remove `==[version]` to get the latest version)

Please use `dev.x` versions only on the test server

It's safest to specify version, because of caching (?) the latest version may not be used otherwise

`-v` - the most verbose (the v flag is "addative")

More info here: https://packaging.python.org/en/latest/guides/using-testpypi/


## Manual testing

The most important things to test after building:
1. Start by unzipping the file (rather than starting with the result of the build, since this will risk that the application is distributed with a db file inside the zip file)
2. Verify that the intro dialog is shown
3. Verify that the audio is playing
4. Verify that the breathing notifications, breathing dialogs, and settings dialog can be seen
5. Verify that the application behaves as expected with regards to closing, opening, minimizing to task bar, minimizing to system tray
6. Verify that you can add a new entry in the breathing phrase list


## Building a live version for PyPI

*This must be done by SunyataZero* since he has the login credentials for PyPI

On a GNU/Linux computer: `make build-pypi-live`


## Updating the release number in the website repo

https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer.gitlab.io/-/blob/master/application-version.txt


## Notifying people of the new version (outreach)

There's a list of places that may be interested in the application on the wiki [here](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/wikis/Outreach)

Some of these places we have already made a page or post, and in these cases maybe it will suffice with a comment (unless we are moving from alpha to beta.)


***

## References

* Deploying Pyside6 applications using Pyinstaller: https://doc.qt.io/qtforpython/deployment-pyinstaller.html
* Linux deployment for Qt (C++): https://doc.qt.io/qt-5/linux-deployment.html

## Pyinstaller Issues

### `lib not found: MSVCP140.dll`, followed by `DLL load failed while importing`

On Windows 7/10 we may get a warning from pyinstaller while building:
```
2697 WARNING: lib not found: MSVCP140.dll dependency of C:\Python39\Lib\site-packages\PySide6\Qt6Gui.dll
2702 WARNING: lib not found: MSVCP140_2.dll dependency of C:\Python39\Lib\site-packages\PySide6\Qt6Gui.dll
2765 WARNING: lib not found: MSVCP140_1.dll dependency of C:\Python39\Lib\site-packages\PySide6\Qt6Widgets.dll
```

And if we try to start the binary file:
`Failed to execute script due to unhandled exception: DLL load failed while importing ___ The specified module could not be found`

#### Explanation

> - vccorlib140.dll (only used for C++/CX)
> - msvcp140_1.dll: (added in VS 2017) C++17 memory_resource
> - msvcp140_2.dll: (added in VS 2017 15.7) C++17 mathematical special functions

--- [Source](https://stackoverflow.com/questions/63108627/more-efficient-way-to-collect-all-dll-in-a-project)

#### Solution

One file, three ways to get it:
* On the page https://visualstudio.microsoft.com/vs/older-downloads/ under "Other Tools, Frameworks, and Redistributables" we find this: "Microsoft Visual C++ Redistributable for Visual Studio 2017"
* https://visualstudio.microsoft.com/vs/older-downloads/#microsoft-visual-c-redistributable-for-visual-studio-2017
* Direct link: https://go.microsoft.com/fwlink/?LinkId=746572


### qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.

This happens
* when trying to build binaries using pyinstaller
* on Ubuntu 20.04, but not on 22.04
* for both PyQt5 and PySide6

Underlying problem: `Cannot load library /home/sunyata/PycharmProjects/mindfulness-at-the-computer/dist/mindfulness-at-the-computer/PySide6/Qt/plugins/platforms/libqxcb.so: (libxcb-icccm.so.4: cannot open shared object file: No such file or directory)`

Solution: `sudo apt install -y libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-icccm4`

See [this issue](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/-/issues/403) for details
