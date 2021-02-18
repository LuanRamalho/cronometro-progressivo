# -*- coding: utf-8 -*-
from tkinter import Tk,Label,Button,Frame
 
proceso=0
 
def iniciar(h=0, m=0, s=0, ms=0):
    global proceso
 
    #Verificamos si los segundos y los minutos son mayores a 60
    #Verificamos si las horas son mayores a 24
    if ms>=1000:
        ms=0
        s=s+1
        if s >= 60:
            s=0
            m=m+1
            if m >= 60:
                m=0
                h=h+1
                if h >= 24:
                    h=0
 
    #etiqueta que muestra el cronometro en pantalla
    time['text'] = str(h)+":"+str(m)+":"+str(s)+":"+str(ms)
 
    # iniciamos la cuenta progresiva de los segundos
    proceso=time.after(1, iniciar, (h), (m), (s),(ms+1))
 
def parar():
    global proceso
    time.after_cancel(proceso)
 
root = Tk()
root.title('Cronômetro')
 
time = Label(root, fg='red', width=20, font=("","18"))
time.pack()
 
# si queremos que se autoejecuta al iniciar el programa hay que desomentar
# esta linea y comentar los botones
#iniciar()
 
# Generamos un frame para poner los botones de iniciar y parar
frame=Frame(root)
btnIniciar=Button(frame, fg='blue', text='Iniciar', command=iniciar)
btnIniciar.grid(row=1, column=1)
btnParar=Button(frame, fg='blue', text='Parar', command=parar)
btnParar.grid(row=1, column=2)
frame.pack()
 
root.mainloop()