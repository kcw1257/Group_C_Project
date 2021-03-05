from PyQt5 import QtCore, QtGui, QtWidgets
import time

class Ui_MainWindow(object):
    def initUi(self, MainWindow):
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 900))

        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))

        self.pageHome = QtWidgets.QWidget()
        self.pageAuto = QtWidgets.QWidget()
        self.pageManual = QtWidgets.QWidget()
        self.pageDatabase = QtWidgets.QWidget()
        self.pageStats = QtWidgets.QWidget()
        self.pageAutoHelp = QtWidgets.QWidget()
        self.pageManualHelp = QtWidgets.QWidget()

        self.stackedWidget.addWidget(self.pageHome)
        self.stackedWidget.addWidget(self.pageAuto)
        self.stackedWidget.addWidget(self.pageManual)
        self.stackedWidget.addWidget(self.pageDatabase)
        self.stackedWidget.addWidget(self.pageStats)
        self.stackedWidget.addWidget(self.pageAutoHelp)
        self.stackedWidget.addWidget(self.pageManualHelp)

        self.pageHomeWidgets()
        self.pageAutoWidgets()
        self.pageManualWidgets()
        self.pageAutoHelpWidgets()
        self.pageManualHelpWidgets()

    def pageHomeWidgets(self):
        font = QtGui.QFont()

        self.buttonAuto = QtWidgets.QPushButton(self.pageHome)
        self.buttonAuto.setGeometry(QtCore.QRect(500, 150, 650, 140))
        font.setPointSize(32)
        self.buttonAuto.setFont(font)
        self.buttonAuto.setText("Automated Solve")
        self.buttonAuto.clicked.connect(self.switchPageAuto)

        self.buttonManual = QtWidgets.QPushButton(self.pageHome)
        self.buttonManual.setGeometry(QtCore.QRect(500, 300, 650, 140))
        font.setPointSize(32)
        self.buttonManual.setFont(font)
        self.buttonManual.setText("Manual Solve")
        self.buttonManual.clicked.connect(self.switchPageManual)

        self.buttonDatabase = QtWidgets.QPushButton(self.pageHome)
        self.buttonDatabase.setGeometry(QtCore.QRect(500, 450, 650, 140))
        font.setPointSize(32)
        self.buttonDatabase.setFont(font)
        self.buttonDatabase.setText("Database")

        self.buttonStats = QtWidgets.QPushButton(self.pageHome)
        self.buttonStats.setGeometry(QtCore.QRect(500, 600, 650, 140))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.buttonStats.setFont(font)
        self.buttonStats.setText("Stats")

        self.labelTitle = QtWidgets.QLabel(self.pageHome)
        self.labelTitle.setGeometry(QtCore.QRect(140, 10, 1320, 91))
        font.setPointSize(50)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setText("Group C's Automated Ball in the Maze Solver")

    def pageAutoWidgets(self):
        font = QtGui.QFont()

        self.buttonBack = QtWidgets.QPushButton(self.pageAuto)
        self.buttonBack.setGeometry(QtCore.QRect(20, 830, 81, 31))
        font.setPointSize(12)
        self.buttonBack.setFont(font)
        self.buttonBack.setText("Back")
        self.buttonBack.clicked.connect(self.switchPageHome)

        self.labelTitleAuto = QtWidgets.QLabel(self.pageAuto)
        self.labelTitleAuto.setGeometry(QtCore.QRect(140, 0, 1320, 60))
        font.setPointSize(32)
        self.labelTitleAuto.setFont(font)
        self.labelTitleAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitleAuto.setText("Automated Solve")

        self.frameVideo = QtWidgets.QFrame(self.pageAuto)
        self.frameVideo.setGeometry(QtCore.QRect(60, 60, 1280, 720))
        self.frameVideo.setFrameShape(QtWidgets.QFrame.Box)
        self.frameVideo.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frameInfo = QtWidgets.QFrame(self.pageAuto)
        self.frameInfo.setGeometry(QtCore.QRect(1340, 60, 200, 720))
        self.frameInfo.setFrameShape(QtWidgets.QFrame.Box)
        self.frameInfo.setFrameShadow(QtWidgets.QFrame.Raised)

        self.labelSpeed = QtWidgets.QLabel(self.frameInfo)
        self.labelSpeed.setGeometry(QtCore.QRect(0, 0, 200, 20))
        font.setPointSize(12)
        self.labelSpeed.setFont(font)
        self.labelSpeed.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelSpeed.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSpeed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelSpeed.setLineWidth(1)
        self.labelSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeed.setText("Speed")

        self.labelSpeedVal = QtWidgets.QLabel(self.frameInfo)
        self.labelSpeedVal.setGeometry(QtCore.QRect(0, 20, 200, 20))
        font.setPointSize(12)
        self.labelSpeedVal.setFont(font)
        self.labelSpeedVal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelSpeedVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSpeedVal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelSpeedVal.setLineWidth(1)
        self.labelSpeedVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeedVal.setText("0")

        self.labelAccel = QtWidgets.QLabel(self.frameInfo)
        self.labelAccel.setGeometry(QtCore.QRect(0, 170, 200, 20))
        font.setPointSize(12)
        self.labelAccel.setFont(font)
        self.labelAccel.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelAccel.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAccel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAccel.setLineWidth(1)
        self.labelAccel.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccel.setText("Acceleration")

        self.labelAccelVal = QtWidgets.QLabel(self.frameInfo)
        self.labelAccelVal.setGeometry(QtCore.QRect(0, 190, 200, 20))
        font.setPointSize(12)
        self.labelAccelVal.setFont(font)
        self.labelAccelVal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelAccelVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAccelVal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAccelVal.setLineWidth(1)
        self.labelAccelVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccelVal.setText("0")

        self.labelXTiltVal = QtWidgets.QLabel(self.frameInfo)
        self.labelXTiltVal.setGeometry(QtCore.QRect(0, 360, 200, 20))
        font.setPointSize(12)
        self.labelXTiltVal.setFont(font)
        self.labelXTiltVal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelXTiltVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXTiltVal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelXTiltVal.setLineWidth(1)
        self.labelXTiltVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXTiltVal.setText("0")

        self.labelXTilt = QtWidgets.QLabel(self.frameInfo)
        self.labelXTilt.setGeometry(QtCore.QRect(0, 340, 200, 20))
        font.setPointSize(12)
        self.labelXTilt.setFont(font)
        self.labelXTilt.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelXTilt.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXTilt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelXTilt.setLineWidth(1)
        self.labelXTilt.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXTilt.setText("X Tilt")

        self.labelYTilt = QtWidgets.QLabel(self.frameInfo)
        self.labelYTilt.setGeometry(QtCore.QRect(0, 510, 200, 20))
        font.setPointSize(12)
        self.labelYTilt.setFont(font)
        self.labelYTilt.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelYTilt.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYTilt.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelYTilt.setLineWidth(1)
        self.labelYTilt.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYTilt.setText("Y Tilt")

        self.labelYTiltVal = QtWidgets.QLabel(self.frameInfo)
        self.labelYTiltVal.setGeometry(QtCore.QRect(0, 530, 200, 20))
        font.setPointSize(12)
        self.labelYTiltVal.setFont(font)
        self.labelYTiltVal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelYTiltVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYTiltVal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelYTiltVal.setLineWidth(1)
        self.labelYTiltVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYTiltVal.setText("0")

        self.frameSpeed = QtWidgets.QFrame(self.frameInfo)
        self.frameSpeed.setGeometry(QtCore.QRect(0, 40, 200, 130))
        self.frameSpeed.setFrameShape(QtWidgets.QFrame.Box)
        self.frameSpeed.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frameAccel = QtWidgets.QFrame(self.frameInfo)
        self.frameAccel.setGeometry(QtCore.QRect(0, 210, 200, 130))
        self.frameAccel.setFrameShape(QtWidgets.QFrame.Box)
        self.frameAccel.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frameXTilt = QtWidgets.QFrame(self.frameInfo)
        self.frameXTilt.setGeometry(QtCore.QRect(0, 380, 200, 130))
        self.frameXTilt.setFrameShape(QtWidgets.QFrame.Box)
        self.frameXTilt.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frameYTilt = QtWidgets.QFrame(self.frameInfo)
        self.frameYTilt.setGeometry(QtCore.QRect(0, 550, 200, 130))
        self.frameYTilt.setFrameShape(QtWidgets.QFrame.Box)
        self.frameYTilt.setFrameShadow(QtWidgets.QFrame.Raised)

        self.labelBallCood = QtWidgets.QLabel(self.frameInfo)
        self.labelBallCood.setGeometry(QtCore.QRect(0, 680, 200, 20))
        font.setPointSize(12)
        self.labelBallCood.setFont(font)
        self.labelBallCood.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelBallCood.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBallCood.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelBallCood.setLineWidth(1)
        self.labelBallCood.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBallCood.setText("Ball Coordinates")

        self.labelBallCoodVal = QtWidgets.QLabel(self.frameInfo)
        self.labelBallCoodVal.setGeometry(QtCore.QRect(0, 700, 200, 20))
        font.setPointSize(12)
        self.labelBallCoodVal.setFont(font)
        self.labelBallCoodVal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelBallCoodVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBallCoodVal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelBallCoodVal.setLineWidth(1)
        self.labelBallCoodVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBallCoodVal.setText("(0,0)")

        self.buttonStart = QtWidgets.QPushButton(self.pageAuto)
        self.buttonStart.setGeometry(QtCore.QRect(740, 850, 120, 41))
        self.buttonStart.setText("Start")
        self.buttonStart.clicked.connect(self.startTimerAuto)

        self.buttonHelp = QtWidgets.QPushButton(self.pageAuto)
        self.buttonHelp.setGeometry(QtCore.QRect(1500, 10, 75, 23))
        self.buttonHelp.setText("Help")
        self.buttonHelp.clicked.connect(self.switchPageAutoHelp)

        self.frameTimer = QtWidgets.QFrame(self.pageAuto)
        self.frameTimer.setGeometry(QtCore.QRect(685, 785, 231, 61))
        self.frameTimer.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.frameTimer.setFrameShape(QtWidgets.QFrame.Box)
        self.frameTimer.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameTimerValue = QtWidgets.QFrame(self.frameTimer)
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

        self.labelMin = QtWidgets.QLabel(self.frameTimer)
        self.labelMin.setGeometry(QtCore.QRect(10, 41, 61, 16))
        font.setPointSize(11)
        self.labelMin.setFont(font)
        self.labelMin.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMin.setText("min")

        self.labelSec = QtWidgets.QLabel(self.frameTimer)
        self.labelSec.setGeometry(QtCore.QRect(90, 41, 61, 16))
        font.setPointSize(11)
        self.labelSec.setFont(font)
        self.labelSec.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSec.setText("sec")

        self.labelMs = QtWidgets.QLabel(self.frameTimer)
        self.labelMs.setGeometry(QtCore.QRect(175, 41, 41, 16))
        font.setPointSize(11)
        self.labelMs.setFont(font)
        self.labelMs.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMs.setText("ms")

    def pageManualWidgets(self):
        font = QtGui.QFont()

        self.frameVideo_2 = QtWidgets.QFrame(self.pageManual)
        self.frameVideo_2.setGeometry(QtCore.QRect(60, 40, 1280, 720))
        self.frameVideo_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frameVideo_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.labelTitleManual = QtWidgets.QLabel(self.pageManual)
        self.labelTitleManual.setGeometry(QtCore.QRect(0, 0, 1601, 41))
        font.setPointSize(32)
        self.labelTitleManual.setFont(font)
        self.labelTitleManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitleManual.setText("Manual Solve")

        self.frameInfo_2 = QtWidgets.QFrame(self.pageManual)
        self.frameInfo_2.setGeometry(QtCore.QRect(1340, 40, 200, 720))
        self.frameInfo_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frameInfo_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.labelSpeed_2 = QtWidgets.QLabel(self.frameInfo_2)
        self.labelSpeed_2.setGeometry(QtCore.QRect(0, 0, 200, 20))
        font.setPointSize(12)
        self.labelSpeed_2.setFont(font)
        self.labelSpeed_2.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelSpeed_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSpeed_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelSpeed_2.setLineWidth(1)
        self.labelSpeed_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeed_2.setText("Speed")

        self.labelSpeedVal_2 = QtWidgets.QLabel(self.frameInfo_2)
        self.labelSpeedVal_2.setGeometry(QtCore.QRect(0, 20, 200, 20))
        font.setPointSize(12)
        self.labelSpeedVal_2.setFont(font)
        self.labelSpeedVal_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelSpeedVal_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSpeedVal_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelSpeedVal_2.setLineWidth(1)
        self.labelSpeedVal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeedVal_2.setText("0")

        self.labelAccel_2 = QtWidgets.QLabel(self.frameInfo_2)
        self.labelAccel_2.setGeometry(QtCore.QRect(0, 170, 200, 20))
        font.setPointSize(12)
        self.labelAccel_2.setFont(font)
        self.labelAccel_2.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelAccel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAccel_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAccel_2.setLineWidth(1)
        self.labelAccel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccel_2.setText("Acceleration")

        self.labelXTiltVal_2 = QtWidgets.QLabel(self.frameInfo_2)
        self.labelXTiltVal_2.setGeometry(QtCore.QRect(0, 360, 200, 20))
        font.setPointSize(12)
        self.labelXTiltVal_2.setFont(font)
        self.labelXTiltVal_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelXTiltVal_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXTiltVal_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelXTiltVal_2.setLineWidth(1)
        self.labelXTiltVal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXTiltVal_2.setText("0")

        self.labelXTilt_2 = QtWidgets.QLabel(self.frameInfo_2)
        self.labelXTilt_2.setGeometry(QtCore.QRect(0, 340, 200, 20))
        font.setPointSize(12)
        self.labelXTilt_2.setFont(font)
        self.labelXTilt_2.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelXTilt_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXTilt_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelXTilt_2.setLineWidth(1)
        self.labelXTilt_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXTilt_2.setText("X-Tilt")

        self.labelAccelVal_2 = QtWidgets.QLabel(self.frameInfo_2)
        self.labelAccelVal_2.setGeometry(QtCore.QRect(0, 190, 200, 20))
        font.setPointSize(12)
        self.labelAccelVal_2.setFont(font)
        self.labelAccelVal_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelAccelVal_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAccelVal_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAccelVal_2.setLineWidth(1)
        self.labelAccelVal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccelVal_2.setText("0")

        self.labelYTilt_2 = QtWidgets.QLabel(self.frameInfo_2)
        self.labelYTilt_2.setGeometry(QtCore.QRect(0, 510, 200, 20))
        font.setPointSize(12)
        self.labelYTilt_2.setFont(font)
        self.labelYTilt_2.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelYTilt_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYTilt_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelYTilt_2.setLineWidth(1)
        self.labelYTilt_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYTilt_2.setText("Y-Tilt")

        self.labelYTiltVal_2 = QtWidgets.QLabel(self.frameInfo_2)
        self.labelYTiltVal_2.setGeometry(QtCore.QRect(0, 530, 200, 20))
        font.setPointSize(12)
        self.labelYTiltVal_2.setFont(font)
        self.labelYTiltVal_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelYTiltVal_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYTiltVal_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelYTiltVal_2.setLineWidth(1)
        self.labelYTiltVal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYTiltVal_2.setText("0")

        self.frameSpeed_2 = QtWidgets.QFrame(self.frameInfo_2)
        self.frameSpeed_2.setGeometry(QtCore.QRect(0, 40, 200, 130))
        self.frameSpeed_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frameSpeed_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frameAccel_2 = QtWidgets.QFrame(self.frameInfo_2)
        self.frameAccel_2.setGeometry(QtCore.QRect(0, 210, 200, 130))
        self.frameAccel_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frameAccel_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frameXTilt_2 = QtWidgets.QFrame(self.frameInfo_2)
        self.frameXTilt_2.setGeometry(QtCore.QRect(0, 380, 200, 130))
        self.frameXTilt_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frameXTilt_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frameYTilt_2 = QtWidgets.QFrame(self.frameInfo_2)
        self.frameYTilt_2.setGeometry(QtCore.QRect(0, 550, 200, 130))
        self.frameYTilt_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frameYTilt_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.labelBallCood_2 = QtWidgets.QLabel(self.frameInfo_2)
        self.labelBallCood_2.setGeometry(QtCore.QRect(0, 680, 200, 20))
        font.setPointSize(12)
        self.labelBallCood_2.setFont(font)
        self.labelBallCood_2.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelBallCood_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBallCood_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelBallCood_2.setLineWidth(1)
        self.labelBallCood_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBallCood_2.setText("Ball Coordinates")

        self.labelBallCoodVal_2 = QtWidgets.QLabel(self.frameInfo_2)
        self.labelBallCoodVal_2.setGeometry(QtCore.QRect(0, 700, 200, 20))
        font.setPointSize(12)
        self.labelBallCoodVal_2.setFont(font)
        self.labelBallCoodVal_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelBallCoodVal_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBallCoodVal_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelBallCoodVal_2.setLineWidth(1)
        self.labelBallCoodVal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBallCoodVal_2.setText("(0,0)")

        self.frameTimer_2 = QtWidgets.QFrame(self.pageManual)
        self.frameTimer_2.setGeometry(QtCore.QRect(685, 800, 231, 61))
        self.frameTimer_2.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.frameTimer_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frameTimer_2.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameTimerValue_2 = QtWidgets.QFrame(self.frameTimer_2)
        self.frameTimerValue_2.setGeometry(QtCore.QRect(0, 0, 231, 41))
        self.frameTimerValue_2.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.frameTimerValue_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frameTimerValue_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameTimerValue_2.setLineWidth(1)

        self.labelMinVal_2 = QtWidgets.QLabel(self.frameTimerValue_2)
        self.labelMinVal_2.setGeometry(QtCore.QRect(10, 0, 60, 41))
        font.setPointSize(32)
        self.labelMinVal_2.setFont(font)
        self.labelMinVal_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelMinVal_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelMinVal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMinVal_2.setText("00")

        self.labelSecVal_2 = QtWidgets.QLabel(self.frameTimerValue_2)
        self.labelSecVal_2.setGeometry(QtCore.QRect(90, 0, 61, 41))
        font.setPointSize(32)
        self.labelSecVal_2.setFont(font)
        self.labelSecVal_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelSecVal_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSecVal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSecVal_2.setText("00")

        self.labelMsVal_2 = QtWidgets.QLabel(self.frameTimerValue_2)
        self.labelMsVal_2.setGeometry(QtCore.QRect(170, 0, 51, 41))
        font.setPointSize(32)
        self.labelMsVal_2.setFont(font)
        self.labelMsVal_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelMsVal_2.setFrameShape(QtWidgets.QFrame.Box)
        self.labelMsVal_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMsVal_2.setText("00")

        self.labelColonL_2 = QtWidgets.QLabel(self.frameTimerValue_2)
        self.labelColonL_2.setGeometry(QtCore.QRect(71, 1, 19, 39))
        font.setPointSize(18)
        self.labelColonL_2.setFont(font)
        self.labelColonL_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelColonL_2.setText(":")

        self.labelColonR_2 = QtWidgets.QLabel(self.frameTimerValue_2)
        self.labelColonR_2.setGeometry(QtCore.QRect(151, 1, 19, 39))
        font.setPointSize(18)
        self.labelColonR_2.setFont(font)
        self.labelColonR_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelColonR_2.setText(":")

        self.labelMin_2 = QtWidgets.QLabel(self.frameTimer_2)
        self.labelMin_2.setGeometry(QtCore.QRect(10, 41, 61, 16))
        font.setPointSize(11)
        self.labelMin_2.setFont(font)
        self.labelMin_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMin_2.setText("min")

        self.labelSec_2 = QtWidgets.QLabel(self.frameTimer_2)
        self.labelSec_2.setGeometry(QtCore.QRect(90, 41, 61, 16))
        font.setPointSize(11)
        self.labelSec_2.setFont(font)
        self.labelSec_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSec_2.setText("sec")

        self.labelMs_2 = QtWidgets.QLabel(self.frameTimer_2)
        self.labelMs_2.setGeometry(QtCore.QRect(175, 41, 41, 16))
        font.setPointSize(11)
        self.labelMs_2.setFont(font)
        self.labelMs_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMs_2.setText("00")

        self.buttonStart_2 = QtWidgets.QPushButton(self.pageManual)
        self.buttonStart_2.setGeometry(QtCore.QRect(540, 810, 120, 41))
        self.buttonStart_2.setText("Start")
        self.buttonStart_2.clicked.connect(self.startTimerManual)

        self.buttonBack_2 = QtWidgets.QPushButton(self.pageManual)
        self.buttonBack_2.setGeometry(QtCore.QRect(30, 820, 81, 31))
        font.setPointSize(12)
        self.buttonBack_2.setFont(font)
        self.buttonBack_2.setText("Back")
        self.buttonBack_2.clicked.connect(self.switchPageHome)

        self.frameManual = QtWidgets.QFrame(self.pageManual)
        self.frameManual.setGeometry(QtCore.QRect(940, 770, 241, 121))
        self.frameManual.setFrameShape(QtWidgets.QFrame.Box)
        self.frameManual.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameJoystick = QtWidgets.QFrame(self.frameManual)
        self.frameJoystick.setGeometry(QtCore.QRect(0, 0, 121, 121))
        self.frameJoystick.setFrameShape(QtWidgets.QFrame.Box)
        self.frameJoystick.setFrameShadow(QtWidgets.QFrame.Plain)

        self.labelXControl = QtWidgets.QLabel(self.frameManual)
        self.labelXControl.setGeometry(QtCore.QRect(120, 0, 121, 30))
        font.setPointSize(12)
        self.labelXControl.setFont(font)
        self.labelXControl.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelXControl.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXControl.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXControl.setText("X - Control")

        self.labelXControlVal = QtWidgets.QLabel(self.frameManual)
        self.labelXControlVal.setGeometry(QtCore.QRect(120, 30, 121, 30))
        font.setPointSize(12)
        self.labelXControlVal.setFont(font)
        self.labelXControlVal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelXControlVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXControlVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXControlVal.setText("0")

        self.labelYControl = QtWidgets.QLabel(self.frameManual)
        self.labelYControl.setGeometry(QtCore.QRect(120, 60, 121, 30))
        font.setPointSize(12)
        self.labelYControl.setFont(font)
        self.labelYControl.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelYControl.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYControl.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYControl.setText("Y - Control")

        self.labelYControlVal = QtWidgets.QLabel(self.frameManual)
        self.labelYControlVal.setGeometry(QtCore.QRect(120, 90, 121, 30))
        font.setPointSize(12)
        self.labelYControlVal.setFont(font)
        self.labelYControlVal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelYControlVal.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYControlVal.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYControlVal.setText("0")

        self.buttonHelp_2 = QtWidgets.QPushButton(self.pageManual)
        self.buttonHelp_2.setGeometry(QtCore.QRect(1500, 10, 75, 23))
        self.buttonHelp_2.setText("Help")
        self.buttonHelp_2.clicked.connect(self.switchPageManualHelp)

        self.verticalSlider = QtWidgets.QSlider(self.pageManual)
        self.verticalSlider.setGeometry(QtCore.QRect(1190, 770, 22, 121))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setValue(50)

        self.horizontalSlider = QtWidgets.QSlider(self.pageManual)
        self.horizontalSlider.setGeometry(QtCore.QRect(1220, 820, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setValue(50)

    def pageAutoHelpWidgets(self):
        font = QtGui.QFont()

        self.labelAutoHelp = QtWidgets.QLabel(self.pageAutoHelp)
        self.labelAutoHelp.setGeometry(QtCore.QRect(500, 500, 500, 500))
        font.setPointSize(32)
        self.labelAutoHelp.setFont(font)
        self.labelAutoHelp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAutoHelp.setText("Auto Help")

        self.buttonBack = QtWidgets.QPushButton(self.pageAutoHelp)
        self.buttonBack.setGeometry(QtCore.QRect(1500, 10, 75, 23))
        self.buttonBack.setText("Back")
        self.buttonBack.clicked.connect(self.switchPageAuto)

    def pageManualHelpWidgets(self):
        font = QtGui.QFont()

        self.labelAutoHelp = QtWidgets.QLabel(self.pageManualHelp)
        self.labelAutoHelp.setGeometry(QtCore.QRect(500, 500, 500, 500))
        font.setPointSize(32)
        self.labelAutoHelp.setFont(font)
        self.labelAutoHelp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAutoHelp.setText("Manual Help")

        self.buttonBack = QtWidgets.QPushButton(self.pageManualHelp)
        self.buttonBack.setGeometry(QtCore.QRect(1500, 10, 75, 23))
        self.buttonBack.setText("Back")
        self.buttonBack.clicked.connect(self.switchPageManual)

    def switchPageHome(self,index):
        self.stackedWidget.setCurrentIndex(0)

    def switchPageAuto(self):
        self.stackedWidget.setCurrentIndex(1)

    def switchPageManual(self):
        self.stackedWidget.setCurrentIndex(2)

    def switchPageDatabase(self):
        self.stackedWidget.setCurrentIndex(3)

    def switchPageStats(self):
        self.stackedWidget.setCurrentIndex(4)

    def switchPageAutoHelp(self):
        self.stackedWidget.setCurrentIndex(5)

    def switchPageManualHelp(self):
        self.stackedWidget.setCurrentIndex(6)

    def startTimerAuto(self):
        self.currTime = QtCore.QTime(00, 00, 00)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timeAuto)
        self.timer.start(10)
        
        if self.buttonStart.text() == "Start":
            self.buttonStart.setText("Force Stop")
        else:
            self.timer.stop()
            self.buttonStart.setText("Start")

    def timeAuto(self):
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
        if self.stackedWidget.currentIndex() != 1:
            self.timer.stop()
            self.labelMinVal.setText("00")
            self.labelSecVal.setText("00")
            self.labelMsVal.setText("00")
            self.buttonStart.setText("Start")

    def startTimerManual(self):
        self.currTime = QtCore.QTime(00, 00, 00)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timeManual)
        self.timer.start(10)

        if self.buttonStart_2.text() == "Start":
            self.buttonStart_2.setText("Force Stop")
        else:
            self.timer.stop()
            self.buttonStart_2.setText("Start")

    def timeManual(self):
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
        self.labelMinVal_2.setText(str(self.minute))
        self.labelSecVal_2.setText(str(self.second))
        self.labelMsVal_2.setText(str(self.msecond)[:-1])
        if self.stackedWidget.currentIndex() != 2:
            self.timer.stop()
            self.labelMinVal_2.setText("00")
            self.labelSecVal_2.setText("00")
            self.labelMsVal_2.setText("00")
            self.buttonStart_2.setText("Start")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.initUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())