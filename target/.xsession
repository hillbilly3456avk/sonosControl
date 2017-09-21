#!/bin/bash
#/usr/bin/python3 /home/pi/sonosControl/SonosController.py&
#exec matchbox-window-manager -use_titlebar no
#xset s noblank
#matchbox-window-manager -use_titlebar no&
exec openbox-session&
while true; do
    /usr/bin/python3 /home/pi/sonosControl/SonosController.py
    sleep 1
done
