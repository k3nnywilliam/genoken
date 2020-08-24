import sys
from PyQt5 import QtWidgets as QtW
from view import MainWindow

if __name__ == '__main__':
    app = QtW.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())