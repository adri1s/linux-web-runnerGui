#!/bin/bash

export DISPLAY=:1.0
/usr/bin/screen -S joplin -d -m /usr/bin/flatpak run net.cozic.joplin_desktop 
