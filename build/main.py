import sys
from view import MainWindow, QtW

if __name__ == '__main__':
    app = QtW.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())