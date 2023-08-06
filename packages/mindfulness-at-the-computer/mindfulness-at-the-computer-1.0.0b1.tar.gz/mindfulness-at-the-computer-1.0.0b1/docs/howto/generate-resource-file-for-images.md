### Generating a resource file for images

Because we are using a `.qss` file for the Qt version of css, we need a way to reference image paths that will work on all operating systems.

We are using Qt's resource system for that.

In order to generate a new resource file (`matc_rc.py` in our case), you will have to make a `.qrc` file first. This is an xml file that holds the paths to the files:

```
<!DOCTYPE RCC><RCC version="1.0">
<qresource>
    <file>checkbox_checked.svg</file>
    <file>checkbox_unchecked.svg</file>
    <file>down.svg</file>
    <file>down_disabled.svg</file>
    <file>up.svg</file>
    <file>up_disabled.svg</file>
</qresource>
</RCC>
```

The images have to reside in the same folder as the `.qrc` file, or in a subfolder. If they are in a subfolder, you will have to provide the relative path to them, and reference them like that in the code.

Given the above `.qrc` file, we can reference the `checkbox_checked.svg` like this:

`:/checkbox_checked.svg`

Once we have a `.qrc` file, we will have to generate a python file that we can import:

`pyrcc5 -o matc/matc_rc.py res/matc.qrc`

Then, to be able to reference the resources (our icons) in the code, and in the `.qss` file, we have to import it in `__main__.py`

If you are using Pycharm or another IDE, it may look like it is never used (displayed in grey color), but it is necessary for the `.qss` file to see it.


`[prj-dir]/matc/matc_rc.py`
`[prj-dir]/res/matc.qrc`
`[prj-dir]/matc/matc.qss`
