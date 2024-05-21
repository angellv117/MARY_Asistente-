import webbrowser
import os
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import tkinter as tk
from google_trans_new import google_translator


import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QDialog
from PySide2.QtCore import QFile
from PyQt5 import QtCore, QtGui, QtWidgets

engine = pyttsx3.init()

#-----------------FUNCION PARA REPRODUCIR---------------#
def reproducir(self):
    text = self
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

#----------------------- TRADUCTOR --------------------#

def traductor(text):
    traductor = google_translator()
    text = traductor.translate(text, lang_tgt="es")
    reproducir(text)



#------------------------ LINEA DE COMANDOS ------------------#
def comandos (text):
        #text = self
        if "YouTube" in text and "Abre" in text:
            text="abriendo YouTube"
            webbrowser.open('https://www.youtube.com/?hl=es-419&gl=MX')
            reproducir(text)
        elif "Adiós Mary" in text  in text:
            text="Adiós jefe"
            reproducir(text)
        elif "Hola" in text :
            text="Hola jefe"
            reproducir(text)
        elif "archivos" in text and "Abre" in text :
            os.system('explorer')
            text="Abriendo explorador de archivos"
            reproducir(text)
        elif "correo" in text and "Abre" in text  :
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
            text="Abriendo Gmail"
            reproducir(text)
        elif "Facebook" in text and "Abre" in text or "facebook" in text or "face" in text :
            webbrowser.open('https://www.facebook.com')
            text="Abriendo Facebook"
            reproducir(text)
        elif "Instagram" in text in text or "intagram"in text or "insta" in text and "Abre" in text :
            webbrowser.open('https://www.instagram.com')
            text="Abriendo Instagram"
            reproducir(text)
        elif "el navegador" in text and "Abre" in text in text or "Google" in text or "Chrome" in text:
            webbrowser.open('https://www.google.com/webhp?hl=es&sa=X&ved=0ahUKEwjj19aYuczuAhUJ26wKHTWaDHcQPAgI')
            text="Abriendo google"
            reproducir(text)
        elif "WhatsApp" in text and "Abre" in text or "abre" in text:
            webbrowser.open('https://web.whatsapp.com/')
            text="abriendo WhatsApp"
            reproducir(text)
        elif "la" in text and "fecha" in text :
            now = datetime.now()
            fecha=now.date()
            text=fecha
            reproducir(text)
        elif "Reproduce" in text :
            cancion = text.replace('Reproduce','')
            reproducir('reproduciendo '+ cancion)
            pywhatkit.playonyt(cancion)
        elif "Quién es" in  text  or "Quién fue" in  text or "quién es" in  text  or "quién fue" in  text:
            busqueda = text.replace('quién fue' or 'Quién fue','')
            info = wikipedia.summary(busqueda,1 )
            traductor(info)
        elif "Qué es" in  text  or "qué es" in  text:
            busqueda = text.replace('Qué es' or 'qué es','')
            info = wikipedia.summary(busqueda,1 )
            traductor(info)
        elif "broma" in  text or "chiste" in text:
            reproducir(pyjokes.get_joke('es'))
        else:
            reproducir('Lo siento, aun no tengo ese comando')


bien=('hola jefe, bienvenido de nuevo')
reproducir (bien)

#------------------------ VENTANA DE INTERFAS -------------------------#
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(200, 400)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Escuchando = QtWidgets.QLabel(self.centralwidget)
        self.Escuchando.setGeometry(QtCore.QRect(70, 330, 81, 31))
        self.Escuchando.setText("")
        self.Escuchando.setObjectName("Escuchando")
        self.Bmary = QtWidgets.QPushButton(self.centralwidget)
        self.Bmary.clicked.connect(self.microfono)
        self.Bmary.setGeometry(QtCore.QRect(60, 310, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        self.Bmary.setFont(font)
        self.Bmary.setObjectName("Bmary")
        self.imagen = QtWidgets.QLabel(self.centralwidget)
        self.imagen.setGeometry(QtCore.QRect(-120, -40, 321, 341))
        self.imagen.setObjectName("imagen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "M*A*R*Y"))
        self.Bmary.setText(_translate("MainWindow", "Iniciar"))
        self.imagen.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/cct/Cortana2557.png\"/></p></body></html>"))


    def microfono(self):
        r = sr.Recognizer()
        palabra=""
        with sr.Microphone() as micro:
            print('Escuchando ... ')
            audio = r.listen(micro)
            try:
                text = r.recognize_google(audio, language="es_ES")
                palabra=text
                print('Dijiste: {}'.format(text))
                comandos(text)

            except:
                text='Lo siento no pude escucharte'
                reproducir(text)


import holograma


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
