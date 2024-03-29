from PyQt5 import QtCore, QtGui, QtWidgets
import motor_sync_control

class LabelWidget(QtWidgets.QLabel):
    def __init__(self, parent=None, controlVal = 0, joystick=None,slider=None,cood=[0,0],axis=None):
        super(LabelWidget, self).__init__(parent)
        self.controlVal = controlVal
        self.axis = axis

        font = QtGui.QFont()
        self.setGeometry(QtCore.QRect(cood[0], cood[1], 121, 30))
        font.setPointSize(12)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.setFrameShape(QtWidgets.QFrame.Box)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setText("0")

        self.slider = slider
        self.joystick = joystick

    def updateFromJoystick(self, controlVal):
        self.slider.setValue(controlVal)
        self.updateVal(controlVal)

    def updateVal(self, controlVal):
        self.controlVal = controlVal
        self.setText(str(controlVal))
        motor_sync_control.move(controlVal, axis)

    def updateFromSlider(self, controlVal,axis):
        if not self.joystick.grabJoystick:
            self.joystick.moveCursor(controlVal,axis)
            self.updateVal(controlVal)

    def resetTilt(self, axis):
        controlVal = 0
        self.updateFromSlider(controlVal, axis)
        self.updateFromJoystick(controlVal)