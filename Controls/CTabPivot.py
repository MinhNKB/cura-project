from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QLabel
from PyQt5.QtCore import pyqtSignal

class CTabPivot(QWidget):
    clicked = pyqtSignal()

    def __init__(self, label_text, parent=None):
        QWidget.__init__(self,parent)
        self.label_text = label_text
        self.prepare_layout()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()

    def prepare_layout(self):
        hbox_layout = QHBoxLayout()
        hbox_layout.setAlignment(QtCore.Qt.AlignVCenter)
        self.setLayout(hbox_layout)

        # CIRCLE IMAGE
        tab_image = QFrame()
        tab_image.setObjectName("TabImage")
        tab_image.setFixedSize(35, 35)
        tab_image.setStyleSheet("QFrame#TabImage {background-image: url(Resources/images/icons/icon-rounded.png);}")
        hbox_layout.addWidget(tab_image)

        # TEXT
        label = QLabel()
        label.setText(self.label_text)
        label.setFixedWidth(100)
        hbox_layout.addWidget(label)

        # ARROW IMAGE
        tab_image = QFrame()
        tab_image.setObjectName("ArrowImage")
        tab_image.setFixedSize(25, 25)
        tab_image.setStyleSheet("QFrame#ArrowImage {background-image: url(Resources/images/icons/icon-arrow.png);}")
        hbox_layout.addWidget(tab_image)