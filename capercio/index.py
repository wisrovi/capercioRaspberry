from properties import *
from indexM import *   #modelo
from indexCV import *   #vista y controlador


def procesoReconocimiento():
    proceso = 0
    persona = ""
    for x in range(propiedades.numberSendPhotosToIA):
        ruta, hayRostro = buscarRostro(True)
        if hayRostro == True :
            respuestaPost = enviarImagenPost(urlDestino = "https://paul.fcv.org:8443/capercio/Servlet", rutaImagen = ruta)
            if respuestaPost == "0":
                print("Usuario Desconocido - intento reconocimiento: " + str(x))
            else:
                if respuestaPost[:1] == "N":
                    proceso = 1
                    persona = respuestaPost[1:]
                    print("El usuario %s no tiene opciones para calificar." %(persona))
                elif respuestaPost == "-":
                    print("No se pudo enviar la foto a la IA")
                else:
                    print("abriendo ventana a usuario conocido...")
                    os.system("sh ejecutarNavegador.sh "+respuestaPost)
                break
        else:
            x = x + 2
    if proceso == 1:        
        utilidades.mensajeAutoDestroid("Notificación %s: El usuario no tiene opciones para calificar." %(persona))
    if proceso == 0:
        utilidades.mensajeAutoDestroid(texto="Notificación 0: El usuario no tiene opciones para calificar.")

#funcion boton
def reconocerPersona():
    utilidades.progressbarAutoDestroid("Cargando...", 30000)
    Thread(target=procesoReconocimiento).start()

class MyApp:
    def __init__(self, parent):
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        d = MyDialog(raiz)
        self.parent.wait_window(d.top)

if __name__ == "__main__":
    raiz = Tk()#inicializo la raiz
    app = MyApp(raiz)    
    propiedades = properties()

    raiz.title(propiedades.tituloVentana)
    raiz.resizable(propiedades.usuarioModificaAnchoVentana,propiedades.usuarioModificaAltoVentana) 
    raiz.geometry(propiedades.anchoVentana + "x" + propiedades.altoVentana)
    raiz.config(background=propiedades.colorFondo)
    if propiedades.activarFullScreen == True:
        raiz.attributes('-fullscreen', True) #maximizar ventana
    centrarVentana(raiz)
    utilidades = util(raiz)
        
        #creo el Frame
    miFrame = Frame() #inicializo el Frame
    miFrame.config(width = propiedades.anchoVentana, height = propiedades.altoVentana)
    miFrame.config(background = propiedades.colorFondo)
    miFrame.config(cursor="hand2")
    miFrame.pack(fill = "both", expand = "True") #empaqueto el Frame en la raiz

    miBoton = Button(miFrame, text = "Error al cargar la imagen." , command=reconocerPersona)
    miBoton.config(width = propiedades.anchoVentana, height = propiedades.altoVentana)
    
    
    if os.path.exists(propiedades.imagenFondo):    
        imagenFondo = PhotoImage(file=propiedades.imagenFondo) #https://convertio.co/es/jpg-ppm/
        miBoton.config(image = imagenFondo, relief=FLAT)
        miBoton.config(background = propiedades.colorFondo)
        miBoton.pack()
    else:
        ReiniciarSistema(raiz)
    
    miBoton.pack()
        
    #lanzo la raiz
    raiz.mainloop()


    
    
    

