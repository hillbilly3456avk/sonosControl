# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_raspi.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        MainWindow.setMinimumSize(QtCore.QSize(480, 320))
        MainWindow.setMaximumSize(QtCore.QSize(480, 320))
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
        MainWindow.setPalette(palette)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 496, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopSelectionBar = QtWidgets.QHBoxLayout()
        self.TopSelectionBar.setObjectName("TopSelectionBar")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.TopSelectionBar.addItem(spacerItem)
        self.BT_openHomeScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BT_openHomeScreen.setFlat(True)
        self.BT_openHomeScreen.setObjectName("BT_openHomeScreen")
        self.TopSelectionBar.addWidget(self.BT_openHomeScreen)
        self.BT_openSonosScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BT_openSonosScreen.setFlat(True)
        self.BT_openSonosScreen.setObjectName("BT_openSonosScreen")
        self.TopSelectionBar.addWidget(self.BT_openSonosScreen)
        self.BT_openWeatherScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BT_openWeatherScreen.setFlat(True)
        self.BT_openWeatherScreen.setObjectName("BT_openWeatherScreen")
        self.TopSelectionBar.addWidget(self.BT_openWeatherScreen)
        self.BT_openMeteoScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BT_openMeteoScreen.setFlat(True)
        self.BT_openMeteoScreen.setObjectName("BT_openMeteoScreen")
        self.TopSelectionBar.addWidget(self.BT_openMeteoScreen)
        self.BT_openSbbScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.BT_openSbbScreen.setFlat(True)
        self.BT_openSbbScreen.setObjectName("BT_openSbbScreen")
        self.TopSelectionBar.addWidget(self.BT_openSbbScreen)
        self.BT_openLogScreen = QtWidgets.QPushButton(self.verticalLayoutWidget)
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
        self.LN_boarderLine = QtWidgets.QFrame(self.verticalLayoutWidget)
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
        self.ST_workerStack = QtWidgets.QStackedWidget(self.centralwidget)
        self.ST_workerStack.setGeometry(QtCore.QRect(0, 50, 481, 271))
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
        self.WD_clock = QtWidgets.QWidget(self.SC_welcomeScreen)
        self.WD_clock.setGeometry(QtCore.QRect(9, 9, 451, 251))
        self.WD_clock.setObjectName("WD_clock")
        self.webView_2 = QtWebKitWidgets.QWebView(self.WD_clock)
        self.webView_2.setGeometry(QtCore.QRect(-1, -1, 451, 251))
        self.webView_2.setUrl(QtCore.QUrl("qrc:/newPrefix/index.html"))
        self.webView_2.setObjectName("webView_2")
        self.ST_workerStack.addWidget(self.SC_welcomeScreen)
        self.SC_sonosScreen = QtWidgets.QWidget()
        self.SC_sonosScreen.setObjectName("SC_sonosScreen")
        self.LB_sonosScreen = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_sonosScreen.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.LB_sonosScreen.setObjectName("LB_sonosScreen")
        self.BT_sonosPlay = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_sonosPlay.setGeometry(QtCore.QRect(100, 40, 75, 23))
        self.BT_sonosPlay.setFlat(True)
        self.BT_sonosPlay.setObjectName("BT_sonosPlay")
        self.SL_volume = QtWidgets.QSlider(self.SC_sonosScreen)
        self.SL_volume.setGeometry(QtCore.QRect(440, 40, 19, 160))
        self.SL_volume.setAutoFillBackground(False)
        self.SL_volume.setProperty("value", 14)
        self.SL_volume.setOrientation(QtCore.Qt.Vertical)
        self.SL_volume.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.SL_volume.setTickInterval(0)
        self.SL_volume.setObjectName("SL_volume")
        self.BT_pause = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_pause.setGeometry(QtCore.QRect(100, 80, 75, 23))
        self.BT_pause.setFlat(True)
        self.BT_pause.setObjectName("BT_pause")
        self.BT_stop = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_stop.setGeometry(QtCore.QRect(100, 120, 75, 23))
        self.BT_stop.setFlat(True)
        self.BT_stop.setObjectName("BT_stop")
        self.BT_skip = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_skip.setGeometry(QtCore.QRect(190, 80, 75, 23))
        self.BT_skip.setFlat(True)
        self.BT_skip.setObjectName("BT_skip")
        self.LB_currentlyPlaying = QtWidgets.QLabel(self.SC_sonosScreen)
        self.LB_currentlyPlaying.setGeometry(QtCore.QRect(10, 170, 281, 16))
        self.LB_currentlyPlaying.setObjectName("LB_currentlyPlaying")
        self.BT_previous = QtWidgets.QPushButton(self.SC_sonosScreen)
        self.BT_previous.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.BT_previous.setFlat(True)
        self.BT_previous.setObjectName("BT_previous")
        self.ST_workerStack.addWidget(self.SC_sonosScreen)
        self.SC_weatherScreen = QtWidgets.QWidget()
        self.SC_weatherScreen.setObjectName("SC_weatherScreen")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.SC_weatherScreen)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 481, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.LB_weatherScreen = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.LB_weatherScreen.setObjectName("LB_weatherScreen")
        self.horizontalLayout.addWidget(self.LB_weatherScreen)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LB_oldFreezer = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.LB_oldFreezer.setObjectName("LB_oldFreezer")
        self.gridLayout.addWidget(self.LB_oldFreezer, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        self.LB_newFreezer = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.LB_newFreezer.setObjectName("LB_newFreezer")
        self.gridLayout.addWidget(self.LB_newFreezer, 2, 1, 1, 1)
        self.LB_internalTemp = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LB_internalTemp.sizePolicy().hasHeightForWidth())
        self.LB_internalTemp.setSizePolicy(sizePolicy)
        self.LB_internalTemp.setObjectName("LB_internalTemp")
        self.gridLayout.addWidget(self.LB_internalTemp, 0, 1, 1, 1)
        self.LCD_newFreezer = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.LCD_newFreezer.setProperty("value", -16.2)
        self.LCD_newFreezer.setObjectName("LCD_newFreezer")
        self.gridLayout.addWidget(self.LCD_newFreezer, 2, 2, 1, 1)
        self.LCD_piTemp = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.LCD_piTemp.setSmallDecimalPoint(True)
        self.LCD_piTemp.setProperty("intValue", 40)
        self.LCD_piTemp.setObjectName("LCD_piTemp")
        self.gridLayout.addWidget(self.LCD_piTemp, 0, 2, 1, 1)
        self.LCD_oldFreezer = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.LCD_oldFreezer.setProperty("value", -15.5)
        self.LCD_oldFreezer.setObjectName("LCD_oldFreezer")
        self.gridLayout.addWidget(self.LCD_oldFreezer, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.ST_workerStack.addWidget(self.SC_weatherScreen)
        self.SC_log = QtWidgets.QWidget()
        self.SC_log.setObjectName("SC_log")
        self.TE_Debug = QtWidgets.QTextEdit(self.SC_log)
        self.TE_Debug.setGeometry(QtCore.QRect(10, 0, 461, 261))
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
        self.ST_workerStack.addWidget(self.SC_log)
        self.SC_meteo = QtWidgets.QWidget()
        self.SC_meteo.setObjectName("SC_meteo")
        self.WD_browser = QtWidgets.QWidget(self.SC_meteo)
        self.WD_browser.setGeometry(QtCore.QRect(9, 9, 461, 251))
        self.WD_browser.setObjectName("WD_browser")
        self.webView = QtWebKitWidgets.QWebView(self.WD_browser)
        self.webView.setGeometry(QtCore.QRect(-1, -1, 461, 261))
        self.webView.setUrl(QtCore.QUrl("http://m.srf.ch/meteo"))
        self.webView.setObjectName("webView")
        self.ST_workerStack.addWidget(self.SC_meteo)
        self.SC_sbb = QtWidgets.QWidget()
        self.SC_sbb.setObjectName("SC_sbb")
        self.gridLayoutWidget = QtWidgets.QWidget(self.SC_sbb)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 461, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BT_hb = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BT_hb.setFlat(True)
        self.BT_hb.setObjectName("BT_hb")
        self.gridLayout_2.addWidget(self.BT_hb, 0, 0, 1, 1)
        self.BT_wankdorf = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BT_wankdorf.setFlat(True)
        self.BT_wankdorf.setObjectName("BT_wankdorf")
        self.gridLayout_2.addWidget(self.BT_wankdorf, 0, 1, 1, 1)
        self.BT_breitsch = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.BT_breitsch.setFlat(True)
        self.BT_breitsch.setObjectName("BT_breitsch")
        self.gridLayout_2.addWidget(self.BT_breitsch, 0, 2, 1, 1)
        self.ST_workerStack.addWidget(self.SC_sbb)
        self.SC_hb = QtWidgets.QWidget()
        self.SC_hb.setObjectName("SC_hb")
        self.WD_hb = QtWidgets.QWidget(self.SC_hb)
        self.WD_hb.setGeometry(QtCore.QRect(10, 10, 461, 251))
        self.WD_hb.setObjectName("WD_hb")
        self.ST_workerStack.addWidget(self.SC_hb)
        self.SC_wankdorf = QtWidgets.QWidget()
        self.SC_wankdorf.setObjectName("SC_wankdorf")
        self.WD_wankdorf = QtWidgets.QWidget(self.SC_wankdorf)
        self.WD_wankdorf.setGeometry(QtCore.QRect(10, 10, 461, 251))
        self.WD_wankdorf.setObjectName("WD_wankdorf")
        self.ST_workerStack.addWidget(self.SC_wankdorf)
        self.SC_breitsch = QtWidgets.QWidget()
        self.SC_breitsch.setObjectName("SC_breitsch")
        self.WD_breitsch = QtWidgets.QWidget(self.SC_breitsch)
        self.WD_breitsch.setGeometry(QtCore.QRect(10, 10, 461, 251))
        self.WD_breitsch.setObjectName("WD_breitsch")
        self.ST_workerStack.addWidget(self.SC_breitsch)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.ST_workerStack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SonosController"))
        self.BT_openHomeScreen.setText(_translate("MainWindow", "HOME"))
        self.BT_openSonosScreen.setText(_translate("MainWindow", "SONOS"))
        self.BT_openWeatherScreen.setText(_translate("MainWindow", "WETTER"))
        self.BT_openMeteoScreen.setText(_translate("MainWindow", "METEO"))
        self.BT_openSbbScreen.setText(_translate("MainWindow", "SBB"))
        self.BT_openLogScreen.setText(_translate("MainWindow", "LOG"))
        self.LB_sonosScreen.setText(_translate("MainWindow", "This is the sonos screen"))
        self.BT_sonosPlay.setText(_translate("MainWindow", "Play"))
        self.BT_pause.setText(_translate("MainWindow", "Pause"))
        self.BT_stop.setText(_translate("MainWindow", "Stop"))
        self.BT_skip.setText(_translate("MainWindow", "Next"))
        self.LB_currentlyPlaying.setText(_translate("MainWindow", "currently playing..."))
        self.BT_previous.setText(_translate("MainWindow", "Previous"))
        self.LB_weatherScreen.setText(_translate("MainWindow", "This is the weather screen"))
        self.LB_oldFreezer.setText(_translate("MainWindow", "Temp alter Gefrierschrank"))
        self.LB_newFreezer.setText(_translate("MainWindow", "Temp neuer Gefrierschrank"))
        self.LB_internalTemp.setText(_translate("MainWindow", "internal Temp"))
        self.BT_hb.setText(_translate("MainWindow", "Bahnhof"))
        self.BT_wankdorf.setText(_translate("MainWindow", "Wankdorf"))
        self.BT_breitsch.setText(_translate("MainWindow", "Breitsch"))

from PyQt5 import QtWebKitWidgets
import clock_rc
