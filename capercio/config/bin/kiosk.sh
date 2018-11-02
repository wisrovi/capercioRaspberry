#!/bin/bash
export DISPLAY=:0.0
xset s off
xset -dpms
xset s noblank
#chromium-browser --noerrdialogs --disable-session-crashed-bubble --disable-infobars --kiosk --incognito https://paul.fcv.org:8443/capercio/
cd /home/pi/capercio

sleep 5

#descargar imagen fondo
nohup python3 descargarImagen.py &

sleep 5

#abrir servidor POST para PI
nohup python3 servidorPI.py &

sleep 5

#abrir aplicacion nativa de python
nohup python3 index.py &
