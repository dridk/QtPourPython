from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import datetime 

class MyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__()


    def paintEvent(self, event: QPaintEvent):
        print("hello")
        super().paintEvent(event)

    def keyPressEvent(self, event: QKeyEvent):
        
        if event.key() == Qt.Key_A and event.modifiers() == Qt.ControlModifier:
            print("yes")

        super().keyPressEvent(event)

    def mousePressEvent(self, event: QMouseEvent):
        print(event.pos())
        super().mousePressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWidget()
    w.move(800,300)
    w.show()


    app.exec_()