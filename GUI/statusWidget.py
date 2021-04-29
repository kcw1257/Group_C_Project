from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets, QtGui


class StatusWidget(QWidget):
    def __init__(self, parent=None):
        super(StatusWidget, self).__init__(parent)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(260,780,271,101)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelType = QtWidgets.QLabel(self)
        self.labelType.setGeometry(0,0,136,31)
        self.labelType.setText("Board Type:")
        self.labelType.setFont(font)
        self.labelType.setStyleSheet("background-color: rgb(202,202,202);")
        self.labelType.setFrameShape(QtWidgets.QFrame.Box)
        self.labelType.setAlignment(Qt.AlignCenter)

        self.labelTypeVal = QtWidgets.QLabel(self)
        self.labelTypeVal.setGeometry(135, 0, 136, 31)
        self.labelTypeVal.setText("Custom")
        self.labelTypeVal.setFont(font)
        self.labelTypeVal.setStyleSheet("background-color: rgb(255,255,255);")
        self.labelTypeVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelTypeVal.setAlignment(Qt.AlignCenter)

        self.labelStatus = QtWidgets.QLabel(self)
        self.labelStatus.setGeometry(0, 30, 136, 31)
        self.labelStatus.setText("Solve Status:")
        self.labelStatus.setFont(font)
        self.labelStatus.setStyleSheet("background-color: rgb(202,202,202);")
        self.labelStatus.setFrameShape(QtWidgets.QFrame.Box)
        self.labelStatus.setAlignment(Qt.AlignCenter)

        self.labelStatusVal = QtWidgets.QLabel(self)
        self.labelStatusVal.setGeometry(135, 30, 136, 31)
        self.labelStatusVal.setText("Not Started")
        self.labelStatusVal.setFont(font)
        self.labelStatusVal.setStyleSheet("background-color: rgb(255,255,255);")
        self.labelStatusVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelStatusVal.setAlignment(Qt.AlignCenter)

        font.setPointSize(10)
        self.labelMessage = QtWidgets.QLabel(self)
        self.labelMessage.setGeometry(0, 60, 271, 41)
        self.labelMessage.setText("Not Started")
        self.labelMessage.setFont(font)
        self.labelMessage.setStyleSheet("background-color: rgb(255,255,255);")
        self.labelMessage.setFrameShape(QtWidgets.QFrame.Box)
        self.labelMessage.setAlignment(Qt.AlignCenter)

    def updateStatus(self, status):
        if status == "not started":
            self.labelStatusVal.setText("Not Started")
            self.labelStatusVal.setStyleSheet("color: rgb(0,0,0)")
        if status == "in progress":
            self.labelStatusVal.setText("In Progress")
            self.labelStatusVal.setStyleSheet("color: rgb(0,0,0)")
        if status == "success":
            self.labelStatusVal.setText("Success!")
            self.labelStatusVal.setStyleSheet("color: rgb(0,255,0)")
        if status == "failure":
            self.labelStatusVal.setText("Failure...")
            self.labelStatusVal.setStyleSheet("color: rgb(255,0,0)")

    def updateType(self, type):
        if type == "Easy":
            self.labelTypeVal.setText("Easy")
        if type == "Medium":
            self.labelTypeVal.setText("Medium")
        if type == "Hard":
            self.labelTypeVal.setText("Hard")
        if type == "Custom":
            self.labelTypeVal.setText("Custom")

    def updateMessage(self, message):
        self.labelMessage.setText(message)
