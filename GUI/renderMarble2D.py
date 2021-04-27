from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets, QtGui

class RenderMarble(QWidget):
    def __init__(self, parent=None, minimumWidth=1280, minimumHeight=720, xPos=0, yPos=0, mazeWidth=0, mazeHeight=0, mazeX=0, mazeY=0,
                 labelCoodVal=None, speed=None, accel=None, speedVal=0, accelVal=0):
        super(RenderMarble, self).__init__(parent)
        self.setMinimumSize(minimumWidth,minimumHeight)
        self.labelCoodVal = labelCoodVal
        self.speedDirection = speed.directionVal
        self.accelDirection = accel.directionVal
        self.mazeHeight = mazeHeight
        self.mazeX = mazeX
        self.mazeY = mazeY
        self.xPos = yPos - self.mazeX
        self.yPos = self.mazeHeight - xPos - self.mazeY
        self.speedVal = speed.val
        self.accelVal = accel.val

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 0, 1280, 720)
        self.label.setAlignment(Qt.AlignCenter)
        self.canvas = QtGui.QPixmap(mazeWidth,mazeHeight)
        self.canvas.fill(Qt.transparent)

    def paintEvent(self, event):
        self.canvas.fill(Qt.transparent)
        # self.speedDirectionVal = self.speedDirection
        # self.speedDirectionVal = 90 - self.speedDirectionVal
        # if self.speedDirectionVal < 0:
        #     self.speedDirectionVal += 360
        #
        # self.accelDirectionVal = self.accelDirection
        # self.accelDirectionVal = 90 - self.accelDirectionVal
        # if self.accelDirectionVal < 0:
        #     self.accelDirectionVal += 360

        painter = QPainter(self.canvas)
        painter.setBrush(Qt.darkBlue)
        painter.drawEllipse(QPoint(self.xPos,self.yPos),15,15)

        painter.setPen(QPen(Qt.darkGreen, 2))
        directionLineS = QLineF()
        directionLineS.setP1(QPointF(self.xPos, self.yPos))
        directionLineS.setAngle(self.speedDirection)
        directionLineS.setLength(self.speedVal)
        painter.drawLine(directionLineS)

        painter.setPen(QPen(Qt.darkRed, 2))
        directionLineA = QLineF()
        directionLineA.setP1(QPointF(self.xPos, self.yPos))
        directionLineA.setAngle(self.accelDirection)
        directionLineA.setLength(self.accelVal)
        painter.drawLine(directionLineA)
        painter.end()

        self.canvas2 = self.canvas.scaledToHeight(720)
        self.label.setPixmap(self.canvas2)

    def updateCood(self, xPos, yPos):
        self.xPos = yPos - self.mazeX
        self.yPos = self.mazeHeight - xPos - self.mazeY
        self.labelCoodVal.setText(f"({self.xPos},{self.yPos})")
        self.update()

    def updateSpeedDirection(self, speedVal, speedDirection):
        self.speedVal = speedVal
        self.speedDirection = speedDirection
        self.update()

    def updateAccelDirection(self, accelVal, accelDirection):
        self.accelVal = accelVal
        self.accelDirection = accelDirection
        self.update()
