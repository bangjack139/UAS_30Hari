import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QWidget
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def _init_(self):
        super()._init_()

        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)
        
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(35)
        self.layout.addWidget(self.display)

        self.create_buttons()

    def create_buttons(self):
        buttons_layout = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(50, 50)
            buttons_layout.addWidget(button, row, col)
            button.clicked.connect(self.on_button_click)

        self.layout.addLayout(buttons_layout)

    def on_button_click(self):
        button_text = self.sender().text()

        if button_text == 'C':
            self.display.clear()
        elif button_text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText('Error')
        else:
            self.display.setText(self.display.text() + button_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())