from Tkinter import Frame, BOTH, Button, Menu, Label, Scale
import tkFileDialog

import pyaudio
import struct
import threading
import wave


class Window(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.parent.title("Proyecto PyGame")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        self.value_str = ''
        self.audio = pyaudio.PyAudio()
        self.bandsArray = []
        self.filename1 = ''
        self.filename2 = ''
        self.filename3 = ''
        self.filename4 = ''
        self.waveArray = []

        self.datos_archivo1 = []
        self.datos_archivo2 = []
        self.datos_archivo3 = []
        self.datos_archivo4 = []


        # creating a menu instance
        menu = Menu(self.parent)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)



        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        file.add_command(label="Exit", command=self.QuitAction)



        self.slider_track1 = Scale(self, from_=0, to=-100)
        self.slider_track1.place(x = 10, y =80)

        button_opentrack1 = Button(self, text="Open", command=self.askopenfilename1)
        button_opentrack1.place(x=25, y=50)

        self.slider_track2 = Scale(self, from_=0, to=-100)
        self.slider_track2.place(x=90, y=80)

        button_opentrack2 = Button(self, text="Open", command=self.askopenfilename2)
        button_opentrack2.place(x=105, y=50)

        self.slider_track3 = Scale(self, from_=0, to=-100)
        self.slider_track3.place(x=170, y=80)

        button_opentrack3 = Button(self, text="Open", command=self.askopenfilename3)
        button_opentrack3.place(x=185, y=50)

        self.slider_track4 = Scale(self, from_=0, to=-100)
        self.slider_track4.place(x=260, y=80)

        button_opentrack4 = Button(self, text="Open", command=self.askopenfilename4)
        button_opentrack4.place(x=275, y=50)

        button_save = Button(self, text="Export", command=self.press_button_export)
        button_save.place(x=240, y=0)

        quitButton = Button(self, text="Quit",
                            command=self.QuitAction)
        quitButton.place(x=325, y=0)


        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.wav'
        options['filetypes'] = [('all files', '.*'), ('wav files', '.wav')]
        options['initialdir'] = 'C:\\'

        # define options for opening or saving a file
        self.file_opt1 = options = {}
        options['defaultextension'] = '.wav'
        options['filetypes'] = [('all files', '.*'), ('wav files', '.wav')]
        options['initialdir'] = 'C:\\'





    #To open and analize images
    def showImg(self):
        load = Image.open(self.filename)




    #to center the window
    def centerWindow(self):
        w = 410
        h = 200

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


    #To Quit the app and Turn off sound in puredata
    def QuitAction(self):
        self.parent.quit()




    #To open an image and process it
    def askopenfilename1(self):
        # getting the filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)
        self.filename1 = filename
        self.datosarchivo1 = self.abrirarchivo1()

    def abrirarchivo1(self):
        archivo1 = wave.open(self.filename1, 'r')
        nivel1=self.slider_track1.get()
        amplitud1=32678.0*(10**(float(nivel1)/20))
        cuadros1 = archivo1.getnframes()
        canales1=archivo1.getnchannels()
        muestreo1=archivo1.getframerate()
        datos1= archivo1.readframes(cuadros1)

        #completar codigo

        wavearray1 = []
        for i in range(0,len(datos1),2):
            datoNum1=datos1[i]+datos1[i+1]
            dato1=struct.unpack('<h',datoNum1)
            wavearray1.append((dato1[0]/32678.0)*amplitud1)
        return wavearray1

    def askopenfilename2(self):
        # getting the filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)
        self.filename2 = filename
        self.datosarchivo2 = self.abrirarchivo2()

    def abrirarchivo2(self):
        archivo2 = wave.open(self.filename2, 'r')
        nivel2=self.slider_track2.get()
        amplitud2=32678.0*(10**(float(nivel2)/20))
        cuadros2 = archivo2.getnframes()
        canales2=archivo2.getnchannels()
        muestreo2=archivo2.getframerate()
        datos2= archivo2.readframes(cuadros2)


        # completar codigo

        wavearray2 = []
        for i in range(0,len(datos2),2):
            datoNum2=datos2[i]+datos2[i+1]
            dato2=struct.unpack('<h',datoNum2)
            wavearray2.append((dato2[0]/32678.0)*amplitud2)
        return wavearray2

    def askopenfilename3(self):
        # getting the filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)
        self.filename3 = filename
        self.datosarchivo3 = self.abrirarchivo3()

    def abrirarchivo3(self):
        archivo3 = wave.open(self.filename3, 'r')
        nivel3=self.slider_track3.get()
        amplitud3=32678.0*(10**(float(nivel3)/20))
        cuadros3 = archivo3.getnframes()
        canales3=archivo3.getnchannels()
        muestreo3=archivo3.getframerate()
        datos3=archivo3.readframes(cuadros3)



        # completar codigo

        wavearray3 = []
        for i in range(0,len(datos3),2):
            datoNum3=datos3[i]+datos3[i+1]
            dato3=struct.unpack('<h',datoNum3)
            wavearray3.append((dato3[0]/32678.0)*amplitud3)
        return wavearray3

    def askopenfilename4(self):
        # getting the filename
        filename = tkFileDialog.askopenfilename(**self.file_opt)
        self.filename4 = filename
        self.datosarchivo4 = self.abrirarchivo4()

    def abrirarchivo4(self):
        archivo4 = wave.open(self.filename4, 'r')
        nivel4=self.slider_track3.get()
        amplitud4=32678.0*(10**(float(nivel4)/20))
        cuadros4 = archivo4.getnframes()
        canales4=archivo4.getnchannels()
        muestreo4=archivo4.getframerate()

        datos4=archivo4.readframes(cuadros4)



        # completar codigo

        wavearray4 = []
        for i in range(0,len(datos4),2):
            datoNum4=datos4[i]+datos4[i+1]
            dato4=struct.unpack('<h',datoNum4)
            wavearray4.append((dato4[0]/32678.0)*amplitud4)
        return wavearray4


    def press_button_export(self):

        nivel1 =  self.slider_track1.get()
        nivel2 =  self.slider_track2.get()
        nivel3 =  self.slider_track3.get()
        nivel4 =  self.slider_track4.get()

        sum1=[]


        if len(self.datosarchivo1)>len(self.datosarchivo2):
         for i in range (len(self.datosarchivo2),len(self.datosarchivo1)):
            self.datosarchivo2.append(0)

         for i in range(len(self.datosarchivo1)):
            x=self.datosarchivo1[i]+self.datosarchivo2[i]
            sum1.append(x)

        if len(self.datosarchivo2)>len(self.datosarchivo1):
            for i in range (len(self.datosarchivo1),len(self.datosarchivo2)):
                self.datosarchivo1.append(0)

            for i in range(len(self.datosarchivo2)):
                x=self.datosarchivo2[i]+ self.datosarchivo1[i]
                sum1.append(x)
        sum2=[]
        if len(self.datosarchivo3)>len(self.datosarchivo4):
         for i in range (len(self.datosarchivo4),len(self.datosarchivo3)):
            self.datosarchivo4.append(0)

         for i in range(len(self.datosarchivo3)):
            x=self.datosarchivo3[i]+self.datosarchivo4[i]
            sum2.append(x)

        if len(self.datosarchivo4)>len(self.datosarchivo3):
            for i in range (len(self.datosarchivo3),len(self.datosarchivo4)):
                self.datosarchivo3.append(0)

            for i in range(len(self.datosarchivo4)):
                x=self.datosarchivo4[i]+ self.datosarchivo3[i]
                sum2.append(x)


        print nivel1, nivel2, nivel3, nivel4

        val=max(abs(i)for i in (sum1))
        #Completar Codigo


        filename = tkFileDialog.asksaveasfilename(**self.file_opt1)

        file = wave.open(filename, 'w')
        file.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
        a=[]
        for i in range(len(sum1)):
             x=(sum1[i]/val)*(32767)
             a.append(x)
        val2=max(abs(i)for i in (sum2))
        b=[]
        for i in range(len(sum2)):
            x=(sum2[i]/val2)*(32767)
            b.append(x)

        for i in range(len(sum1)) :
            try:
                file.writeframes(struct.pack("<h",int(a[i])))
                file.writeframes(struct.pack("<h",int(b[i])))
            except:IndexError


        file.close()


        # completar codigo







