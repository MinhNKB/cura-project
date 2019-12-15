from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSignal

class CMenuView(QFrame):
    changed_view = pyqtSignal()

    def __init__(self, parent = None):
        QFrame.__init__(self, parent)
        self.setStyleSheet("CMenuView {background-image: url(Resources/images/backgrounds/menu-background.png);}")
        self.prepare_layout()


    def prepare_layout(self):
        vbox_button_layout = QVBoxLayout()
        vbox_button_layout.setAlignment(QtCore.Qt.AlignHCenter)
        self.setLayout(vbox_button_layout)

        button = QPushButton()
        button.setFixedSize(800,100)
        button.setIconSize(QSize(800, 100))
        button.setObjectName("MenuButton")
        # button.setStyleSheet("""QPushButton { background-color: white;
        #                                                 color: black;
        #                                                 border-width: 2px;
        #                                                 border-radius: 15px;
        #                                                 padding: 4px;
        #                                                 font-family: Comic Sans MS;
        #                                                 font-size: 36px }
        #                         QPushButton:pressed {background-color: rgb(200, 200, 200)}""")

        button.setStyleSheet("""QPushButton#MenuButton {background-image: url(Resources/images/icons/icon-menu-1.png);}""")
        button.clicked.connect(self.on_button_clicked)
        vbox_button_layout.addWidget(button)
        vbox_button_layout.addSpacing(12)

        button = QPushButton()
        button.setFixedSize(800, 100)
        button.setIconSize(QSize(800, 100))
        button.setObjectName("MenuButton")
        # button.setStyleSheet("""QPushButton { background-color: white;
        #                                                 color: black;
        #                                                 border-width: 2px;
        #                                                 border-radius: 15px;
        #                                                 padding: 4px;
        #                                                 font-family: Comic Sans MS;
        #                                                 font-size: 36px }
        #                         QPushButton:pressed {background-color: rgb(200, 200, 200)}""")

        button.setStyleSheet("""QPushButton#MenuButton {background-image: url(Resources/images/icons/icon-menu-2.png);}""")
        button.clicked.connect(self.on_button_clicked)
        vbox_button_layout.addWidget(button)

    def on_button_clicked(self):
        self.changed_view.emit()


