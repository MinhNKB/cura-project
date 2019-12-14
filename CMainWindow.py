from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from Views.CMenuView import CMenuView
from Views.CMainView import CMainView

class CMainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.showFullScreen()
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        menu_view = CMainView()
        self.setCentralWidget(menu_view)