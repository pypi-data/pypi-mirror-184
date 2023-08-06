## Styling elements using qss (Qt version of CSS)

Some elements are styled using QSS (Qt Style Sheets), the Qt version of CSS.
In this project the styling is in [matc.qss](../../matc/matc.qss)

Widgets can be styled as described in [this](http://doc.qt.io/qt-5/stylesheet-reference.html) document.
For instance, as you can see at lines 1 - 7 of `matc.qss`, you can use an image for a checked QCheckBox and another image for an unchecked QCheckBox. 

The downside of directly using the Qt Widgets as selectors, is that every instance of that widget will look the same.
So, in our project, every checkbox will look the same, because we are styling QCheckBox.

If we don't want that, we have two options:

#### Create a custom widget by extending a Qt Widget

We can extend a Qt Widget and thus make a [reusable component](../../matc/gui/reusable_components.py)
For instance, there are several "headings", extended from QtWidgets.QLabel, like `H1` and `H2`
Now we can use a different styling for each child widget that extends QtWidgets.QLabel. 
Wherever we want to use a large heading, we use the reusable component `H1` instead of a regular QLabel.
This is very useful if you have many places where you would like to use this component.

#### Set an object name on a Qt Widget and specify that in the qss

We can use the original Qt Widget, for instance QtWidgets.QPushButton, and then set the object name.
For instance:

    self.notif_select_audio_qpb.setObjectName("notif_select_audio_qpb")

Where `notif_select_audio_qpb` is an instance of `QPushButton`.

Then we can style it by using `<widget>#<object-name>` 

    QPushButton#notif_select_audio_qpb {
        border: 1px solid #B3B3B3;
        border-radius: 10px;
        height: 20px;
        background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);
        min-width: 200px;
    }

### Using the *.qss file in the project

In `mindfulness-at-the-computer.py` we are using the `matc.qss` file as follows:

    stream = QtCore.QFile(os.path.join(matc.shared.get_base_dir(), "matc.qss"))
    stream.open(QtCore.QIODevice.ReadOnly)
    matc_qapplication.setStyleSheet(QtCore.QTextStream(stream).readAll())

***

Reference: [Qt Style Sheets documentation](https://doc.qt.io/qt-5/stylesheet.html)
