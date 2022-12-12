from PyQt5 import QtWidgets, uic, QtCore, QtGui
import time
from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
import pyttsx3


app = QtWidgets.QApplication([])

# carga archivos
principal = uic.loadUi(
    'D:\\Ariff\\Documentos\\Visual Codex\\Proyecto uni\\proyecto lenguaje expresivo\\ventanas\\mainventana.ui')
acerca = uic.loadUi(
    'D:\\Ariff\\Documentos\\Visual Codex\\Proyecto uni\\proyecto lenguaje expresivo\\ventanas\\acercaventana.ui')
sw = uic.loadUi(
    'D:\\Ariff\\Documentos\\Visual Codex\\Proyecto uni\\proyecto lenguaje expresivo\\ventanas\\primero.ui')
sw2 = uic.loadUi(
    'D:\\Ariff\\Documentos\\Visual Codex\\Proyecto uni\\proyecto lenguaje expresivo\\ventanas\\segundo.ui')
calif = uic.loadUi(
    'D:\\Ariff\\Documentos\\Visual Codex\\Proyecto uni\\proyecto lenguaje expresivo\\ventanas\\calificar.ui')
explica = uic.loadUi(
    'D:\\Ariff\\Documentos\\Visual Codex\\Proyecto uni\\proyecto lenguaje expresivo\\ventanas\\explicacionLEventana.ui')
instrucc = uic.loadUi(
    'D:\\Ariff\\Documentos\\Visual Codex\\Proyecto uni\\proyecto lenguaje expresivo\\ventanas\\instruccionesventana.ui')
califhome = uic.loadUi(
    'D:\\Ariff\\Documentos\\Visual Codex\\Proyecto uni\\proyecto lenguaje expresivo\\ventanas\\calificar2.ui')


# ACCIONES
class Soft():
    def MostrarAcercapp():
        principal.hide()
        acerca.show()

    def Salir():
        app.exit()

    def Entrar():
        principal.hide()
        explica.show()

    def BackInico():
        acerca.hide()
        explica.hide()
        instrucc.hide()
        principal.show()

    def avanzarinst():
        explica.hide()
        instrucc.show()

    def iniciosw():
        instrucc.hide()
        sw.texto1.setText("Amarte a ti es lo más hermoso que me pudo suceder \n tenerte a mi lado es algo que no puedo entender\n solía pensar que la vida no me iba a dar más\n pero no fue así pues aquí estas.\n Amarte a ti es transformar mi mundo\n porque cada día que pasa, todo se vuelve absurdo\n eres mi razón de vivir y mi sentir\n al tenerte a mi lado mi mundo está iluminado\n por eso te pido, jamás te alejes de mi lado.")
        sw.show()

    def segundsw():
        calif.hide()
        sw2.texto1.setText(
            "Este lunes debemos de entregar la tarea de toda la semana.....\n ¿¡Alguien tiene mi cuaderno de notas!? \n¡¿qué pasó con mi cuaderno?!, tiene que aparecer antes de que me vaya a la escuela.")
        sw2.show()


