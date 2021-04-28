from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget

class DirectionWidget(QWidget):
    def __init__(self, parent=None, minimumWidth=200, minimumHeight = 130, directionVal = 0, val=0, labelVal=None, type=None, marble=None):
        super(DirectionWidget, self).__init__(parent)
        self.setMinimumSize(minimumWidth, minimumHeight)
        self.maxDistance = 64
        self.directionVal = directionVal
        self.val = val
        self.labelVal = labelVal
        self.type = type
        self.marble = marble

    def paintEvent(self, event):
        self.directionVal = 90 - self.directionVal
        if self.directionVal < 0:
            self.directionVal += 360


        painter = QPainter(self)

        painter.drawEllipse(35, 0, 128, 128)

        if self.type == "speed":
            painter.setPen(QPen(Qt.darkGreen, 2))
            self.marble.updateSpeedDirection(self.val, self.directionVal)
        if self.type == "accel":
            painter.setPen(QPen(Qt.darkRed, 2))
            self.marble.updateAccelDirection(self.val, self.directionVal)

        directionLine = QLineF()
        directionLine.setP1(QPointF(100,65))
        directionLine.setAngle(self.directionVal)
        directionLine.setLength(self.maxDistance)
        painter.drawLine(directionLine)
        painter.end()

        self.labelVal.setText(str(self.val))

    def setVal(self, val):
        self.val = val
        self.update()

    def setDirection(self, direction):
        self.directionVal = direction
        self.update()


