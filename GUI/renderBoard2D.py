from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets, QtGui

class RenderBoard2D(QWidget):
    def __init__(self, parent=None, minimumWidth=1280, minimumHeight=720, holes = [], walls = [], path = [], difficulty=None):
        super(RenderBoard2D, self).__init__(parent)
        self.setMinimumSize(minimumWidth, minimumHeight)
        self.holes = holes
        self.walls = walls
        self.path = path
        self.difficulty = difficulty

        minX = 720
        minY = 1280
        maxX = 0
        maxY = 0

        for i in range(len(self.walls)):
            for j in range(len(self.walls[i])):
                if self.walls[i][j][0] < minX:
                    minX = self.walls[i][j][0]
                if self.walls[i][j][0] > maxX:
                    maxX = self.walls[i][j][0]
                if self.walls[i][j][1] < minY:
                    minY = self.walls[i][j][1]
                if self.walls[i][j][1] > maxY:
                    maxY = self.walls[i][j][1]

        self.height = maxX - minX
        self.width = maxY - minY
        aspectRatio = self.width/self.height

        desiredAspectRatio = 868/720

        while not aspectRatio > (desiredAspectRatio - 0.005) or not aspectRatio < (desiredAspectRatio + 0.005):
            minY -= 1
            maxY += 1
            self.height = maxX - minX
            self.width = maxY - minY

            aspectRatio = self.width/self.height


        self.maxY = self.height - minX  # rotate board
        self.minX = minY
        self.minY = self.height - maxX
        self.maxX = maxY

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 0, 1280, 720)
        self.label.setAlignment(Qt.AlignCenter)

        if self.difficulty == "Custom":
            self.canvas = QtGui.QPixmap(self.width,self.height)
            self.canvas.fill(Qt.white)
        else:
            self.canvas = QtGui.QPixmap(868,720)
            self.canvas.fill(Qt.white)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(0, 0, 1280, 720)
        self.label2.setAlignment(Qt.AlignCenter)

    def paintEvent(self, event):

        if self.difficulty == "Custom":
            self.drawCustom()

        if self.difficulty == "Easy":
            self.drawEasy()

        if self.difficulty == "Medium":
            self.drawMedium()

        if self.difficulty == "Hard":
            self.drawHard()

    def drawCustom(self):
        self.drawCustomHoles()
        self.drawCustomWalls()
        self.drawCustomPath()

        self.drawCustomStartEnd()

        painter = QPainter(self.canvas)
        painter.setPen(QPen(Qt.black))
        painter.drawRect(0, 0, self.width - 1, self.height - 1)
        painter.end()

        self.canvas2 = self.canvas.scaled(868, 720)
        self.label.setPixmap(self.canvas2)

    def drawCustomHoles(self):
        painter = QPainter(self.canvas)
        painter.setBrush(Qt.black)
        for i in range(len(self.holes)): # has to turn 90 degrees anticlockwise (1200 x 1000)
            centerX = self.translateXCood(self.holes[i][1]) # new x = old y
            centerY = self.translateYCood(self.holes[i][0]) # new y = height - x
            radius = self.holes[i][2]
            painter.drawEllipse(QPoint(centerX,centerY),radius,radius)

        painter.end()

    def drawCustomWalls(self):
        painter = QPainter(self.canvas)
        painter.setPen(QPen(Qt.black, 1))
        color = QBrush(QColor("grey"))

        for i in range(len(self.walls)):
            self.path2 = QPainterPath()
            self.path2.moveTo(self.translateXCood(self.walls[i][0][1]),self.translateYCood(self.walls[i][0][0]))

            for j in range(len(self.walls[i])):
                if j == len(self.walls[i]) - 1:
                    self.path2.lineTo(self.translateXCood(self.walls[i][0][1]),self.translateYCood(self.walls[i][0][0]))
                else:
                    self.path2.lineTo(self.translateXCood(self.walls[i][j+1][1]),self.translateYCood(self.walls[i][j+1][0]))

            painter.fillPath(self.path2, color)
            painter.drawPath(self.path2)

        painter.end()

    def drawCustomPath(self):
        painter = QPainter(self.canvas)
        painter.setPen(QPen(Qt.darkBlue,2))

        for i in range(len(self.path) - 1):
            xPos1 = self.translateXCood(self.path[i][1]) # new x = old y
            yPos1 = self.translateYCood(self.path[i][0]) # new y = 1000 - x

            xPos2 = self.translateXCood(self.path[i+1][1]) # new x = old y
            yPos2 = self.translateYCood(self.path[i+1][0]) # new y = 1000 - x

            painter.drawLine(xPos1, yPos1, xPos2, yPos2)

        painter.end()

    def drawCustomStartEnd(self):
        xPos2 = self.translateXCood(self.path[0][1])  # new x = old y (also the first element in path is the end)
        yPos2 = self.translateYCood(self.path[0][0])  # new y = 1000 - x

        xPos1 = self.translateXCood(self.path[-1][1])  # new x = old y  (also the last element in path is the start)
        yPos1 = self.translateYCood(self.path[-1][0])  # new y = 1000 - x

        painter = QPainter(self.canvas)
        painter.setPen(Qt.darkGreen)
        painter.drawEllipse(QPoint(xPos1, yPos1), 5, 5)
        painter.setPen(Qt.darkRed)
        painter.drawEllipse(QPoint(xPos2, yPos2), 5, 5)
        painter.end()

        scaleRatio = 720/self.height
        xPos1 = xPos1*scaleRatio
        yPos1 = yPos1 * scaleRatio
        xPos2 = xPos2*scaleRatio
        yPos2 = yPos2 * scaleRatio

        canvas3 = QtGui.QPixmap(self.width,self.height)
        canvas3.fill(Qt.transparent)
        canvas4 = canvas3.scaledToHeight(720)
        painter = QPainter(canvas4)

        font = QFont("Times", 20)
        painter.setFont(font)

        painter.setPen(Qt.darkGreen)
        painter.setBrush(Qt.transparent)
        startText = QRect(QPoint(xPos1-40,yPos1-40),QPoint(xPos1+40,yPos1))
        painter.drawText(startText,Qt.AlignHCenter,"Start")

        painter.setPen(Qt.darkRed)
        endText = QRect(QPoint(xPos2-40,yPos2-40),QPoint(xPos2+40,yPos2))
        painter.drawText(endText, Qt.AlignHCenter, "End")
        painter.end()

        self.label2.setPixmap(canvas4)

    def translateXCood(self,y):
        return y - self.minX

    def translateYCood(self,x):
        return self.height - x - self.minY

    def drawHard(self):
        painter = QPainter(self.canvas)
        painter.setPen(QPen(Qt.black))
        painter.drawRect(0, 0, 867, 719)

        painter.setBrush(Qt.black)

        wallCood = [[[206,0],[225,50]],[[0,70],[84,85]],[[136,70],[152,112]],[[48,140],[83,154]],[[207,117],[224,161]],[[135,165],[151,292]],[[51,278],[151,292]],[[0,212],[83,226]],
                    [[206,212],[224,265]],[[66,333],[83,400]],[[206,335],[224,419]],[[136,334],[153,400]],[[51,453],[153,468]],[[134,454],[154,633]],[[0,579],[51,593]],[[207,544],[223,600]],
                    [[207,654],[223,720]],[[279,70],[296,161]],[[279,70],[496,86]],[[496,1],[514,350]],[[514,131],[566,149]],[[511,222],[653,239]],[[351,132],[367,239]],[[279,223],[366,239]],
                    [[279,223],[296,280]],[[279,336],[295,420]],[[279,524],[295,636]],[[279,524],[362,539]],[[352,303],[367,472]],[[352,458],[436,472]],[[350,592],[366,638]],
                    [[420,535],[435,638]],[[422,353],[437,404]],[[422,132],[439,190]],[[423,240],[439,302]],[[494,397],[511,521]],[[491,629],[578,647]],[[567,430],[580,483]],
                    [[567,481],[651,498]],[[635,484],[651,647]],[[635,293],[651,425]],[[564,372],[640,388]],[[642,112],[655,170]],[[642,112],[732,127]],[[717,112],[732,335]],
                    [[719,0],[737,39]],[[796,49],[867,65]],[[792,118],[808,196]],[[787,252],[804,396]],[[787,397],[867,412]],[[710,396],[726,553]],[[708,602],[724,651]],[[779,668],[798,720]]]


        for i in range(len(wallCood)):
            x1 = wallCood[i][0][0]
            y1 = wallCood[i][0][1]
            x2 = wallCood[i][1][0]
            y2 = wallCood[i][1][1]
            painter.drawRect(QRect(QPoint(x1,y1),QPoint(x2,y2)))

        holeCood = [[40,43],[113,140],[181,141],[253,139],[252,221],[180,314],[327,268],[40,375],[181,435],[253,378],[252,489],[322,491],[181,588],[40,549],[108,623],[250,665],[392,613],
                    [465,368],[464,532],[539,494],[539,596],[539,673],[541,271],[540,186],[541,39],[468,117],[395,257],[688,37],[763,38],[685,159],[682,305],[608,342],[679,537],
                    [751,679],[754,540],[828,590],[831,446],[758,272],[838,94]]

        for i in range(len(holeCood)):
            centerX = holeCood[i][0]
            centerY = holeCood[i][1]
            painter.drawEllipse(QPoint(centerX, centerY), 23, 23)

        startCood = [448,38]
        painter.setBrush(Qt.darkGreen)
        painter.drawEllipse(QPoint(startCood[0], startCood[1]), 5, 5)
        font = QFont("Times", 16)
        painter.setFont(font)
        startCoodText = QRect(QPoint(startCood[0] - 25, startCood[1] - 30),
                              QPoint(startCood[0] + 25, startCood[1] + 10))
        painter.drawText(startCoodText, Qt.AlignHCenter, "Start")

        endCood = [823,321]
        painter.setBrush(Qt.darkRed)
        painter.drawEllipse(QPoint(endCood[0], endCood[1]), 5, 5)
        endCoodText = QRect(QPoint(endCood[0] - 0, endCood[1] + 10), QPoint(endCood[0] + 35, endCood[1] + 30))
        painter.drawText(endCoodText, Qt.AlignHCenter, "End")

        pathCood = [[448,38],[252,38],[252,82],[180,82],[180,38],[111,38],[111,97],[35,97],[35,187],[106,187],[106,249],[35,249],[35,312],[106,312],[106,423],[35,423],[35,491],[95,555],
                    [61,621],[61,664],[156,664],[254,579],[254,524],[198,524],[198,481],[233,446],[322,446],[322,318],[258,318],[180,267],[180,184],[326,184],[326,116],[396,116],[396,212],
                    [465,213],[465,323],[395,323],[395,436],[462,436],[462,494],[394,494],[394,553],[321,553],[321,672],[460,672],[460,592],[525,548],[603,548],[603,680],[673,680],
                    [673,585],[764,585],[815,539],[815,487],[753,487],[753,367],[680,367],[680,459],[605,459],[605,419],[536,419],[536,338],[616,267],[680,267],[680,207],[611,207],
                    [611,86],[768,86],[768,221],[823,221],[823,321]]
        path = QPainterPath()
        painter.setPen(QPen(Qt.black, 3))

        ################################################################################################################

        path.moveTo(448,38)

        for i in range(len(pathCood)):
            path.lineTo(pathCood[i][0],pathCood[i][1])

        painter.setBrush(Qt.transparent)
        painter.drawPath(path)





        self.label.setPixmap(self.canvas)

    def drawMedium(self):
        painter = QPainter(self.canvas)
        painter.setPen(QPen(Qt.black))
        painter.drawRect(0, 0, 867, 719)

        painter.setBrush(Qt.black)

        wallCood = [[[130,0],[150,105]],[[0,87],[150,105]],[[0,247],[178,266]],[[100,154],[120,247]],[[0,331],[178,349]],[[120,429],[137,520]],[[70,460],[120,476]],[[0, 600],[126,618]],
                    [[126,573],[146,720]],[[205,47],[550,63]],[[205,47],[220,162]],[[205,162],[248,177]],[[550,0],[566,118]],[[568,30],[867,45]],[[347,137],[364,257]],[[365,173],
                    [508,190]],[[490,173],[508,470]],[[508,438],[553,457]],[[245,249],[263,404]],[[263,324],[311,340]],[[197,404],[401,421]],[[197,407],[214,484]],[[382,407],[401,549]],
                    [[197,569],[274,587]],[[274,498],[292,720]],[[292,609],[639,628]],[[570,516],[587,614]],[[568,191],[651,206]],[[568,191],[583,236]],[[635,164],[651,206]],[[704,96],[785,111]],
                    [[704,96],[720,141]],[[764,218],[867,233]],[[664,314],[867,332]],[[664,314],[680,426]],[[584,357],[664,373]],[[664,425],[757,444]],[[757,425],[777,507]],
                    [[710,554],[725,720]],[[422,262],[439,353]]]

        for i in range(len(wallCood)):
            x1 = wallCood[i][0][0]
            y1 = wallCood[i][0][1]
            x2 = wallCood[i][1][0]
            y2 = wallCood[i][1][1]
            painter.drawRect(QRect(QPoint(x1,y1),QPoint(x2,y2)))

        holeCood = [[104,130],[248,210],[177,301],[172,438],[97,503],[177,594],[320,493],[463,362],[394,246],[250,131],[469,109],[681,158],[755,260],[540,260],[537,492],[754,535]]

        for i in range(len(holeCood)):
            centerX = holeCood[i][0]
            centerY = holeCood[i][1]
            painter.drawEllipse(QPoint(centerX,centerY),23,23)

        startCood = [506,29]
        painter.setBrush(Qt.darkGreen)
        painter.drawEllipse(QPoint(startCood[0],startCood[1]),5,5)
        font = QFont("Times", 16)
        painter.setFont(font)
        startCoodText = QRect(QPoint(startCood[0]-25,startCood[1]-30),QPoint(startCood[0]+25,startCood[1]+10))
        painter.drawText(startCoodText,Qt.AlignHCenter,"Start")

        endCood = [353,671]
        painter.setBrush(Qt.darkRed)
        painter.drawEllipse(QPoint(endCood[0], endCood[1]), 5, 5)
        endCoodText = QRect(QPoint(endCood[0] - 25, endCood[1] - 30),QPoint(endCood[0] + 25, endCood[1] + 10))
        painter.drawText(endCoodText, Qt.AlignHCenter, "End")

        pathCood = [[506,29],[180,29],[180,190],[193,226],[222,263],[222,343],[77,410],[39,468],[39,548],[188,532],[250,532],[250,452],[364,452],[364,580],[442,580],[442,425],[370,325],
                    [305,266],[305,102],[400,102],[400,151],[588,152],[621,124],[666,84],[825,83],[825,164],[768,164],[690,245],[546,332],[546,411],[610,411],[610,470],[647,521],
                    [675,568],[675,671],[353,671]]
        path = QPainterPath()
        painter.setPen(QPen(Qt.black,3))



        ################################################################################################################

        painter.drawLine(QPoint(506,29),QPoint(180,29))
        painter.drawLine(QPoint(180,29), QPoint(180,190))
        path.moveTo(180,190)
        path.cubicTo(180,190,178,221,193,226)
        path.cubicTo(193,226, 215,227, 222,263)
        painter.drawLine(QPoint(222,263), QPoint(222,343))
        path.moveTo(222,343)
        path.cubicTo(222,343, 215,386, 77,410)
        path.moveTo(77,410)
        path.cubicTo(77,410, 47,415, 39,468)
        painter.drawLine(QPoint(39,468), QPoint(39,548))
        path.moveTo(39,548)
        path.cubicTo(39,548, 20,630, 188,532)
        painter.drawLine(QPoint(188,532), QPoint(250,532))
        painter.drawLine(QPoint(250,532), QPoint(250,452))
        painter.drawLine(QPoint(250,452), QPoint(364,452))
        painter.drawLine(QPoint(364,452), QPoint(364,580))
        painter.drawLine(QPoint(364,580), QPoint(442,580))
        painter.drawLine(QPoint(442,580), QPoint(442,425))
        painter.drawLine(QPoint(442,425), QPoint(370,325))
        path.moveTo(370,325)
        path.cubicTo(370,325, 313,315, 305,266)
        painter.drawLine(QPoint(305,266), QPoint(305,102))
        painter.drawLine(QPoint(305,102), QPoint(400,102))
        painter.drawLine(QPoint(400,102), QPoint(400,151))
        painter.drawLine(QPoint(400, 151), QPoint(588,152))
        path.moveTo(588,152)
        path.cubicTo(588,152, 617,149, 621,124)
        path.moveTo(621,124)
        path.cubicTo(621,124, 627,94, 666,84)
        painter.drawLine(QPoint(666,84), QPoint(825,83))
        painter.drawLine(QPoint(825,83), QPoint(825, 164))
        painter.drawLine(QPoint(825, 164), QPoint(768,164))
        path.moveTo(768,164)
        path.cubicTo(768,164, 720,158, 690,245)
        path.moveTo(690,245)
        path.cubicTo(690,245, 544,306, 546,332)
        painter.drawLine(QPoint(546,332), QPoint(546,411))
        painter.drawLine(QPoint(546,411), QPoint(610,411))
        painter.drawLine(QPoint(610,411), QPoint(610,470))
        path.moveTo(610,470)
        path.cubicTo(610,470, 612,500, 647,521)
        path.moveTo(647,521)
        path.cubicTo(647,521, 670,530, 675,568)
        painter.drawLine(QPoint(675,568), QPoint(675,671))
        painter.drawLine(QPoint(675,671), QPoint(353, 671))

        painter.setBrush(Qt.transparent)
        painter.drawPath(path)

        ################################################################################################################


        self.label.setPixmap(self.canvas)

    def drawEasy(self):
        painter = QPainter(self.canvas)
        painter.setPen(QPen(Qt.black))
        painter.drawRect(0, 0, 867, 719)

        painter.setBrush(Qt.black)

        wallCood = [[[113,47],[132,92]],[[113,47],[500,64]],[[482,0],[500,139]],[[500,120],[547,139]],[[56,147],[76,220]],[[75,163],[364,181]],[[345,163],[365,491]],[[366,219],[535,235]],
                    [[156,473],[491,491]],[[311,491],[329,571]],[[139,450],[155,574]],[[83,557],[155,574]],[[0,440],[52,456]],[[225,571],[243,720]],[[243,643],[593,660]],[[425,592],[443,643]],
                    [[572,296],[593,660]],[[594,486],[783,504]],[[574,296],[725,314]],[[704,119],[726,573]],[[511,359],[571,376]],[[668,119],[765,139]],[[668,55],[687,139]],[[616,55],[687,74]],
                    [[665,620],[685,720]],[[796,370],[867,388]],[[813,166],[867,182]],[[0,347],[277,363]],[[101,297],[122,347]],[[214,296],[232,346]],[[0,440],[53,456]],[[728,216],[773,233]]]

        for i in range(len(wallCood)):
            x1 = wallCood[i][0][0]
            y1 = wallCood[i][0][1]
            x2 = wallCood[i][1][0]
            y2 = wallCood[i][1][1]
            painter.drawRect(QRect(QPoint(x1,y1),QPoint(x2,y2)))

        holeCood = [[101,137],[174,315],[100,513],[545,606],[471,367],[543,180],[760,265],[762,540]]

        for i in range(len(holeCood)):
            centerX = holeCood[i][0]
            centerY = holeCood[i][1]
            painter.drawEllipse(QPoint(centerX,centerY),23,23)

        startCood = [388, 23]
        painter.setBrush(Qt.darkGreen)
        painter.drawEllipse(QPoint(startCood[0], startCood[1]), 5, 5)
        font = QFont("Times", 16)
        painter.setFont(font)
        startCoodText = QRect(QPoint(startCood[0] + 15, startCood[1] - 15),
                              QPoint(startCood[0] + 65, startCood[1] + 15))
        painter.drawText(startCoodText, Qt.AlignHCenter, "Start")

        endCood = [333, 692]
        painter.setBrush(Qt.darkRed)
        painter.drawEllipse(QPoint(endCood[0], endCood[1]), 5, 5)
        endCoodText = QRect(QPoint(endCood[0] - 25, endCood[1] - 30), QPoint(endCood[0] + 25, endCood[1] + 10))
        painter.drawText(endCoodText, Qt.AlignHCenter, "End")

        pathCood = [[388, 23],[128,23],[37,122],[37,223],[81,270],[146,243],[320,341],[163,409],[99,434],[38,553],[41,629],[194,629],[194,532],[281,532],[281,603],[377,603],
                    [377,534],[538,534],[538,430],[446,430],[407,372],[425,325],[609,233],[630,177],[581,98],[565,65],[594,29],[702,29],[789,99],[793,122],[823,233],[822,296],
                    [770,348],[771,417],[823,451],[839,477],[839,549],[800,614],[686,585],[729,627],[656,588],[637,665],[604,692],[333, 692]]

        path = QPainterPath()
        painter.setPen(QPen(Qt.black, 3))

        ################################################################################################################

        painter.drawLine(QPoint(388, 23), QPoint(128,23))
        path.moveTo(128,23)
        path.cubicTo(128,23, 58,47, 37,122)
        painter.drawLine(QPoint(37,122), QPoint(37,223))
        path.moveTo(37,223)
        path.cubicTo(37,223, 46,273, 81,270)
        path.cubicTo(81,270, 125,271, 146,243)
        path.cubicTo(146,243, 265,185, 320,341)
        path.cubicTo(320,341, 349,460, 163,409)
        path.cubicTo(163,409, 135,380, 99,434)
        painter.drawLine(QPoint(99,434), QPoint(38,553))
        painter.drawLine(QPoint(38,553), QPoint(38,629))
        painter.drawLine(QPoint(38,629), QPoint(194,629))
        painter.drawLine(QPoint(194,629), QPoint(194,532))
        painter.drawLine(QPoint(194,532), QPoint(281,532))
        painter.drawLine(QPoint(281,532), QPoint(281,603))
        painter.drawLine(QPoint(281,603), QPoint(377,603))
        painter.drawLine(QPoint(377,603), QPoint(377,534))
        painter.drawLine(QPoint(377,534), QPoint(538,534))
        painter.drawLine(QPoint(538,534), QPoint(538,430))
        painter.drawLine(QPoint(538,430), QPoint(446,430))
        path.moveTo(446,430)
        path.cubicTo(446,430, 403,415, 407,372)
        path.cubicTo(407,372, 400,340, 425,325)
        painter.drawLine(QPoint(425,325), QPoint(609,233))
        path.moveTo(609,233)
        path.cubicTo(609,233, 634,224, 630,177)
        path.cubicTo(630,177, 624,115, 581,98)
        path.cubicTo(581,98, 559,87, 565,65)
        path.cubicTo(565,65, 565,33, 594,29)
        painter.drawLine(QPoint(594,29), QPoint(702,29))
        path.moveTo(702,29)
        path.cubicTo(702,29, 732,85, 789,99)
        path.cubicTo(789,99, 813,104, 793,122)
        path.cubicTo(793,122, 777,187, 823,233)
        path.cubicTo(823,233, 851,258, 822,296)
        painter.drawLine(QPoint(822,296), QPoint(770,348))
        path.moveTo(770,348)
        path.cubicTo(770,348, 740,383, 771,417)
        painter.drawLine(QPoint(771,417), QPoint(823,451))
        path.moveTo(823,451)
        path.cubicTo(823,451, 838,458, 839,477)
        painter.drawLine(QPoint(839,477), QPoint(839,549))
        path.moveTo(839,549)
        path.cubicTo(839,549, 832,617, 800,614)
        path.cubicTo(800,614, 729,627, 686,585)
        path.cubicTo(686,585, 664,563, 656,588)
        painter.drawLine(QPoint(656,588), QPoint(637,665))
        path.moveTo(637,665)
        path.cubicTo(637,665, 635,690, 604,692)
        painter.drawLine(QPoint(604,692), QPoint(333, 692))


        ################################################################################################################

        painter.setBrush(Qt.transparent)
        painter.drawPath(path)


        self.label.setPixmap(self.canvas)







