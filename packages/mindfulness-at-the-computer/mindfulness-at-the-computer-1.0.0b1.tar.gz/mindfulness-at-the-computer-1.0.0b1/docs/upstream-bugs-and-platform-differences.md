# Upstream Bugs

A list of [upstream](https://en.wikipedia.org/wiki/Upstream_(software_development)) bugs that are not covered in our issue list

## Gentoo: No audio

This is because [gstreamer](https://gstreamer.freedesktop.org/) has been built without the [wayland](https://wayland.freedesktop.org/) flag

vimzim wrote on matrix/gitter:
> Gentoo, because it builds all packages from source, allows to configure what parts of a package needs to be build via use-flags. Each package in the repository has a set of use-flags. This is the set of use flags for gst-plugins-base
> 
> the symbol in the error when I import qtmultimedia in python is obviously related to wayland, so I enable it for example with
> `sudo euse --enable wayland` to enable it globally
> or by writing `media-libs/gst-plugins-base wayland` to `/etc/portage/package.use/media-libs/gst-plugins-base` to enable it only for this package
> 
> and then re-install the package (which causes it to be rebuild from source again now with wayland support)


## XFCE: messageClicked is not triggered

(Clicking on systray popup messages just closes the message)

## LXDE: Systray icon tooltip not visible

This must be an LXDE or Qt bug, not something that we can fix ourselves

## LXDE: System tray file icon "shown as missing" while showing notification

This is a bug in Qt or PyQt

![](https://i.stack.imgur.com/2Kc6x.png)

I've posted a question here: https://stackoverflow.com/questions/45827951/missing-file-icon-is-shown-in-the-system-tray-when-running-showmessage-with-no

Qt version: 5.7.1, 5.9.0

This bug is not seen in XFCE (version 4.12)

## MacOS: Fullscreen windows not closed when `close()` is called

Bug found by mbed67 on MacOS Sierra

Stackoverflow has a question related to this here: https://stackoverflow.com/questions/31666744/pyqt5-can-not-close-a-topmost-fullscreen-qdialog-on-mac-osx


# Platform differences

## Behavior at application error

Windows: When an error is encountered, the application will crash

Linux-based: The application just prints to stdout

## Notifications

Some systems do not show notifications

For example, older versions of MacOS seem to have this problem. In such a case, the user will need to install growl

## Systray

Some systems do not have a system tray

XFCE: Left clicking icon in system tray does nothing

## Minimize area

Systems that lack a minimizing area

## 64 and 32 bit Linux-based systems

Application binaries must be built on the same bit-numbered system as the OS where they will run. This may be because of glibc

## Virtual desktop and multiple desktops, etc

First some definitions:
* Multiple desktops: A computer with more than one graphics card (or a graphics card with several physical outputs) can have multiple desktops
  * Virtual desktop: A computer with multiple desktops (see above) and where the user has chosen to set up the system so that it seems like everything is on one long desktop
* (unknown what word to use): A computer where the OS provides several different desktops that the user can switch between (on LXDE called the "desktop pager"). Please note that this isn't called "virtual desktops" even though this would be natural

Multiple desktops and virtual desktops are covered here: http://doc.qt.io/qt-5/qdesktopwidget.html

## "No source for code" when running coverage

```bash
(venv) $ coverage report
No source for code: '/home/sunyata/PycharmProjects/mindfulness-at-the-computer/shibokensupport/__init__.py'.
```

https://stackoverflow.com/questions/2386975/no-source-for-code-message-in-coverage-py

