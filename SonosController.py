# -*- coding: utf-8 -*-
import argparse

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QUrl

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
    myZone = 0
    activeSpeaker = 0
    queuePosition = 0
    artists=''
    radioStations=''
    playMode='music'
    tunein_service = 'SA_RINCON65031_'
    meta_template = """
    <DIDL-Lite xmlns:dc="http://purl.org/dc/elements/1.1/"
        xmlns:upnp="urn:schemas-upnp-org:metadata-1-0/upnp/"
        xmlns:r="urn:schemas-rinconnetworks-com:metadata-1-0/"
        xmlns="urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/">
        <item id="R:0/0/0" parentID="R:0/0" restricted="true">
            <dc:title>{title}</dc:title>
            <upnp:class>object.item.audioItem.audioBroadcast</upnp:class>
            <desc id="cdudn" nameSpace="urn:schemas-rinconnetworks-com:metadata-1-0/">
                {service}
            </desc>
        </item>
    </DIDL-Lite>' """
    def __init__(self, ui, args):
        if args.noSonos=='hasSonos':
            if args.host == 'host':
                SonosInterface.myZone = list(soco.discover(timeout=5, include_invisible=False, interface_addr='192.168.1.109'))
            else:
                SonosInterface.myZone = list(soco.discover())
            SonosInterface.activeSpeaker = 0
    def getArtists(self):
        SonosInterface.artists=self.myZone[self.activeSpeaker].music_library.get_artists(complete_result=True)
        ui.LW_artists.clear()
        for artist in SonosInterface.artists:
            ui.LW_artists.addItem(artist.title)
    def getRadio(self):
        SonosInterface.radioStations=self.myZone[self.activeSpeaker].get_favorite_radio_stations(start=0, max_items=100)
        SonosInterface.radioStations=SonosInterface.radioStations["favorites"]
        print(SonosInterface.radioStations)                
        ui.LW_artists.clear()
        for radios in SonosInterface.radioStations:
            item=radios.get('title')
            print(item)
            ui.LW_artists.addItem(item)
    def addToQueue(self, homeScreenTimer):
        if SonosInterface.playMode=='music':
            self.myZone[self.activeSpeaker].clear_queue()
            self.myZone[self.activeSpeaker].add_to_queue(SonosInterface.artists[ui.LW_artists.currentRow()])
            SonosInterface.queuePosition = 0
            self.playMusic()
        if SonosInterface.playMode=='radio':
            uri=SonosInterface.radioStations[ui.LW_artists.currentRow()].get('uri')
            uri=uri.replace('&', '&amp;')
            titleunformated=SonosInterface.radioStations[ui.LW_artists.currentRow()].get('title')
            metadata=SonosInterface.meta_template.format(title=titleunformated, service=SonosInterface.tunein_service)
            self.myZone[self.activeSpeaker].play_uri(uri, metadata)
            SonosInterface.queuePosition = 0
        homeScreenTimer.rearmTimer()
    def displayMyZone(self):
        print(self.myZone[self.activeSpeaker])
    def selectLineIn(self):
        self.myZone[self.activeSpeaker].switch_to_line_in()
    def selectTv(self, homeScreenTimer):
        self.myZone[self.activeSpeaker].switch_to_tv()
        homeScreenTimer.rearmTimer()
    def playMusic(self, homeScreenTimer):
        self.myZone[self.activeSpeaker].play_from_queue(int(SonosInterface.queuePosition) - 1)
        homeScreenTimer.rearmTimer()
    def play(self, homeScreenTimer):
        self.myZone[self.activeSpeaker].play()
        homeScreenTimer.rearmTimer()
    def stopMusic(self, homeScreenTimer):
        self.myZone[self.activeSpeaker].stop()
        homeScreenTimer.rearmTimer()
    def muteMusic(self):
        self.myZone[self.activeSpeaker].mute(True)
    def pauseMusic(self, homeScreenTimer):
        self.myZone[self.activeSpeaker].pause()
        homeScreenTimer.rearmTimer()
    def skipMusic(self, homeScreenTimer):
        self.myZone[self.activeSpeaker].next() 
        homeScreenTimer.rearmTimer()
    def previousMusic(self, homeScreenTimer):
        self.myZone[self.activeSpeaker].previous()
        homeScreenTimer.rearmTimer()
    def setVolume(self, vol, homeScreenTimer):
        self.myZone[self.activeSpeaker].volume=vol
        homeScreenTimer.rearmTimer()
    def getVolume(self):
        return self.myZone[self.activeSpeaker].volume
    def volumeUp(self, homeScreenTimer):
        vol=self.myZone[self.activeSpeaker].volume
        self.myZone[self.activeSpeaker].volume=vol+5
        homeScreenTimer.rearmTimer()
    def volumeDown(self, homeScreenTimer):
        vol=self.myZone[self.activeSpeaker].volume
        vol=max(vol, 0)
        self.myZone[self.activeSpeaker].volume=vol-5
        homeScreenTimer.rearmTimer()
    def get_current_track_info(self):
        info=self.myZone[self.activeSpeaker].get_current_track_info()
        SonosInterface.queuePosition = info["playlist_position"]
        ui.LB_currentlyPlayingTitle.setText(str(info["title"]))
        ui.LB_currentlyPlayingArtist.setText(str(info["artist"]))
        ui.LB_currentlyPlayingPosition.setText(str(info["playlist_position"]))
        ui.LB_currentlyPlayingTotal.setText(str(info["duration"]))
        ui.LB_currentlyPlayingCurrentTime.setText(str(info["position"]))
        ui.SL_volume.setValue(self.getVolume())
    def switchMode(self, ui, mode, homeScreenTimer):
        if mode == 'tv':
            ui.BT_tvMode.setStyleSheet   ("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #000000; image: url(icons/tv.png)")
            ui.BT_musicMode.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(icons/music.png)")
            ui.BT_radioMode.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(icons/radio.png)")
            SonosInterface.playMode='tv'
            if args.noSonos=='hasSonos':
                self.selectLineIn()
                self.play()
        if mode == 'radio':
            if args.noSonos=='hasSonos':
                self.getRadio()
            ui.BT_radioMode.setStyleSheet("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #000000; image: url(icons/radio.png)")
            ui.BT_musicMode.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(icons/music.png)")
            ui.BT_tvMode.setStyleSheet   ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(icons/tv.png)")
            SonosInterface.playMode='radio'
        if mode == 'music':
            if args.noSonos=='hasSonos':
                self.getArtists()
            ui.BT_musicMode.setStyleSheet("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #000000; image: url(icons/music.png)")
            ui.BT_radioMode.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(icons/radio.png)")
            ui.BT_tvMode.setStyleSheet   ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(icons/tv.png)")
            SonosInterface.playMode='music'
        homeScreenTimer.rearmTimer()
    def musicIcons(self, ui):
        ui.BT_sonosPlay.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(icons/play.png)")
        ui.BT_pause.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(icons/pause.png)")
        ui.BT_stop.setStyleSheet     ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(icons/stop.png)")
        ui.BT_skip.setStyleSheet     ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(icons/skip.png)")
        ui.BT_previous.setStyleSheet ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(icons/rewind.png)")
        ui.BT_volumeUp.setStyleSheet ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(icons/increaseVolume.png)")
        ui.BT_volumeDown.setStyleSheet ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(icons/reduceVolume.png)")
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
    def openHb(self, args):
        ui.ST_workerStack.setCurrentIndex(6)
        timeDate=self.getTimeDate()
        myUrl=QUrl("https://www.sbb.ch/de/kaufen/pages/fahrplan/fahrplan.xhtml?von=Bern+Breitfeld&nach=Bern&datum=" + timeDate[0] + "&zeit=" + timeDate[1] + "&suche=true")
        logging.info(myUrl)
        if args.host == 'host':
            ui.WD_hb.load(myUrl)
        else:
            ui.WV_sbbHb.load(myUrl)
    def openBreitsch(self, args):
        ui.ST_workerStack.setCurrentIndex(8)
        timeDate=self.getTimeDate()
        myUrl=QUrl("https://www.sbb.ch/de/kaufen/pages/fahrplan/fahrplan.xhtml?von=Bern+Wylerbad&nach=Bern+Breitenrainplatz&datum=" + timeDate[0] + "&zeit=" + timeDate[1] + "&suche=true")
        logging.info(myUrl)
        if args.host == 'host':
            ui.WD_breitsch.load(myUrl)
        else:
            ui.WV_sbbBreitsch.load(myUrl)
    def openWankdorf(self, args):
        ui.ST_workerStack.setCurrentIndex(7)
        timeDate=self.getTimeDate()
        myUrl=QUrl("https://www.sbb.ch/de/kaufen/pages/fahrplan/fahrplan.xhtml?von=Bern+Breitfeld&nach=Bern+Wankdorf&datum=" + timeDate[0] + "&zeit=" + timeDate[1] + "&suche=true")
        logging.info(myUrl)
        if args.host == 'host':
            ui.WD_wankdorf.load(myUrl)
        else:
            ui.WV_sbbWankdorf.load(myUrl)
    def openMeteo(self, args):
        myUrl=QUrl("https://m.srf.ch/meteo")
        logging.info(myUrl)
        if args.host == 'host':
            ui.WD_browser.load(myUrl)
        else:
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
    
