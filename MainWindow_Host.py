# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_Host.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindowHost(object):
    def setupUi(self, MainWindowHost):
        MainWindowHost.setObjectName("MainWindowHost")
        MainWindowHost.resize(480, 334)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowHost.sizePolicy().hasHeightForWidth())
        MainWindowHost.setSizePolicy(sizePolicy)
        MainWindowHost.setMinimumSize(QtCore.QSize(480, 320))
        MainWindowHost.setMaximumSize(QtCore.QSize(2000, 2000))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(83, 83, 83))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindowHost.setPalette(palette)
        MainWindowHost.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindowHost.setWindowOpacity(1.0)
        MainWindowHost.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindowHost)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopSelectionBar = QtWidgets.QHBoxLayout()
        self.TopSelectionBar.setObjectName("TopSelectionBar")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.TopSelectionBar.addItem(spacerItem)
        self.BT_openHomeScreen = QtWidgets.QPushButton(self.centralwidget)
        self.BT_openHomeScreen.setFlat(True)
        self.BT_openHomeScreen.setObjectName("BT_openHomeScreen")
        self.TopSelectionBar.addWidget(self.BT_openHomeScreen)
        self.BT_openSonosScreen = QtWidgets.QPushButton(self.centralwidget)
        self.BT_openSonosScreen.setFlat(True)
        self.BT_openSonosScreen.setObjectName("BT_openSonosScreen")
        self.TopSelectionBar.addWidget(self.BT_openSonosScreen)
        self.BT_openWeatherScreen = QtWidgets.QPushButton(self.centralwidget)
        self.BT_openWeatherScreen.setFlat(True)
        self.BT_openWeatherScreen.setObjectName("BT_openWeatherScreen")
        self.TopSelectionBar.addWidget(self.BT_openWeatherScreen)
        self.BT_openMeteoScreen = QtWidgets.QPushButton(self.centralwidget)
        self.BT_openMeteoScreen.setFlat(True)
        self.BT_openMeteoScreen.setObjectName("BT_openMeteoScreen")
        self.TopSelectionBar.addWidget(self.BT_openMeteoScreen)
        self.BT_openSbbScreen = QtWidgets.QPushButton(self.centralwidget)
        self.BT_openSbbScreen.setFlat(True)
        self.BT_openSbbScreen.setObjectName("BT_openSbbScreen")
        self.TopSelectionBar.addWidget(self.BT_openSbbScreen)
        self.BT_openLogScreen = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_openLogScreen.sizePolicy().hasHeightForWidth())
        self.BT_openLogScreen.setSizePolicy(sizePolicy)
        self.BT_openLogScreen.setMaximumSize(QtCore.QSize(40, 16777215))
        self.BT_openLogScreen.setFlat(True)
        self.BT_openLogScreen.setObjectName("BT_openLogScreen")
        self.TopSelectionBar.addWidget(self.BT_openLogScreen)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.TopSelectionBar.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.TopSelectionBar)
        self.LN_boarderLine = QtWidgets.QFrame(self.centralwidget)
        self.LN_boarderLine.setEnabled(False)
        self.LN_boarderLine.setMinimumSize(QtCore.QSize(480, 3))
        self.LN_boarderLine.setAutoFillBackground(False)
        self.LN_boarderLine.setStyleSheet("color: rgb(0, 85, 255)")
        self.LN_boarderLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.LN_boarderLine.setLineWidth(3)
        self.LN_boarderLine.setMidLineWidth(3)
        self.LN_boarderLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.LN_boarderLine.setObjectName("LN_boarderLine")
        self.verticalLayout.addWidget(self.LN_boarderLine)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.ST_workerStack = QtWidgets.QStackedWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.ST_workerStack.setPalette(palette)
        self.ST_workerStack.setObjectName("ST_workerStack")
        self.SC_welcomeScreen = QtWidgets.QWidget()
        self.SC_welcomeScreen.setObjectName("SC_welcomeScreen")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SC_welcomeScreen)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.WD_clock = QtWebEngineWidgets.QWebEngineView(self.SC_welcomeScreen)
        self.WD_clock.setObjectName("WD_clock")
        self.horizontalLayout_4.addWidget(self.WD_clock)
        self.ST_workerStack.addWidget(self.SC_welcomeScreen)
        self.SC_sonosScreen = QtWidgets.QWidget()
        self.SC_sonosScreen.setObjectName("SC_sonosScreen")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.SC_sonosScreen)
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.BT_sonosPlay = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_sonosPlay.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_sonosPlay.setIcon(icon)
        self.BT_sonosPlay.setFlat(True)
        self.BT_sonosPlay.setObjectName("BT_sonosPlay")
        self.horizontalLayout_8.addWidget(self.BT_sonosPlay)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.BT_previous = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_previous.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/rewind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_previous.setIcon(icon1)
        self.BT_previous.setFlat(True)
        self.BT_previous.setObjectName("BT_previous")
        self.horizontalLayout_7.addWidget(self.BT_previous)
        self.BT_pause = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_pause.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_pause.setIcon(icon2)
        self.BT_pause.setFlat(True)
        self.BT_pause.setObjectName("BT_pause")
        self.horizontalLayout_7.addWidget(self.BT_pause)
        self.BT_skip = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_skip.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/skip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_skip.setIcon(icon3)
        self.BT_skip.setFlat(True)
        self.BT_skip.setObjectName("BT_skip")
        self.horizontalLayout_7.addWidget(self.BT_skip)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.BT_stop = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_stop.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_stop.setIcon(icon4)
        self.BT_stop.setFlat(True)
        self.BT_stop.setObjectName("BT_stop")
        self.horizontalLayout_6.addWidget(self.BT_stop)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.BT_select = QtWidgets.QPushButton(self.SC_sonosScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_select.sizePolicy().hasHeightForWidth())
        self.BT_select.setSizePolicy(sizePolicy)
        self.BT_select.setMaximumSize(QtCore.QSize(50, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_select.setIcon(icon5)
        self.BT_select.setFlat(True)
        self.BT_select.setObjectName("BT_select")
        self.verticalLayout_8.addWidget(self.BT_select)
        self.gridLayout_4.addLayout(self.verticalLayout_8, 0, 1, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.BT_volumeDown = QtWidgets.QToolButton(self.SC_sonosScreen)
        self.BT_volumeDown.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/reduceVolume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_volumeDown.setIcon(icon6)
        self.BT_volumeDown.setObjectName("BT_volumeDown")
        self.horizontalLayout_9.addWidget(self.BT_volumeDown)
        self.SL_volume = QtWidgets.QSlider(self.SC_sonosScreen)
        self.SL_volume.setOrientation(QtCore.Qt.Horizontal)
        self.SL_volume.setObjectName("SL_volume")
        self.horizontalLayout_9.addWidget(self.SL_volume)
        self.BT_volumeUp = QtWidgets.QToolButton(self.SC_sonosScreen)
        self.BT_volumeUp.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/increaseVolume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_volumeUp.setIcon(icon7)
        self.BT_volumeUp.setObjectName("BT_volumeUp")
        self.horizontalLayout_9.addWidget(self.BT_volumeUp)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.LB_currentlyPlayingTitle = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlayingTitle.setObjectName("LB_currentlyPlayingTitle")
        self.verticalLayout_7.addWidget(self.LB_currentlyPlayingTitle)
        self.LB_currentlyPlayingPosition = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlayingPosition.setObjectName("LB_currentlyPlayingPosition")
        self.verticalLayout_7.addWidget(self.LB_currentlyPlayingPosition)
        self.LB_currentlyPlayingArtist = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlayingArtist.setObjectName("LB_currentlyPlayingArtist")
        self.verticalLayout_7.addWidget(self.LB_currentlyPlayingArtist)
        self.LB_currentlyPlayingTotal = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlayingTotal.setObjectName("LB_currentlyPlayingTotal")
        self.verticalLayout_7.addWidget(self.LB_currentlyPlayingTotal)
        self.LB_currentlyPlayingCurrentTime = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlayingCurrentTime.setObjectName("LB_currentlyPlayingCurrentTime")
        self.verticalLayout_7.addWidget(self.LB_currentlyPlayingCurrentTime)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.BT_musicMode = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_musicMode.setText("")
        self.BT_musicMode.setIcon(icon5)
        self.BT_musicMode.setFlat(True)
        self.BT_musicMode.setObjectName("BT_musicMode")
        self.horizontalLayout_12.addWidget(self.BT_musicMode)
        self.BT_radioMode = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_radioMode.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/radio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_radioMode.setIcon(icon8)
        self.BT_radioMode.setFlat(True)
        self.BT_radioMode.setObjectName("BT_radioMode")
        self.horizontalLayout_12.addWidget(self.BT_radioMode)
        self.BT_tvMode = QtWidgets.QPushButton(self.SC_sonosScreen)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(60, 186, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 186, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 186, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 186, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 186, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(60, 186, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.BT_tvMode.setPalette(palette)
        self.BT_tvMode.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/tv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_tvMode.setIcon(icon9)
        self.BT_tvMode.setFlat(True)
        self.BT_tvMode.setObjectName("BT_tvMode")
        self.horizontalLayout_12.addWidget(self.BT_tvMode)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.LW_artists = QtWidgets.QListWidget(self.SC_sonosScreen)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.LW_artists.setPalette(palette)
        self.LW_artists.setObjectName("LW_artists")
        self.verticalLayout_9.addWidget(self.LW_artists)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.BT_listArtists = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_listArtists.setFlat(True)
        self.BT_listArtists.setObjectName("BT_listArtists")
        self.horizontalLayout_5.addWidget(self.BT_listArtists)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11.addLayout(self.verticalLayout_9)
        self.horizontalLayout_41.addLayout(self.horizontalLayout_11)
        self.ST_workerStack.addWidget(self.SC_sonosScreen)
        self.SC_weatherScreen = QtWidgets.QWidget()
        self.SC_weatherScreen.setObjectName("SC_weatherScreen")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.SC_weatherScreen)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.LB_weatherScreen = QtWidgets.QLabel(self.SC_weatherScreen)
        self.LB_weatherScreen.setObjectName("LB_weatherScreen")
        self.horizontalLayout.addWidget(self.LB_weatherScreen)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LB_oldFreezer = QtWidgets.QLabel(self.SC_weatherScreen)
        self.LB_oldFreezer.setObjectName("LB_oldFreezer")
        self.gridLayout.addWidget(self.LB_oldFreezer, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.LB_newFreezer = QtWidgets.QLabel(self.SC_weatherScreen)
        self.LB_newFreezer.setObjectName("LB_newFreezer")
        self.gridLayout.addWidget(self.LB_newFreezer, 2, 1, 1, 1)
        self.LB_internalTemp = QtWidgets.QLabel(self.SC_weatherScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_internalTemp.sizePolicy().hasHeightForWidth())
        self.LB_internalTemp.setSizePolicy(sizePolicy)
        self.LB_internalTemp.setObjectName("LB_internalTemp")
        self.gridLayout.addWidget(self.LB_internalTemp, 0, 1, 1, 1)
        self.LCD_newFreezer = QtWidgets.QLCDNumber(self.SC_weatherScreen)
        self.LCD_newFreezer.setProperty("value", -16.2)
        self.LCD_newFreezer.setObjectName("LCD_newFreezer")
        self.gridLayout.addWidget(self.LCD_newFreezer, 2, 2, 1, 1)
        self.LCD_piTemp = QtWidgets.QLCDNumber(self.SC_weatherScreen)
        self.LCD_piTemp.setSmallDecimalPoint(True)
        self.LCD_piTemp.setProperty("intValue", 40)
        self.LCD_piTemp.setObjectName("LCD_piTemp")
        self.gridLayout.addWidget(self.LCD_piTemp, 0, 2, 1, 1)
        self.LCD_oldFreezer = QtWidgets.QLCDNumber(self.SC_weatherScreen)
        self.LCD_oldFreezer.setProperty("value", -15.5)
        self.LCD_oldFreezer.setObjectName("LCD_oldFreezer")
        self.gridLayout.addWidget(self.LCD_oldFreezer, 1, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.ST_workerStack.addWidget(self.SC_weatherScreen)
        self.SC_log = QtWidgets.QWidget()
        self.SC_log.setObjectName("SC_log")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.SC_log)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.TE_Debug = QtWidgets.QTextEdit(self.SC_log)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.TE_Debug.setPalette(palette)
        self.TE_Debug.setObjectName("TE_Debug")
        self.horizontalLayout_31.addWidget(self.TE_Debug)
        self.ST_workerStack.addWidget(self.SC_log)
        self.SC_meteo = QtWidgets.QWidget()
        self.SC_meteo.setObjectName("SC_meteo")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.SC_meteo)
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.WD_browser = QtWebEngineWidgets.QWebEngineView(self.SC_meteo)
        self.WD_browser.setObjectName("WD_browser")
        self.horizontalLayout_32.addWidget(self.WD_browser)
        self.ST_workerStack.addWidget(self.SC_meteo)
        self.SC_sbb = QtWidgets.QWidget()
        self.SC_sbb.setObjectName("SC_sbb")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.SC_sbb)
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BT_hb = QtWidgets.QPushButton(self.SC_sbb)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BT_hb.setFont(font)
        self.BT_hb.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 240px; color: #FFFFFF")
        self.BT_hb.setFlat(True)
        self.BT_hb.setObjectName("BT_hb")
        self.gridLayout_2.addWidget(self.BT_hb, 0, 0, 1, 1)
        self.BT_wankdorf = QtWidgets.QPushButton(self.SC_sbb)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BT_wankdorf.setFont(font)
        self.BT_wankdorf.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 240px; color: #FFFFFF")
        self.BT_wankdorf.setFlat(True)
        self.BT_wankdorf.setObjectName("BT_wankdorf")
        self.gridLayout_2.addWidget(self.BT_wankdorf, 0, 1, 1, 1)
        self.BT_breitsch = QtWidgets.QPushButton(self.SC_sbb)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.BT_breitsch.setFont(font)
        self.BT_breitsch.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 240px; color: #FFFFFF")
        self.BT_breitsch.setFlat(True)
        self.BT_breitsch.setObjectName("BT_breitsch")
        self.gridLayout_2.addWidget(self.BT_breitsch, 0, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_33.addLayout(self.horizontalLayout_2)
        self.ST_workerStack.addWidget(self.SC_sbb)
        self.SC_hb = QtWidgets.QWidget()
        self.SC_hb.setObjectName("SC_hb")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.SC_hb)
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.WD_hb = QtWebEngineWidgets.QWebEngineView(self.SC_hb)
        self.WD_hb.setObjectName("WD_hb")
        self.horizontalLayout_34.addWidget(self.WD_hb)
        self.ST_workerStack.addWidget(self.SC_hb)
        self.SC_wankdorf = QtWidgets.QWidget()
        self.SC_wankdorf.setObjectName("SC_wankdorf")
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.SC_wankdorf)
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_35.setObjectName("horizontalLayout_35")
        self.WD_wankdorf = QtWebEngineWidgets.QWebEngineView(self.SC_wankdorf)
        self.WD_wankdorf.setObjectName("WD_wankdorf")
        self.horizontalLayout_35.addWidget(self.WD_wankdorf)
        self.ST_workerStack.addWidget(self.SC_wankdorf)
        self.SC_breitsch = QtWidgets.QWidget()
        self.SC_breitsch.setObjectName("SC_breitsch")
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.SC_breitsch)
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.WD_breitsch = QtWebEngineWidgets.QWebEngineView(self.SC_breitsch)
        self.WD_breitsch.setObjectName("WD_breitsch")
        self.horizontalLayout_36.addWidget(self.WD_breitsch)
        self.ST_workerStack.addWidget(self.SC_breitsch)
        self.verticalLayout_3.addWidget(self.ST_workerStack)
        MainWindowHost.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowHost)
        self.ST_workerStack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindowHost)

    def retranslateUi(self, MainWindowHost):
        _translate = QtCore.QCoreApplication.translate
        MainWindowHost.setWindowTitle(_translate("MainWindowHost", "SonosController"))
        self.BT_openHomeScreen.setText(_translate("MainWindowHost", "HOME"))
        self.BT_openSonosScreen.setText(_translate("MainWindowHost", "SONOS"))
        self.BT_openWeatherScreen.setText(_translate("MainWindowHost", "WETTER"))
        self.BT_openMeteoScreen.setText(_translate("MainWindowHost", "METEO"))
        self.BT_openSbbScreen.setText(_translate("MainWindowHost", "SBB"))
        self.BT_openLogScreen.setText(_translate("MainWindowHost", "LOG"))
        self.BT_select.setText(_translate("MainWindowHost", "wählen"))
        self.LB_currentlyPlayingTitle.setText(_translate("MainWindowHost", "currently playing..."))
        self.LB_currentlyPlayingPosition.setText(_translate("MainWindowHost", "currently playing..."))
        self.LB_currentlyPlayingArtist.setText(_translate("MainWindowHost", "currently playing..."))
        self.LB_currentlyPlayingTotal.setText(_translate("MainWindowHost", "currently playing..."))
        self.LB_currentlyPlayingCurrentTime.setText(_translate("MainWindowHost", "currently playing..."))
        self.BT_listArtists.setText(_translate("MainWindowHost", "back"))
        self.LB_weatherScreen.setText(_translate("MainWindowHost", "This is the weather screen"))
        self.LB_oldFreezer.setText(_translate("MainWindowHost", "Temp alter Gefrierschrank"))
        self.LB_newFreezer.setText(_translate("MainWindowHost", "Temp neuer Gefrierschrank"))
        self.LB_internalTemp.setText(_translate("MainWindowHost", "internal Temp"))
        self.BT_hb.setText(_translate("MainWindowHost", "Bahnhof"))
        self.BT_wankdorf.setText(_translate("MainWindowHost", "Wankdorf"))
        self.BT_breitsch.setText(_translate("MainWindowHost", "Breitsch"))

from PyQt5 import QtWebEngineWidgets
import musicIcons_rc
