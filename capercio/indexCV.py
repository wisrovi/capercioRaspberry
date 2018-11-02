
############################ tkinter ######################################
                                                                          #
try:                                                                      #
    from tkinter import *                                                 #
except ImportError:                                                       #
    print("Se requiere el modulo tkinter *")                              #
                                                                          #    
try:                                                                      #
    from tkinter.ttk import Progressbar                                   #
except ImportError:                                                       #
    print("Se requiere el modulo tkinter - Progressbar")                  #
                                                                          #
try:                                                                      #
    from tkinter import ttk                                               #
except ImportError:                                                       #
    print("Se requiere el modulo tkinter - ttk")                          #
                                                                          #
###########################################################################





############################ Libraries ####################################
try:                                                                      #    
    import os.path                                                        #
except ImportError:                                                       #
    print("Error importar os.path")                                       #
                                                                          #
try:                                                                      #
    from threading import Thread                                          #
except ImportError:                                                       #
    print("Se requiere el modulo threading")                              #
                                                                          #
try:                                                                      #
    import time                                                           #
except ImportError:                                                       #
    print("Se requiere el modulo time")                                   #
                                                                          #
###########################################################################



############################### centrar ventana #################################################################
                                                                                                                #
# https://stackoverflow.com/questions/36050192/how-to-position-toplevel-widget-relative-to-root-window          #                                                               
class centrarVentana:                                                                                           #
    def __init__(self, parent):                                                                                 #
        self.parent = parent                                                                                    #
        self.parent.update_idletasks()                                                                          #
        w = self.parent.winfo_screenwidth()                                                                     #
        h = self.parent.winfo_screenheight()                                                                    #
        size = tuple(int(_) for _ in self.parent.geometry().split('+')[0].split('x'))                           #
        x = w / 2 - size[0] / 2                                                                                 #
        y = h / 2 - size[1] / 2                                                                                 #
        self.parent.geometry("%dx%d+%d+%d" % (size + (x, y)))                                                   #
                                                                                                                #
#################################################################################################################        







################################################# utilidades ##################################################
                                                                                                              #
class util:                                                                                                   #
    def __init__(self, parent):                                                                               #
        self.parent = parent                                                                                  #
                                                                                                              #
    def mensajeAutoDestroid(self, texto="Probando..."):                                                       #
        self.top = Toplevel()                                                                                 #
        self.top.title('Capercio')                                                                            #
        self.top.geometry("650" + "x" + "50")                                                                 #
        Message(self.top, text=texto, padx=20, pady=20, font=("Helvetica", 16), width=600).pack()             #
        centrarVentana(self.top)                                                                              #
        self.top.after(3000, self.top.destroy)                                                                #
                                                                                                              #
    def progressbarAutoDestroid(self, texto="Probando...", tiempo=10000):                                     #
        self.topProgressbar = Toplevel()                                                                      #
        self.topProgressbar.title('Capercio')                                                                 #
        # top.wm_attributes('-alpha', 0.3)                                                                    #
        self.topProgressbar.geometry("620" + "x" + "50")                                                      #
        pbar_ind = ttk.Progressbar(self.topProgressbar, orient="horizontal", length=620, mode="indeterminate")#
        pbar_ind.grid(row=1, column=0, pady=2, padx=2, sticky=E + W + N + S)                                  #
        pbar_ind.start()                                                                                      #
        Label(self.topProgressbar, text=texto, font="Helvetica 16 bold italic").grid(row=0, column=0)         #
        centrarVentana(self.topProgressbar)                                                                   #
        self.topProgressbar.after(tiempo, self.topProgressbar.destroy)                                        #    
                                                                                                              #                                                                                                             #
###############################################################################################################


class ReiniciarSistema:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.parent = parent
        self.top.title("Reiniciar")
        Label(self.top, text="No se encontró la imagen en el servidor para cargar en la aplicación,\npor favor reinicie el dispositivo para actualizar.", font = "Helvetica 12 italic").grid(row=0, column=0, columnspan=2)
        Label(self.top, text="¿Desea Reiniciar?", font = "Helvetica 12").grid(row=1, column=0, columnspan=2)
        self.button1 = Button(self.top, text="Si, Reiniciar el dispositivo.", font = "Helvetica 12 bold", command=self.reiniciar)
        self.button2 = Button(self.top, text="No, solo minimizar.", font = "Helvetica 12 bold", command=self.minimizar)
        self.button1.grid(row=2, column=0, padx=5, pady=5)
        self.button2.grid(row=2, column=1, padx=5, pady=5)
        centrarVentana(self.top)
        
    def reiniciar(self):
        os.system("sudo reboot ")
        self.top.destroy()
        self.parent.destroy()
    
    def minimizar(self):
        self.top.destroy()
        self.parent.iconify()
        time.sleep(1)
        self.parent.deiconify()

class MyDialog:
    def __init__(self, parent):
        self.top = Toplevel(parent)
        self.parent = parent
        self.top.title("Salir")
        Label(self.top, text="¿Está seguro?", font = "Helvetica 12 bold").grid(row=0, column=0, columnspan=2)
        self.button1 = Button(self.top, text="Si, salir de la app.", font = "Helvetica 12 bold", command=self.salir)
        self.button2 = Button(self.top, text="No, solo minimizar.", font = "Helvetica 12 bold", command=self.minimizar)
        self.button1.grid(row=1, column=0, padx=5, pady=5)
        self.button2.grid(row=1, column=1, padx=5, pady=5)              
        centrarVentana(self.top)

    def salir(self):
        self.top.destroy()
        self.parent.destroy()

    def minimizar(self):
        self.top.destroy()
        self.parent.iconify()
        time.sleep(3)
        self.parent.deiconify()