class Audiosw():

    def reproducetuaudio():
        audio2 = AudioSegment.from_wav(
            'D:\Ariff\Documentos\Visual Codex\GrabacionUsuario.wav')
        play(audio2)

    def home():
        califhome.hide()
        principal.show()

    def PlayAudio1():
        audio1 = AudioSegment.from_wav(
            'D:/Ariff/Documentos/Visual Codex/Proyecto uni/proyecto lenguaje expresivo/AudiosBuenos/primeralectura.wav')
        play(audio1)

    def PlayAudio2():
        audio = AudioSegment.from_wav(
            'D:/Ariff/Documentos/Visual Codex/Proyecto uni/proyecto lenguaje expresivo/AudiosBuenos/segundalectura.wav')
        play(audio)

    def Escuchar():
        engine = pyttsx3.init()
        voice_id = 'mbrola-es1'
        engine.setProperty("voice", voice_id)

        escucha = sr.Recognizer()

        def talk(text):
            engine.say(text)
            engine.runAndWait()

        def hablar():
            with sr.Microphone() as source:
                talk("Te escucho")
                audio = escucha.listen(source)
                with open('GrabacionUsuario.wav', "wb") as fichero:
                    fichero.write(audio.get_wav_data())

            talk("Grabación finalizada")
        hablar()

    def calf():
        sw.hide()
        sw2.hide()

        import wave
        import contextlib
        import librosa

        audio = 'D:/Ariff/Documentos/Visual Codex/GrabacionUsuario.wav'
        with contextlib.closing(wave.open(audio, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / (rate)
        print('Duracion de la primera grabacion {}'.format(duration))

        y, sr = librosa.load(audio)
        seccionesconsonido = librosa.effects.split(
            y, frame_length=8000, top_db=30)
        print(seccionesconsonido)
        print('---------------------------------------------------------------------')
        lista = seccionesconsonido.tolist()

        # Duracion del audio
        if duration >= 30 and duration <= 33:
            icalificacion = 5
            print('Optuviste 5')

        elif duration >= 20 and duration <= 30:
            icalificacion = 3
            print('Optuviste 3')
        else:
            icalificacion = 0
            print('Optuviste 0')

        # Espacios
        if len(lista) == 9:
            icalificacion2 = 5
            print('Optuviste 5')
        elif len(lista) >= 6 and len(lista) <= 8:
            icalificacion2 = 3
            print('Optuviste 3')
        else:
            icalificacion2 = 0
            print('Optuviste 0')

        califinal = icalificacion+icalificacion2
        print('Optuviste en la suma: {}'.format(califinal))

        if califinal == 10:
            calif.calificacion.setText('10')
            calif.labeltxtoleer_3.setText(
                '\nPerfecto, Felicidades!! sigue practicando:)')
        elif califinal == 8:
            calif.calificacion.setText('8')
            calif.labeltxtoleer_3.setText(
                '\nTu lectura es buena,\n pero necesitas mejorar el tiempo empleado en la misma.\nProcura marcar los tiempo necesarios, pero no excederte, \nmantén la entonación en toda la lectura y no por partes')
        elif califinal == 5:
            calif.calificacion.setText('5')
            calif.labeltxtoleer_3.setText(
                '\nRegular el volumen ajustándolo al tipo de texto.\nLeer con seguridad, sin vacilaciones, evitando volver atrás.\nEntonar adecuadamente las palabras, marcando las sílabas tónicas.')
        elif califinal == 6:
            calif.calificacion.setText('6')
            calif.labeltxtoleer_3.setText(
                'Respetar la mayor o menor duración de las pausas indicada por los signos de puntuación.\nPoner énfasis en los momentos o palabras claves evitando la monotonía en el tono.\nModular la voz; tratar de expresar con ella los sentimientos y las actitudes del escritor.')
        elif califinal == 3:
            calif.calificacion.setText('3')
            calif.labeltxtoleer_3.setText(
                '\nLeer adecuadamente frases y párrafos con su correspondiente entonación enunciativa, \ninterrogativa, imperativa, dubitativa, irónica.')
        else:
            calif.calificacion.setText('0')
            calif.labeltxtoleer_3.setText(
                '\nSe aprende más de los errores que de los acierto, \ntrata de seguir estos pasos: \nLee cuidadosamente todos las palabras.\nTrata de hacer pausas en los puntos, comas y saltos de linea cuando sea necesario')

        calif.show()

    def calf2():
        sw2.hide()
        import wave
        import librosa
        import contextlib

        audio = 'D:/Ariff/Documentos/Visual Codex/GrabacionUsuario.wav'
        with contextlib.closing(wave.open(audio, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / (rate)

        print('Duracion de la primera grabacion{}'.format(duration))

        y, sr = librosa.load(audio)
        seccionesconsonido = librosa.effects.split(
            y, frame_length=2000, top_db=35)

        print('---------------------------------------------------------------------')
        print(seccionesconsonido)
        lista = seccionesconsonido.tolist()

        # Duracion del audio
        if duration >= 10 and duration <= 13:
            icalificacion = 5
            print('Obtuviste 5')

        elif duration >= 7 and duration <= 10:
            icalificacion = 3
            print('Obtuviste 3')
        else:
            icalificacion = 0
            print('Obtuviste 0')

        # Espacios
        if len(lista) >= 3 and len(lista) <= 5:
            icalificacion2 = 5
            print('Obtuviste 5')
        elif len(lista) == 2:
            icalificacion2 = 3
            print('Obtuviste 3')
        else:
            icalificacion2 = 0
            print('Obtuviste 0')

        califinal = icalificacion+icalificacion2
        print('Obtuviste final {}'.format(califinal))

        if califinal == 10:
            califhome.calificacion.setText('10')
            califhome.labeltxtoleer_3.setText(
                '\nPerfecto, Felicidades!! sigue practicando:)')
        elif califinal == 8:
            califhome.calificacion.setText('8')
            califhome.labeltxtoleer_3.setText(
                '\nTu lectura es buena,\n pero necesitas mejorar el tiempo empleado en la misma.\nProcura marcar los tiempo necesarios, pero no excederte, \nmantén la entonación en toda la lectura y no por partes')
        elif califinal == 5:
            califhome.calificacion.setText('5')
            califhome.labeltxtoleer_3.setText(
                '\nRegular el volumen ajustándolo al tipo de texto.\nLeer con seguridad, sin vacilaciones, evitando volver atrás.\nEntonar adecuadamente las palabras, marcando las sílabas tónicas.')
        elif califinal == 6:
            califhome.calificacion.setText('6')
            califhome.labeltxtoleer_3.setText(
                '\nRespetar la mayor o menor duración de las pausas indicada por los signos de puntuación.\nPoner énfasis en los momentos o palabras claves evitando la monotonía en el tono.\nModular la voz; tratar de expresar con ella los sentimientos y las actitudes del escritor.')
        elif califinal == 3:
            califhome.calificacion.setText('3')
            califhome.labeltxtoleer_3.setText(
                '\nLeer adecuadamente frases y párrafos con su correspondiente entonación enunciativa, \ninterrogativa, imperativa, dubitativa, irónica.')
        else:
            califhome.calificacion.setText('0')
            califhome.labeltxtoleer_3.setText(
                '\nSe aprende más de los errores que de los acierto, \ntrata de seguir estos pasos: \nLee cuidadosamente todos las palabras.\nTrata de hacer pausas en los puntos, comas y saltos de linea cuando sea necesario')

        califhome.show()

    def back():
        calif.hide()
        principal.show()


######################### botones####################################
# VENTANA PRINCIPAL O MAIN
principal.actionAcerca_de_la_app.triggered.connect(Soft.MostrarAcercapp)
principal.actionSalir.triggered.connect(Soft.Salir)
principal.boton.clicked.connect(Soft.Entrar)

# VENTANA ACERCA DE LA APP
acerca.actionSalir.triggered.connect(Soft.Salir)
acerca.back.triggered.connect(Soft.BackInico)

# VENTANA EXPLICACION
explica.back.triggered.connect(Soft.BackInico)
explica.btncontinuar.clicked.connect(Soft.avanzarinst)
explica.actionSalir.triggered.connect(Soft.Salir)

# VENTANA INSTRUCCION
instrucc.back.triggered.connect(Soft.BackInico)
instrucc.actionSalir.triggered.connect(Soft.Salir)
instrucc.btnempezarsw.clicked.connect(Soft.iniciosw)
#################################################################

#######################CALIFICA######################
sw.btncalificar.clicked.connect(Audiosw.calf)
# botones reproducir
sw.botonplay.clicked.connect(Audiosw.PlayAudio1)
sw.botonescuchar_3.clicked.connect(Audiosw.Escuchar)
sw.botonescuchatuaudio.clicked.connect(Audiosw.reproducetuaudio)
# calif
calif.btnregresar.clicked.connect(Audiosw.back)
calif.btnsiguiente.clicked.connect(Soft.segundsw)
########################################################
# botones reproducir
sw2.botonplay.clicked.connect(Audiosw.PlayAudio2)
sw2.botonescuchar_3.clicked.connect(Audiosw.Escuchar)
sw2.btncalificar.clicked.connect(Audiosw.calf2)
sw2.botonescuchatuaudio2.clicked.connect(Audiosw.reproducetuaudio)
califhome.btnregresarhome.clicked.connect(Audiosw.home)
##################################################################


# Ejecutable
principal.show()
app.exec()
