#openCV
import cv2
face_classifier = cv2.CascadeClassifier('detectors/haarcascade_frontalface_alt2.xml')

#pi camera
import picamera
import picamera.array
import numpy as np


#hacer post
import requests

#OS
import os
import webbrowser


#definiciones auxiliares
def rostroVacio():
    rostro = np.ones((96, 96 ,3), np.uint8) 

def ObtenerRostroImagen(imagen):    
    ImagenTonosGrises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    CoordenadaRostro = face_classifier.detectMultiScale(ImagenTonosGrises, 1.2, 2)

    rostro = rostroVacio()
    HayRostros = False
    for (x,y,w,h) in CoordenadaRostro:
        rostro = imagen[y:y+h,x:x+w]
        HayRostros = True
    return rostro, HayRostros

def enviarImagenPost(rutaImagen, urlDestino = "http://172.30.19.88:5001/"):
    respuestaPost = "-"
    with open(rutaImagen, 'rb') as archivoEnviar:
        archivoJson = {'file': archivoEnviar}
        certificadosServidor = "ca.crt"
        r = requests.post(urlDestino, files=archivoJson, verify=certificadosServidor) #http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification
        respuestaPost = r.text
        estadoRespuestaPost = r.status_code    
        razonConexion = r.reason
        if estadoRespuestaPost != 200:
            respuestaPost = "0"
        #print(estadoRespuestaPost, razonConexion)
        #print(respuestaPost)
    return respuestaPost     

def buscarRostro(prenderCamara = False):    
    with picamera.PiCamera() as camera:
        camera.led= prenderCamara
        #camera.brightness= 60
        with picamera.array.PiRGBArray(camera) as stream:
            camera.resolution = (1024, 768)
            rostroEncontrado = False
            ruta = "pictures/foto.jpeg"
            for x in range(10):
                camera.capture(stream, 'bgr', use_video_port=True)
                imagenCamara = stream.array
                rostro, HayRostros = ObtenerRostroImagen(imagenCamara)
                
                if HayRostros == True:
                    cv2.imwrite(ruta,rostro)
                    rostroEncontrado = True
                    break           
                stream.seek(0)
                stream.truncate()                
            return ruta, rostroEncontrado    


def AbrirURL(url):
    b = webbrowser.open(url, new=0, autoraise=True)
    if b == False:
        print("No se pudo abrir el navegador.")
    


