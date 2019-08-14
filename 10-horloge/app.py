from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys

class MyWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__()

        # Un wiget carré 
        self.resize(600,600)
        self.dark = "#3B3A44"
        self.light ="#4a4953"
        self.color ="#75ECB5"

        # Création d'un timer qui appelle self.update() toutes les 1 sec
        # La fonction update() appelle paintEvent()
        self.timer = QTimer()
        self.timer.setInterval(1000)
        # Le signal timeout() connect self.update()
        self.timer.timeout.connect(self.update)
        # Lancement du timer
        self.timer.start()

        # # Decommenter pour avoir du windowsLess
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.setWindowFlag(Qt.FramelessWindowHint)



    def paintEvent(self, event: QPaintEvent):
        """ Dessine l'horloge """ 

        painter = QPainter(self)
        # Pour éviter d'avoir des traits pixelisés 
        painter.setRenderHint(QPainter.Antialiasing)  

        # Récupère la date de maintenant 
        datetime = QDateTime().currentDateTime()

        # Dessine le premier cercle dans un rectangle plus petit que le widget
        # Les marges sont à 20 
        base_rect = self.rect().adjusted(20,20,-20,-20)
        painter.setBrush(QBrush(QColor(self.dark)))
        painter.drawEllipse(base_rect)
        
        # Dessine le deuxième cercle dans un rectangle encore plus petit
        # Les marghes sont à 40 
        pen = QPen(QColor(self.light))
        pen.setWidth(30)
        pen.setCapStyle(Qt.RoundCap)
        painter.setPen(pen)
        arc_rect = base_rect.adjusted(40,40,-40,-40)
        painter.drawEllipse(arc_rect)

        # Dessine l'arc des secondes 
        pen.setColor(QColor(self.color))
        start_angle = 90
        span_angle = self.sec_to_angle(datetime.time().second())
        painter.setPen(pen)
        painter.drawArc(arc_rect, start_angle * 16, span_angle * 16 )

        ## Récupere les textes à dessiner 
        time = datetime.toString("hh:mm")
        day = datetime.toString("dddd")
        date = datetime.toString("dd/MM/yyyy")
        seconde = datetime.toString("ss")

        #Dessine l'heure
        painter.setPen(QPen(Qt.white))
        font = QFont()
        font.setPixelSize(90)
        painter.setFont(font) 
        painter.drawText(arc_rect, Qt.AlignCenter, time)

        #Dessine le jour
        font = QFont()
        font.setPixelSize(20)
        painter.setFont(font)
        arc_rect.moveTop(-60)
        painter.drawText(arc_rect, Qt.AlignCenter|Qt.AlignBottom, day)

        #Dessine la date 
        arc_rect.moveTop(-20)
        painter.drawText(arc_rect, Qt.AlignCenter|Qt.AlignBottom, date)

        #Dessine les secondes 
        arc_rect.moveTop(-120)
        painter.setPen(QPen(self.color))
        painter.drawText(arc_rect, Qt.AlignCenter|Qt.AlignTop, seconde)



    def sec_to_angle(self, sec):
        """ retourne l'angle à partir des secondes """ 
        return -sec * 360 / 60

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.move(800,300)
    w.show()


    app.exec_()