from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QWidget, QPushButton, QTextBrowser, QLabel, QGridLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout()

        label_1 = QLabel("Subjekt")
        layout.addWidget(label_1, 1, 1, 1, 4)

        push_button_1_1 = QPushButton("Hansi")
        push_button_1_1.pressed.connect(self.handle_first_row)
        layout.addWidget(push_button_1_1, 2, 1)

        push_button_1_2 = QPushButton("Das Auto")
        push_button_1_2.pressed.connect(self.handle_first_row)
        layout.addWidget(push_button_1_2, 2, 2)

        push_button_1_3 = QPushButton("Herr Hey")
        push_button_1_3.pressed.connect(self.handle_first_row)
        layout.addWidget(push_button_1_3, 2, 3)

        push_button_1_4 = QPushButton("Deine Mutter")
        push_button_1_4.pressed.connect(self.handle_first_row)
        layout.addWidget(push_button_1_4, 2, 4)

        label_2 = QLabel("Prädikat")
        layout.addWidget(label_2, 3, 1, 1, 4)

        push_button_2_1 = QPushButton("trägt")
        push_button_2_1.pressed.connect(self.handle_first_row)
        layout.addWidget(push_button_2_1, 4, 1)

        push_button_2_2 = QPushButton("isst")
        push_button_2_2.pressed.connect(self.handle_first_row)
        layout.addWidget(push_button_2_2, 4, 2)

        push_button_2_3 = QPushButton("sieht")
        push_button_2_3.pressed.connect(self.handle_first_row)
        layout.addWidget(push_button_2_3, 4, 3)

        push_button_2_4 = QPushButton("trinkt")
        push_button_2_4.pressed.connect(self.handle_first_row)
        layout.addWidget(push_button_2_4, 4, 4)

        label_3 = QLabel("Objekt")
        layout.addWidget(label_3, 5, 1, 1, 4)

        push_button_3_1 = QPushButton("einen Porsche.")
        push_button_3_1.pressed.connect(self.handle_last_row)
        layout.addWidget(push_button_3_1, 6, 1)

        push_button_3_2 = QPushButton("Pommes.")
        push_button_3_2.pressed.connect(self.handle_last_row)
        layout.addWidget(push_button_3_2, 6, 2)

        push_button_3_3 = QPushButton("Cola.")
        push_button_3_3.pressed.connect(self.handle_last_row)
        layout.addWidget(push_button_3_3, 6, 3)

        push_button_3_4 = QPushButton("die Sterne.")
        push_button_3_4.pressed.connect(self.handle_last_row)
        layout.addWidget(push_button_3_4, 6, 4)

        label_4 = QLabel("Textausgabe:")
        layout.addWidget(label_4, 7, 1, 1, 4)

        self.text_browser = QTextBrowser()
        layout.addWidget(self.text_browser, 8, 1, 1, 4)

        self.setLayout(layout)

    @pyqtSlot()
    def handle_first_row(self):
        text = self.text_browser.toPlainText()
        text += self.sender().text() + " "

        self.text_browser.setText(text)

    @pyqtSlot()
    def handle_last_row(self):
        text = self.text_browser.toPlainText()
        text += self.sender().text() + "\n"

        self.text_browser.setText(text)


