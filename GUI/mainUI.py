from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from numpy import array, int32
import joystickWidget, renderBoard2D, renderMarble2D, directionWidget, tiltWidget, timerWidget, labelWidget, replayWidget, statusWidget, motor_sync_control
from bson.objectid import ObjectId

client = pymongo.MongoClient(host="localhost", port=27017)
db = client.project
solves = db.solves

class Ui_MainWindow(object):
    def initUi(self, MainWindow):
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 900))
        MainWindow.setWindowTitle("Group C's Automated Maze Solver")

        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))

        self.pageHome = QtWidgets.QWidget()         #index 0
        self.pageAuto = QtWidgets.QWidget()         #index 1
        self.pageManual = QtWidgets.QWidget()       #index 2
        self.pageDatabase = QtWidgets.QWidget()     #index 3
        self.pageStats = QtWidgets.QWidget()        #index 4
        self.pageAutoHelp = QtWidgets.QWidget()     #index 5
        self.pageManualHelp = QtWidgets.QWidget()   #index 6
        self.pageReplay = QtWidgets.QWidget()       #index 7

        self.stackedWidget.addWidget(self.pageHome)
        self.stackedWidget.addWidget(self.pageAuto)
        self.stackedWidget.addWidget(self.pageManual)
        self.stackedWidget.addWidget(self.pageDatabase)
        self.stackedWidget.addWidget(self.pageStats)
        self.stackedWidget.addWidget(self.pageAutoHelp)
        self.stackedWidget.addWidget(self.pageManualHelp)
        self.stackedWidget.addWidget(self.pageReplay)

        self.pageHomeWidgets()
        self.pageAutoWidgets()
        self.pageManualWidgets()
        self.pageDatabaseWidgets()
        self.pageStatsWidgets()
        self.pageAutoHelpWidgets()
        self.pageManualHelpWidgets()
        self.pageReplayWidgets()

    def pageHomeWidgets(self):
        font = QtGui.QFont()

        self.buttonAuto = QtWidgets.QPushButton(self.pageHome)
        self.buttonAuto.setGeometry(QtCore.QRect(500, 150, 650, 140))
        font.setPointSize(32)
        self.buttonAuto.setFont(font)
        self.buttonAuto.setText("Automated Solve")
        self.buttonAuto.clicked.connect(self.loadAuto)

        self.buttonManual = QtWidgets.QPushButton(self.pageHome)
        self.buttonManual.setGeometry(QtCore.QRect(500, 300, 650, 140))
        font.setPointSize(32)
        self.buttonManual.setFont(font)
        self.buttonManual.setText("Manual Solve")
        self.buttonManual.clicked.connect(self.loadManual)

        self.buttonDatabase = QtWidgets.QPushButton(self.pageHome)
        self.buttonDatabase.setGeometry(QtCore.QRect(500, 450, 650, 140))
        font.setPointSize(32)
        self.buttonDatabase.setFont(font)
        self.buttonDatabase.setText("Database")
        self.buttonDatabase.clicked.connect(lambda: self.switchPage(3))

        self.buttonStats = QtWidgets.QPushButton(self.pageHome)
        self.buttonStats.setGeometry(QtCore.QRect(500, 600, 650, 140))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.buttonStats.setFont(font)
        self.buttonStats.setText("Stats")
        self.buttonStats.clicked.connect(lambda: self.switchPage(4))

        self.labelTitle = QtWidgets.QLabel(self.pageHome)
        self.labelTitle.setGeometry(QtCore.QRect(140, 10, 1320, 91))
        font.setPointSize(50)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setText("Group C's Automated Ball in the Maze Solver")

    def pageAutoWidgets(self):
        font = QtGui.QFont()

        self.buttonBackAuto = QtWidgets.QPushButton(self.pageAuto)
        self.buttonBackAuto.setGeometry(QtCore.QRect(20, 830, 81, 35))
        self.buttonBackAuto.setFont(font)
        self.buttonBackAuto.setText("Back")
        self.buttonBackAuto.clicked.connect(lambda: self.deleteBoardMarble("auto"))

        self.labelTitleAuto = QtWidgets.QLabel(self.pageAuto)
        self.labelTitleAuto.setGeometry(QtCore.QRect(140, 0, 1320, 40))
        font.setPointSize(32)
        self.labelTitleAuto.setFont(font)
        self.labelTitleAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitleAuto.setText("Automated Solve")

        self.frameVideoAuto = QtWidgets.QFrame(self.pageAuto)
        self.frameVideoAuto.setGeometry(QtCore.QRect(60, 40, 1280, 720))
        self.frameVideoAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.frameVideoAuto.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameInfoAuto = QtWidgets.QFrame(self.pageAuto)
        self.frameInfoAuto.setGeometry(QtCore.QRect(1340, 40, 200, 720))
        self.frameInfoAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.frameInfoAuto.setFrameShadow(QtWidgets.QFrame.Plain)

        self.labelSpeedAuto = QtWidgets.QLabel(self.frameInfoAuto)
        self.labelSpeedAuto.setGeometry(QtCore.QRect(0, 0, 200, 20))
        font.setPointSize(12)
        self.labelSpeedAuto.setFont(font)
        self.labelSpeedAuto.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelSpeedAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSpeedAuto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelSpeedAuto.setLineWidth(1)
        self.labelSpeedAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeedAuto.setText("Speed (m/s)")

        self.labelSpeedValAuto = QtWidgets.QLabel(self.frameInfoAuto)
        self.labelSpeedValAuto.setGeometry(QtCore.QRect(0, 20, 200, 20))
        font.setPointSize(12)
        self.labelSpeedValAuto.setFont(font)
        self.labelSpeedValAuto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelSpeedValAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSpeedValAuto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelSpeedValAuto.setLineWidth(1)
        self.labelSpeedValAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeedValAuto.setText("0")

        self.labelAccelAuto = QtWidgets.QLabel(self.frameInfoAuto)
        self.labelAccelAuto.setGeometry(QtCore.QRect(0, 170, 200, 20))
        font.setPointSize(12)
        self.labelAccelAuto.setFont(font)
        self.labelAccelAuto.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelAccelAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAccelAuto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAccelAuto.setLineWidth(1)
        self.labelAccelAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccelAuto.setText("Acceleration (m/s²)")

        self.labelAccelValAuto = QtWidgets.QLabel(self.frameInfoAuto)
        self.labelAccelValAuto.setGeometry(QtCore.QRect(0, 190, 200, 20))
        font.setPointSize(12)
        self.labelAccelValAuto.setFont(font)
        self.labelAccelValAuto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelAccelValAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAccelValAuto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAccelValAuto.setLineWidth(1)
        self.labelAccelValAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccelValAuto.setText("0")

        self.labelXTiltValAuto = QtWidgets.QLabel(self.frameInfoAuto)
        self.labelXTiltValAuto.setGeometry(QtCore.QRect(0, 360, 200, 20))
        font.setPointSize(12)
        self.labelXTiltValAuto.setFont(font)
        self.labelXTiltValAuto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelXTiltValAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXTiltValAuto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelXTiltValAuto.setLineWidth(1)
        self.labelXTiltValAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXTiltValAuto.setText("0")

        self.labelXTiltAuto = QtWidgets.QLabel(self.frameInfoAuto)
        self.labelXTiltAuto.setGeometry(QtCore.QRect(0, 340, 200, 20))
        font.setPointSize(12)
        self.labelXTiltAuto.setFont(font)
        self.labelXTiltAuto.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelXTiltAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXTiltAuto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelXTiltAuto.setLineWidth(1)
        self.labelXTiltAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXTiltAuto.setText("X Tilt (°)")

        self.labelYTiltAuto = QtWidgets.QLabel(self.frameInfoAuto)
        self.labelYTiltAuto.setGeometry(QtCore.QRect(0, 510, 200, 20))
        font.setPointSize(12)
        self.labelYTiltAuto.setFont(font)
        self.labelYTiltAuto.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelYTiltAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYTiltAuto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelYTiltAuto.setLineWidth(1)
        self.labelYTiltAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYTiltAuto.setText("Y Tilt (°)")

        self.labelYTiltValAuto = QtWidgets.QLabel(self.frameInfoAuto)
        self.labelYTiltValAuto.setGeometry(QtCore.QRect(0, 530, 200, 20))
        font.setPointSize(12)
        self.labelYTiltValAuto.setFont(font)
        self.labelYTiltValAuto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelYTiltValAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYTiltValAuto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelYTiltValAuto.setLineWidth(1)
        self.labelYTiltValAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYTiltValAuto.setText("0")

        self.frameSpeedAuto = QtWidgets.QFrame(self.frameInfoAuto)
        self.frameSpeedAuto.setGeometry(QtCore.QRect(0, 40, 200, 130))
        self.frameSpeedAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.frameSpeedAuto.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameAccelAuto = QtWidgets.QFrame(self.frameInfoAuto)
        self.frameAccelAuto.setGeometry(QtCore.QRect(0, 210, 200, 130))
        self.frameAccelAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.frameAccelAuto.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameXTiltAuto = QtWidgets.QFrame(self.frameInfoAuto)
        self.frameXTiltAuto.setGeometry(QtCore.QRect(0, 380, 200, 130))
        self.frameXTiltAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.frameXTiltAuto.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameYTiltAuto = QtWidgets.QFrame(self.frameInfoAuto)
        self.frameYTiltAuto.setGeometry(QtCore.QRect(0, 550, 200, 130))
        self.frameYTiltAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.frameYTiltAuto.setFrameShadow(QtWidgets.QFrame.Plain)

        self.labelBallCoodAuto = QtWidgets.QLabel(self.frameInfoAuto)
        self.labelBallCoodAuto.setGeometry(QtCore.QRect(0, 680, 200, 20))
        font.setPointSize(12)
        self.labelBallCoodAuto.setFont(font)
        self.labelBallCoodAuto.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelBallCoodAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBallCoodAuto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelBallCoodAuto.setLineWidth(1)
        self.labelBallCoodAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBallCoodAuto.setText("Ball Coordinates")

        self.labelBallCoodValAuto = QtWidgets.QLabel(self.frameInfoAuto)
        self.labelBallCoodValAuto.setGeometry(QtCore.QRect(0, 700, 200, 20))
        font.setPointSize(12)
        self.labelBallCoodValAuto.setFont(font)
        self.labelBallCoodValAuto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelBallCoodValAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBallCoodValAuto.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelBallCoodValAuto.setLineWidth(1)
        self.labelBallCoodValAuto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBallCoodValAuto.setText("(0,0)")

        self.buttonClearAuto = QtWidgets.QPushButton(self.pageAuto)
        self.buttonClearAuto.setGeometry(QtCore.QRect(805, 850, 100, 41))
        self.buttonClearAuto.setText("Clear Timer")

        self.buttonStartAuto = QtWidgets.QPushButton(self.pageAuto)
        self.buttonStartAuto.setGeometry(QtCore.QRect(695, 850, 100, 41))
        self.buttonStartAuto.setText("Start")

        self.buttonHelpAuto = QtWidgets.QPushButton(self.pageAuto)
        self.buttonHelpAuto.setGeometry(QtCore.QRect(1500, 10, 75, 23))
        self.buttonHelpAuto.setText("Help")
        self.buttonHelpAuto.clicked.connect(lambda: self.switchPage(5))

        self.buttonRefreshAuto = QtWidgets.QPushButton(self.pageAuto)
        self.buttonRefreshAuto.setGeometry(QtCore.QRect(570, 815, 100, 40))
        self.buttonRefreshAuto.setText("Refresh")
        self.buttonRefreshAuto.clicked.connect(self.refreshBoard)

        self.buttonSwitchAuto = QtWidgets.QPushButton(self.pageAuto)
        self.buttonSwitchAuto.setGeometry(QtCore.QRect(1261, 18, 80, 23))
        self.buttonSwitchAuto.setText("Switch Camera")

        self.statusAuto = statusWidget.StatusWidget(self.pageAuto)
        self.statusAuto.move(285,790)
        
        ###################################################################################################################
        
        #directional widgets

        self.directionSpeedAuto = directionWidget.DirectionWidget(self.frameSpeedAuto, labelVal=self.labelSpeedValAuto, type="speed")
        self.directionAccelAuto = directionWidget.DirectionWidget(self.frameAccelAuto, labelVal=self.labelAccelValAuto, type="accel")
        self.xTiltAuto = tiltWidget.TiltWidget(self.frameXTiltAuto, labelTilt=self.labelXTiltValAuto)
        self.yTiltAuto = tiltWidget.TiltWidget(self.frameYTiltAuto, labelTilt=self.labelYTiltValAuto)

        ##################################################################################################################
        
        #timer widget

        timerAuto = timerWidget.TimerWidget(self.pageAuto, buttonStart=self.buttonStartAuto, stackedWidget=self.stackedWidget)
        self.buttonClearAuto.clicked.connect(timerAuto.timerClear)
        self.buttonStartAuto.clicked.connect(timerAuto.timerClick)

        ######################################################################################################################

    def pageManualWidgets(self):
        font = QtGui.QFont()

        self.frameVideoManual = QtWidgets.QFrame(self.pageManual)
        self.frameVideoManual.setGeometry(QtCore.QRect(60, 40, 1280, 720))
        self.frameVideoManual.setFrameShape(QtWidgets.QFrame.Box)
        self.frameVideoManual.setFrameShadow(QtWidgets.QFrame.Plain)

        self.labelTitleManual = QtWidgets.QLabel(self.pageManual)
        self.labelTitleManual.setGeometry(QtCore.QRect(0, 0, 1601, 41))
        font.setPointSize(32)
        self.labelTitleManual.setFont(font)
        self.labelTitleManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitleManual.setText("Manual Solve")

        self.frameInfoManual = QtWidgets.QFrame(self.pageManual)
        self.frameInfoManual.setGeometry(QtCore.QRect(1340, 40, 200, 720))
        self.frameInfoManual.setFrameShape(QtWidgets.QFrame.Box)
        self.frameInfoManual.setFrameShadow(QtWidgets.QFrame.Plain)

        self.labelSpeedManual = QtWidgets.QLabel(self.frameInfoManual)
        self.labelSpeedManual.setGeometry(QtCore.QRect(0, 0, 200, 20))
        font.setPointSize(12)
        self.labelSpeedManual.setFont(font)
        self.labelSpeedManual.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelSpeedManual.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSpeedManual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelSpeedManual.setLineWidth(1)
        self.labelSpeedManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeedManual.setText("Speed (m/s)")

        self.labelSpeedValManual = QtWidgets.QLabel(self.frameInfoManual)
        self.labelSpeedValManual.setGeometry(QtCore.QRect(0, 20, 200, 20))
        font.setPointSize(12)
        self.labelSpeedValManual.setFont(font)
        self.labelSpeedValManual.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelSpeedValManual.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSpeedValManual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelSpeedValManual.setLineWidth(1)
        self.labelSpeedValManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeedValManual.setText("0")

        self.labelAccelManual = QtWidgets.QLabel(self.frameInfoManual)
        self.labelAccelManual.setGeometry(QtCore.QRect(0, 170, 200, 20))
        font.setPointSize(12)
        self.labelAccelManual.setFont(font)
        self.labelAccelManual.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelAccelManual.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAccelManual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAccelManual.setLineWidth(1)
        self.labelAccelManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccelManual.setText("Acceleration (m/s²)")

        self.labelXTiltValManual = QtWidgets.QLabel(self.frameInfoManual)
        self.labelXTiltValManual.setGeometry(QtCore.QRect(0, 360, 200, 20))
        font.setPointSize(12)
        self.labelXTiltValManual.setFont(font)
        self.labelXTiltValManual.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelXTiltValManual.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXTiltValManual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelXTiltValManual.setLineWidth(1)
        self.labelXTiltValManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXTiltValManual.setText("0")

        self.labelXTiltManual = QtWidgets.QLabel(self.frameInfoManual)
        self.labelXTiltManual.setGeometry(QtCore.QRect(0, 340, 200, 20))
        font.setPointSize(12)
        self.labelXTiltManual.setFont(font)
        self.labelXTiltManual.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelXTiltManual.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXTiltManual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelXTiltManual.setLineWidth(1)
        self.labelXTiltManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXTiltManual.setText("X-Tilt (°)")

        self.labelAccelValManual = QtWidgets.QLabel(self.frameInfoManual)
        self.labelAccelValManual.setGeometry(QtCore.QRect(0, 190, 200, 20))
        font.setPointSize(12)
        self.labelAccelValManual.setFont(font)
        self.labelAccelValManual.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelAccelValManual.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAccelValManual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAccelValManual.setLineWidth(1)
        self.labelAccelValManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccelValManual.setText("0")

        self.labelYTiltManual = QtWidgets.QLabel(self.frameInfoManual)
        self.labelYTiltManual.setGeometry(QtCore.QRect(0, 510, 200, 20))
        font.setPointSize(12)
        self.labelYTiltManual.setFont(font)
        self.labelYTiltManual.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelYTiltManual.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYTiltManual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelYTiltManual.setLineWidth(1)
        self.labelYTiltManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYTiltManual.setText("Y-Tilt (°)")

        self.labelYTiltValManual = QtWidgets.QLabel(self.frameInfoManual)
        self.labelYTiltValManual.setGeometry(QtCore.QRect(0, 530, 200, 20))
        font.setPointSize(12)
        self.labelYTiltValManual.setFont(font)
        self.labelYTiltValManual.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelYTiltValManual.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYTiltValManual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelYTiltValManual.setLineWidth(1)
        self.labelYTiltValManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYTiltValManual.setText("0")

        self.frameSpeedManual = QtWidgets.QFrame(self.frameInfoManual)
        self.frameSpeedManual.setGeometry(QtCore.QRect(0, 40, 200, 130))
        self.frameSpeedManual.setFrameShape(QtWidgets.QFrame.Box)
        self.frameSpeedManual.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameAccelManual = QtWidgets.QFrame(self.frameInfoManual)
        self.frameAccelManual.setGeometry(QtCore.QRect(0, 210, 200, 130))
        self.frameAccelManual.setFrameShape(QtWidgets.QFrame.Box)
        self.frameAccelManual.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameXTiltManual = QtWidgets.QFrame(self.frameInfoManual)
        self.frameXTiltManual.setGeometry(QtCore.QRect(0, 380, 200, 130))
        self.frameXTiltManual.setFrameShape(QtWidgets.QFrame.Box)
        self.frameXTiltManual.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameYTiltManual = QtWidgets.QFrame(self.frameInfoManual)
        self.frameYTiltManual.setGeometry(QtCore.QRect(0, 550, 200, 130))
        self.frameYTiltManual.setFrameShape(QtWidgets.QFrame.Box)
        self.frameYTiltManual.setFrameShadow(QtWidgets.QFrame.Plain)

        self.labelBallCoodManual = QtWidgets.QLabel(self.frameInfoManual)
        self.labelBallCoodManual.setGeometry(QtCore.QRect(0, 680, 200, 20))
        font.setPointSize(12)
        self.labelBallCoodManual.setFont(font)
        self.labelBallCoodManual.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelBallCoodManual.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBallCoodManual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelBallCoodManual.setLineWidth(1)
        self.labelBallCoodManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBallCoodManual.setText("Ball Coordinates")

        self.labelBallCoodValManual = QtWidgets.QLabel(self.frameInfoManual)
        self.labelBallCoodValManual.setGeometry(QtCore.QRect(0, 700, 200, 20))
        font.setPointSize(12)
        self.labelBallCoodValManual.setFont(font)
        self.labelBallCoodValManual.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelBallCoodValManual.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBallCoodValManual.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelBallCoodValManual.setLineWidth(1)
        self.labelBallCoodValManual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBallCoodValManual.setText("(0,0)")

        self.buttonBackManual = QtWidgets.QPushButton(self.pageManual)
        self.buttonBackManual.setGeometry(QtCore.QRect(20, 830, 81, 35))
        font.setPointSize(8)
        self.buttonBackManual.setFont(font)
        self.buttonBackManual.setText("Back")
        self.buttonBackManual.clicked.connect(lambda: self.deleteBoardMarble("manual"))

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

        self.labelYControl = QtWidgets.QLabel(self.frameManual)
        self.labelYControl.setGeometry(QtCore.QRect(120, 60, 121, 30))
        font.setPointSize(12)
        self.labelYControl.setFont(font)
        self.labelYControl.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelYControl.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYControl.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYControl.setText("Y - Control")

        self.buttonHelpManual = QtWidgets.QPushButton(self.pageManual)
        self.buttonHelpManual.setGeometry(QtCore.QRect(1500, 10, 75, 23))
        self.buttonHelpManual.setText("Help")
        self.buttonHelpManual.clicked.connect(lambda: self.switchPage(6))

        self.buttonStartManual = QtWidgets.QPushButton(self.pageManual)
        self.buttonStartManual.setGeometry(QtCore.QRect(695, 850, 100, 41))
        self.buttonStartManual.setText("Start")
        
        self.buttonClearManual = QtWidgets.QPushButton(self.pageManual)
        self.buttonClearManual.setGeometry(QtCore.QRect(805, 850, 100, 41))
        self.buttonClearManual.setText("Clear Timer")

        self.buttonRefreshManual = QtWidgets.QPushButton(self.pageManual)
        self.buttonRefreshManual.setGeometry(QtCore.QRect(570, 815, 100, 40))
        self.buttonRefreshManual.setText("Refresh")
        self.buttonRefreshManual.clicked.connect(self.refreshBoard)

        self.statusManual = statusWidget.StatusWidget(self.pageManual)
        self.statusManual.move(285,780)

        self.buttonSwitchManual = QtWidgets.QPushButton(self.pageManual)
        self.buttonSwitchManual.setGeometry(QtCore.QRect(1261, 18, 80, 23))
        self.buttonSwitchManual.setText("Switch Camera")

        ########################################################################################################################
        
        #joystick and slider widgets

        self.verticalSlider = QtWidgets.QSlider(self.pageManual)
        self.verticalSlider.setGeometry(QtCore.QRect(1190, 770, 22, 121))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setMaximum(50)
        self.verticalSlider.setMinimum(-50)
        self.verticalSlider.valueChanged.connect(lambda: self.labelYControlVal.updateFromSlider(self.verticalSlider.value(),"y"))

        self.horizontalSlider = QtWidgets.QSlider(self.pageManual)
        self.horizontalSlider.setGeometry(QtCore.QRect(1220, 820, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMaximum(50)
        self.horizontalSlider.setMinimum(-50)
        self.horizontalSlider.valueChanged.connect(lambda: self.labelXControlVal.updateFromSlider(self.horizontalSlider.value(),"x"))

        self.buttonResetXTilt = QtWidgets.QPushButton(self.pageManual)
        self.buttonResetXTilt.setText("Reset X Tilt")
        self.buttonResetXTilt.setGeometry(QtCore.QRect(1220, 860, 75, 23))
        self.buttonResetXTilt.clicked.connect(lambda: self.labelXControlVal.resetTilt("x"))

        self.buttonResetYTilt = QtWidgets.QPushButton(self.pageManual)
        self.buttonResetYTilt.setText("Reset Y Tilt")
        self.buttonResetYTilt.setGeometry(QtCore.QRect(1300, 860, 75, 23))
        self.buttonResetYTilt.clicked.connect(lambda: self.labelYControlVal.resetTilt("y"))

        self.labelXControlVal = labelWidget.LabelWidget(self.frameManual, slider=self.horizontalSlider, cood=[120,30], axis="x")
        self.labelYControlVal = labelWidget.LabelWidget(self.frameManual, slider=self.verticalSlider, cood=[120,90], axis="y")

        joystickManual = joystickWidget.Joystick(self.frameJoystick,labelX=self.labelXControlVal, labelY=self.labelYControlVal)

        self.labelXControlVal.joystick = joystickManual
        self.labelYControlVal.joystick = joystickManual


        
        ########################################################################################################################

        
        #timer widgets

        timerManual = timerWidget.TimerWidget(self.pageManual, buttonStart=self.buttonStartManual, stackedWidget=self.stackedWidget)
        self.buttonStartManual.clicked.connect(timerManual.timerClick)
        self.buttonClearManual.clicked.connect(timerManual.timerClear)
        
        ############################################################################################################################
        
        #directional widgets

        self.directionSpeedManual = directionWidget.DirectionWidget(self.frameSpeedManual, labelVal=self.labelSpeedValManual, type="speed")
        self.directionAccelManual = directionWidget.DirectionWidget(self.frameAccelManual, labelVal=self.labelAccelValManual, type="accel")
        self.xTiltManual = tiltWidget.TiltWidget(self.frameXTiltManual, labelTilt=self.labelXTiltValManual)
        self.yTiltManual = tiltWidget.TiltWidget(self.frameYTiltManual, labelTilt=self.labelYTiltValManual)

        ##########################################################################################################################

    def pageDatabaseWidgets(self):
        font = QtGui.QFont()

        self.labelTitleDatabase = QtWidgets.QLabel(self.pageDatabase)
        self.labelTitleDatabase.setGeometry(QtCore.QRect(710, 20, 181, 41))
        self.labelTitleDatabase.setText("Database")
        font.setPointSize(32)
        self.labelTitleDatabase.setFont(font)
        self.labelTitleDatabase.setAlignment(QtCore.Qt.AlignCenter)

        self.buttonBackDatabase = QtWidgets.QPushButton(self.pageDatabase)
        self.buttonBackDatabase.setGeometry(QtCore.QRect(20, 830, 81, 35))
        self.buttonBackDatabase.setText("Back")
        self.buttonBackDatabase.clicked.connect(lambda: self.switchPage(0))

        self.frameDatabase = QtWidgets.QFrame(self.pageDatabase)
        self.frameDatabase.setGeometry(QtCore.QRect(350, 90, 900, 720))
        self.frameDatabase.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDatabase.setFrameShadow(QtWidgets.QFrame.Plain)

        self.buttonSelect = QtWidgets.QPushButton(self.pageDatabase)
        self.buttonSelect.setGeometry(QtCore.QRect(1280, 760, 101, 41))
        self.buttonSelect.setText("Select")
        self.buttonSelect.clicked.connect(self.loadReplay)

        self.buttonHelpDatabase = QtWidgets.QPushButton(self.pageDatabase)
        self.buttonHelpDatabase.setGeometry(QtCore.QRect(1500, 10, 75, 23))
        self.buttonHelpDatabase.setText("Help")

        self.treeWidgetDatabase = QtWidgets.QTreeWidget(self.frameDatabase)
        self.treeWidgetDatabase.setGeometry(QtCore.QRect(0, 0, 900, 720))
        font.setPointSize(16)
        self.treeWidgetDatabase.setFont(font)
        self.treeWidgetDatabase.setHeaderLabels(["Date (Time)", "Time Completed", "Solve Success?", "Auto or Manual", "Board Type"])

        self.frameFilter = QtWidgets.QFrame(self.pageDatabase)
        self.frameFilter.setGeometry(QtCore.QRect(1280, 160, 181, 241))
        self.frameFilter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFilter.setFrameShadow(QtWidgets.QFrame.Plain)

        font.setPointSize(10)
        self.comboBoxAutoManual = QtWidgets.QComboBox(self.frameFilter)
        self.comboBoxAutoManual.setGeometry(0,150,180, 30)
        self.comboBoxAutoManual.addItem("Show All")
        self.comboBoxAutoManual.addItem("Auto")
        self.comboBoxAutoManual.addItem("Manual")
        self.comboBoxAutoManual.setFont(font)
        self.comboBoxAutoManual.activated[str].connect(self.arrangeDatabase)

        self.comboBoxType = QtWidgets.QComboBox(self.frameFilter)
        self.comboBoxType.setGeometry(0, 210, 180, 30)
        self.comboBoxType.addItem("Show All")
        self.comboBoxType.addItem("Easy")
        self.comboBoxType.addItem("Medium")
        self.comboBoxType.addItem("Hard")
        self.comboBoxType.addItem("Custom")
        self.comboBoxType.setFont(font)
        self.comboBoxType.activated[str].connect(self.arrangeDatabase)

        self.comboBoxResult = QtWidgets.QComboBox(self.frameFilter)
        self.comboBoxResult.setGeometry(0, 90, 180, 30)
        self.comboBoxResult.addItem("Show All")
        self.comboBoxResult.addItem("Success")
        self.comboBoxResult.addItem("Failure")
        self.comboBoxResult.setFont(font)
        self.comboBoxResult.activated[str].connect(self.arrangeDatabase)

        self.comboBoxTime = QtWidgets.QComboBox(self.frameFilter)
        self.comboBoxTime.setGeometry(0, 30, 180, 30)
        self.comboBoxTime.addItem("Most Recent First")
        self.comboBoxTime.addItem("Oldest First")
        self.comboBoxTime.addItem("Fastest Time First")
        self.comboBoxTime.addItem("Slowest Time First")
        self.comboBoxTime.setFont(font)
        self.comboBoxTime.activated[str].connect(self.arrangeDatabase)



        self.labelSort = QtWidgets.QLabel(self.frameFilter)
        self.labelSort.setGeometry(QtCore.QRect(0, 0, 181, 31))
        self.labelSort.setText("Sort By:")
        self.labelSort.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSort.setStyleSheet("background-color: rgb(255, 255, 255);")
        font.setPointSize(14)
        self.labelSort.setFont(font)
        self.labelSort.setAlignment(QtCore.Qt.AlignCenter)

        self.labelFilterResult = QtWidgets.QLabel(self.frameFilter)
        self.labelFilterResult.setGeometry(QtCore.QRect(0, 60, 181, 31))
        self.labelFilterResult.setFrameShape(QtWidgets.QFrame.Box)
        self.labelFilterResult.setText("Filter Result:")
        self.labelFilterResult.setStyleSheet("background-color: rgb(255, 255, 255);")
        font.setPointSize(14)
        self.labelFilterResult.setFont(font)
        self.labelFilterResult.setAlignment(QtCore.Qt.AlignCenter)

        self.labelFilterAuto = QtWidgets.QLabel(self.frameFilter)
        self.labelFilterAuto.setGeometry(QtCore.QRect(0, 120, 181, 31))
        self.labelFilterAuto.setFrameShape(QtWidgets.QFrame.Box)
        self.labelFilterAuto.setText("Filter Auto:")
        self.labelFilterAuto.setStyleSheet("background-color: rgb(255, 255, 255);")
        font.setPointSize(14)
        self.labelFilterAuto.setFont(font)
        self.labelFilterAuto.setAlignment(QtCore.Qt.AlignCenter)

        self.labelFilterType = QtWidgets.QLabel(self.frameFilter)
        self.labelFilterType.setGeometry(QtCore.QRect(0, 180, 181, 31))
        self.labelFilterType.setFrameShape(QtWidgets.QFrame.Box)
        self.labelFilterType.setText("Filter Type:")
        self.labelFilterType.setStyleSheet("background-color: rgb(255, 255, 255);")
        font.setPointSize(14)
        self.labelFilterType.setFont(font)
        self.labelFilterType.setAlignment(QtCore.Qt.AlignCenter)



        ###########################################################

        #database

        self.arrangeDatabase()

        self.treeWidgetDatabase.resizeColumnToContents(0)
        self.treeWidgetDatabase.setColumnWidth(0,self.treeWidgetDatabase.columnWidth(0)+50)
        self.treeWidgetDatabase.resizeColumnToContents(1)
        self.treeWidgetDatabase.resizeColumnToContents(2)
        self.treeWidgetDatabase.resizeColumnToContents(3)
        self.treeWidgetDatabase.resizeColumnToContents(4)

        ###########################################################

    def pageStatsWidgets(self):
        font = QtGui.QFont()

        self.buttonBackStats = QtWidgets.QPushButton(self.pageStats)
        self.buttonBackStats.setGeometry(QtCore.QRect(20, 830, 81, 35))
        self.buttonBackStats.setText("Back")
        self.buttonBackStats.clicked.connect(lambda: self.switchPage(0))

        self.labelTitleStats = QtWidgets.QLabel(self.pageStats)
        self.labelTitleStats.setGeometry(QtCore.QRect(720, 10, 161, 41))
        font.setPointSize(32)
        self.labelTitleStats.setFont(font)
        self.labelTitleStats.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitleStats.setText("Stats")

        self.frameStats = QtWidgets.QFrame(self.pageStats)
        self.frameStats.setGeometry(QtCore.QRect(500, 70, 600, 741))
        self.frameStats.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameStats.setFrameShadow(QtWidgets.QFrame.Plain)

        self.treeWidgetStats = QtWidgets.QTreeWidget(self.frameStats)
        self.treeWidgetStats.setGeometry(QtCore.QRect(0, 0, 600, 741))
        font.setPointSize(16)
        self.treeWidgetStats.setFont(font)

        for i in range(15):
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetStats)

        self.treeWidgetStats.setHeaderLabels(["Statistic", "Value"])
        self.treeWidgetStats.header().setVisible(True)
        self.treeWidgetStats.header().setDefaultSectionSize(300)
        self.treeWidgetStats.header().setHighlightSections(False)
        self.treeWidgetStats.header().setSortIndicatorShown(False)
        self.treeWidgetStats.header().setStretchLastSection(True)

        self.treeWidgetStats.topLevelItem(0).setText(0, "Total Number of Attempts")
        self.treeWidgetStats.topLevelItem(1).setText(0, "Total Number of Sucessful Solves")
        self.treeWidgetStats.topLevelItem(2).setText(0, "Total Number of Fails")
        self.treeWidgetStats.topLevelItem(3).setText(0, "Number of Automatic Attempts")
        self.treeWidgetStats.topLevelItem(4).setText(0, "Number of Sucessful Automatic Solves")
        self.treeWidgetStats.topLevelItem(5).setText(0, "Number of Failed Automatic Solves")
        self.treeWidgetStats.topLevelItem(6).setText(0, "Average Automatic Solve Time")
        self.treeWidgetStats.topLevelItem(7).setText(0, "Fastest Automatic Solve Time")
        self.treeWidgetStats.topLevelItem(8).setText(0, "Slowest Automatic Solve Time")
        self.treeWidgetStats.topLevelItem(9).setText(0, "Number of Manual Attempts")
        self.treeWidgetStats.topLevelItem(10).setText(0, "Number of Successful Manual Solves")
        self.treeWidgetStats.topLevelItem(11).setText(0, "Number of Failed Manual Solves")
        self.treeWidgetStats.topLevelItem(12).setText(0, "Average Manual Solve Time")
        self.treeWidgetStats.topLevelItem(13).setText(0, "Fastest Manual Solve Time")
        self.treeWidgetStats.topLevelItem(14).setText(0, "Slowest Manual Solve Time")

        self.treeWidgetStats.topLevelItem(0).setText(1, str(solves.count_documents({})))
        self.treeWidgetStats.topLevelItem(1).setText(1, str(solves.count_documents({"success":True})))
        self.treeWidgetStats.topLevelItem(2).setText(1, str(solves.count_documents({"success": False})))
        self.treeWidgetStats.topLevelItem(3).setText(1, str(solves.count_documents({"auto":True})))
        self.treeWidgetStats.topLevelItem(4).setText(1, str(solves.count_documents({"auto":True,"success":True})))
        self.treeWidgetStats.topLevelItem(5).setText(1, str(solves.count_documents({"auto":True,"success":False})))

        ###################################################################################################################

        totalAutoFrames = 0
        lowestAutoFrames = 9999999999
        highestAutoFrames = 0

        for solve in solves.find({"success":True,"auto":True}):
            totalAutoFrames += solve.get("totalFrames")
            if lowestAutoFrames > solve.get("totalFrames"):
                lowestAutoFrames = solve.get("totalFrames")
            if highestAutoFrames < solve.get("totalFrames"):
                highestAutoFrames = solve.get("totalFrames")

        try:
            averageAutoSolve = totalAutoFrames / solves.count_documents({"success": True, "auto": True})
            averageAutoSolve = self.framesToTime(averageAutoSolve)
        except:
            averageAutoSolve = "N/A"
        self.treeWidgetStats.topLevelItem(6).setText(1, averageAutoSolve)

        if lowestAutoFrames == 9999999999:
            lowestAutoFrames = "N/A"
        else:
            lowestAutoFrames = self.framesToTime(lowestAutoFrames)
        self.treeWidgetStats.topLevelItem(7).setText(1, lowestAutoFrames)

        if highestAutoFrames == 0:
            highestAutoFrames = "N/A"
        else:
            highestAutoFrames = self.framesToTime(highestAutoFrames)
        self.treeWidgetStats.topLevelItem(8).setText(1, highestAutoFrames)
        
        self.treeWidgetStats.topLevelItem(9).setText(1, str(solves.count_documents({"auto":False})))
        self.treeWidgetStats.topLevelItem(10).setText(1, str(solves.count_documents({"auto":False,"success":True})))
        self.treeWidgetStats.topLevelItem(11).setText(1, str(solves.count_documents({"auto":False,"success":False})))

        totalManualFrames = 0
        lowestManualFrames = 9999999999
        highestManualFrames = 0

        for i,solve in enumerate(solves.find({"success": True, "auto": False})):
            totalManualFrames += solve.get("totalFrames")
            if lowestManualFrames > solve.get("totalFrames"):
                lowestManualFrames = solve.get("totalFrames")
            if highestManualFrames < solve.get("totalFrames"):
                highestManualFrames = solve.get("totalFrames")

        try:
            averageManualSolve = totalManualFrames / solves.count_documents({"success": True, "auto": False})
            averageManualSolve = self.framesToTime(averageManualSolve)
        except:
            averageManualSolve = "N/A"
        self.treeWidgetStats.topLevelItem(12).setText(1, averageManualSolve)

        if lowestManualFrames == 9999999999:
            lowestManualFrames = "N/A"
        else:
            lowestManualFrames = self.framesToTime(lowestManualFrames)
        self.treeWidgetStats.topLevelItem(13).setText(1, lowestManualFrames)

        if highestManualFrames == 0:
            highestManualFrames = "N/A"
        else:
            highestManualFrames = self.framesToTime(highestManualFrames)
        self.treeWidgetStats.topLevelItem(14).setText(1, highestManualFrames)

        self.treeWidgetStats.resizeColumnToContents(0)
        self.treeWidgetStats.resizeColumnToContents(1)

        ################################################################################################################

    def pageAutoHelpWidgets(self):
        font = QtGui.QFont()

        self.labelAutoHelp = QtWidgets.QLabel(self.pageAutoHelp)
        self.labelAutoHelp.setGeometry(QtCore.QRect(0, 0, 1600, 200))
        font.setPointSize(12)
        self.labelAutoHelp.setFont(font)
        self.labelAutoHelp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAutoHelp.setText("This is the Automated Solve Page. Ensure the ball bearing is in the starting location before beginning your solve.\n "
                                   "Click the Start button to begin the automated solve. If the ball bearing is stuck and the timer does not stop automatically,\n"
                                   "Click the Force Stop button to stop the timer.\n"
                                   "Real time information is displayed to the right.\n"
                                   "When the timer stops automatically, all data of the solve will be saved, including if the solve was sucessful.\n"
                                   "If the solve was forced to stop, all data of the solve will also be saved, but it will result as a fail.\n"
                                   "If the motors do not reset to their default positions automatically, you can click the Reset Position button to do so.")

        self.buttonBackAuto = QtWidgets.QPushButton(self.pageAutoHelp)
        self.buttonBackAuto.setGeometry(QtCore.QRect(1500, 10, 75, 23))
        self.buttonBackAuto.setText("Back")
        self.buttonBackAuto.clicked.connect(lambda: self.switchPage(1))

    def pageManualHelpWidgets(self):
        font = QtGui.QFont()

        self.labelAutoHelp = QtWidgets.QLabel(self.pageManualHelp)
        self.labelAutoHelp.setGeometry(QtCore.QRect(0, 0, 1600, 200))
        font.setPointSize(12)
        self.labelAutoHelp.setFont(font)
        self.labelAutoHelp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAutoHelp.setText("This is the Manual Solve Page. Ensure the ball bearing is in the starting location before beginning your solve.\n "
                                   "Click on the Reset Position button to reset motors to their default position\n"
                                   "When you click the Start button, there will be a countdown before you can move.\n"
                                   "You can use either the Joystick or the sliders to tilt the maze.\n"
                                   "The timer will stop automatically when you reach the goal.\n"
                                   "If the ball bearing is stuck, use the Force Stop button to stop.\n"
                                   "All solves will be saved.\n"
                                   "Real time information is displayed to the right.")

        self.buttonBackAuto = QtWidgets.QPushButton(self.pageManualHelp)
        self.buttonBackAuto.setGeometry(QtCore.QRect(1500, 10, 75, 23))
        self.buttonBackAuto.setText("Back")
        self.buttonBackAuto.clicked.connect(lambda: self.switchPage(2))

    def pageReplayWidgets(self):
        font = QtGui.QFont()

        self.frameVideoReplay = QtWidgets.QFrame(self.pageReplay)
        self.frameVideoReplay.setGeometry(QtCore.QRect(60, 60, 1280, 720))
        self.frameVideoReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.frameVideoReplay.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameInfoReplay = QtWidgets.QFrame(self.pageReplay)
        self.frameInfoReplay.setGeometry(QtCore.QRect(1340, 60, 200, 720))
        self.frameInfoReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.frameInfoReplay.setFrameShadow(QtWidgets.QFrame.Plain)

        self.labelSpeedReplay = QtWidgets.QLabel(self.frameInfoReplay)
        self.labelSpeedReplay.setGeometry(QtCore.QRect(0, 0, 200, 20))
        font.setPointSize(12)
        self.labelSpeedReplay.setFont(font)
        self.labelSpeedReplay.setAutoFillBackground(False)
        self.labelSpeedReplay.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelSpeedReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSpeedReplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelSpeedReplay.setLineWidth(1)
        self.labelSpeedReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeedReplay.setText("Speed (m/s)")

        self.labelSpeedValReplay = QtWidgets.QLabel(self.frameInfoReplay)
        self.labelSpeedValReplay.setGeometry(QtCore.QRect(0, 20, 200, 20))
        font.setPointSize(12)
        self.labelSpeedValReplay.setFont(font)
        self.labelSpeedValReplay.setAutoFillBackground(False)
        self.labelSpeedValReplay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelSpeedValReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.labelSpeedValReplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelSpeedValReplay.setLineWidth(1)
        self.labelSpeedValReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSpeedValReplay.setText("0")

        self.labelAccelReplay = QtWidgets.QLabel(self.frameInfoReplay)
        self.labelAccelReplay.setGeometry(QtCore.QRect(0, 170, 200, 20))
        font.setPointSize(12)
        self.labelAccelReplay.setFont(font)
        self.labelAccelReplay.setAutoFillBackground(False)
        self.labelAccelReplay.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelAccelReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAccelReplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAccelReplay.setLineWidth(1)
        self.labelAccelReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccelReplay.setText("Acceleration (m/s²)")

        self.labelXTiltValReplay = QtWidgets.QLabel(self.frameInfoReplay)
        self.labelXTiltValReplay.setGeometry(QtCore.QRect(0, 360, 200, 20))
        font.setPointSize(12)
        self.labelXTiltValReplay.setFont(font)
        self.labelXTiltValReplay.setAutoFillBackground(False)
        self.labelXTiltValReplay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelXTiltValReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXTiltValReplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelXTiltValReplay.setLineWidth(1)
        self.labelXTiltValReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXTiltValReplay.setText("0")

        self.labelXTiltReplay = QtWidgets.QLabel(self.frameInfoReplay)
        self.labelXTiltReplay.setGeometry(QtCore.QRect(0, 340, 200, 20))
        font.setPointSize(12)
        self.labelXTiltReplay.setFont(font)
        self.labelXTiltReplay.setAutoFillBackground(False)
        self.labelXTiltReplay.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelXTiltReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.labelXTiltReplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelXTiltReplay.setLineWidth(1)
        self.labelXTiltReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelXTiltReplay.setText("X-Tilt (°)")

        self.labelAccelValReplay = QtWidgets.QLabel(self.frameInfoReplay)
        self.labelAccelValReplay.setGeometry(QtCore.QRect(0, 190, 200, 20))
        font.setPointSize(12)
        self.labelAccelValReplay.setFont(font)
        self.labelAccelValReplay.setAutoFillBackground(False)
        self.labelAccelValReplay.setStyleSheet("background-color: rgb(202, 202, 202);\n"
                                           "background-color: rgb(255, 255, 255);")
        self.labelAccelValReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.labelAccelValReplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelAccelValReplay.setLineWidth(1)
        self.labelAccelValReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAccelValReplay.setText("0")

        self.labelYTiltReplay = QtWidgets.QLabel(self.frameInfoReplay)
        self.labelYTiltReplay.setGeometry(QtCore.QRect(0, 510, 200, 20))
        font.setPointSize(12)
        self.labelYTiltReplay.setFont(font)
        self.labelYTiltReplay.setAutoFillBackground(False)
        self.labelYTiltReplay.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelYTiltReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYTiltReplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelYTiltReplay.setLineWidth(1)
        self.labelYTiltReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYTiltReplay.setText("Y-Tilt (°)")

        self.labelYTiltValReplay = QtWidgets.QLabel(self.frameInfoReplay)
        self.labelYTiltValReplay.setGeometry(QtCore.QRect(0, 530, 200, 20))
        font.setPointSize(12)
        self.labelYTiltValReplay.setFont(font)
        self.labelYTiltValReplay.setAutoFillBackground(False)
        self.labelYTiltValReplay.setStyleSheet("background-color: rgb(202, 202, 202);\n"
                                           "background-color: rgb(255, 255, 255);")
        self.labelYTiltValReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.labelYTiltValReplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelYTiltValReplay.setLineWidth(1)
        self.labelYTiltValReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelYTiltValReplay.setText("0")

        self.frameSpeedReplay = QtWidgets.QFrame(self.frameInfoReplay)
        self.frameSpeedReplay.setGeometry(QtCore.QRect(0, 40, 200, 130))
        self.frameSpeedReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.frameSpeedReplay.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameAccelReplay = QtWidgets.QFrame(self.frameInfoReplay)
        self.frameAccelReplay.setGeometry(QtCore.QRect(0, 210, 200, 130))
        self.frameAccelReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.frameAccelReplay.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameXTiltReplay = QtWidgets.QFrame(self.frameInfoReplay)
        self.frameXTiltReplay.setGeometry(QtCore.QRect(0, 380, 200, 130))
        self.frameXTiltReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.frameXTiltReplay.setFrameShadow(QtWidgets.QFrame.Plain)

        self.frameYTiltReplay = QtWidgets.QFrame(self.frameInfoReplay)
        self.frameYTiltReplay.setGeometry(QtCore.QRect(0, 550, 200, 130))
        self.frameYTiltReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.frameYTiltReplay.setFrameShadow(QtWidgets.QFrame.Plain)

        self.labelBallCoodReplay = QtWidgets.QLabel(self.frameInfoReplay)
        self.labelBallCoodReplay.setGeometry(QtCore.QRect(0, 680, 200, 20))
        font.setPointSize(12)
        self.labelBallCoodReplay.setFont(font)
        self.labelBallCoodReplay.setAutoFillBackground(False)
        self.labelBallCoodReplay.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.labelBallCoodReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBallCoodReplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelBallCoodReplay.setLineWidth(1)
        self.labelBallCoodReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBallCoodReplay.setText("Ball Coordinates")

        self.labelBallCoodValReplay = QtWidgets.QLabel(self.frameInfoReplay)
        self.labelBallCoodValReplay.setGeometry(QtCore.QRect(0, 700, 200, 20))
        font.setPointSize(12)
        self.labelBallCoodValReplay.setFont(font)
        self.labelBallCoodValReplay.setAutoFillBackground(False)
        self.labelBallCoodValReplay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelBallCoodValReplay.setFrameShape(QtWidgets.QFrame.Box)
        self.labelBallCoodValReplay.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelBallCoodValReplay.setLineWidth(1)
        self.labelBallCoodValReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBallCoodValReplay.setText("(0,0)")

        self.labelTitleReplay = QtWidgets.QLabel(self.pageReplay)
        self.labelTitleReplay.setGeometry(QtCore.QRect(140, 0, 1320, 60))
        font.setPointSize(32)
        self.labelTitleReplay.setFont(font)
        self.labelTitleReplay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitleReplay.setText("Replay")

        self.buttonBackReplay = QtWidgets.QPushButton(self.pageReplay)
        self.buttonBackReplay.setGeometry(QtCore.QRect(20, 830, 81, 31))
        font.setPointSize(8)
        self.buttonBackReplay.setFont(font)
        self.buttonBackReplay.setText("Back")
        self.buttonBackReplay.clicked.connect(self.switchPageDatabase)

        self.frameReplayControl = QtWidgets.QFrame(self.pageReplay)
        self.frameReplayControl.setGeometry(QtCore.QRect(490, 790, 600, 100))
        self.frameReplayControl.setFrameShape(QtWidgets.QFrame.Box)
        self.frameReplayControl.setFrameShadow(QtWidgets.QFrame.Plain)

        #######################################################################################################################

        #directional widgets

        self.directionSpeedReplay = directionWidget.DirectionWidget(self.frameSpeedReplay, labelVal=self.labelSpeedValReplay, type="speed")
        self.directionAccelReplay = directionWidget.DirectionWidget(self.frameAccelReplay, labelVal=self.labelAccelValReplay,type="accel")
        self.xTiltReplay = tiltWidget.TiltWidget(self.frameXTiltReplay, labelTilt=self.labelXTiltValReplay)
        self.yTiltReplay = tiltWidget.TiltWidget(self.frameYTiltReplay, labelTilt=self.labelYTiltValReplay)


        ####################################################################################################################

    def switchPage(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def prettyTime(self, time):
        x = time.split(":")
        return f"{x[2]}/{x[1]}/{x[0]} ({x[3]}:{x[4]}:{x[5]})"

    #holes walls path
    def imageProcessing(self):
        holesArrayTemp = [
            [150, 264, 34, 186, 126, 106, 185, 250, 324, 377, 150, 83, 224, 222, 295, 297, 57, 86, 71, 348, 125, 441,
             142, 232, 391, 94, 125, 377, 34, 296, 303, 152, 408, 444, 273, 366, 34, 377, 442, 441, 200],
            [211, 164, 211, 581, 349, 68, 164, 439, 210, 163, 257, 164, 211, 68, 256, 532, 117, 396, 304, 394, 535, 393,
             118, 349, 348, 582, 488, 116, 536, 394, 303, 396, 578, 532, 485, 485, 396, 211, 485, 68, 313],
            [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
             17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 16, 17, 16]]
        holesArray = list(map(list, zip(holesArrayTemp[0], holesArrayTemp[1])))

        for i, _ in enumerate(holesArray):
            holesArray[i].append(holesArrayTemp[2][i])

        wallsArray = [[450, 200, 20, 100], [900, 500, 200, 30]]
        wallsArrayTemp = [array([[[13, 553]],

                                 [[14, 552]],

                                 [[26, 552]],

                                 [[27, 553]],

                                 [[45, 553]],

                                 [[47, 555]],

                                 [[47, 566]],

                                 [[46, 567]],

                                 [[46, 568]],

                                 [[42, 572]],

                                 [[17, 572]],

                                 [[16, 573]],

                                 [[6, 573]],

                                 [[4, 571]],

                                 [[4, 558]],

                                 [[5, 557]],

                                 [[5, 556]],

                                 [[8, 553]]], dtype=int32), array([[[210, 549]],

                                                                   [[311, 549]],

                                                                   [[313, 551]],

                                                                   [[313, 553]],

                                                                   [[314, 554]],

                                                                   [[314, 565]],

                                                                   [[311, 568]],

                                                                   [[224, 568]],

                                                                   [[223, 569]],

                                                                   [[222, 569]],

                                                                   [[222, 606]],

                                                                   [[220, 608]],

                                                                   [[208, 608]],

                                                                   [[206, 606]],

                                                                   [[206, 552]],

                                                                   [[207, 551]],

                                                                   [[208, 551]]], dtype=int32), array([[[426, 548]],

                                                                                                       [[436, 548]],

                                                                                                       [[441, 553]],

                                                                                                       [[441, 554]],

                                                                                                       [[442, 555]],

                                                                                                       [[442, 604]],

                                                                                                       [[441, 605]],

                                                                                                       [[429, 605]],

                                                                                                       [[427, 603]],

                                                                                                       [[426, 603]],

                                                                                                       [[424, 601]],

                                                                                                       [[424, 570]],

                                                                                                       [[423, 569]],

                                                                                                       [[423, 552]],

                                                                                                       [[424, 551]],

                                                                                                       [[424, 550]]],
                                                                                                      dtype=int32),
                          array([[[344, 548]],

                                 [[394, 548]],

                                 [[396, 550]],

                                 [[396, 551]],

                                 [[398, 553]],

                                 [[398, 565]],

                                 [[396, 567]],

                                 [[346, 567]],

                                 [[342, 563]],

                                 [[342, 562]],

                                 [[341, 561]],

                                 [[341, 551]]], dtype=int32), array([[[53, 506]],

                                                                     [[54, 505]],

                                                                     [[86, 505]],

                                                                     [[88, 507]],

                                                                     [[88, 518]],

                                                                     [[86, 520]],

                                                                     [[86, 521]],

                                                                     [[84, 523]],

                                                                     [[83, 523]],

                                                                     [[82, 524]],

                                                                     [[51, 524]],

                                                                     [[48, 521]],

                                                                     [[48, 511]],

                                                                     [[50, 509]],

                                                                     [[50, 508]],

                                                                     [[52, 506]]], dtype=int32), array([[[195, 503]],

                                                                                                        [[196, 502]],

                                                                                                        [[219, 502]],

                                                                                                        [[221, 504]],

                                                                                                        [[221, 505]],

                                                                                                        [[222, 506]],

                                                                                                        [[222, 516]],

                                                                                                        [[221, 517]],

                                                                                                        [[221, 518]],

                                                                                                        [[218, 521]],

                                                                                                        [[171, 521]],

                                                                                                        [[170, 522]],

                                                                                                        [[132, 522]],

                                                                                                        [[131, 521]],

                                                                                                        [[130, 521]],

                                                                                                        [[129, 520]],

                                                                                                        [[114, 520]],

                                                                                                        [[113, 519]],

                                                                                                        [[113, 508]],

                                                                                                        [[114, 507]],

                                                                                                        [[114, 506]],

                                                                                                        [[115, 505]],

                                                                                                        [[116, 505]],

                                                                                                        [[117, 504]],

                                                                                                        [[141, 504]],

                                                                                                        [[142, 503]]],
                                                                                                       dtype=int32),
                          array([[[436, 501]],

                                 [[474, 501]],

                                 [[477, 504]],

                                 [[477, 505]],

                                 [[478, 506]],

                                 [[478, 518]],

                                 [[477, 519]],

                                 [[451, 519]],

                                 [[450, 518]],

                                 [[449, 518]],

                                 [[448, 517]],

                                 [[437, 517]],

                                 [[436, 516]],

                                 [[435, 516]],

                                 [[434, 515]],

                                 [[434, 503]]], dtype=int32), array([[[359, 454]],

                                                                     [[395, 454]],

                                                                     [[396, 455]],

                                                                     [[397, 455]],

                                                                     [[399, 457]],

                                                                     [[400, 457]],

                                                                     [[401, 458]],

                                                                     [[401, 459]],

                                                                     [[402, 460]],

                                                                     [[402, 478]],

                                                                     [[403, 479]],

                                                                     [[403, 516]],

                                                                     [[400, 519]],

                                                                     [[331, 519]],

                                                                     [[330, 520]],

                                                                     [[309, 520]],

                                                                     [[308, 519]],

                                                                     [[304, 519]],

                                                                     [[303, 518]],

                                                                     [[302, 518]],

                                                                     [[301, 517]],

                                                                     [[294, 517]],

                                                                     [[293, 518]],

                                                                     [[292, 518]],

                                                                     [[291, 519]],

                                                                     [[290, 519]],

                                                                     [[289, 520]],

                                                                     [[256, 520]],

                                                                     [[253, 517]],

                                                                     [[253, 516]],

                                                                     [[252, 515]],

                                                                     [[252, 505]],

                                                                     [[253, 504]],

                                                                     [[253, 503]],

                                                                     [[254, 502]],

                                                                     [[255, 502]],

                                                                     [[256, 501]],

                                                                     [[266, 501]],

                                                                     [[267, 502]],

                                                                     [[301, 502]],

                                                                     [[302, 501]],

                                                                     [[355, 501]],

                                                                     [[356, 502]],

                                                                     [[372, 502]],

                                                                     [[373, 501]],

                                                                     [[385, 501]],

                                                                     [[385, 484]],

                                                                     [[384, 483]],

                                                                     [[384, 472]],

                                                                     [[373, 472]],

                                                                     [[372, 471]],

                                                                     [[371, 471]],

                                                                     [[370, 470]],

                                                                     [[370, 469]],

                                                                     [[358, 469]],

                                                                     [[357, 468]],

                                                                     [[357, 456]]], dtype=int32), array([[[160, 412]],

                                                                                                         [[161, 411]],

                                                                                                         [[195, 411]],

                                                                                                         [[197, 413]],

                                                                                                         [[197, 425]],

                                                                                                         [[194, 428]],

                                                                                                         [[164, 428]],

                                                                                                         [[163, 429]],

                                                                                                         [[163, 470]],

                                                                                                         [[159, 474]],

                                                                                                         [[130, 474]],

                                                                                                         [[129, 473]],

                                                                                                         [[122, 473]],

                                                                                                         [[121, 474]],

                                                                                                         [[115, 474]],

                                                                                                         [[114, 475]],

                                                                                                         [[74, 475]],

                                                                                                         [[73, 476]],

                                                                                                         [[52, 476]],

                                                                                                         [[51, 475]],

                                                                                                         [[50, 475]],

                                                                                                         [[49, 474]],

                                                                                                         [[49, 463]],

                                                                                                         [[50, 462]],

                                                                                                         [[50, 461]],

                                                                                                         [[54, 457]],

                                                                                                         [[126, 457]],

                                                                                                         [[128, 459]],

                                                                                                         [[128, 461]],

                                                                                                         [[150, 461]],

                                                                                                         [[151, 460]],

                                                                                                         [[151, 459]],

                                                                                                         [[149, 459]],

                                                                                                         [[148, 458]],

                                                                                                         [[148, 451]],

                                                                                                         [[147, 450]],

                                                                                                         [[147, 440]],

                                                                                                         [[148, 439]],

                                                                                                         [[148, 414]],

                                                                                                         [[149, 413]],

                                                                                                         [[150, 413]],

                                                                                                         [[151, 412]]],
                                                                                                        dtype=int32),
                          array([[[218, 409]],

                                 [[219, 408]],

                                 [[231, 408]],

                                 [[234, 411]],

                                 [[234, 456]],

                                 [[235, 455]],

                                 [[246, 455]],

                                 [[247, 456]],

                                 [[252, 456]],

                                 [[253, 455]],

                                 [[283, 455]],

                                 [[286, 458]],

                                 [[286, 469]],

                                 [[285, 470]],

                                 [[270, 470]],

                                 [[269, 471]],

                                 [[268, 471]],

                                 [[267, 472]],

                                 [[235, 472]],

                                 [[234, 473]],

                                 [[197, 473]],

                                 [[194, 470]],

                                 [[194, 458]],

                                 [[197, 455]],

                                 [[218, 455]]], dtype=int32), array([[[53, 366]],

                                                                     [[64, 366]],

                                                                     [[67, 369]],

                                                                     [[67, 424]],

                                                                     [[66, 425]],

                                                                     [[66, 426]],

                                                                     [[64, 428]],

                                                                     [[63, 428]],

                                                                     [[62, 429]],

                                                                     [[50, 429]],

                                                                     [[49, 428]],

                                                                     [[49, 427]],

                                                                     [[48, 426]],

                                                                     [[48, 409]],

                                                                     [[49, 408]],

                                                                     [[49, 401]],

                                                                     [[50, 400]],

                                                                     [[50, 393]],

                                                                     [[49, 392]],

                                                                     [[49, 370]]], dtype=int32), array([[[197, 365]],

                                                                                                        [[198, 364]],

                                                                                                        [[214, 364]],

                                                                                                        [[217, 367]],

                                                                                                        [[217, 378]],

                                                                                                        [[214, 381]],

                                                                                                        [[131, 381]],

                                                                                                        [[129, 379]],

                                                                                                        [[129, 368]],

                                                                                                        [[131, 366]],

                                                                                                        [[132, 366]],

                                                                                                        [[133, 365]]],
                                                                                                       dtype=int32),
                          array([[[52, 320]],

                                 [[53, 319]],

                                 [[67, 319]],

                                 [[68, 320]],

                                 [[75, 320]],

                                 [[76, 319]],

                                 [[131, 319]],

                                 [[132, 320]],

                                 [[133, 320]],

                                 [[134, 321]],

                                 [[134, 331]],

                                 [[132, 333]],

                                 [[129, 333]],

                                 [[128, 334]],

                                 [[123, 334]],

                                 [[122, 335]],

                                 [[52, 335]],

                                 [[49, 332]],

                                 [[49, 322]],

                                 [[51, 320]]], dtype=int32), array([[[273, 319]],

                                                                    [[274, 318]],

                                                                    [[299, 318]],

                                                                    [[300, 319]],

                                                                    [[316, 319]],

                                                                    [[318, 321]],

                                                                    [[318, 331]],

                                                                    [[315, 334]],

                                                                    [[274, 334]],

                                                                    [[271, 331]],

                                                                    [[271, 320]],

                                                                    [[272, 319]]], dtype=int32), array([[[215, 318]],

                                                                                                        [[243, 318]],

                                                                                                        [[246, 321]],

                                                                                                        [[246, 331]],

                                                                                                        [[243, 334]],

                                                                                                        [[212, 334]],

                                                                                                        [[211, 333]],

                                                                                                        [[211, 323]],

                                                                                                        [[212, 322]],

                                                                                                        [[212, 321]]],
                                                                                                       dtype=int32),
                          array([[[347, 317]],

                                 [[370, 317]],

                                 [[371, 318]],

                                 [[383, 318]],

                                 [[384, 319]],

                                 [[385, 319]],

                                 [[386, 320]],

                                 [[386, 331]],

                                 [[383, 334]],

                                 [[349, 334]],

                                 [[348, 333]],

                                 [[347, 333]],

                                 [[344, 330]],

                                 [[344, 320]]], dtype=int32), array([[[165, 273]],

                                                                     [[166, 272]],

                                                                     [[273, 272]],

                                                                     [[276, 275]],

                                                                     [[276, 285]],

                                                                     [[275, 286]],

                                                                     [[275, 287]],

                                                                     [[274, 288]],

                                                                     [[179, 288]],

                                                                     [[178, 289]],

                                                                     [[177, 289]],

                                                                     [[177, 332]],

                                                                     [[175, 334]],

                                                                     [[163, 334]],

                                                                     [[161, 332]],

                                                                     [[161, 276]],

                                                                     [[164, 273]]], dtype=int32), array([[[72, 273]],

                                                                                                         [[73, 272]],

                                                                                                         [[83, 272]],

                                                                                                         [[84, 273]],

                                                                                                         [[86, 273]],

                                                                                                         [[87, 274]],

                                                                                                         [[88, 274]],

                                                                                                         [[89, 275]],

                                                                                                         [[89, 286]],

                                                                                                         [[87, 288]],

                                                                                                         [[86, 288]],

                                                                                                         [[85, 289]],

                                                                                                         [[72, 289]],

                                                                                                         [[71, 288]],

                                                                                                         [[51, 288]],

                                                                                                         [[49, 286]],

                                                                                                         [[49, 275]],

                                                                                                         [[51, 273]]],
                                                                                                        dtype=int32),
                          array([[[195, 226]],

                                 [[220, 226]],

                                 [[221, 227]],

                                 [[228, 227]],

                                 [[229, 226]],

                                 [[253, 226]],

                                 [[255, 228]],

                                 [[255, 239]],

                                 [[251, 243]],

                                 [[222, 243]],

                                 [[221, 242]],

                                 [[219, 242]],

                                 [[218, 243]],

                                 [[196, 243]],

                                 [[193, 240]],

                                 [[193, 228]]], dtype=int32), array([[[384, 226]],

                                                                     [[385, 225]],

                                                                     [[424, 225]],

                                                                     [[425, 226]],

                                                                     [[426, 226]],

                                                                     [[427, 227]],

                                                                     [[427, 364]],

                                                                     [[429, 364]],

                                                                     [[430, 363]],

                                                                     [[442, 363]],

                                                                     [[443, 364]],

                                                                     [[474, 364]],

                                                                     [[476, 366]],

                                                                     [[476, 367]],

                                                                     [[477, 368]],

                                                                     [[477, 378]],

                                                                     [[476, 379]],

                                                                     [[475, 379]],

                                                                     [[474, 380]],

                                                                     [[456, 380]],

                                                                     [[455, 379]],

                                                                     [[446, 379]],

                                                                     [[445, 378]],

                                                                     [[438, 378]],

                                                                     [[437, 379]],

                                                                     [[412, 379]],

                                                                     [[411, 380]],

                                                                     [[389, 380]],

                                                                     [[388, 379]],

                                                                     [[387, 379]],

                                                                     [[387, 388]],

                                                                     [[388, 389]],

                                                                     [[388, 412]],

                                                                     [[387, 413]],

                                                                     [[387, 414]],

                                                                     [[386, 415]],

                                                                     [[374, 415]],

                                                                     [[370, 411]],

                                                                     [[370, 380]],

                                                                     [[353, 380]],

                                                                     [[352, 379]],

                                                                     [[345, 379]],

                                                                     [[344, 380]],

                                                                     [[325, 380]],

                                                                     [[328, 380]],

                                                                     [[329, 381]],

                                                                     [[329, 389]],

                                                                     [[330, 390]],

                                                                     [[330, 469]],

                                                                     [[328, 471]],

                                                                     [[317, 471]],

                                                                     [[313, 467]],

                                                                     [[313, 380]],

                                                                     [[301, 380]],

                                                                     [[300, 379]],

                                                                     [[293, 379]],

                                                                     [[292, 380]],

                                                                     [[244, 380]],

                                                                     [[241, 377]],

                                                                     [[241, 366]],

                                                                     [[242, 365]],

                                                                     [[243, 365]],

                                                                     [[244, 364]],

                                                                     [[357, 364]],

                                                                     [[358, 363]],

                                                                     [[380, 363]],

                                                                     [[381, 364]],

                                                                     [[381, 373]],

                                                                     [[383, 375]],

                                                                     [[383, 376]],

                                                                     [[385, 376]],

                                                                     [[385, 365]],

                                                                     [[386, 364]],

                                                                     [[407, 364]],

                                                                     [[409, 362]],

                                                                     [[409, 241]],

                                                                     [[394, 241]],

                                                                     [[393, 242]],

                                                                     [[383, 242]],

                                                                     [[382, 241]],

                                                                     [[362, 241]],

                                                                     [[360, 239]],

                                                                     [[360, 229]],

                                                                     [[363, 226]],

                                                                     [[373, 226]],

                                                                     [[374, 227]],

                                                                     [[381, 227]],

                                                                     [[382, 226]]], dtype=int32), array([[[289, 226]],

                                                                                                         [[290, 225]],

                                                                                                         [[304, 225]],

                                                                                                         [[305, 226]],

                                                                                                         [[326, 226]],

                                                                                                         [[329, 229]],

                                                                                                         [[329, 272]],

                                                                                                         [[384, 272]],

                                                                                                         [[386, 274]],

                                                                                                         [[386, 285]],

                                                                                                         [[384, 287]],

                                                                                                         [[380, 287]],

                                                                                                         [[379, 288]],

                                                                                                         [[316, 288]],

                                                                                                         [[315, 287]],

                                                                                                         [[314, 287]],

                                                                                                         [[313, 286]],

                                                                                                         [[313, 285]],

                                                                                                         [[312, 284]],

                                                                                                         [[312, 244]],

                                                                                                         [[311, 243]],

                                                                                                         [[309, 243]],

                                                                                                         [[308, 242]],

                                                                                                         [[300, 242]],

                                                                                                         [[299, 241]],

                                                                                                         [[286, 241]],

                                                                                                         [[284, 239]],

                                                                                                         [[284, 229]],

                                                                                                         [[286, 227]],

                                                                                                         [[287, 227]],

                                                                                                         [[288, 226]]],
                                                                                                        dtype=int32),
                          array([[[52, 225]],

                                 [[67, 225]],

                                 [[68, 226]],

                                 [[129, 226]],

                                 [[130, 227]],

                                 [[131, 227]],

                                 [[134, 230]],

                                 [[134, 249]],

                                 [[133, 250]],

                                 [[133, 265]],

                                 [[134, 266]],

                                 [[134, 285]],

                                 [[131, 288]],

                                 [[120, 288]],

                                 [[117, 285]],

                                 [[117, 242]],

                                 [[53, 242]],

                                 [[52, 241]],

                                 [[51, 241]],

                                 [[49, 239]],

                                 [[49, 228]]], dtype=int32), array([[[297, 179]],

                                                                    [[332, 179]],

                                                                    [[334, 181]],

                                                                    [[334, 192]],

                                                                    [[331, 195]],

                                                                    [[314, 195]],

                                                                    [[313, 196]],

                                                                    [[296, 196]],

                                                                    [[295, 195]],

                                                                    [[294, 195]],

                                                                    [[293, 194]],

                                                                    [[293, 183]]], dtype=int32), array([[[196, 179]],

                                                                                                        [[252, 179]],

                                                                                                        [[255, 182]],

                                                                                                        [[255, 193]],

                                                                                                        [[252, 196]],

                                                                                                        [[231, 196]],

                                                                                                        [[230, 195]],

                                                                                                        [[218, 195]],

                                                                                                        [[217, 196]],

                                                                                                        [[195, 196]],

                                                                                                        [[193, 194]],

                                                                                                        [[193, 182]]],
                                                                                                       dtype=int32),
                          array([[[87, 180]],

                                 [[88, 179]],

                                 [[113, 179]],

                                 [[117, 183]],

                                 [[117, 194]],

                                 [[116, 195]],

                                 [[115, 195]],

                                 [[114, 196]],

                                 [[80, 196]],

                                 [[79, 195]],

                                 [[77, 195]],

                                 [[74, 192]],

                                 [[74, 181]],

                                 [[75, 180]]], dtype=int32), array([[[435, 179]],

                                                                    [[436, 178]],

                                                                    [[476, 178]],

                                                                    [[477, 179]],

                                                                    [[477, 190]],

                                                                    [[476, 191]],

                                                                    [[476, 192]],

                                                                    [[474, 194]],

                                                                    [[457, 194]],

                                                                    [[456, 195]],

                                                                    [[434, 195]],

                                                                    [[431, 192]],

                                                                    [[431, 182]],

                                                                    [[434, 179]]], dtype=int32), array([[[381, 179]],

                                                                                                        [[382, 178]],

                                                                                                        [[393, 178]],

                                                                                                        [[394, 179]],

                                                                                                        [[395, 179]],

                                                                                                        [[396, 180]],

                                                                                                        [[396, 192]],

                                                                                                        [[395, 193]],

                                                                                                        [[394, 193]],

                                                                                                        [[392, 195]],

                                                                                                        [[380, 195]],

                                                                                                        [[379, 194]],

                                                                                                        [[376, 194]],

                                                                                                        [[375, 195]],

                                                                                                        [[362, 195]],

                                                                                                        [[361, 194]],

                                                                                                        [[361, 182]],

                                                                                                        [[364, 179]]],
                                                                                                       dtype=int32),
                          array([[[3, 179]],

                                 [[4, 178]],

                                 [[42, 178]],

                                 [[43, 179]],

                                 [[44, 179]],

                                 [[46, 181]],

                                 [[47, 181]],

                                 [[48, 182]],

                                 [[48, 193]],

                                 [[46, 195]],

                                 [[6, 195]],

                                 [[4, 193]],

                                 [[4, 192]],

                                 [[3, 191]]], dtype=int32), array([[[207, 132]],

                                                                   [[252, 132]],

                                                                   [[255, 135]],

                                                                   [[255, 146]],

                                                                   [[251, 150]],

                                                                   [[207, 150]],

                                                                   [[205, 148]],

                                                                   [[205, 147]],

                                                                   [[204, 146]],

                                                                   [[204, 136]],

                                                                   [[205, 135]],

                                                                   [[205, 134]]], dtype=int32), array([[[397, 131]],

                                                                                                       [[398, 130]],

                                                                                                       [[425, 130]],

                                                                                                       [[428, 133]],

                                                                                                       [[428, 143]],

                                                                                                       [[423, 148]],

                                                                                                       [[422, 148]],

                                                                                                       [[421, 149]],

                                                                                                       [[395, 149]],

                                                                                                       [[393, 147]],

                                                                                                       [[392, 147]],

                                                                                                       [[391, 146]],

                                                                                                       [[391, 135]],

                                                                                                       [[393, 133]],

                                                                                                       [[394, 133]],

                                                                                                       [[396, 131]]],
                                                                                                      dtype=int32),
                          array([[[207, 84]],

                                 [[252, 84]],

                                 [[255, 87]],

                                 [[255, 99]],

                                 [[254, 100]],

                                 [[254, 101]],

                                 [[252, 103]],

                                 [[206, 103]],

                                 [[204, 101]],

                                 [[204, 88]],

                                 [[205, 87]],

                                 [[205, 86]]], dtype=int32), array([[[279, 72]],

                                                                    [[289, 72]],

                                                                    [[291, 74]],

                                                                    [[291, 75]],

                                                                    [[292, 76]],

                                                                    [[292, 131]],

                                                                    [[363, 131]],

                                                                    [[365, 133]],

                                                                    [[365, 144]],

                                                                    [[364, 145]],

                                                                    [[364, 146]],

                                                                    [[362, 148]],

                                                                    [[361, 148]],

                                                                    [[360, 149]],

                                                                    [[278, 149]],

                                                                    [[275, 146]],

                                                                    [[275, 78]],

                                                                    [[276, 77]],

                                                                    [[276, 76]],

                                                                    [[277, 75]],

                                                                    [[277, 74]]], dtype=int32), array([[[160, 73]],

                                                                                                       [[161, 72]],

                                                                                                       [[172, 72]],

                                                                                                       [[174, 74]],

                                                                                                       [[174, 75]],

                                                                                                       [[175, 76]],

                                                                                                       [[175, 129]],

                                                                                                       [[176, 130]],

                                                                                                       [[176, 146]],

                                                                                                       [[175, 147]],

                                                                                                       [[175, 148]],

                                                                                                       [[174, 149]],

                                                                                                       [[173, 149]],

                                                                                                       [[172, 150]],

                                                                                                       [[158, 150]],

                                                                                                       [[157, 149]],

                                                                                                       [[87, 149]],

                                                                                                       [[86, 148]],

                                                                                                       [[78, 148]],

                                                                                                       [[77, 149]],

                                                                                                       [[54, 149]],

                                                                                                       [[53, 148]],

                                                                                                       [[52, 148]],

                                                                                                       [[51, 147]],

                                                                                                       [[50, 147]],

                                                                                                       [[48, 145]],

                                                                                                       [[48, 134]],

                                                                                                       [[49, 133]],

                                                                                                       [[61, 133]],

                                                                                                       [[62, 132]],

                                                                                                       [[63, 132]],

                                                                                                       [[64, 131]],

                                                                                                       [[133, 131]],

                                                                                                       [[134, 132]],

                                                                                                       [[136, 132]],

                                                                                                       [[137, 133]],

                                                                                                       [[138, 133]],

                                                                                                       [[139, 134]],

                                                                                                       [[146, 134]],

                                                                                                       [[147, 133]],

                                                                                                       [[148, 133]],

                                                                                                       [[149, 132]],

                                                                                                       [[158, 132]],

                                                                                                       [[159, 131]],

                                                                                                       [[159, 75]],

                                                                                                       [[160, 74]]],
                                                                                                      dtype=int32),
                          array([[[415, 42]],

                                 [[416, 41]],

                                 [[427, 41]],

                                 [[429, 43]],

                                 [[429, 60]],

                                 [[428, 61]],

                                 [[428, 62]],

                                 [[427, 63]],

                                 [[427, 64]],

                                 [[426, 65]],

                                 [[426, 72]],

                                 [[427, 73]],

                                 [[427, 74]],

                                 [[428, 75]],

                                 [[428, 76]],

                                 [[429, 77]],

                                 [[429, 94]],

                                 [[428, 95]],

                                 [[428, 96]],

                                 [[425, 99]],

                                 [[425, 100]],

                                 [[424, 101]],

                                 [[412, 101]],

                                 [[411, 100]],

                                 [[411, 99]],

                                 [[410, 98]],

                                 [[410, 46]],

                                 [[411, 45]],

                                 [[411, 44]],

                                 [[412, 43]],

                                 [[413, 43]],

                                 [[414, 42]]], dtype=int32), array([[[323, 42]],

                                                                    [[324, 41]],

                                                                    [[334, 41]],

                                                                    [[336, 43]],

                                                                    [[336, 95]],

                                                                    [[335, 96]],

                                                                    [[335, 97]],

                                                                    [[334, 98]],

                                                                    [[334, 100]],

                                                                    [[332, 102]],

                                                                    [[321, 102]],

                                                                    [[318, 99]],

                                                                    [[318, 46]],

                                                                    [[319, 45]],

                                                                    [[319, 44]],

                                                                    [[321, 42]]], dtype=int32), array([[[71, 42]],

                                                                                                       [[72, 41]],

                                                                                                       [[86, 41]],

                                                                                                       [[88, 43]],

                                                                                                       [[88, 44]],

                                                                                                       [[89, 45]],

                                                                                                       [[89, 76]],

                                                                                                       [[86, 79]],

                                                                                                       [[76, 79]],

                                                                                                       [[72, 75]],

                                                                                                       [[72, 73]],

                                                                                                       [[71, 72]]],
                                                                                                      dtype=int32)]

        wallsArray = []

        for i, _ in enumerate(wallsArrayTemp):
            wall = []
            for j, _ in enumerate(wallsArrayTemp[i]):
                wall.append(list(wallsArrayTemp[i][j][0]))
            wallsArray.append(wall)

        pathArray = [[266, 574], [267, 574], [297, 573], [327, 570], [329, 540], [359, 537], [389, 537], [415, 529],
                     [414, 499], [414, 469], [410, 439], [380, 439], [350, 438], [338, 459], [330, 485], [300, 481],
                     [298, 451], [279, 422], [254, 394], [224, 392], [201, 404], [201, 434], [177, 446], [176, 476],
                     [201, 485], [231, 485], [236, 513], [221, 532], [191, 532], [161, 534], [158, 564], [133, 574],
                     [105, 552], [96, 523], [96, 493], [68, 487], [38, 487], [29, 463], [41, 441], [71, 440],
                     [101, 441], [116, 421], [117, 391], [95, 361], [69, 349], [39, 349], [30, 324], [30, 294],
                     [30, 264], [56, 257], [86, 257], [110, 267], [110, 297], [138, 303], [150, 325], [161, 347],
                     [189, 342], [189, 312], [213, 302], [243, 302], [259, 320], [266, 347], [296, 348], [326, 347],
                     [332, 320], [347, 303], [377, 302], [394, 285], [388, 256], [358, 256], [349, 231], [349, 201],
                     [349, 171], [323, 163], [293, 167], [274, 197], [263, 227], [258, 256], [228, 256], [198, 257],
                     [180, 241], [179, 211], [163, 183], [133, 176], [129, 204], [104, 214], [75, 197], [51, 170],
                     [28, 142], [27, 112], [29, 82], [59, 82], [89, 99], [119, 92], [147, 65], [177, 64], [191, 85],
                     [194, 114], [224, 115], [254, 116], [264, 92], [271, 65], [301, 65], [306, 94], [319, 115],
                     [346, 110], [346, 80], [365, 65], [395, 65], [405, 88], [413, 115], [442, 118], [443, 148],
                     [422, 160], [413, 186], [425, 209], [442, 225], [442, 255], [442, 285], [442, 315], [443, 334]]

        return holesArray, wallsArray, pathArray

    def imageProcessingMarble(self):
        try:
            self.marbleManual.updateCood(40, 40)
            self.marbleManual.updateSpeedDirection(50, 50)
            self.marbleManual.updateAccelDirection(70, 70)

            self.marbleAuto.updateCood(40,40)
            self.marbleAuto.updateSpeedDirection(50,50)
            self.marbleAuto.updateAccelDirection(70, 70)


        except:
            pass

    def loadReplay(self):
            self.mazeID = self.treeWidgetDatabase.currentItem().text(5)
            cursor = solves.find_one({"_id":ObjectId(self.mazeID)})
            difficulty = cursor.get("type")
            walls = cursor.get("wall")
            path = cursor.get("path")
            holes = cursor.get("holes")
            frameData = cursor.get("frameData")
            self.boardReplay = renderBoard2D.RenderBoard2D(self.frameVideoReplay, difficulty=difficulty, walls=walls, path=path, holes=holes)
            self.marbleReplay = renderMarble2D.RenderMarble(self.frameVideoReplay, mazeWidth=self.boardReplay.width, mazeHeight=self.boardReplay.height,
                                             mazeX=self.boardReplay.minX, mazeY=self.boardReplay.minY, labelCoodVal=self.labelBallCoodValReplay, speed=self.directionSpeedReplay,
                                             accel=self.directionAccelReplay)
            self.directionSpeedReplay.marble = self.marbleReplay
            self.directionAccelReplay.marble = self.marbleReplay

            self.playback = replayWidget.ReplayWidget(self.frameReplayControl, frameData=frameData, marble=self.marbleReplay, speed=self.directionSpeedReplay,
                                                      accel=self.directionAccelReplay, tiltX=self.xTiltReplay, tiltY=self.yTiltReplay)

            self.switchPage(7)

    def loadAuto(self):
        self.boardAuto = renderBoard2D.RenderBoard2D(self.frameVideoAuto,holes=self.imageProcessing()[0],walls=self.imageProcessing()[1],path=self.imageProcessing()[2], difficulty="Easy")
        self.marbleAuto = renderMarble2D.RenderMarble(self.frameVideoAuto, mazeWidth=self.boardAuto.width, mazeHeight=self.boardAuto.height, mazeX=self.boardAuto.minX,
                                                            mazeY=self.boardAuto.minY, labelCoodVal=self.labelBallCoodValAuto, speed=self.directionSpeedAuto, accel=self.directionAccelAuto)
        self.directionSpeedAuto.marble = self.marbleAuto
        self.directionAccelAuto.marble = self.marbleAuto
        self.imageProcessingMarble()
        self.switchPage(1)

    def loadManual(self):
        self.boardManual = renderBoard2D.RenderBoard2D(self.frameVideoManual, holes=self.imageProcessing()[0],
                                                     walls=self.imageProcessing()[1], path=self.imageProcessing()[2],
                                                     difficulty="Custom")
        self.marbleManual = renderMarble2D.RenderMarble(self.frameVideoManual, mazeWidth=self.boardManual.width,
                                                      mazeHeight=self.boardManual.height, mazeX=self.boardManual.minX,
                                                      mazeY=self.boardManual.minY, labelCoodVal=self.labelBallCoodValManual,
                                                      speed=self.directionSpeedManual, accel=self.directionAccelManual)
        self.directionSpeedManual.marble = self.marbleManual
        self.directionAccelManual.marble = self.marbleManual
        self.imageProcessingMarble()
        self.switchPage(2)

    def arrangeDatabase(self):
        self.treeWidgetDatabase.clear()

        if self.comboBoxResult.currentText() == "Show All":
            result = [True,False]
        if self.comboBoxResult.currentText() == "Success":
            result = [True]
        if self.comboBoxResult.currentText() == "Failure":
            result = [False]

        if self.comboBoxType.currentText() == "Show All":
            _type = ["Easy","Medium","Hard","Custom"]
        if self.comboBoxType.currentText() == "Easy":
            _type = ["Easy"]
        if self.comboBoxType.currentText() == "Medium":
            _type = ["Medium"]
        if self.comboBoxType.currentText() == "Hard":
            _type = ["Hard"]
        if self.comboBoxType.currentText() == "Custom":
            _type = ["Custom"]

        if self.comboBoxAutoManual.currentText() == "Show All":
            auto = [True,False]
        if self.comboBoxAutoManual.currentText() == "Auto":
            auto = [True]
        if self.comboBoxAutoManual.currentText() == "Manual":
            auto = [False]

        if self.comboBoxTime.currentText() == "Most Recent First":
            sort = ["time",pymongo.DESCENDING]
        if self.comboBoxTime.currentText() == "Oldest First":
            sort = ["time",pymongo.ASCENDING]
        if self.comboBoxTime.currentText() == "Fastest Time First":
            sort = ["totalFrames",pymongo.ASCENDING]
        if self.comboBoxTime.currentText() == "Slowest Time First":
            sort = ["totalFrames",pymongo.DESCENDING]


        for i,solve in enumerate(solves.find({'success':{"$in": result},"type": {"$in": _type},"auto": {"$in": auto}}).sort(sort[0],sort[1])):
            itemList = QtWidgets.QTreeWidgetItem(self.treeWidgetDatabase)
            self.treeWidgetDatabase.topLevelItem(i).setText(0, self.prettyTime(solve.get("time")))
            self.treeWidgetDatabase.topLevelItem(i).setText(1, self.framesToTime(solve.get("totalFrames")))
            self.treeWidgetDatabase.topLevelItem(i).setText(2, str(solve.get("success")))
            autoString = "Auto" if solve.get("auto") else "Manual"
            self.treeWidgetDatabase.topLevelItem(i).setText(3, autoString)
            self.treeWidgetDatabase.topLevelItem(i).setText(4,solve.get("type"))
            self.treeWidgetDatabase.topLevelItem(i).setText(5,str(solve.get("_id")))

    def deleteBoardMarble(self, currentPage):
        if currentPage == "replay":
            self.switchPage(3)
            self.playback.deleteLater()
            self.marbleReplay.deleteLater()
            self.boardReplay.deleteLater()
        if currentPage == "auto":
            self.switchPage(0)
            self.marbleAuto.deleteLater()
            self.boardAuto.deleteLater()
        if currentPage == "manual":
            self.switchPage(0)
            self.marbleManual.deleteLater()
            self.boardManual.deleteLater()

    def switchPageDatabase(self):
        self.switchPage(3)
        self.playback.deleteLater()

    def refreshBoard(self):
        if self.stackedWidget.currentIndex() == 1:
            self.boardAuto.deleteLater()
            self.marbleAuto.deleteLater()
            # add new board
        if self.stackedWidget.currentIndex() == 2:
            self.boardManual.deleteLater()
            self.marbleManual.deleteLater()

    def framesToTime(self, frames):
        msecond= frames * 31.25
        second = msecond / 1000
        minute = second / 60

        msecondText = str(int(msecond % 1000))
        secondText = str(int(second % 60))
        minuteText = str(int(minute))
        if len(msecondText) == 3:
            msecondText = msecondText[:-1]
        if len(msecondText) == 1:
            msecondText = "0" + msecondText
        if len(secondText) == 1:
            secondText = "0" + secondText
        if len(minuteText) == 1:
            minuteText = "0" + minuteText

        return f"{minuteText}:{secondText}:{msecondText}"

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.initUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())