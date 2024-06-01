import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class PyQtApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Example')

        self.layout = QVBoxLayout()

        self.label = QLabel('Hello, PyQt5!', self)
        self.layout.addWidget(self.label)

        self.button = QPushButton('Click me', self)
        self.button.clicked.connect(self.on_click)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def on_click(self):
        self.label.setText('Button Clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyQtApp()
    ex.show()
    sys.exit(app.exec_())
