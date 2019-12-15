from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow
from Views.CMenuView import CMenuView
from Views.CMainView import CMainView

class CMainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.showFullScreen()
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        menu_view = CMenuView()
        menu_view.changed_view.connect(self.on_changed_view)
        self.setCentralWidget(menu_view)

    def on_changed_view(self):
        print("Clicked")
        main_view = CMainView()
        self.setCentralWidget(main_view)