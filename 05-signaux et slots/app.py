from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys


class MyWidget(QWidget):

    validated = Signal()

    def __init__(self, parent=None):
        super().__init__()

        self.edit = QLineEdit("hello")
        self.btn = QPushButton("valider")

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.btn.clicked.connect(self.on_press)

    def on_press(self):

        btn = self.sender()
        btn.setDisabled(True)

        if self.edit.text() == "boby":
            self.validated.emit()


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = MyWidget()
    w.show()

    app.exec_()