class selectTopLevelPage():
    def __init__(self, ui):
        Ui=ui
    def selectHome(self, ui, homeScreenTimer):
        ui.ST_workerStack.setCurrentIndex(0)
        ui.BT_openHomeScreen.setStyleSheet   ("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #000000")
        ui.BT_openSonosScreen.setStyleSheet  ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openWeatherScreen.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openMeteoScreen.setStyleSheet  ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openSbbScreen.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openLogScreen.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 40px; min-height: 23px; color: #FFFFFF")
        homeScreenTimer.rearmTimer()
    def selectSonos(self, ui, homeScreenTimer):
        ui.ST_workerStack.setCurrentIndex(1)
        ui.BT_openHomeScreen.setStyleSheet   ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openSonosScreen.setStyleSheet  ("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #000000")
        ui.BT_openWeatherScreen.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openMeteoScreen.setStyleSheet  ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openSbbScreen.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openLogScreen.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 40px; min-height: 23px; color: #FFFFFF")
        homeScreenTimer.rearmTimer()
    def selectFridge(self, ui, homeScreenTimer):
        ui.ST_workerStack.setCurrentIndex(2)
        ui.BT_openHomeScreen.setStyleSheet   ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openSonosScreen.setStyleSheet  ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openWeatherScreen.setStyleSheet("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #000000")
        ui.BT_openMeteoScreen.setStyleSheet  ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openSbbScreen.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openLogScreen.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 40px; min-height: 23px; color: #FFFFFF")
        homeScreenTimer.rearmTimer()
    def selectMeteo(self, ui, homeScreenTimer):
        ui.ST_workerStack.setCurrentIndex(4)
        ui.BT_openHomeScreen.setStyleSheet   ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openSonosScreen.setStyleSheet  ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openWeatherScreen.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openMeteoScreen.setStyleSheet  ("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #000000")
        ui.BT_openSbbScreen.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openLogScreen.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 40px; min-height: 23px; color: #FFFFFF")
        homeScreenTimer.rearmTimer()
    def selectSbb(self, ui, homeScreenTimer):
        ui.ST_workerStack.setCurrentIndex(5)
        ui.BT_openHomeScreen.setStyleSheet   ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openSonosScreen.setStyleSheet  ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openWeatherScreen.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openMeteoScreen.setStyleSheet  ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openSbbScreen.setStyleSheet    ("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #000000")
        ui.BT_openLogScreen.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 40px; min-height: 23px; color: #FFFFFF")
        homeScreenTimer.rearmTimer()
    def selectLog(self, ui, homeScreenTimer):
        ui.ST_workerStack.setCurrentIndex(3)
        ui.BT_openHomeScreen.setStyleSheet   ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openSonosScreen.setStyleSheet  ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openWeatherScreen.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openMeteoScreen.setStyleSheet  ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openSbbScreen.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 70px; min-height: 23px; color: #FFFFFF")
        ui.BT_openLogScreen.setStyleSheet    ("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 40px; min-height: 23px; color: #000000")
        homeScreenTimer.rearmTimer()
    
