from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton

class CMenuView(QFrame):
    def __init__(self, parent = None):
        QFrame.__init__(self, parent)
        self.setStyleSheet("CMenuView {background-image: url(Resources/images/backgrounds/menu-background.png);}")
        self.prepare_layout()


    def prepare_layout(self):
        vbox_button_layout = QVBoxLayout()
        vbox_button_layout.setAlignment(QtCore.Qt.AlignHCenter)
        self.setLayout(vbox_button_layout)

        button = QPushButton()
        button.setText("Dr. INVIVO 4D2")
        button.setFixedSize(800,100)
        button.setStyleSheet("""QPushButton { background-color: white;
                                                        color: black;
                                                        border-width: 2px;
                                                        border-radius: 15px;
                                                        padding: 4px;
                                                        font-family: Comic Sans MS;
                                                        font-size: 36px }
                                QPushButton:pressed {background-color: rgb(200, 200, 200)}""")
        vbox_button_layout.addWidget(button)
        vbox_button_layout.addSpacing(12)
        button = QPushButton()
        button.setText("Dr. INVIVO 4D6")
        button.setFixedSize(800, 100)
        button.setStyleSheet("""QPushButton { background-color: white;
                                                color: black;
                                                border-width: 2px;
                                                border-radius: 15px;
                                                padding: 4px;
                                                font-family: Comic Sans MS;
                                                font-size: 36px }
                                QPushButton:pressed {background-color: rgb(200, 200, 200)}""")
        vbox_button_layout.addWidget(button)


