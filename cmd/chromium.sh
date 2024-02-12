#!/bin/bash

export DISPLAY=:1
/usr/bin/screen -S chromium -d -m /usr/bin/chromium "https://meet.google.com" --profile-directory="Adrien Schaller"
