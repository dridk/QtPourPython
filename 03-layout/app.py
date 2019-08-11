from PySide2.QtWidgets import *
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)

    bt1 = QPushButton("bt1")
    bt2 = QPushButton("bt2")
    bt3 = QPushButton("bt3")

    layout2 = QHBoxLayout()
    layout2.addWidget(QPushButton("ok"))
    layout2.addWidget(QPushButton("cancel"))

    layout = QVBoxLayout()
    layout.addWidget(bt1)
    layout.addWidget(bt2)
    layout.addStretch()
    layout.addLayout(layout2)

    widget = QWidget()
    widget.setLayout(layout)
    widget.show()

    app.exec_()
