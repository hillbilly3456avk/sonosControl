# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QUrl

from MainWindow_raspi import Ui_MainWindow
from PyQt5.QtGui import QDesktopServices
import sys
import datetime
import os as os
import logging

import soco

class QPlainTextEditLogger(logging.Handler):
    """create a logger class that emits to the TE_Debug field in Gui
    
    :param ui:              instance to the ui forma
    :type ui:               class 'MainForm.Ui_MainWindow'     
    """
    __criticalHtml = "<font color=\"DeepPink\">"
    __errorHtml = "<font color=\"red\">"
    __warningHtml = "<font color=\"Lime\">"
    __infoHtml = "<font color=\"Aqua\">"
    __dbgHtml = "<font color=\"blue\">"
    __endHtml = "</font><br>"
    __htmlMsg = ""
        
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

    def emit(self, record):
        msg = self.format(record)
        print(msg)
        if ": CRITICAL" in msg:
            self.__htmlMsg = self.__criticalHtml + msg
        elif ": ERROR" in msg:
            self.__htmlMsg = self.__errorHtml + msg
        elif ": WARNING" in msg:
            self.__htmlMsg = self.__warningHtml + msg
        elif ": INFO" in msg:
            self.__htmlMsg = self.__infoHtml + msg
        elif ": DEBUG" in msg:
            self.__htmlMsg = self.__dbgHtml + msg
        self.__htmlMsg = self.__htmlMsg + self.__endHtml
        print(self.__htmlMsg)
        self.ui.TE_Debug.insertHtml(self.__htmlMsg)
        self.ui.TE_Debug.ensureCursorVisible()

def createLogger(logFile):
    """ create a logger facility that logs to a file and to the stdout
    :param logFile:         File name of the log
    :type logFile:          class 'str'
    
    :rtype:                 class 'logging.Logger'
    """
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(funcName)s - %(levelname)s - %(lineno)d - %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=logFile,
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(funcName)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
                        
    logger = logging.getLogger(__name__)
    logger.info('---end of logger create function---')
    return logger
	
class SonosInterface():
  myZone=0
  activeSpeaker=0
  def __init__(self, ui):
    SonosInterface.myZone = list(soco.discover())
    SonosInterface.activeSpeaker = 0
  def displayMyZone(self):
    print(self.myZone[self.activeSpeaker])
  def selectLineIn(self):
    self.myZone[self.activeSpeaker].switchto_line_in()
  def selectTv(self):
    self.myZone[self.activeSpeaker].switch_to_tv()
  def playMusic(self):
    self.myZone[self.activeSpeaker].play()
  def stopMusic(self):
    self.myZone[self.activeSpeaker].stop()
  def muteMusic(self):
    self.myZone[self.activeSpeaker].mute(True)
  def pauseMusic(self):
    self.myZone[self.activeSpeaker].pause()  
  def skipMusic(self):
    self.myZone[self.activeSpeaker].next() 
  def previousMusic(self):
    self.myZone[self.activeSpeaker].previous()     
  def setVolume(self, vol):
    self.myZone[self.activeSpeaker].volume=vol
  def getVolume(self):
    return self.myZone[self.activeSpeaker].volume
  def volumeUp(self):
    vol=self.myZone[self.activeSpeaker].volume
    self.myZone[self.activeSpeaker].volume=vol+5
  def volumeDown(self):
    vol=self.myZone[self.activeSpeaker].volume
    vol=min(vol, 0)
    self.myZone[self.activeSpeaker].volume=vol-5
  def get_current_track_info(self):
    info=self.myZone[self.activeSpeaker].get_current_track_info()
    ui.LB_currentlyPlaying.setText(str(info))
  def printMyZone(self):
    for speaker in speakers:
      print(speaker.player_name, speaker.ip_address)
  def selectWohnzimmer(self):
    for speaker in speakers:
      if speaker.player_name=="Wohnzimmer":
        self.activeSpeaker = 0
		
if __name__ == '__main__':
    #logger = createLogger("myFirstTask.log")
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    #myMusicPlayer=SonosInterface(ui)
    
    logTextBox = QPlainTextEditLogger(ui)
    logTextBox.setFormatter(logging.Formatter('%(funcName)-12s: %(levelname)-8s %(message)s'))
    logging.getLogger().addHandler(logTextBox)
    # You can control the logging level
    logging.getLogger().setLevel(logging.DEBUG)
    
    logging.info('Here we are')
    logging.error('Oops')
    
    
    
    ui.ST_workerStack.setCurrentIndex(0)
    ui.BT_openHomeScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(0))
    ui.BT_openSonosScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(1))
    ui.BT_openWeatherScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(2))
    ui.BT_openLogScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(3))
    ui.BT_openMeteoScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(4))
    #ui.BT_sonosPlay.clicked.connect(lambda: myMusicPlayer.playMusic())
    #ui.BT_stop.clicked.connect(lambda: myMusicPlayer.stopMusic())
    #ui.BT_pause.clicked.connect(lambda: myMusicPlayer.pauseMusic())
    #ui.BT_skip.clicked.connect(lambda: myMusicPlayer.skipMusic())
    #ui.BT_previous.clicked.connect(lambda: myMusicPlayer.previousMusic())
    #ui.SL_volume.valueChanged.connect(lambda: myMusicPlayer.setVolume(ui.SL_volume.value()))
    
    ui.WD_browser.load(QUrl("http://m.srf.ch/meteo"))
    
    myTimer =QtCore.QTimer()
    #myTimer.timeout.connect(myMusicPlayer.get_current_track_info)
    myTimer.start(6000)
    
    volume=50
    #volume = myMusicPlayer.getVolume()
    ui.SL_volume.setValue(volume)
    
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    
    MainWindow.show()
    sys.exit(app.exec_())