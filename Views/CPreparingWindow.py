from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QFrame, QLabel, QMainWindow

class CPreparingWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setFixedSize(900, 450)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.prepare_layout()
        self.move(900, 100)


    def prepare_layout(self):
        main_view = QFrame()
        main_view.setObjectName("CPreparingWindowView")
        main_view.setStyleSheet("""QFrame#CPreparingWindowView {background-image: url(Resources/images/backgrounds/prepare-background.png);
                                                                border-width: 2px;}""")
        vbox_main_layout = QVBoxLayout()
        vbox_main_layout.setAlignment(QtCore.Qt.AlignTop)
        vbox_main_layout.setContentsMargins(2, 2, 2, 2)
        vbox_main_layout.setSpacing(0)
        main_view.setLayout(vbox_main_layout)

        self.setCentralWidget(main_view)


        # TITLE BAR
        title_bar = QFrame()
        title_bar.setFixedSize(500, 36)
        vbox_main_layout.addWidget(title_bar)

        # TOP PART
        top_part = QFrame()
        top_part.setFixedHeight(238)
        top_part.setObjectName("TopPart")
        top_part.setStyleSheet("""QFrame#TopPart { background-image: url(Resources/images/backgrounds/prepare-top-part.png); }""")
        vbox_main_layout.addWidget(top_part)

        # BOTTOM PART
        hbox_bottom_layout = QHBoxLayout()
        hbox_bottom_layout.setAlignment(QtCore.Qt.AlignTop)
        vbox_main_layout.addLayout(hbox_bottom_layout)

        parts_detail = {
            "Number" : ["100090", "100060", "100035"],
            "Number of wells" : ["96", "48", "24", "12", "6"],
            "Size (mm)" : ["38000S2CL", "38000S6CL", "38000S8CL"]
        }
        for k, v in parts_detail.items():
            bottom_part_element = QWidget()

            vbox_bottom_part_layout = QVBoxLayout()
            vbox_bottom_part_layout.setAlignment(QtCore.Qt.AlignTop)
            bottom_part_element.setLayout(vbox_bottom_part_layout)


            bottom_part_element.setFixedSize(299, 176)
            hbox_bottom_layout.addWidget(bottom_part_element)
            hbox_bottom_layout.setSpacing(1)

            # TEXT
            label = QLabel()
            label.setText(k)
            label.setObjectName("PreparingWindowLabel")
            label.setStyleSheet("""QLabel#PreparingWindowLabel { font-size: 18px }""")
            vbox_bottom_part_layout.addWidget(label)

            combo_box = QComboBox()
            combo_box.setObjectName("PreparingWindowComboBox")
            combo_box.addItems(v)
            bottom_part_element.setStyleSheet(
                """QComboBox#PreparingWindowComboBox { background-color: white;
                                                        padding: 6px;
                                                        font-size: 18px}""")
            vbox_bottom_part_layout.addWidget(combo_box)
