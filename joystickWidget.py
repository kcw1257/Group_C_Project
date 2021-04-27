from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget

class Joystick(QWidget):
    def __init__(self, parent=None, minimumWidth=120, minimumHeight = 120,labelX=None, labelY=None):
        super(Joystick, self).__init__(parent)
        self.setMinimumSize(minimumWidth, minimumHeight)
        self.center = QPoint(minimumWidth/2,minimumHeight/2)
        self.maxDistance = 50
        self.cursor = QPoint(60,60)
        self.grabJoystick = False
        self.xControlVal = 0
        self.yControlVal = 0
        self.labelX = labelX
        self.labelY = labelY

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2))
        painter.drawRect(10, 10, self.minimumWidth()-20, self.minimumHeight()-20)
        painter.setBrush(Qt.black)
        painter.drawEllipse(self.cursor,15,15)

    def joystickBoundaries(self, event):
        self.cursor = event.pos()
        rightBound = self.center.x() + 50
        leftBound = self.center.x() - 50
        upperBound = self.center.y() + 50
        lowerBound = self.center.y() - 50
        if self.cursor.x() > rightBound:
            self.cursor.setX(rightBound)
        if self.cursor.x() < leftBound:
            self.cursor.setX(leftBound)
        if self.cursor.y() > upperBound:
            self.cursor.setY(upperBound)
        if self.cursor.y() < lowerBound:
            self.cursor.setY(lowerBound)
        limitLine = QLineF(self.center, self.cursor)

        directionAngle = 90 - limitLine.angle()
        if directionAngle < 0:
            directionAngle += 360

        self.xControlVal = self.cursor.x() - 60
        self.yControlVal = 60 - self.cursor.y()

        self.labelX.updateFromJoystick(self.xControlVal)
        self.labelY.updateFromJoystick(self.yControlVal)

        self.update()

    def mousePressEvent(self, event):
        self.grabJoystick = True
        self.joystickBoundaries(event)

    def mouseReleaseEvent(self, event):
        self.grabJoystick = False
        self.update()

    def mouseMoveEvent(self, event):
        if self.grabJoystick:
            self.joystickBoundaries(event)

    def moveCursor(self, controlVal, axis):
        if axis == "x":
            self.cursor.setX(self.center.x() + controlVal)
        if axis == "y":
            self.cursor.setY(self.center.y() - controlVal)
        self.update()