class noClickTimer():
    myHomeScreenTimer=QtCore.QTimer()
    def __init__(self, ui):
        self.myHomeScreenTimer.timeout.connect(lambda: selectHome.selectHome(ui, self))
        self.myHomeScreenTimer.start(300000)
    def rearmTimer(self):
        self.myHomeScreenTimer.start(300000)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sonos Controller')
    parser.add_argument('--host', nargs='?', const='host', default='target',
                        help='start the program on host computer (default: start raspberry pi)')
    parser.add_argument('--noSonos', nargs='?', const='noSonos', default='hasSonos',
                        help='test mode when no sonos player is available in network (default: sonos available in network)')
    parser.add_argument('--discover', nargs='?', const='discover', default='noDiscover',
                        help='discover the network for sonos devices (default: no discovery)')

    args = parser.parse_args()
    if args.host == 'host':
        from MainWindow_Host import Ui_MainWindowHost
    else:
        from MainWindow_raspi import Ui_MainWindowTarget

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    MainWindow = QtWidgets.QMainWindow()
    
    if args.host == 'host':
        ui = Ui_MainWindowHost()
    else:
        ui = Ui_MainWindowTarget()
    
    ui.setupUi(MainWindow)
    
    logTextBox = QPlainTextEditLogger(ui)
    logTextBox.setFormatter(logging.Formatter('%(funcName)-12s: %(levelname)-8s %(message)s'))
    logger=logging.getLogger()
    # file handler 
    fh=logging.FileHandler('spam.log')
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(lineno)d - %(message)s'))
    # add the handlers
    logger.addHandler(logTextBox)
    logger.addHandler(fh)
    # You can control the logging level
    logger.setLevel(logging.INFO)
    logging.info('Session started')
    
    homeScreenTimer=noClickTimer(ui)
    
    myMusicPlayer=SonosInterface(ui, args)
    myMusicPlayer.switchMode(ui, 'music', homeScreenTimer)
    myMusicPlayer.musicIcons(ui)
    
    selectHome=selectTopLevelPage(ui)
    selectHome.selectHome(ui, homeScreenTimer)
    
    openBrowser=openBrowserWidget(ui)
    
    ui.ST_workerStack.setCurrentIndex(0)
    ui.BT_openHomeScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(0))
    filepath=os.path.abspath(os.path.join(os.path.dirname(__file__), "index.html"))
    myUrl=QUrl.fromLocalFile(filepath)
    if args.host == 'host':
        ui.WD_clock.load(myUrl)
        ui.BT_openHomeScreen.clicked.connect(lambda: ui.WD_clock.load(myUrl))
    else:
        ui.WV_clock.load(myUrl)
        ui.BT_openHomeScreen.clicked.connect(lambda: ui.WV_clock.load(myUrl))
    
    ui.BT_openHomeScreen.clicked.connect(lambda: selectHome.selectHome(ui, homeScreenTimer))
    ui.BT_openSonosScreen.clicked.connect(lambda: selectHome.selectSonos(ui, homeScreenTimer))
    ui.BT_openWeatherScreen.clicked.connect(lambda: selectHome.selectFridge(ui, homeScreenTimer))
    ui.BT_openLogScreen.clicked.connect(lambda: selectHome.selectLog(ui, homeScreenTimer))
    ui.BT_openMeteoScreen.clicked.connect(lambda: selectHome.selectMeteo(ui, homeScreenTimer))
    ui.BT_openMeteoScreen.clicked.connect(lambda: openBrowser.openMeteo(args))
    ui.BT_openSbbScreen.clicked.connect(lambda: selectHome.selectSbb(ui, homeScreenTimer))
    
    ui.BT_musicMode.clicked.connect(lambda: myMusicPlayer.switchMode(ui, "music", homeScreenTimer))
    ui.BT_radioMode.clicked.connect(lambda: myMusicPlayer.switchMode(ui, "radio", homeScreenTimer))
    ui.BT_tvMode.clicked.connect(lambda: myMusicPlayer.switchMode(ui, "tv", homeScreenTimer))
    
    ui.BT_hb.clicked.connect(lambda: openBrowser.openHb(args))
    ui.BT_breitsch.clicked.connect(lambda: openBrowser.openBreitsch(args))
    ui.BT_wankdorf.clicked.connect(lambda: openBrowser.openWankdorf(args))
    
    ui.BT_sonosPlay.clicked.connect(lambda: myMusicPlayer.playMusic(homeScreenTimer))
    ui.BT_stop.clicked.connect(lambda: myMusicPlayer.stopMusic(homeScreenTimer))
    ui.BT_pause.clicked.connect(lambda: myMusicPlayer.pauseMusic(homeScreenTimer))
    ui.BT_skip.clicked.connect(lambda: myMusicPlayer.skipMusic(homeScreenTimer))
    ui.BT_previous.clicked.connect(lambda: myMusicPlayer.previousMusic(homeScreenTimer))
    ui.BT_volumeUp.clicked.connect(lambda: myMusicPlayer.volumeUp(homeScreenTimer))
    ui.BT_volumeDown.clicked.connect(lambda: myMusicPlayer.volumeDown(homeScreenTimer))
    ui.SL_volume.valueChanged.connect(lambda: myMusicPlayer.setVolume(ui.SL_volume.value(), homeScreenTimer))
    ui.LW_artists.doubleClicked.connect(lambda: myMusicPlayer.addToQueue(homeScreenTimer))
    
    myTimer=QtCore.QTimer()
    if args.noSonos=='hasSonos':
        myTimer.timeout.connect(myMusicPlayer.get_current_track_info)
    myTimer.start(2001)
    
    volume=50
    if args.noSonos=='hasSonos':
        volume = myMusicPlayer.getVolume()
        ui.SL_volume.setValue(volume)
    
    if args.host == 'target':
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    
    MainWindow.show()
    sys.exit(app.exec_())
    