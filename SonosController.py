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
    albums=''
    titles=''
    radioStations=''
    __playMode='music'
    __listMode='artists'
    __nextListMode='albums'
    __selectedArtist=''
    __selectedAlbum=''
    __Widget=''
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
    def __init__(self, ui, appWidget, args):
        if args.noSonos=='hasSonos':
            if args.host == 'host':
                self.myZone = list(soco.discover(timeout=5, include_invisible=False, interface_addr='192.168.1.118'))
            else:
                self.myZone = list(soco.discover())
            self.activeSpeaker = 0
        self.__Widget=appWidget
    def getListInfo(self, homeScreenTimer):
        if self.__playMode is 'radio':
            self.addToQueue(homeScreenTimer)
        elif self.__playMode is 'music':
            if self.__nextListMode is 'albums':
                logging.error('album mode')
                self.__selectedArtist = ui.LW_artists.currentItem().text()
                logging.error(self.__selectedArtist)
                self.albums=self.myZone[self.activeSpeaker].music_library.get_music_library_information('artists', subcategories=[self.__selectedArtist])
                self.__listMode='albums'
                self.__nextListMode='titles'
                ui.LW_artists.clear()
                for album in self.albums:
                    ui.LW_artists.addItem(album.title)
            elif self.__nextListMode is 'titles':
                logging.error('title mode')
                self.__nextListMode='addToQueue'
                self.__listMode='titles'
                self.__selectedAlbum = ui.LW_artists.currentItem().text()            
                self.titles=self.myZone[self.activeSpeaker].music_library.get_music_library_information('artists', subcategories=[self.__selectedArtist, self.__selectedAlbum])
                ui.LW_artists.clear()
                for title in self.titles:
                    ui.LW_artists.addItem(title.title)
            elif self.__nextListMode is 'addToQueue':
                self.addToQueue(homeScreenTimer)
        
        homeScreenTimer.rearmTimer()
    def getArtists(self, homeScreenTimer):
        logging.error('hier auch?')
        self.__listMode='artists'
        self.__nextListMode='albums'
        self.artists=self.myZone[self.activeSpeaker].music_library.get_artists(complete_result=True)
        ui.LW_artists.clear()
        for artist in self.artists:
            ui.LW_artists.addItem(artist.title)
        homeScreenTimer.rearmTimer()
    def getAlbums(self, homeScreenTimer):
        self.albums=self.myZone[self.activeSpeaker].music_library.get_music_library_information('artists', subcategories=[self.__selectedArtist])
        self.__listMode='albums'
        self.__nextListMode='titles'
        ui.LW_artists.clear()
        for album in self.albums:
            ui.LW_artists.addItem(album.title)
        homeScreenTimer.rearmTimer()
    def handleBackButton(self, homeScreenTimer):
        if(self.__listMode=='titles'):
            self.getAlbums(homeScreenTimer)
        elif(self.__listMode=='albums'):
            self.getArtists(homeScreenTimer)
        homeScreenTimer.rearmTimer()
    def getRadio(self):
        self.radioStations=self.myZone[self.activeSpeaker].get_favorite_radio_stations(start=0, max_items=100)
        self.radioStations=self.radioStations["favorites"]
        print(self.radioStations)                
        ui.LW_artists.clear()
        for radios in self.radioStations:
            item=radios.get('title')
            print(item)
            ui.LW_artists.addItem(item)
    def addToQueue(self, homeScreenTimer):
        if self.__playMode=='music':
            if self.__listMode is 'artists':
                logging.error('artist mode')
                self.myZone[self.activeSpeaker].clear_queue()
                self.myZone[self.activeSpeaker].add_to_queue(self.artists[ui.LW_artists.currentRow()])
                self.queuePosition = 0
            elif self.__listMode is 'albums':
                logging.error('album mode')
                self.myZone[self.activeSpeaker].clear_queue()
                self.myZone[self.activeSpeaker].add_to_queue(self.albums[ui.LW_artists.currentRow()])
                self.queuePosition = 0
            elif self.__listMode is 'titles':
                logging.error('title mode')
                self.myZone[self.activeSpeaker].clear_queue()
                self.myZone[self.activeSpeaker].add_to_queue(self.titles[ui.LW_artists.currentRow()])
                self.queuePosition = 0
            self.playMusic(homeScreenTimer)
        elif self.__playMode=='radio':
            uri=self.radioStations[ui.LW_artists.currentRow()].get('uri')
            uri=uri.replace('&', '&amp;')
            titleunformated=self.radioStations[ui.LW_artists.currentRow()].get('title')
            metadata=self.meta_template.format(title=titleunformated, service=self.tunein_service)
            self.myZone[self.activeSpeaker].play_uri(uri, metadata)
            self.queuePosition = 0
        else:
            logging.error('showWidget start')
            self.__Widget.show()
            logging.error('showWidget end')
        homeScreenTimer.rearmTimer()    
    def displayMyZone(self):
        print(self.myZone[self.activeSpeaker])
    def selectLineIn(self):
        self.myZone[self.activeSpeaker].switch_to_line_in()
    def selectTv(self, homeScreenTimer):
        self.myZone[self.activeSpeaker].switch_to_tv()
        homeScreenTimer.rearmTimer()
    def playMusic(self, homeScreenTimer):
        self.myZone[self.activeSpeaker].play_from_queue(int(self.queuePosition))
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
        self.queuePosition = info["playlist_position"]
        ui.LB_currentlyPlayingTitle.setText(str(info["title"]))
        ui.LB_currentlyPlayingArtist.setText(str(info["artist"]))
        ui.LB_currentlyPlayingPosition.setText(str(info["playlist_position"]))
        ui.LB_currentlyPlayingTotal.setText(str(info["duration"]))
        ui.LB_currentlyPlayingCurrentTime.setText(str(info["position"]))
        ui.SL_volume.setValue(self.getVolume())
    def switchMode(self, ui, mode, homeScreenTimer):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if mode == 'tv':
            the_path=dir_path
            ui.BT_tvMode.setStyleSheet   ("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #000000; image: url(" + dir_path + "/icons/tv.png)")
            ui.BT_musicMode.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(" + dir_path + "/icons/music.png)")
            ui.BT_radioMode.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(" + dir_path + "/icons/radio.png)")
            self.__playMode='tv'
            if args.noSonos=='hasSonos':
                self.selectLineIn()
                self.play(homeScreenTimer)
        if mode == 'radio':
            if args.noSonos=='hasSonos':
                self.getRadio()
            ui.BT_radioMode.setStyleSheet("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #000000; image: url(" + dir_path + "/icons/radio.png)")
            ui.BT_musicMode.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(" + dir_path + "/icons/music.png)")
            ui.BT_tvMode.setStyleSheet   ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(" + dir_path + "/icons/tv.png)")
            self.__playMode='radio'
        if mode == 'music':
            if args.noSonos=='hasSonos':
                self.getArtists(homeScreenTimer)
            ui.BT_musicMode.setStyleSheet("background-color: #e3e3e3; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #000000; image: url(" + dir_path + "/icons/music.png)")
            ui.BT_radioMode.setStyleSheet("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(" + dir_path + "/icons/radio.png)")
            ui.BT_tvMode.setStyleSheet   ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; min-width: 20px; min-height: 23px; color: #FFFFFF; image: url(" + dir_path + "/icons/tv.png)")
            self.__playMode='music'
        homeScreenTimer.rearmTimer()
    def musicIcons(self, ui):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path=dir_path + "/icons/play.png"
        logging.error(path)
        ui.BT_sonosPlay.setStyleSheet("background-color: #a8a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(" + dir_path + "/icons/play.png)")
        ui.BT_pause.setStyleSheet    ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(" + dir_path + "/icons/pause.png)")
        ui.BT_stop.setStyleSheet     ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(" + dir_path + "/icons/stop.png)")
        ui.BT_skip.setStyleSheet     ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(" + dir_path + "/icons/skip.png)")
        ui.BT_previous.setStyleSheet ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(" + dir_path + "/icons/rewind.png)")
        ui.BT_volumeUp.setStyleSheet ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(" + dir_path + "/icons/increaseVolume.png)")
        ui.BT_volumeDown.setStyleSheet ("background-color: #a0a0a0; padding: 0px; border: 0px solid black; margin: 0px; border-radius: 8px; max-width: 30px; min-height: 23px; color: #000000; image: url(" + dir_path + "/icons/reduceVolume.png)")
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
    from Widget_chooseSource import Ui_Info

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    MainWindow = QtWidgets.QMainWindow()
    InfoWindow = QtWidgets.QDialog()
       
    if args.host == 'host':
        ui = Ui_MainWindowHost()
    else:
        ui = Ui_MainWindowTarget()
    wx = Ui_Info()
    wx.setupUi(InfoWindow)
        
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
    logger.setLevel(logging.ERROR)
    logging.info('Session started')
    
    homeScreenTimer=noClickTimer(ui)
    
    myMusicPlayer=SonosInterface(ui, InfoWindow, args)
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
    ui.LW_artists.doubleClicked.connect(lambda: myMusicPlayer.getListInfo(homeScreenTimer))
    ui.BT_select.clicked.connect(lambda: myMusicPlayer.addToQueue(homeScreenTimer))
    ui.BT_listArtists.clicked.connect(lambda: myMusicPlayer.handleBackButton(homeScreenTimer))
    
    
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
    