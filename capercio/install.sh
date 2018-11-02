sudo apt  --purge remove -y scratch*
sudo apt  --purge remove -y minecraft-pi
sudo apt-get --purge remove -y geany
sudo apt-get --purge remove -y sonic-pi
sudo apt-get --purge remove -y python2*
sudo apt-get --purge remove -y libreoffice*
sudo apt-get remove --purge -y bluej
sudo apt-get remove --purge -y dillo
sudo apt-get remove --purge -y epiphany*
sudo apt-get remove --purge -y netsurf-gtk

sudo apt-get -y clean
sudo apt-get -y autoremove
sudo apt-get -y update
sudo apt-get -y upgrade

sleep 10

sudo apt-get install -y libjpeg-dev 
sudo apt-get install -y libtiff5-dev 
sudo apt-get install -y libjasper-dev 
sudo apt-get install -y libpng12-dev
sudo apt-get install -y libavcodec-dev 
sudo apt-get install -y libavformat-dev 
sudo apt-get install -y libswscale-dev 
sudo apt-get install -y libv4l-dev
sudo apt-get install -y libxvidcore-dev 
sudo apt-get install -y libx264-dev
sudo apt-get install -y qt4-dev-tools


sleep 5

sudo apt install -y libqt4-test
sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y build-essential 

sleep 5

sudo apt-get install -y build-essential cmake
sudo apt-get install -y libopenblas-dev liblapack-dev 
sudo apt-get install -y libx11-dev libgtk-3-dev
sudo apt-get install -y python3 python3-dev python3-pip

sudo apt-get install -y libhdf5-dev
sudo apt-get install -y libhdf5-serial-dev

pip3 install opencv-python
pip3 install opencv-contrib-python
pip3 install request
pip3 install numpy

sleep 5

echo cargando configuracion en el root
sudo cp /home/pi/capercio/config/config.txt /boot/config.txt

echo cargando binarios
sudo cp -r /home/pi/capercio/config/bin /home/pi/bin/

echo cargando autoarranque
mkdir -p /home/pi/.config/autostart/
cd config/autostart/
sudo cp kiosk.desktop /home/pi/.config/autostart/kiosk.desktop
cd ..
cd ..

cd /home/pi/capercio/
sudo cp config/splash.png /usr/share/plymouth/themes/pix/splash.png

echo colocando imagen de fondo en la carpeta de fondos de escritorio
cd /home/pi/capercio/
chmod +x config/capercioWallpaper.jpg
sudo cp config/capercioWallpaper.jpg /usr/share/rpd-wallpaper/capercioWallPaper.jpg

echo quitando el icono en el arranque de dispositivo
sudo cp /home/pi/capercio/config/cmdline.txt /boot/cmdline.txt

