from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets, QtGui, QtCore

class ReplayWidget(QWidget):
    def __init__(self, parent=None, frameData=[], marble=None, speed=None, accel=None, tiltX=None, tiltY=None):
        super(ReplayWidget, self).__init__(parent)
        font = QtGui.QFont()
        self.marble = marble
        self.frameData = frameData
        self.speed = speed
        self.accel = accel
        self.tiltX = tiltX
        self.tiltY = tiltY

        self.horizontalSliderReplay = QtWidgets.QSlider(self)
        self.horizontalSliderReplay.setGeometry(QtCore.QRect(10, 10, 580, 22))
        self.horizontalSliderReplay.setOrientation(QtCore.Qt.Horizontal)

        self.labelTime = QtWidgets.QLabel(self)
        self.labelTime.setGeometry(QtCore.QRect(220, 30, 81, 31))
        font.setPointSize(14)
        self.labelTime.setFont(font)
        self.labelTime.setText("00:00:00")

        self.labelFrames = QtWidgets.QLabel(self)
        self.labelFrames.setGeometry(QtCore.QRect(300, 30, 299, 31))
        font.setPointSize(14)
        self.labelFrames.setFont(font)
        self.labelFrames.setText(f"(0/{len(frameData)-1})")

        self.frameReplayControlBottom = QtWidgets.QFrame(self)
        self.frameReplayControlBottom.setGeometry(QtCore.QRect(0, 60, 600, 40))
        self.frameReplayControlBottom.setFrameShape(QtWidgets.QFrame.Box)
        self.frameReplayControlBottom.setFrameShadow(QtWidgets.QFrame.Plain)

        self.buttonRewindHeavy = QtWidgets.QPushButton(self.frameReplayControlBottom)
        self.buttonRewindHeavy.setGeometry(QtCore.QRect(115, 10, 70, 23))
        self.buttonRewindHeavy.setText("<<")
        self.buttonRewindHeavy.clicked.connect(self.updateRewindHeavy)

        self.buttonRewind = QtWidgets.QPushButton(self.frameReplayControlBottom)
        self.buttonRewind.setGeometry(QtCore.QRect(190, 10, 70, 23))
        self.buttonRewind.setText("<")
        self.buttonRewind.clicked.connect(self.updateRewind)

        self.buttonPlayReplay = QtWidgets.QPushButton(self.frameReplayControlBottom)
        self.buttonPlayReplay.setGeometry(QtCore.QRect(265, 10, 70, 23))
        self.buttonPlayReplay.setText("Play")
        self.buttonPlayReplay.clicked.connect(self.updatePlay)

        self.buttonFoward = QtWidgets.QPushButton(self.frameReplayControlBottom)
        self.buttonFoward.setGeometry(QtCore.QRect(340, 10, 70, 23))
        self.buttonFoward.setText(">")
        self.buttonFoward.clicked.connect(self.updateFoward)

        self.buttonFowardHeavy = QtWidgets.QPushButton(self.frameReplayControlBottom)
        self.buttonFowardHeavy.setGeometry(QtCore.QRect(415, 10, 70, 23))
        self.buttonFowardHeavy.setText(">>")
        self.buttonFowardHeavy.clicked.connect(self.updateFowardHeavy)

        ###############################################################################################################

        self.horizontalSliderReplay.setMinimum(0)
        self.horizontalSliderReplay.setMaximum(len(frameData)-1)
        self.horizontalSliderReplay.valueChanged.connect(self.updateFrame)

    def updateFrame(self):
        self.marbleCood = self.frameData[self.horizontalSliderReplay.value()].get("ballCood")
        self.marble.updateCood(self.marbleCood[0],self.marbleCood[1])
        self.labelFrames.setText(f"({self.horizontalSliderReplay.value()}/{len(self.frameData)-1})")
        msecond = self.horizontalSliderReplay.value() * 31.25
        second = msecond/1000
        minute = second/60
        msecondText = str(int(msecond%1000))
        secondText = str(int(second%60))
        minuteText = str(int(minute))
        if len(msecondText) == 3:
            msecondText = msecondText[:-1]
        if len(msecondText) == 1:
            msecondText = "0" + msecondText
        if len(secondText) == 1:
            secondText = "0" + secondText
        if len(minuteText) == 1:
            minuteText = "0" + minuteText
        self.labelTime.setText(f"{minuteText}:{secondText}:{msecondText}")

        self.speed.setVal(self.frameData[self.horizontalSliderReplay.value()].get("speed"))
        self.speed.setDirection(self.frameData[self.horizontalSliderReplay.value()].get("speedDirection"))
        self.accel.setVal(self.frameData[self.horizontalSliderReplay.value()].get("acceleration"))
        self.accel.setDirection(self.frameData[self.horizontalSliderReplay.value()].get("accelerationDirection"))
        self.tiltX.setTilt(self.frameData[self.horizontalSliderReplay.value()].get("xTilt"))
        self.tiltY.setTilt(self.frameData[self.horizontalSliderReplay.value()].get("yTilt"))


    def updateFoward(self):
        self.horizontalSliderReplay.setValue(self.horizontalSliderReplay.value()+1)

    def updateFowardHeavy(self):
        self.horizontalSliderReplay.setValue(self.horizontalSliderReplay.value()+32)

    def updateRewind(self):
        self.horizontalSliderReplay.setValue(self.horizontalSliderReplay.value()-1)

    def updateRewindHeavy(self):
        self.horizontalSliderReplay.setValue(self.horizontalSliderReplay.value()-32)

    def updatePlay(self):
        if self.buttonPlayReplay.text() == "Play":
            self.buttonPlayReplay.setText("Stop")
            self.counter = 0
            self.timer = QtCore.QTimer()
            self.timer.start(31)
            self.timer.timeout.connect(self.time)
        else:
            self.buttonPlayReplay.setText("Play")
            self.timer.stop()

    def time(self):
        if self.counter == 3:
            self.horizontalSliderReplay.setValue(self.horizontalSliderReplay.value() + 2)   #to get a delay of 31.25ms (32 fps)
            self.counter = 0

        else:
            self.counter += 1
            self.horizontalSliderReplay.setValue(self.horizontalSliderReplay.value()+1)








