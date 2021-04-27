from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget

class TiltWidget(QWidget):
    def __init__(self, parent=None, minimumWidth=200, minimumHeight = 130, tiltVal = 0, labelTilt=None):
        super(TiltWidget, self).__init__(parent)
        self.setMinimumSize(minimumWidth, minimumHeight)
        self.tiltVal = tiltVal
        self.labelTilt = labelTilt
        self.maxDistance = 64


    def paintEvent(self, event):
        painter = QPainter(self)

        painter.drawEllipse(35, 0, 128, 128)

        painter.setPen(QPen(Qt.black, 1))

        tiltLine1 = QLineF()
        tiltLine1.setP1(QPointF(100,65))
        tiltLine1.setAngle(self.tiltVal)
        tiltLine1.setLength(self.maxDistance)
        painter.drawLine(tiltLine1)

        tiltLine2 = QLineF()
        tiltLine2.setP1(QPointF(100, 65))
        tiltLine2.setAngle(self.tiltVal)
        tiltLine2.setLength(-self.maxDistance)
        painter.drawLine(tiltLine2)

        self.labelTilt.setText(str(self.tiltVal))

    def setTilt(self, tilt):
        self.tiltVal = tilt
        self.update()

