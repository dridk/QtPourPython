from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys


class CalcWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QVBoxLayout()

        line_edit = QLineEdit()

        operator_layout = QHBoxLayout()

        operator_layout.addWidget(QPushButton("+"))
        operator_layout.addWidget(QPushButton("-"))
        operator_layout.addWidget(QPushButton("/"))
        operator_layout.addWidget(QPushButton("*"))

        digits = list(range(10)) + [".", "C"]

        grid_layout = QGridLayout()

        for index, digit in enumerate(digits):

            x = int(index / 3)
            y = int(index % 3)
            btn = QPushButton(str(digit))
            grid_layout.addWidget(btn, x, y)

        line_edit.setMinimumHeight(50)
        line_edit.setAlignment(Qt.AlignRight)
        font = QFont()
        font.setPixelSize(30)
        line_edit.setFont(font)

        main_layout.addWidget(line_edit)
        main_layout.addLayout(operator_layout)
        main_layout.addLayout(grid_layout)

        main_layout.addWidget(QPushButton("egal"))

        self.setLayout(main_layout)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = CalcWidget()
    w.show()
    app.exec_()
