from PySide2.QtWidgets import *
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)

    w = QPushButton("salut")

    w.move(600, 400)
    w.resize(600, 200)

    w.show()

    w.setWindowTitle("ceci est mon application")

    app.exec_()
