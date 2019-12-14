from PyQt5 import QtWidgets, QtCore
from CMainWindow import CMainWindow

def main():
    app = QtWidgets.QApplication([])
    window = CMainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()