from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys


class CalcWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_layout = QVBoxLayout()

        self.line_edit = QLineEdit()

        self.expressions = []
        self.after_operator = False

        operators = ["+", "-", "*", "/"]

        operator_layout = QHBoxLayout()
        for operator in operators:
            btn = QPushButton(operator)
            operator_layout.addWidget(btn)
            btn.clicked.connect(self.on_operator_press)

        digits = list(range(10)) + [".", "C"]

        grid_layout = QGridLayout()

        for index, digit in enumerate(digits):

            x = int(index / 3)
            y = int(index % 3)
            btn = QPushButton(str(digit))
            btn.clicked.connect(self.on_digit_press)
            grid_layout.addWidget(btn, x, y)

        self.line_edit.setMinimumHeight(50)
        self.line_edit.setAlignment(Qt.AlignRight)
        font = QFont()
        font.setPixelSize(30)
        self.line_edit.setReadOnly(True)
        self.line_edit.setFont(font)

        main_layout.addWidget(self.line_edit)
        main_layout.addLayout(operator_layout)
        main_layout.addLayout(grid_layout)
        egal_btn = QPushButton("egal")
        egal_btn.clicked.connect(self.on_egal_press)
        main_layout.addWidget(egal_btn)

        self.setLayout(main_layout)

    def set_value(self, value):
        if value.is_integer():
            self.line_edit.setText(str(int(value)))
        else:
            self.line_edit.setText(str(value))

    def get_value(self) -> float:
        return float(self.line_edit.text())

    def on_digit_press(self):

        digit = self.sender().text()
        text = self.line_edit.text()

        if self.after_operator:
            text = ""
            self.after_operator = False

        if digit in [str(i) for i in range(9)]:
            self.line_edit.setText(text + digit)

        if digit == "." and "." not in text:
            self.line_edit.setText(text + digit)

        if digit == "C":
            self.line_edit.clear()
            self.expressions.clear()
            self.after_operator = False

    def on_operator_press(self):
        symbol = self.sender().text()
        value = float(self.line_edit.text())
        self.expressions += [value, symbol]
        self.after_operator = True

    def on_egal_press(self):

        value = float(self.line_edit.text())
        self.expressions.append(value)

        if len(self.expressions) == 3:
            exp = "".join([str(i) for i in self.expressions])
            result = eval(exp)
            self.set_value(result)
            self.expressions.clear()
            self.after_operator = True


if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = CalcWidget()
    w.show()
    app.exec_()
