from PySide2.QtWidgets import QApplication, QPushButton
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)

    button = QPushButton("Hello world")
    button.show()

    app.exec_()
