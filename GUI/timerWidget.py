from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets, QtOpenGL

class TimerWidget(QtWidgets.QFrame):
    def __init__(self, parent=None, buttonStart=None, buttonClear=None, stackedWidget=None):
        super(TimerWidget, self).__init__(parent)

        self.buttonStart = buttonStart
        self.buttonClear = buttonClear
        self.start = False
        self.stackedWidget = stackedWidget

        self.setGeometry(QtCore.QRect(685, 785, 231, 61))
        self.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.setFrameShape(QtWidgets.QFrame.Box)
        self.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameTimerValue = QtWidgets.QFrame(self)
        self.frameTimerValue.setGeometry(QtCore.QRect(0, 0, 231, 41))
        self.frameTimerValue.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.frameTimerValue.setFrameShape(QtWidgets.QFrame.Box)
        self.frameTimerValue.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameTimerValue.setLineWidth(1)

        self.labelMinVal = QtWidgets.QLabel(self.frameTimerValue)
        self.labelMinVal.setGeometry(QtCore.QRect(10, 0, 60, 41))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.labelMinVal.setFont(font)
        self.labelMinVal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelMinVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelMinVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMinVal.setText("00")

        self.labelSecVal = QtWidgets.QLabel(self.frameTimerValue)
        self.labelSecVal.setGeometry(QtCore.QRect(90, 0, 61, 41))
        font.setPointSize(32)
        self.labelSecVal.setFont(font)
        self.labelSecVal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelSecVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSecVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSecVal.setText("00")

        self.labelMsVal = QtWidgets.QLabel(self.frameTimerValue)
        self.labelMsVal.setGeometry(QtCore.QRect(170, 0, 51, 41))
        font.setPointSize(32)
        self.labelMsVal.setFont(font)
        self.labelMsVal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelMsVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelMsVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMsVal.setText("00")

        self.labelColonL = QtWidgets.QLabel(self.frameTimerValue)
        self.labelColonL.setGeometry(QtCore.QRect(71, 1, 19, 39))
        font.setPointSize(18)
        self.labelColonL.setFont(font)
        self.labelColonL.setAlignment(QtCore.Qt.AlignCenter)
        self.labelColonL.setText(":")

        self.labelColonR = QtWidgets.QLabel(self.frameTimerValue)
        self.labelColonR.setGeometry(QtCore.QRect(151, 1, 19, 39))
        font.setPointSize(18)
        self.labelColonR.setFont(font)
        self.labelColonR.setAlignment(QtCore.Qt.AlignCenter)
        self.labelColonR.setText(":")

        self.labelMin = QtWidgets.QLabel(self)
        self.labelMin.setGeometry(QtCore.QRect(10, 41, 61, 16))
        font.setPointSize(11)
        self.labelMin.setFont(font)
        self.labelMin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMin.setText("min")

        self.labelSec = QtWidgets.QLabel(self)
        self.labelSec.setGeometry(QtCore.QRect(90, 41, 61, 16))
        font.setPointSize(11)
        self.labelSec.setFont(font)
        self.labelSec.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSec.setText("sec")

        self.labelMs = QtWidgets.QLabel(self)
        self.labelMs.setGeometry(QtCore.QRect(175, 41, 41, 16))
        font.setPointSize(11)
        self.labelMs.setFont(font)
        self.labelMs.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMs.setText("ms")

    def time(self):
        self.currTime = self.currTime.addMSecs(10)
        self.minute = self.currTime.minute()
        self.second = self.currTime.second()
        self.msecond = self.currTime.msec()
        if self.minute < 10:
            self.minute = "0" + str(self.minute)
        if self.second < 10:
            self.second = "0" + str(self.second)
        if self.msecond < 100:
            self.msecond = "0" + str(self.msecond)
        self.labelMinVal.setText(str(self.minute))
        self.labelSecVal.setText(str(self.second))
        self.labelMsVal.setText(str(self.msecond)[:-1])
        if self.stackedWidget.currentIndex() != 1 and self.stackedWidget.currentIndex() != 2 and self.stackedWidget.currentIndex() != 7:
            self.timer.stop()
            self.labelMinVal.setText("00")
            self.labelSecVal.setText("00")
            self.labelMsVal.setText("00")
            self.buttonStart.setText("Start")
            self.start = False

    def timerClear(self):
        if not self.start:
            self.labelMinVal.setText("00")
            self.labelSecVal.setText("00")
            self.labelMsVal.setText("00")

    def timerClick(self):
        if not self.start:
            self.start = True
            self.currTime = QtCore.QTime(00, 00, 00)
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.time)
            self.timer.start(10)
            self.buttonStart.setText("Force Stop")
        else:
            self.start = False
            self.timer.stop()
            self.buttonStart.setText("Start")






