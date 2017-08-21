clean-pyc:
	del /s *.pyc

clean-build:

run host:
	python.exe SonosController.py --host --noSonos
	
run target:
	python34 SonosController.py

qt:
	python.exe -m PyQt5.uic.pyuic MainWindow_Host.ui -o MainWindow_Host.py
	python.exe -m PyQt5.uic.pyuic MainWindow_raspi.ui -o MainWindow_raspi.py
	pyrcc5 musicIcons.qrc -o musicIcons_rc.py