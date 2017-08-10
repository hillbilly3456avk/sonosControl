# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QUrl

from MainWindow_raspi import Ui_MainWindow
from PyQt5.QtGui import QDesktopServices
import sys
import datetime
import os as os
import logging
import time

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
    artists=''
    activeSpeaker=0
    def __init__(self, ui):
        SonosInterface.myZone = list(soco.discover())
        SonosInterface.activeSpeaker = 0
    def getArtists(self):
        #SonosInterface.artists=self.myZone[self.activeSpeaker].music_library.get_artists(start=0, max_items=100)
        SonosInterface.artists=self.myZone[self.activeSpeaker].music_library.get_artists(complete_result=True)
        for artist in SonosInterface.artists:
            ui.LW_artists.addItem(artist.title)
    def addToQueue(self):
        self.myZone[self.activeSpeaker].clear_queue()
        self.myZone[self.activeSpeaker].add_to_queue(SonosInterface.artists[ui.LW_artists.currentRow()])
    def displayMyZone(self):
        print(self.myZone[self.activeSpeaker])
    def selectLineIn(self):
        self.myZone[self.activeSpeaker].switchto_line_in()
    def selectTv(self):
        self.myZone[self.activeSpeaker].switch_to_tv()
    def playMusic(self):
        self.myZone[self.activeSpeaker].play_from_queue(0)
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
        ui.LB_currentlyPlayingTitle.setText(str(info["title]))
        ui.LB_currentlyPlayingArtist.setText(str(info["artist]))
    def printMyZone(self):
        for speaker in speakers:
            print(speaker.player_name, speaker.ip_address)
    def selectWohnzimmer(self):
        for speaker in speakers:
            if speaker.player_name=="Wohnzimmer":
                self.activeSpeaker = 0

class openBrowserWidget():
    def __init__(self, ui):
        Ui=ui
    def openHb(self):
        ui.ST_workerStack.setCurrentIndex(6)
        timeDate=self.getTimeDate()
        myUrl=QUrl("https://www.sbb.ch/de/kaufen/pages/fahrplan/fahrplan.xhtml?von=Bern+Breitfeld&nach=Bern&datum=" + timeDate[0] + "&zeit=" + timeDate[1] + "&suche=true")
        logging.error(myUrl)
        ui.WV_sbbHb.load(myUrl)
    def openBreitsch(self):
        ui.ST_workerStack.setCurrentIndex(8)
        timeDate=self.getTimeDate()
        myUrl=QUrl("https://www.sbb.ch/de/kaufen/pages/fahrplan/fahrplan.xhtml?von=Bern+Wylerbad&nach=Bern+Breitenrainplatz&datum=" + timeDate[0] + "&zeit=" + timeDate[1] + "&suche=true")
        logging.error(myUrl)
        ui.WV_sbbBreitsch.load(myUrl)
    def openWankdorf(self):
        ui.ST_workerStack.setCurrentIndex(7)
        timeDate=self.getTimeDate()
        myUrl=QUrl("https://www.sbb.ch/de/kaufen/pages/fahrplan/fahrplan.xhtml?von=Bern+Breitfeld&nach=Bern+Wankdorf&datum=" + timeDate[0] + "&zeit=" + timeDate[1] + "&suche=true")
        logging.error(myUrl)
        ui.WV_sbbWankdorf.load(myUrl)
    def openMeteo(self):
        myUrl=QUrl("https://m.srf.ch/meteo")
        ui.WV_srfMeteo.load(myUrl)
    def getTimeDate(self):
        myTime = time.localtime()
        myYear=myTime.tm_year
        myMonth=myTime.tm_mon
        myDay=myTime.tm_mday
        myHour=myTime.tm_hour
        myMin=myTime.tm_min
        myDate=(str(myDay)+"."+str(myMonth)+"."+str(myYear))
        myCurTime=(str(myHour)+":"+str(myMin))
        return [myDate, myCurTime]
    
    
        
if __name__ == '__main__':
    #logger = createLogger("myFirstTask.log")
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    filepath=os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
    myUrl=QUrl.fromLocalFile(filepath)
    ui.WV_clock.load(myUrl)
    
    myMusicPlayer=SonosInterface(ui)
    
    openBrowser=openBrowserWidget(ui)
    
    logTextBox = QPlainTextEditLogger(ui)
    logTextBox.setFormatter(logging.Formatter('%(funcName)-12s: %(levelname)-8s %(message)s'))
    logging.getLogger().addHandler(logTextBox)
    # You can control the logging level
    logging.getLogger().setLevel(logging.ERROR)
    
    logging.info('Here we are')
    logging.error('Oops')
    
    ui.ST_workerStack.setCurrentIndex(0)
    ui.BT_openHomeScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(0))
    filepath=os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
    myUrl=QUrl.fromLocalFile(filepath)
    ui.BT_openHomeScreen.clicked.connect(lambda: ui.WV_clock.load(myUrl))
    ui.BT_openSonosScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(1))
    ui.BT_openWeatherScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(2))
    ui.BT_openLogScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(3))
    ui.BT_openMeteoScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(4))
    ui.BT_openMeteoScreen.clicked.connect(lambda: openBrowser.openMeteo())
    ui.BT_openSbbScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(5))
    
    ui.BT_hb.clicked.connect(lambda: openBrowser.openHb())
    ui.BT_breitsch.clicked.connect(lambda: openBrowser.openBreitsch())
    ui.BT_wankdorf.clicked.connect(lambda: openBrowser.openWankdorf())
    
    ui.BT_sonosPlay.clicked.connect(lambda: myMusicPlayer.playMusic())
    ui.BT_stop.clicked.connect(lambda: myMusicPlayer.stopMusic())
    ui.BT_pause.clicked.connect(lambda: myMusicPlayer.pauseMusic())
    ui.BT_skip.clicked.connect(lambda: myMusicPlayer.skipMusic())
    ui.BT_previous.clicked.connect(lambda: myMusicPlayer.previousMusic())
    ui.SL_volume.valueChanged.connect(lambda: myMusicPlayer.setVolume(ui.SL_volume.value()))
    ui.LW_artists.doubleClicked.connect(lambda: myMusicPlayer.addToQueue())
    
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
    
    '''the clock'''
    local_url = QUrl.fromLocalFile(file_path)
    #ui.WD_clock.load(local_url)
    
    myTimer =QtCore.QTimer()
    myTimer.timeout.connect(myMusicPlayer.get_current_track_info)
    myTimer.start(6000)
    
    volume=50
    volume = myMusicPlayer.getVolume()
    ui.SL_volume.setValue(volume)
    myMusicPlayer.getArtists()
    
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    
    MainWindow.show()
    sys.exit(app.exec_())