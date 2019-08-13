from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import datetime 

class MyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__()


    def paintEvent(self, event: QPaintEvent):
        
        painter = QPainter(self)
        painter.setPen(QPen(QColor("green")))
        painter.save()
        painter.translate(self.rect().center())
        painter.rotate(45)
        painter.translate(-self.rect().center())

        brush = QBrush(QColor("red"))
        pen = QPen(QColor("blue"))
        pen.setWidth(5)

        painter.setBrush(brush)
        painter.setPen(pen)

        rect = QRect(0,0,200,200)
        rect.moveCenter(self.rect().center())
        painter.drawRect(rect) 
        painter.restore()

        painter.drawText(rect, Qt.AlignCenter, "Hello")



if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWidget()
    w.move(800,300)
    w.show()


    app.exec_()