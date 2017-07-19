from soco import SoCo
import soco

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from MainWindow_raspi import Ui_MainWindow
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.BT_openSonosScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(1))
    ui.BT_openWeatherScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(2))
    ui.BT_openHomeScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(0))
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    MainWindow.show()

    speakers = list(soco.discover())

    for speaker in speakers:
        print(speaker.player_name, speaker.ip_address)

    speakers[0].play()
    speakers[0].volume=40
    
    sys.exit(app.exec_())



