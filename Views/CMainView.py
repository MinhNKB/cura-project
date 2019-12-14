from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton
from Controls.CTabPivot import CTabPivot
from Views.CPreparingWindow import CPreparingWindow

class CMainView(QFrame):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setStyleSheet("CMainView {background-image: url(Resources/images/backgrounds/main-background.png);}")
        self.prepare_layout()
        self.preparing_window = None

    def prepare_layout(self):
        vbox_main_layout = QVBoxLayout()
        vbox_main_layout.setAlignment(QtCore.Qt.AlignTop)
        vbox_main_layout.setContentsMargins(0, 0, 0, 0)
        vbox_main_layout.setSpacing(0)

        self.setLayout(vbox_main_layout)

        # TITLE BAR
        title_bar = QFrame()
        title_bar.setFixedHeight(24)
        vbox_main_layout.addWidget(title_bar)

        # TABS
        hbox_tab_layout = QHBoxLayout()
        hbox_tab_layout.setAlignment(QtCore.Qt.AlignLeft)
        vbox_main_layout.addLayout(hbox_tab_layout)
        tab_texts = ["Preparing", "Material", "File", "Layers", "Control", "Generation"]
        for tab_text in tab_texts:
            progress_tab = CTabPivot(tab_text)
            progress_tab.clicked.connect(self.tab_clicked)
            progress_tab.setFixedSize(200, 56)
            hbox_tab_layout.addWidget(progress_tab)
            hbox_tab_layout.addSpacing(1)

        # CONTENT VIEW
        content_frame = QFrame()
        content_frame.setFixedHeight(1080-56-24)
        hbox_content_layout = QHBoxLayout()
        hbox_content_layout.setAlignment(QtCore.Qt.AlignLeft)
        hbox_content_layout.setContentsMargins(0, 0, 12, 12)
        content_frame.setLayout(hbox_content_layout)
        vbox_main_layout.addWidget(content_frame)

        # LEFT MENU
        vbox_left_menu_layout = QVBoxLayout()
        vbox_left_menu_layout.setAlignment(QtCore.Qt.AlignVCenter)
        hbox_content_layout.addLayout(vbox_left_menu_layout)

        for i in range(8):
            left_menu_button = QFrame()
            button_name = "LeftMenuButton" + str(i+1)
            button_icon_path = "url(Resources/images/icons/icon-%d.png)" % (i+1)
            left_menu_button.setObjectName(button_name)
            left_menu_button.setFixedSize(48, 48)
            left_menu_button.setStyleSheet("""QFrame#%s {background-image: %s;}
                                            QFrame#%s:pressed {background-image: url(Resources/images/icons/icon-1.png)
                                            """ % (button_name, button_icon_path, button_name))
            vbox_left_menu_layout.addWidget(left_menu_button)
            vbox_left_menu_layout.addSpacing(1)


        # GRAPH VIEW
        graph_frame = QFrame()
        graph_frame.setFixedSize(1600, 1080-56-24)
        hbox_content_layout.addWidget(graph_frame)


        # BUTTON
        button = QPushButton()
        button.setText("Generation")
        button.setFixedSize(200, 50)
        button.setStyleSheet("""QPushButton { background-color: orange;
                                               color: white;
                                               border-width: 2px;
                                               border-radius: 15px;
                                               padding: 4px;
                                               font-family: Comic Sans MS;
                                               font-size: 12px }
                                 QPushButton:pressed {background-color: rgb(200, 200, 200)}""")
        hbox_content_layout.addWidget(button, alignment = QtCore.Qt.AlignBottom)

    def tab_clicked(self):
        print("Clicked")
        if self.preparing_window is None:
            self.preparing_window = CPreparingWindow()
            self.preparing_window.show()
        else:
            self.preparing_window.activateWindow()
