from PyQt6.QtWidgets import QWidget, QPushButton, QTextBrowser, QLabel, QGridLayout


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout()

        label_1 = QLabel("Subjekt")
        layout.addWidget(label_1, 1, 1, 1, 4)

        push_button_1_1 = QPushButton("Hansi")
        layout.addWidget(push_button_1_1, 2, 1)
        push_button_1_2 = QPushButton("Das Auto")
        layout.addWidget(push_button_1_2, 2, 2)
        push_button_1_3 = QPushButton("Herr Hey")
        layout.addWidget(push_button_1_3, 2, 3)
        push_button_1_4 = QPushButton("Deine Mutter")
        layout.addWidget(push_button_1_4, 2, 4)

        label_2 = QLabel("Prädikat")
        layout.addWidget(label_2, 3, 1, 1, 4)

        push_button_2_1 = QPushButton("trägt")
        layout.addWidget(push_button_2_1, 4, 1)
        push_button_2_2 = QPushButton("isst")
        layout.addWidget(push_button_2_2, 4, 2)
        push_button_2_3 = QPushButton("sieht")
        layout.addWidget(push_button_2_3, 4, 3)
        push_button_2_4 = QPushButton("trinkt")
        layout.addWidget(push_button_2_4, 4, 4)

        label_3 = QLabel("Objekt")
        layout.addWidget(label_3, 5, 1, 1, 4)

        push_button_3_1 = QPushButton("einen Porsche.")
        layout.addWidget(push_button_3_1, 6, 1)
        push_button_3_2 = QPushButton("Pommes.")
        layout.addWidget(push_button_3_2, 6, 2)
        push_button_3_3 = QPushButton("Cola.")
        layout.addWidget(push_button_3_3, 6, 3)
        push_button_3_4 = QPushButton("die Sterne.")
        layout.addWidget(push_button_3_4, 6, 4)

        label_4 = QLabel("Textausgabe:")
        layout.addWidget(label_4, 7, 1, 1, 4)

        self.text_browser = QTextBrowser()
        layout.addWidget(self.text_browser, 8, 1, 1, 4)

        self.setLayout(layout)


