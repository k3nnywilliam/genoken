# -*- coding: utf-8 -*-
#Created by Kenny William Nyallau 2020

from PyQt5 import QtWidgets as QtW
from PyQt5 import QtCore as QtC
from PyQt5 import QtGui as QtG
from myui import Ui_Form

class MainWindow(QtW.QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #self.setWindowIcon(QtG.QIcon('ui_files/images/icon.png'))
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('GenoKen alpha v.0.0.1')
        self.show()