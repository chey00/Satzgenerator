from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QTextBrowser, QLabel, QGridLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout()

        label_1 = QLabel("Subjekt")
        layout.addWidget(label_1, 1, 1, 1, 4)

        self.push_button_1_1 = QPushButton("Hansi")
        self.push_button_1_1.pressed.connect(self.handle_1)
        layout.addWidget(self.push_button_1_1, 2, 1)

        self.push_button_1_2 = QPushButton("Das Auto")
        self.push_button_1_2.pressed.connect(self.handle_1)
        layout.addWidget(self.push_button_1_2, 2, 2)

        self.push_button_1_3 = QPushButton("Herr Hey")
        self.push_button_1_3.pressed.connect(self.handle_1)
        layout.addWidget(self.push_button_1_3, 2, 3)

        self.push_button_1_4 = QPushButton("Deine Mutter")
        self.push_button_1_4.pressed.connect(self.handle_1)
        layout.addWidget(self.push_button_1_4, 2, 4)

        label_2 = QLabel("Prädikat")
        layout.addWidget(label_2, 3, 1, 1, 4)

        self.push_button_2_1 = QPushButton("trägt")
        self.push_button_2_1.pressed.connect(self.handle_2)
        layout.addWidget(self.push_button_2_1, 4, 1)

        self.push_button_2_2 = QPushButton("isst")
        self.push_button_2_2.pressed.connect(self.handle_2)
        layout.addWidget(self.push_button_2_2, 4, 2)

        self.push_button_2_3 = QPushButton("sieht")
        self.push_button_2_3.pressed.connect(self.handle_2)
        layout.addWidget(self.push_button_2_3, 4, 3)

        self.push_button_2_4 = QPushButton("trinkt")
        self.push_button_2_4.pressed.connect(self.handle_2)
        layout.addWidget(self.push_button_2_4, 4, 4)

        self.disable_buttons_2(True)

        label_3 = QLabel("Objekt")
        layout.addWidget(label_3, 5, 1, 1, 4)

        self.push_button_3_1 = QPushButton("einen Porsche.")
        self.push_button_3_1.pressed.connect(self.handle_3)
        layout.addWidget(self.push_button_3_1, 6, 1)

        self.push_button_3_2 = QPushButton("Pommes.")
        self.push_button_3_2.pressed.connect(self.handle_3)
        layout.addWidget(self.push_button_3_2, 6, 2)

        self.push_button_3_3 = QPushButton("Cola.")
        self.push_button_3_3.pressed.connect(self.handle_3)
        layout.addWidget(self.push_button_3_3, 6, 3)

        self.push_button_3_4 = QPushButton("die Sterne.")
        self.push_button_3_4.pressed.connect(self.handle_3)
        layout.addWidget(self.push_button_3_4, 6, 4)

        self.disable_buttons_3(True)

        label_4 = QLabel("Textausgabe:")
        layout.addWidget(label_4, 7, 1, 1, 4)

        self.text_browser = QTextBrowser()
        layout.addWidget(self.text_browser, 8, 1, 1, 4)

        self.setLayout(layout)
        
    def disable_buttons_1(self, disable):
        self.push_button_1_1.setDisabled(disable)
        self.push_button_1_2.setDisabled(disable)
        self.push_button_1_3.setDisabled(disable)
        self.push_button_1_4.setDisabled(disable)

    def disable_buttons_2(self, disable):
        self.push_button_2_1.setDisabled(disable)
        self.push_button_2_2.setDisabled(disable)
        self.push_button_2_3.setDisabled(disable)
        self.push_button_2_4.setDisabled(disable)

    def disable_buttons_3(self, disable):
        self.push_button_3_1.setDisabled(disable)
        self.push_button_3_2.setDisabled(disable)
        self.push_button_3_3.setDisabled(disable)
        self.push_button_3_4.setDisabled(disable)

    @pyqtSlot()
    def handle_1(self):
        text = self.text_browser.toPlainText()
        text += self.sender().text() + " "

        self.text_browser.setText(text)

        self.disable_buttons_1(True)
        self.disable_buttons_2(False)

    @pyqtSlot()
    def handle_2(self):
        text = self.text_browser.toPlainText()
        text += self.sender().text() + " "

        self.text_browser.setText(text)

        self.disable_buttons_2(True)
        self.disable_buttons_3(False)


    @pyqtSlot()
    def handle_3(self):
        text = self.text_browser.toPlainText()
        text += self.sender().text() + "\n"

        self.text_browser.setText(text)

        self.disable_buttons_3(True)
        self.disable_buttons_1(False)


