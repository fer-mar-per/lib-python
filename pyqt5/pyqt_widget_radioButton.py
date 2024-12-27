#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Create dictionary to add gui elements
        self._gui = {}

        # Set window's space, size and title
        self._wnd_settings(positionX=250, positionY=150,
                           sizeX=420, sizeY=200,
                           title='Radio Buttons')

        # Create two lineEdits
        self._add_lineEdits()

        # Create two radioButtons
        self._add_radioButtons()

        # Add submit button
        self._add_button()

        # Show the window
        self.show()

    def _wnd_settings(self, **kwargs):
        u"""
        Sets the following window's settings:
            - self.setGeometry()
            - self.setWindowTitle()
        """
        posX = kwargs.get('py', kwargs.get('positionY', 50))
        posY = kwargs.get('px', kwargs.get('positionX', 50))
        sizeX = kwargs.get('sx', kwargs.get('sizeX', 300))
        sizeY = kwargs.get('sy', kwargs.get('sizeY', 450))
        title = kwargs.get('t', kwargs.get('title', 'Window'))
        # ----------------

        # Place in space and set size
        self.setGeometry(posX, posY, sizeX, sizeY)

        # Set title
        self.setWindowTitle('PyQt Widget example: {}'.format(title))

    def _add_lineEdits(self):
        # Add some LineEdit objects
        self._gui['name'] = QLineEdit(self)
        self._gui['name'].move(150, 50)
        self._gui['name'].setPlaceholderText("Enter your name")
        self._gui['surname'] = QLineEdit(self)
        self._gui['surname'].move(150, 80)
        self._gui['surname'].setPlaceholderText("Enter your surname")

    def _add_radioButtons(self):
        u"""
        Adds two radioButtons.
        """
        # Create the RadioButtons
        self._gui['male'] = QRadioButton("Male", self)
        self._gui['female'] = QRadioButton("Female", self)

        # Use a geometry manager to move them
        self._gui['male'].move(150, 110)
        self._gui['female'].move(200, 110)

        # Set the male to checked
        self._gui['male'].setChecked(True)

    def _add_button(self):
        # Add a button for submit
        button = QPushButton("Submit", self)
        button.move(200, 140)
        button.clicked.connect(self.get_values)

    def get_values(self):
        _name = self._gui['name'].text()
        _surname = self._gui['surname'].text()
        _gender = None
        if self._gui['male'].isChecked():
            _gender = "Sir"
        elif self._gui['female'].isChecked():
            _gender = "Madam"

        print("Hello {} {} {}!".format(_gender, _name, _surname))


def main():
    App = QApplication(sys.argv)
    wnd = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()