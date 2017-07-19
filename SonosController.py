# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from MainWindow_raspi import Ui_MainWindow
from PyQt5.QtGui import QDesktopServices
import sys
import datetime
import os as os
import logging

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

if __name__ == '__main__':
    #logger = createLogger("myFirstTask.log")
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    logTextBox = QPlainTextEditLogger(ui)
    logTextBox.setFormatter(logging.Formatter('%(funcName)-12s: %(levelname)-8s %(message)s'))
    logging.getLogger().addHandler(logTextBox)
    # You can control the logging level
    logging.getLogger().setLevel(logging.DEBUG)
    
    logging.info('Here we are')
    logging.error('Oops')
    
    ui.BT_openHomeScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(0))
    ui.BT_openSonosScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(1))
    ui.BT_openWeatherScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(2))
    ui.BT_openLogScreen.clicked.connect(lambda: ui.ST_workerStack.setCurrentIndex(3))
    MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    MainWindow.show()
    sys.exit(app.exec_())