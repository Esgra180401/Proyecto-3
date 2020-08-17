#importar cosas
from tkinter import *
from tkinter import messagebox
import os
from time import strftime
import time
import pickle
import random
import os
import sys
import fpdf
from fpdf import FPDF
def VentanaPrincipal():
    #configuracion ventana principal
    Ventana_C=Tk()
    Ventana_C.geometry('800x750+450+50')
    Ventana_C.title('Futoshiki')
    Ventana_C.config(bg='beige')
    Ventana_C.resizable(width= False, height=False)
    #titulos
    Mensaje_titulo=Message(Ventana_C,text="FUTOSHIKI",width='300',font=("Comic Sans",20),bg="#C2D8FB",fg="black")
    Mensaje_titulo.place(x=300,y=50)
    Mensaje_nombre=Message(Ventana_C,text="Ingrese su nombre:",width='300',font=("Arial",15),bg='beige',fg="black")
    Mensaje_nombre.place(x=50,y=100)
    Mensaje_reloj=Message(Ventana_C,text="Opciones de reloj:",width='320',font=("Arial",16),bg='beige',fg="black")
    Mensaje_reloj.place(x=15,y=605)
    Mensaje_panel=Message(Ventana_C,text="Orientacion del panel de digitos:",width='320',font=("Arial",16),bg='beige',fg="black")
    Mensaje_panel.place(x=465,y=605)
    Mensaje_dificultad=Message(Ventana_C,text="Dicultad:",width='300',font=("Arial",20),bg='beige',fg="black")
    Mensaje_dificultad.place(x=300,y=150)
    #dato
    Nombre_text=StringVar()
    Nombre_widget=Entry(Ventana_C,width='50',textvariable=Nombre_text)
    Nombre_widget.place(x=250,y=110)
    #limita lo que se ingresa
    def max_name(Nombre_text):
        if len(Nombre_text.get()) > 0:
            Nombre_text.set(Nombre_text.get()[:20])

    Nombre_text.trace("w", lambda *args: max_name(Nombre_text))
    #reloj/temporizador
    var=IntVar()
    RadioButton1=Radiobutton(Ventana_C, text='Reloj',variable=var,value=1)
    RadioButton1.place(x=20,y=640)
    RadioButton2=Radiobutton(Ventana_C, text='Temporizador',variable=var,value=2)
    RadioButton2.place(x=20,y=660)
    RadioButton3=Radiobutton(Ventana_C, text='NO',variable=var,value=3)
    RadioButton3.place(x=20,y=680)
    #lado de los numeros
    var2=IntVar()
    RadioButton4=Radiobutton(Ventana_C, text='Izquierda',variable=var2,value=1)
    RadioButton4.place(x=700,y=640)
    RadioButton5=Radiobutton(Ventana_C, text='Derecha',variable=var2,value=2)
    RadioButton5.place(x=700,y=660)
    #dificultad
    var3=IntVar()
    RadioButton6=Radiobutton(Ventana_C, text='Facil',variable=var3,value=1)
    RadioButton6.place(x=310,y=190)
    RadioButton7=Radiobutton(Ventana_C, text='Intermedio',variable=var3,value=2)
    RadioButton7.place(x=310,y=210)
    RadioButton8=Radiobutton(Ventana_C, text='Dificil',variable=var3,value=3)
    RadioButton8.place(x=310,y=230)
    #archivo de juegos
    filesize=os.path.getsize("futoshiki2020partidas.dat")
    if filesize==0:
        listafacil=[(("2",0,0),("3",2,2)),(("3",3,3),("4",0,3),("1",1,1)),(("1",1,3),("2",0,2))]
        listaintermedio=[((("v",0,1),(">",0,2),(">",0,3),(">",1,1),(">",2,3),("˄",2,3),("<",3,3),("˄",3,4)),(("v",0,0),("v",0,1),(">",1,1),(">",2,0),("v",2,1),("v",3,0),("v",3,1),(">",4,3)),((">",0,0),("<",0,2),("˄",0,2),("v",0,4),("v",1,3),("˄",1,4),("v",3,2),("<",3,3),("˄",3,4),(">",4,3)))]
        listadificil=[((("4",0,0),("˄",0,1),("2",1,1),("<",1,1),("v",2,0),("<",2,0),("v",2,2),(">",2,3),("1",3,0),("v",3,1),(">",3,2),("<",4,0)),(("<",0,0),("2",0,2),("˄",1,0),(">",1,2),("4",1,3),("v",2,1),("v",2,2),("1",2,3),(">",3,2),("<",4,3)),(("<",0,0),("<",0,1),(">",0,2),("4",1,1),("˄",1,1),(">",1,1),("˄",1,3),("v",2,1),("1",2,4),("<",3,2),("˄",3,2),("<",3,3),(">",4,0)))]
        listadefinitiva=[listafacil,listaintermedio,listadificil]
        a=open("futoshiki2020partidas.dat","wb")
        pickle.dump(listadefinitiva,a)
        a.close()
    #el juego nuevo
    def jugar(Nombre,reloj,lado,dificultad):
        if Nombre=="" or reloj==0 or lado==0 or dificultad==0:#control de errores
            messagebox.showerror(message="Error, entradas incompletas")
        else:
            Ventana_C.withdraw()#nueva ventana y se cierra la anterior
            Ventana_J=Tk()#configuracion nueva pantalla
            Ventana_J.geometry('800x750+450+50')
            Ventana_J.title('Futoshiki')
            Ventana_J.config(bg='beige')
            Ventana_J.resizable(width= False, height=False)
            Mensaje_nombre=Label(Ventana_J,text="Nombre: "+Nombre,font=("Arial",20),bg='beige')
            Mensaje_nombre.place(x=275,y=20)#titulos
            #para que el boton seleccionado haga algo
            global uno
            global dos
            global tres
            global cuatro
            global cinco
            global num
            global lista
            global btn0
            global btn1
            global btn2
            global btn3
            global btn4
            global btn5
            global btn6
            global btn7
            global btn8
            global btn9
            global btn10
            global btn11
            global btn12
            global btn13
            global btn14
            global btn15
            global btn16
            global btn17
            global btn18
            global btn19
            global btn20
            global btn21
            global btn22
            global btn23
            global btn24
            global cuadricula
            global algo
            global puntaje
            global top10
            uno="1"
            dos="2"
            tres="3"
            cuatro="4"
            cinco="5"
            num=""
            algo=0
            puntaje=0
            filesize=os.path.getsize("futoshiki2020top10.dat")
            if filesize==0:
                top10=[]
                y=open("futoshiki2020top10.dat","wb")
                pickle.dump(top10,y)
                y.close()
            else:
                y=open("futoshiki2020top10.dat","rb")
                top10=pickle.load(y)
                y.close()
            if isinstance(dificultad,list):
                lista=dificultad[2]
                cuadricula=dificultad[1]
                btn0=cuadricula[0][0]
                btn1=cuadricula[0][1]
                btn2=cuadricula[0][2]
                btn3=cuadricula[0][3]
                btn4=cuadricula[0][4]
                btn5=cuadricula[1][0]
                btn6=cuadricula[1][1]
                btn7=cuadricula[1][2]
                btn8=cuadricula[1][3]
                btn9=cuadricula[1][4]
                btn10=cuadricula[2][0]
                btn11=cuadricula[2][1]
                btn12=cuadricula[2][2]
                btn13=cuadricula[2][3]
                btn14=cuadricula[2][4]
                btn15=cuadricula[3][0]
                btn16=cuadricula[3][1]
                btn17=cuadricula[3][2]
                btn18=cuadricula[3][3]
                btn19=cuadricula[3][4]
                btn20=cuadricula[4][0]
                btn21=cuadricula[4][1]
                btn22=cuadricula[4][2]
                btn23=cuadricula[4][3]
                btn24=cuadricula[4][4]
                algo=1
                cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
            else:
                btn0=0
                btn1=0
                btn2=0
                btn3=0
                btn4=0
                btn5=0
                btn6=0
                btn7=0
                btn8=0
                btn9=0
                btn10=0
                btn11=0
                btn12=0
                btn13=0
                btn14=0
                btn15=0
                btn16=0
                btn17=0
                btn18=0
                btn19=0
                btn20=0
                btn21=0
                btn22=0
                btn23=0
                btn24=0
                lista=[]
                cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
            #funciones de borrado de jugadas
            def borra_todo():
                while lista!=[]:
                    anterior()
            def anterior():
                global lista
                global num
                global btn0
                global btn1
                global btn2
                global btn3
                global btn4
                global btn5
                global btn6
                global btn7
                global btn8
                global btn9
                global btn10
                global btn11
                global btn12
                global btn13
                global btn14
                global btn15
                global btn16
                global btn17
                global btn18
                global btn19
                global btn20
                global btn21
                global btn22
                global btn23
                global btn24
                global cuadricula
                if lista==[]:
                    messagebox.showerror(message="Error, ya no hay jugadas anteriores a esta")
                elif lista[-1]==0:
                    btn0=0
                    lista=lista[:-1]
                    num=""
                    boton0["text"]=num
                    boton0["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==1:
                    btn1=0
                    lista=lista[:-1]
                    num=""
                    boton1["text"]=num
                    boton1["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==2:
                    btn2=0
                    lista=lista[:-1]
                    num=""
                    boton2["text"]=num
                    boton2["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==3:
                    btn3=0
                    lista=lista[:-1]
                    num=""
                    boton3["text"]=num
                    boton3["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==4:
                    btn4=0
                    lista=lista[:-1]
                    num=""
                    boton4["text"]=num
                    boton4["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==5:
                    btn5=0
                    lista=lista[:-1]
                    num=""
                    boton5["text"]=num
                    boton5["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==6:
                    btn6=0
                    lista=lista[:-1]
                    num=""
                    boton6["text"]=num
                    boton6["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==7:
                    btn7=0
                    lista=lista[:-1]
                    num=""
                    boton7["text"]=num
                    boton7["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==8:
                    btn8=0
                    lista=lista[:-1]
                    num=""
                    boton8["text"]=num
                    boton8["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==9:
                    btn9=0
                    lista=lista[:-1]
                    num=""
                    boton9["text"]=num
                    boton9["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==10:
                    btn10=0
                    lista=lista[:-1]
                    num=""
                    boton10["text"]=num
                    boton10["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==11:
                    btn11=0
                    lista=lista[:-1]
                    num=""
                    boton11["text"]=num
                    boton11["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==12:
                    btn12=0
                    lista=lista[:-1]
                    num=""
                    boton12["text"]=num
                    boton12["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==13:
                    btn13=0
                    lista=lista[:-1]
                    num=""
                    boton13["text"]=num
                    boton13["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==14:
                    btn14=0
                    lista=lista[:-1]
                    num=""
                    boton14["text"]=num
                    boton14["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==15:
                    btn15=0
                    lista=lista[:-1]
                    num=""
                    boton15["text"]=num
                    boton15["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==16:
                    btn16=0
                    lista=lista[:-1]
                    num=""
                    boton16["text"]=num
                    boton16["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==17:
                    btn17=0
                    lista=lista[:-1]
                    num=""
                    boton17["text"]=num
                    boton17["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==18:
                    btn18=0
                    lista=lista[:-1]
                    num=""
                    boton18["text"]=num
                    boton18["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==19:
                    btn19=0
                    lista=lista[:-1]
                    num=""
                    boton19["text"]=num
                    boton19["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==20:
                    btn20=0
                    lista=lista[:-1]
                    num=""
                    boton20["text"]=num
                    boton20["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==21:
                    btn21=0
                    lista=lista[:-1]
                    num=""
                    boton21["text"]=num
                    boton21["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==22:
                    btn22=0
                    lista=lista[:-1]
                    num=""
                    boton22["text"]=num
                    boton22["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==23:
                    btn23=0
                    lista=lista[:-1]
                    num=""
                    boton23["text"]=num
                    boton23["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                elif lista[-1]==24:
                    btn24=0
                    lista=lista[:-1]
                    num=""
                    boton24["text"]=num
                    boton24["state"]='normal'
                    cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
            #encuentra si ya se ganó
            def ganar(cuadricula):
                ceros=0
                for i in cuadricula:
                    for j in i:
                        if j==0 or j=="0":
                            ceros+=1
                if ceros==0:
                    if reloj==1:
                        parar()
                    Boton4_J["state"]=DISABLED
                    Mensaje_ganar=Message(Ventana_J,text="¡EXCELENTE! JUEGO TERMINADO CON ÉXITO",width='885',font=("Comic Sans",40),bg="#C2D8FB",fg="black")
                    Mensaje_ganar.place(x=10,y=475)
                    def cerrar():
                        filesize=os.path.getsize("futoshiki2020top10.dat")
                        if filesize!=0:
                            file = open("futoshiki2020top10.dat","r+")
                            file.truncate(0)
                            file.close()
                        top10.append((Nombre,puntaje))
                        y=open("futoshiki2020top10.dat","wb")
                        pickle.dump(top10,y)
                        y.close()
                        Ventana_J.destroy()
                        Ventana_C.destroy()
                    btfin=Button(Ventana_J,text="Fin",width='11',height='3',command=cerrar)
                    btfin.place(x=300,y=200)
            #funciones de los botones de la cuadricula
            def numero(n):
                global num
                num=n
                if num=="1":
                    Boton0_num["bg"]="green"
                    Boton1_num["bg"]="white"
                    Boton2_num["bg"]="white"
                    Boton3_num["bg"]="white"
                    Boton4_num["bg"]="white"
                elif num=="2":
                    Boton0_num["bg"]="white"
                    Boton1_num["bg"]="green"
                    Boton2_num["bg"]="white"
                    Boton3_num["bg"]="white"
                    Boton4_num["bg"]="white"
                elif num=="3":
                    Boton0_num["bg"]="white"
                    Boton1_num["bg"]="white"
                    Boton2_num["bg"]="green"
                    Boton3_num["bg"]="white"
                    Boton4_num["bg"]="white"
                elif num=="4":
                    Boton0_num["bg"]="white"
                    Boton1_num["bg"]="white"
                    Boton2_num["bg"]="white"
                    Boton3_num["bg"]="green"
                    Boton4_num["bg"]="white"
                elif num=="5":
                    Boton0_num["bg"]="white"
                    Boton1_num["bg"]="white"
                    Boton2_num["bg"]="white"
                    Boton3_num["bg"]="white"
                    Boton4_num["bg"]="green"
                #agregar para que cambie de color al presionar 
            def original0():
                global num
                global btn0
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[0]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[0]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==0 and i[2]==0:
                        if btn1!=0 and btn5!=0:
                            if i[0]=="<":
                                if num>=btn1:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn1:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn5:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn5:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn0=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton0["text"]=num
                        boton0["state"]=DISABLED
                        lista.append(0)
                        num=""
                        ganar(cuadricula)
            def original1():
                global num
                global btn1
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[1]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[0]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==0 and i[2]==1:
                        if btn2!=0 and btn6!=0:
                            if i[0]=="<":
                                if num>=btn2:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn2:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn6:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn6:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn1=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton1["text"]=num
                        boton1["state"]=DISABLED
                        lista.append(1)
                        num=""
                        ganar(cuadricula)
            def original2():
                global num
                global btn2
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[2]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[0]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==0 and i[2]==2:
                        if btn3!=0 and btn7!=0:
                            if i[0]=="<":
                                if num>=btn3:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn3:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn7:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn7:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn2=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton2["text"]=num
                        boton2["state"]=DISABLED
                        lista.append(2)
                        num=""
                        ganar(cuadricula)
            def original3():
                global num
                global btn3
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[3]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[0]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==0 and i[2]==3:
                        if btn4!=0 and btn8!=0:
                            if i[0]=="<":
                                if num>=btn4:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn4:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn8:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn8:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn3=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton3["text"]=num
                        boton3["state"]=DISABLED
                        lista.append(3)
                        num=""
                        ganar(cuadricula)
            def original4():
                global num
                global btn4
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[4]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[0]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==0 and i[2]==4:
                        if  btn9!=0:
                            if i[0]=="v":
                                if num<=btn9:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn9:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn4=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton4["text"]=num
                        boton4["state"]=DISABLED
                        lista.append(4)
                        num=""
                        ganar(cuadricula)
            def original5():
                global num
                global btn5
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[0]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[1]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==1 and i[2]==0:
                        if btn6!=0 and btn10!=0:
                            if i[0]=="<":
                                if num>=btn6:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn6:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn10:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn10:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn5=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton5["text"]=num
                        boton5["state"]=DISABLED
                        lista.append(5)
                        num=""
                        ganar(cuadricula)
            def original6():
                global num
                global btn6
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[1]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[1]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==1 and i[2]==1:
                        if btn7!=0 and btn11!=0:
                            if i[0]=="<":
                                if num>=btn7:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn7:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn11:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn11:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn6=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton6["text"]=num
                        boton6["state"]=DISABLED
                        lista.append(6)
                        num=""
                        ganar(cuadricula)
            def original7():
                global num
                global btn7
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[2]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[1]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==1 and i[2]==2:
                        if btn8!=0 and btn12!=0:
                            if i[0]=="<":
                                if num>=btn8:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn8:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn12:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn12:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn7=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton7["text"]=num
                        boton7["state"]=DISABLED
                        lista.append(7)
                        num=""
                        ganar(cuadricula)
            def original8():
                global num
                global btn8
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[3]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[1]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==1 and i[2]==3:
                        if btn9!=0 and btn13!=0:
                            if i[0]=="<":
                                if num>=btn9:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn9:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn13:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn13:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn8=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton8["text"]=num
                        boton8["state"]=DISABLED
                        lista.append(8)
                        num=""
                        ganar(cuadricula)
            def original9():
                global num
                global btn9
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[4]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[1]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==1 and i[2]==4:
                        if btn14!=0:
                            if i[0]=="v":
                                if num<=btn14:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn14:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn9=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton9["text"]=num
                        boton9["state"]=DISABLED
                        lista.append(9)
                        num=""
                        ganar(cuadricula)
            def original10():
                global num
                global btn10
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[0]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[2]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==2 and i[2]==0:
                        if btn11!=0 and btn15!=0:
                            if i[0]=="<":
                                if num>=btn11:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn11:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn15:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn15:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn10=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton10["text"]=num
                        boton10["state"]=DISABLED
                        lista.append(10)
                        num=""
                        ganar(cuadricula)
            def original11():
                global num
                global btn11
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[1]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[2]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==2 and i[2]==1:
                        if btn12!=0 and btn16!=0:
                            if i[0]=="<":
                                if num>=btn12:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn12:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn16:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn16:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn11=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton11["text"]=num
                        boton11["state"]=DISABLED
                        lista.append(11)
                        num=""
                        ganar(cuadricula)
            def original12():
                global num
                global btn12
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[2]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[2]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==2 and i[2]==2:
                        if btn13!=0 and btn17!=0:
                            if i[0]=="<":
                                if num>=btn13:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn13:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn17:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn17:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn12=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton12["text"]=num
                        boton12["state"]=DISABLED
                        lista.append(12)
                        num=""
                        ganar(cuadricula)
            def original13():
                global num
                global btn13
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[3]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[2]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==2 and i[2]==3:
                        if btn14!=0 and btn18!=0:
                            if i[0]=="<":
                                if num>=btn14:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn14:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn18:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn18:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn13=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton13["text"]=num
                        boton13["state"]=DISABLED
                        lista.append(13)
                        num=""
                        ganar(cuadricula)
            def original14():
                global num
                global btn14
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[4]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[2]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==2 and i[2]==4:
                        if btn19!=0:
                            if i[0]=="v":
                                if num<=btn19:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn19:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn14=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton14["text"]=num
                        boton14["state"]=DISABLED
                        lista.append(14)
                        num=""
                        ganar(cuadricula)
            def original15():
                global num
                global btn15
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[0]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[3]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==3 and i[2]==0:
                        if btn16!=0 and btn20!=0:
                            if i[0]=="<":
                                if num>=btn16:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn16:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn20:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn20:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn15=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton15["text"]=num
                        boton15["state"]=DISABLED
                        lista.append(15)
                        num=""
                        ganar(cuadricula)
            def original16():
                global num
                global btn16
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[1]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[3]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==3 and i[2]==1:
                        if btn17!=0 and btn21!=0:
                            if i[0]=="<":
                                if num>=btn17:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn17:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn21:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn21:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn16=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton16["text"]=num
                        boton16["state"]=DISABLED
                        lista.append(16)
                        num=""
                        ganar(cuadricula)
            def original17():
                global num
                global btn17
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[2]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[3]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==3 and i[2]==2:
                        if btn18!=0 and btn22!=0:
                            if i[0]=="<":
                                if num>=btn18:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn18:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn22:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn22:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn17=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton17["text"]=num
                        boton17["state"]=DISABLED
                        lista.append(17)
                        num=""
                        ganar(cuadricula)
            def original18():
                global num
                global btn18
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[3]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[3]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==3 and i[2]==3:
                        if btn19!=0 and btn23!=0:
                            if i[0]=="<":
                                if num>=btn19:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn19:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                            elif i[0]=="v":
                                if num<=btn23:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn23:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn18=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton18["text"]=num
                        boton18["state"]=DISABLED
                        lista.append(18)
                        num=""
                        ganar(cuadricula)
            def original19():
                global num
                global btn19
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[4]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[3]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==3 and i[2]==4:
                        if btn24!=0:
                            if i[0]=="v":
                                if num<=btn24:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo v ")
                            elif i[0]=="˄":
                                if num>=btn24:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo ˄ ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn19=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton19["text"]=num
                        boton19["state"]=DISABLED
                        lista.append(19)
                        num=""
                        ganar(cuadricula)
            def original20():
                global num
                global btn20
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[0]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[4]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==4 and i[2]==0:
                        if btn21!=0:
                            if i[0]=="<":
                                if num>=btn21:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn21:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn20=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton20["text"]=num
                        boton20["state"]=DISABLED
                        lista.append(20)
                        num=""
                        ganar(cuadricula)
            def original21():
                global num
                global btn21
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[1]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[4]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==4 and i[2]==1:
                        if btn22!=0:
                            if i[0]=="<":
                                if num>=btn22:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn22:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn21=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton21["text"]=num
                        boton21["state"]=DISABLED
                        lista.append(21)
                        num=""
                        ganar(cuadricula)
            def original22():
                global num
                global btn22
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[2]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[4]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==4 and i[2]==2:
                        if btn23!=0:
                            if i[0]=="<":
                                if num>=btn23:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn23:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn22=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton22["text"]=num
                        boton22["state"]=DISABLED
                        lista.append(22)
                        num=""
                        ganar(cuadricula)
            def original23():
                global num
                global btn23
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[3]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[4]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==4 and i[2]==3:
                        if btn24!=0:
                            if i[0]=="<":
                                if num>=btn24:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num<=btn24:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn23=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton23["text"]=num
                        boton23["state"]=DISABLED
                        lista.append(23)
                        num=""
                        ganar(cuadricula)
            def original24():
                global num
                global btn24
                global cuadricula
                cumple=0
                for i in cuadricula:
                    if num==i[4]:
                        cumple=1
                        messagebox.showerror(message="Este numero ya esta en esta columna")
                if num in cuadricula[4]:
                    cumple=1
                    messagebox.showerror(message="Este numero ya está en la fila")
                for i in plantilla:
                    if i[1]==4 and i[2]==3:
                        if btn23!=0:
                            if i[0]=="<":
                                if num<=btn23:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo < ")
                            elif i[0]==">":
                                if num>=btn23:
                                    cumple=1
                                    messagebox.showerror(message="numero no cumple con el signo > ")
                if cumple==0:
                    if num=="1":
                        Boton0_num["bg"]="white"
                    elif num=="2":
                        Boton1_num["bg"]="white"
                    elif num=="3":
                        Boton2_num["bg"]="white"
                    elif num=="4":
                        Boton3_num["bg"]="white"
                    else:
                        Boton4_num["bg"]="white"
                    if num!="":
                        btn24=num
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                        boton24["text"]=num
                        boton24["state"]=DISABLED
                        lista.append(24)
                        num=""
                        ganar(cuadricula)
            #reloj
            def parar():
                global proceso
                tiempo.after_cancel(proceso)
            global Estado
            if reloj==1:
                Estado="normal"
                proceso=0
                def iniciar(h=0, m=0, s=0):
                    global puntaje
                    puntaje+=1
                    global proceso
                    if s >= 60:
                        s=0
                        m=m+1
                        if m >= 60:
                            m=0
                            h=h+1
                            if h >= 24:
                                h=0
                    tiempo['text'] = str(h)+":"+str(m)+":"+str(s)
                    proceso=tiempo.after(1000, iniciar, (h), (m), (s+1)) 
                tiempo= Label(Ventana_J, fg='black', width=10, font=("","18"))
                tiempo.place(x=20,y=700)
                iniciar()
            elif reloj==2:
                Estado=DISABLED
                global sec
                global minuto
                global hora
                sec=IntVar()
                minuto=IntVar()
                hora=IntVar()
                sec=Entry(Ventana_J,width='10',textvariable=sec)
                sec.place(x=160,y=698)
                minuto=Entry(Ventana_J,width='10',textvariable=minuto)
                minuto.place(x=90,y=698)
                hora=Entry(Ventana_J,width='10',textvariable=hora)
                hora.place(x=20,y=698)
                def subir():
                    global Estado
                    Estado="normal"
                    Boton1_J["state"]=Estado
                    Boton2_J["state"]=Estado
                    Boton3_J["state"]=Estado
                    Boton4_J["state"]=Estado
                    boton0["state"]=Estado
                    boton1["state"]=Estado
                    boton2["state"]=Estado
                    boton3["state"]=Estado
                    boton4["state"]=Estado
                    boton5["state"]=Estado
                    boton6["state"]=Estado
                    boton7["state"]=Estado
                    boton8["state"]=Estado
                    boton9["state"]=Estado
                    boton10["state"]=Estado
                    boton11["state"]=Estado
                    boton12["state"]=Estado
                    boton13["state"]=Estado
                    boton14["state"]=Estado
                    boton15["state"]=Estado
                    boton16["state"]=Estado
                    boton17["state"]=Estado
                    boton18["state"]=Estado
                    boton19["state"]=Estado
                    boton20["state"]=Estado
                    boton21["state"]=Estado
                    boton22["state"]=Estado
                    boton23["state"]=Estado
                    boton24["state"]=Estado
                    Boton0_num["state"]=Estado
                    Boton1_num["state"]=Estado
                    Boton2_num["state"]=Estado
                    Boton3_num["state"]=Estado
                    Boton4_num["state"]=Estado
                    btn["state"]=DISABLED
                    secs=sec.get()
                    mins=minuto.get()
                    horas=hora.get()
                    proceso=0
                    def acabado():
                        Ventana_Z=Tk()
                        Ventana_Z.geometry('300x75+650+700')
                        Ventana_Z.title('Futoshiki')
                        Ventana_Z.config(bg='beige')
                        Ventana_Z.resizable(width= False, height=False)
                        Mensaje_tiempo=Label(Ventana_Z,text="Se acabó el tiempo, desea continuar",font=("Arial",10),bg='beige')
                        Mensaje_tiempo.place(x=25,y=10)
                        def aceptarT():
                            global reloj
                            reloj=1
                            guardar()
                            Ventana_J.destroy()
                            Ventana_Z.destroy()
                            cargar()
                        def denegarT():
                            Ventana_Z.destroy()
                            Ventana_J.destroy()
                            Ventana_C.deiconify()
                        btsit=Button(Ventana_Z,text="SI",width='5',height='1',command=aceptarT)
                        btsit.place(x=10,y=30)
                        btnot=Button(Ventana_Z,text="NO",width='5',height='1',command=denegarT)
                        btnot.place(x=60,y=30)
                    def start(h, m, s):
                        global puntaje
                        puntaje+=1
                        global proceso
                        if h==0 and m==0 and s==0:
                            acabado()       
                        if s<1 and m<=0:
                            s=0
                            if m<1 and h==0:
                                m=0
                            elif m<1:
                                m=59
                                h-=1
                                if h<1:
                                    h=0
                        elif s<1:
                            s=59
                            m-=1
                        tiempo_Up['text'] = str(h)+":"+str(m)+":"+str(s)
                        proceso=tiempo_Up.after(1000, start, (h), (m), (s-1)) 
                    tiempo_Up= Label(Ventana_J, fg='black', width=20, font=("","18"))
                    tiempo_Up.place(x=20,y=685)
                    start(int(horas),int(mins),int(secs))
                btn = Button(Ventana_J, text='iniciar', bd='5',command=subir) 
                btn.place(x = 20,y = 718)
            else:
                Estado="normal"       
            #creacion de la tabla
            listaBotones=[]
            fila=170
            columna=100
            boton0=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original0)
            listaBotones.append(boton0)
            boton1=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original1)
            listaBotones.append(boton1)
            boton2=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original2)
            listaBotones.append(boton2)
            boton3=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original3)
            listaBotones.append(boton3)
            boton4=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original4)
            listaBotones.append(boton4)
            boton5=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original5)
            listaBotones.append(boton5)
            boton6=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original6)
            listaBotones.append(boton6)
            boton7=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original7)
            listaBotones.append(boton7)
            boton8=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original8)
            listaBotones.append(boton8)
            boton9=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original9)
            listaBotones.append(boton9)
            boton10=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original10)
            listaBotones.append(boton10)
            boton11=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original11)
            listaBotones.append(boton11)
            boton12=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original12)
            listaBotones.append(boton12)
            boton13=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original13)
            listaBotones.append(boton13)
            boton14=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original14)
            listaBotones.append(boton14)
            boton15=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original15)
            listaBotones.append(boton15)
            boton16=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original16)
            listaBotones.append(boton16)
            boton17=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original17)
            listaBotones.append(boton17)
            boton18=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original18)
            listaBotones.append(boton18)
            boton19=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original19)
            listaBotones.append(boton19)
            boton20=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original20)
            listaBotones.append(boton20)
            boton21=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original21)
            listaBotones.append(boton21)
            boton22=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original22)
            listaBotones.append(boton22)
            boton23=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original23)
            listaBotones.append(boton23)
            boton24=Button(Ventana_J,text=num,width='9',height='3',state=Estado,command=original24)
            listaBotones.append(boton24)
            boton=0
            if btn0!=0:
                boton0["text"]=btn0
                boton0["state"]=DISABLED
            if btn1!=0:
                boton1["text"]=btn1
                boton1["state"]=DISABLED
            if btn2!=0:
                boton2["text"]=btn2
                boton2["state"]=DISABLED
            if btn3!=0:
                boton3["text"]=btn3
                boton3["state"]=DISABLED
            if btn4!=0:
                boton4["text"]=btn4
                boton4["state"]=DISABLED
            if btn5!=0:
                boton5["text"]=btn5
                boton5["state"]=DISABLED
            if btn6!=0:
                boton6["text"]=btn6
                boton6["state"]=DISABLED
            if btn7!=0:
                boton7["text"]=btn7
                boton7["state"]=DISABLED
            if btn8!=0:
                boton8["text"]=btn8
                boton8["state"]=DISABLED
            if btn9!=0:
                boton9["text"]=btn9
                boton9["state"]=DISABLED
            if btn10!=0:
                boton10["text"]=btn10
                boton10["state"]=DISABLED
            if btn11!=0:
                boton11["text"]=btn11
                boton11["state"]=DISABLED
            if btn12!=0:
                boton12["text"]=btn12
                boton12["state"]=DISABLED
            if btn13!=0:
                boton13["text"]=btn13
                boton13["state"]=DISABLED
            if btn14!=0:
                boton14["text"]=btn14
                boton14["state"]=DISABLED
            if btn15!=0:
                boton15["text"]=btn15
                boton15["state"]=DISABLED
            if btn16!=0:
                boton16["text"]=btn16
                boton16["state"]=DISABLED
            if btn17!=0:
                boton17["text"]=btn17
                boton17["state"]=DISABLED
            if btn18!=0:
                boton18["text"]=btn18
                boton18["state"]=DISABLED
            if btn19!=0:
                boton19["text"]=btn19
                boton19["state"]=DISABLED
            if btn20!=0:
                boton20["text"]=btn20
                boton20["state"]=DISABLED
            if btn21!=0:
                boton21["text"]=btn21
                boton21["state"]=DISABLED
            if btn22!=0:
                boton22["text"]=btn22
                boton22["state"]=DISABLED
            if btn23!=0:
                boton23["text"]=btn23
                boton23["state"]=DISABLED
            if btn24!=0:
                boton24["text"]=btn24
                boton24["state"]=DISABLED
            for i in range(0,5):
                for j in range(0,5):
                    listaBotones[boton].place(x=fila,y=columna)
                    boton+=1
                    fila+=90
                columna+=80
                fila=170
            global plantilla
            #consigue la plantilla
            if isinstance(dificultad,list):
                plantilla=dificultad[0]
            else:
                a=open("futoshiki2020partidas.dat","rb")
                plantilla=pickle.load(a)
                a.close()
                numT=random.randrange(0,len(plantilla))
                numT2=dificultad-1
                if numT2==0:
                    plantilla=plantilla[numT2][numT]
                else:
                    plantilla=plantilla[numT2][0][numT]
            #dibuja los signos y agrega los numeros necesarios
            for i in plantilla:
                if i[0].isdigit():
                    if i[1]==0 and i[2]==0:
                        boton0["text"]=i[0]
                        boton0["state"]=DISABLED
                        btn0=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==0 and i[2]==1:
                        boton1["text"]=i[0]
                        boton1["state"]=DISABLED
                        btn1=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==0 and i[2]==2:
                        boton2["text"]=i[0]
                        boton2["state"]=DISABLED
                        btn2=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==0 and i[2]==3:
                        boton3["text"]=i[0]
                        boton3["state"]=DISABLED
                        btn3=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==0 and i[2]==4:
                        boton4["text"]=i[0]
                        boton4["state"]=DISABLED
                        btn4=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==1 and i[2]==0:
                        boton5["text"]=i[0]
                        boton5["state"]=DISABLED
                        btn5=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==1 and i[2]==1:
                        boton6["text"]=i[0]
                        boton6["state"]=DISABLED
                        btn6=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==1 and i[2]==2:
                        boton7["text"]=i[0]
                        boton7["state"]=DISABLED
                        btn7=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==1 and i[2]==3:
                        boton8["text"]=i[0]
                        boton8["state"]=DISABLED
                        btn8=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==1 and i[2]==4:
                        boton9["text"]=i[0]
                        boton9["state"]=DISABLED
                        btn9=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==2 and i[2]==0:
                        boton10["text"]=i[0]
                        boton10["state"]=DISABLED
                        btn10=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==2 and i[2]==1:
                        boton11["text"]=i[0]
                        boton11["state"]=DISABLED
                        btn11=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==2 and i[2]==2:
                        boton12["text"]=i[0]
                        boton12["state"]=DISABLED
                        btn12=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==2 and i[2]==3:
                        boton13["text"]=i[0]
                        boton13["state"]=DISABLED
                        btn13=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==2 and i[2]==4:
                        boton14["text"]=i[0]
                        boton14["state"]=DISABLED
                        btn14=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==3 and i[2]==0:
                        boton15["text"]=i[0]
                        boton15["state"]=DISABLED
                        btn15=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==3 and i[2]==1:
                        boton16["text"]=i[0]
                        boton16["state"]=DISABLED
                        btn16=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==3 and i[2]==2:
                        boton17["text"]=i[0]
                        boton17["state"]=DISABLED
                        btn17=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==3 and i[2]==3:
                        boton18["text"]=i[0]
                        boton18["state"]=DISABLED
                        btn18=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==3 and i[2]==4:
                        boton19["text"]=i[0]
                        boton19["state"]=DISABLED
                        btn19=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==4 and i[2]==0:
                        boton20["text"]=i[0]
                        boton20["state"]=DISABLED
                        btn20=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==4 and i[2]==1:
                        boton21["text"]=i[0]
                        boton21["state"]=DISABLED
                        btn21=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==4 and i[2]==2:
                        boton22["text"]=i[0]
                        boton22["state"]=DISABLED
                        btn22=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==4 and i[2]==3:
                        boton23["text"]=i[0]
                        boton23["state"]=DISABLED
                        btn23=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                    elif i[1]==4 and i[2]==4:
                        boton24["text"]=i[0]
                        boton24["state"]=DISABLED
                        btn24=i[0]
                        cuadricula=[[btn0,btn1,btn2,btn3,btn4],[btn5,btn6,btn7,btn8,btn9],[btn10,btn11,btn12,btn13,btn14],[btn15,btn16,btn17,btn18,btn19],[btn20,btn21,btn22,btn23,btn24]]
                else:
                    if i[1]==0 and i[2]==0:
                        lbl1=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl1.place(x=200,y=156) 
                        else:
                            lbl1.place(x=245,y=115)
                    elif i[1]==0 and i[2]==1:
                        lbl2=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl2.place(x=290,y=156) 
                        else:
                            lbl2.place(x=335,y=115)
                    elif i[1]==0 and i[2]==2:
                        lbl3=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl3.place(x=380,y=156) 
                        else:
                            lbl3.place(x=425,y=115)
                    elif i[1]==0 and i[2]==3:
                        lbl4=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl4.place(x=470,y=156) 
                        else:
                            lbl4.place(x=515,y=115)
                    elif i[1]==0 and i[2]==4:
                        lbl5=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl5.place(x=560,y=156) 
                        else:
                            lbl5.place(x=605,y=115)
                    elif i[1]==1 and i[2]==0:
                        lbl6=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl6.place(x=200,y=236) 
                        else:
                            lbl6.place(x=240,y=195)
                    elif i[1]==1 and i[2]==1:
                        lbl7=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl7.place(x=290,y=236) 
                        else:
                            lbl7.place(x=335,y=195)
                    elif i[1]==1 and i[2]==2:
                        lbl8=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl8.place(x=380,y=236) 
                        else:
                            lbl8.place(x=425,y=195)
                    elif i[1]==1 and i[2]==3:
                        lbl9=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl9.place(x=470,y=236) 
                        else:
                            lbl9.place(x=515,y=195)
                    elif i[1]==1 and i[2]==4:
                        lbl10=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl10.place(x=560,y=236) 
                        else:
                            lbl10.place(x=605,y=195)
                    elif i[1]==2 and i[2]==0:
                        lbl11=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl11.place(x=200,y=316) 
                        else:
                            lbl11.place(x=245,y=275)
                    elif i[1]==2 and i[2]==1:
                        lbl12=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl12.place(x=290,y=316) 
                        else:
                            lbl12.place(x=335,y=275)
                    elif i[1]==2 and i[2]==2:
                        lbl13=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl13.place(x=380,y=316) 
                        else:
                            lbl13.place(x=425,y=275)
                    elif i[1]==2 and i[2]==3:
                        lbl14=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl14.place(x=470,y=316) 
                        else:
                            lbl14.place(x=515,y=275)
                    elif i[1]==2 and i[2]==4:
                        lbl15=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl15.place(x=560,y=316) 
                        else:
                            lbl15.place(x=605,y=275)
                    elif i[1]==3 and i[2]==0:
                        lbl16=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl16.place(x=200,y=396) 
                        else:
                            lbl16.place(x=245,y=355)
                    elif i[1]==3 and i[2]==1:
                        lbl17=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl17.place(x=290,y=396) 
                        else:
                            lbl17.place(x=335,y=355)
                    elif i[1]==3 and i[2]==2:
                        lbl18=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl18.place(x=470,y=396) 
                        else:
                            lbl18.place(x=515,y=355)
                    elif i[1]==3 and i[2]==3:
                        lbl19=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl19.place(x=380,y=396) 
                        else:
                            lbl19.place(x=425,y=355)
                    elif i[1]==3 and i[2]==4:
                        lbl20=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl20.place(x=560,y=396) 
                        else:
                            lbl20.place(x=605,y=355)
                    elif i[1]==4 and i[2]==0:
                        lbl21=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl21.place(x=200,y=476) 
                        else:
                            lbl21.place(x=245,y=435)
                    elif i[1]==4 and i[2]==1:
                        lbl22=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl22.place(x=290,y=476) 
                        else:
                            lbl22.place(x=335,y=435)
                    elif i[1]==4 and i[2]==2:
                        lbl23=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl23.place(x=380,y=476) 
                        else:
                            lbl23.place(x=425,y=435)
                    elif i[1]==4 and i[2]==3:
                        lbl24=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl24.place(x=470,y=476) 
                        else:
                            lbl24.place(x=515,y=435)
                    elif i[1]==4 and i[2]==4:
                        lbl25=Label(Ventana_J,text=i[0],bg="beige")
                        if i[0]!=">" and i[0]!="<":
                           lbl25.place(x=560,y=476) 
                        else:
                            lbl25.place(x=605,y=435)
            #boton de terminar partida   
            def terminar():
                Ventana_T=Tk()
                Ventana_T.geometry('300x75+650+700')
                Ventana_T.title('Futoshiki')
                Ventana_T.config(bg='beige')
                Ventana_T.resizable(width= False, height=False)
                Mensaje_nombre=Label(Ventana_T,text="¿Está seguro de salir?",font=("Arial",10),bg='beige')
                Mensaje_nombre.place(x=25,y=10)
                def aceptar():
                    Ventana_J.destroy()
                    Ventana_T.destroy()
                    Ventana_C.deiconify()
                def denegar():
                    Ventana_T.destroy()
                btsi=Button(Ventana_T,text="SI",width='5',height='1',command=aceptar)
                btsi.place(x=10,y=30)
                btno=Button(Ventana_T,text="NO",width='5',height='1',command=denegar)
                btno.place(x=60,y=30)
            #guarda la partida
            def guardar():
                filesize=os.path.getsize("futoshiki2020juegoactual.dat")
                if filesize!=0:
                    file = open("futoshiki2020juegoactual.dat","r+")
                    file.truncate(0)
                    file.close()
                d=open("futoshiki2020juegoactual.dat","wb")
                pickle.dump([Nombre,reloj,lado,[plantilla,cuadricula,lista]],d)
                d.close()
            #rehace jugada
            def rehacer():
                n=0
            #soluciona el futoshiki
            def solucionar():
                n=0
            #botones
            Boton1_J=Button(Ventana_J,text="Borrar Jugada",width='13',height='3',font=("Arial",15),bg='#EF9A54',fg="black",state=Estado,command=anterior)
            Boton1_J.place(x=25,y=520)
            Boton2_J=Button(Ventana_J,text="Borrar Juego",width='13',height='3',font=("Arial",15),bg='grey',fg="black",state=Estado,command=borra_todo)
            Boton2_J.place(x=225,y=520)
            Boton3_J=Button(Ventana_J,text="Terminar Juego",width='13',height='3',font=("Arial",15),bg='#C50000',fg="black",state=Estado,command=terminar)
            Boton3_J.place(x=425,y=520)
            Boton4_J=Button(Ventana_J,text="Guardar Juego",width='13',height='3',font=("Arial",15),bg='#8E9CFF',fg="black",state=Estado,command=guardar)
            Boton4_J.place(x=625,y=520)
            Boton5_J=Button(Ventana_J,text="Rehacer Jugada",width='13',height='3',font=("Arial",15),bg='#BFE1BB',fg="black",state=Estado,command=rehacer)
            Boton5_J.place(x=425,y=620)
            Boton6_J=Button(Ventana_J,text="Solucionar Juego",width='13',height='3',font=("Arial",15),bg='grey',fg="black",state=Estado,command=solucionar)
            Boton6_J.place(x=625,y=620)
            #columna de numeros
            if lado==2:
                Boton0_num=Button(Ventana_J,text=uno,width='3',height='1',font=("Arial",15),bg='white',fg="black",state=Estado,command=lambda:numero(uno))
                Boton0_num.place(x=700,y=170)
                Boton1_num=Button(Ventana_J,text=dos,width='3',height='1',font=("Arial",15),bg='white',fg="black",state=Estado,command=lambda:numero(dos))
                Boton1_num.place(x=700,y=220)
                Boton2_num=Button(Ventana_J,text=tres,width='3',height='1',font=("Arial",15),bg='white',fg="black",state=Estado,command=lambda:numero(tres))
                Boton2_num.place(x=700,y=270)
                Boton3_num=Button(Ventana_J,text=cuatro,width='3',height='1',font=("Arial",15),bg='white',fg="black",state=Estado,command=lambda:numero(cuatro))
                Boton3_num.place(x=700,y=320)
                Boton4_num=Button(Ventana_J,text=cinco,width='3',height='1',font=("Arial",15),bg='white',fg="black",state=Estado,command=lambda:numero(cinco))
                Boton4_num.place(x=700,y=370)
            else:
                Boton0_num=Button(Ventana_J,text=uno,width='3',height='1',font=("Arial",15),bg='white',fg="black",state=Estado,command=lambda:numero(uno))
                Boton0_num.place(x=50,y=170)
                Boton1_num=Button(Ventana_J,text=dos,width='3',height='1',font=("Arial",15),bg='white',fg="black",state=Estado,command=lambda:numero(dos))
                Boton1_num.place(x=50,y=220)
                Boton2_num=Button(Ventana_J,text=tres,width='3',height='1',font=("Arial",15),bg='white',fg="black",state=Estado,command=lambda:numero(tres))
                Boton2_num.place(x=50,y=270)
                Boton3_num=Button(Ventana_J,text=cuatro,width='3',height='1',font=("Arial",15),bg='white',fg="black",state=Estado,command=lambda:numero(cuatro))
                Boton3_num.place(x=50,y=320)
                Boton4_num=Button(Ventana_J,text=cinco,width='3',height='1',font=("Arial",15),bg='white',fg="black",state=Estado,command=lambda:numero(cinco))
                Boton4_num.place(x=50,y=370)
            Ventana_J.mainloop()
    #carga la partida
    def cargar():
        filesize=os.path.getsize("futoshiki2020juegoactual.dat")
        if filesize==0:
            messagebox.showerror(message="Error,no hay partida guardadas")
        else:
            x=open("futoshiki2020juegoactual.dat","rb")
            cosa=pickle.load(x)
            x.close()
            jugar(cosa[0],cosa[1],cosa[2],cosa[3])
    #muestra el top 10
    def top():
        n=0
        j=25
        p=10
        q=open("futoshiki2020top10.dat","rb")
        top10=pickle.load(q)
        q.close()
        if len(top10)>10:
            top10=top10[0:10]
        Ventana_Top=Tk()
        Ventana_Top.geometry('500x500+200+300')
        Ventana_Top.title('Futoshiki')
        Ventana_Top.config(bg='beige')
        Ventana_Top.resizable(width= False, height=False)
        w=10
        pdf=FPDF()
        pdf.add_page()
        pdf.set_font("Arial","B",24)
        for i in top10:
            if isinstance(i,int):
                file = open("futoshiki2020top10.dat","r+")
                file.truncate(0)
                file.close()
                d=open("futoshiki2020top10.dat","wb")
                pickle.dump(top10,d)
                d.close()
            else:
                n+=1
                Mensaje_Top=Label(Ventana_Top,font=("Arial",10),bg='beige')
                cosa=str(n)+") "+str(i[0])+" "+str(i[1])
                Mensaje_Top["text"]=cosa
                Mensaje_Top.place(x=j,y=p)
                pdf.cell(10,w,cosa)
                w+=18
                j+=25
                p+=25
        pdf.output("top10futoshiki2020.pdf","F")
        def ok():
            Ventana_Top.destroy()
        def imprime():
            os.startfile("top10futoshiki2020.pdf")
        btpdf=Button(Ventana_Top,text="imprimir",width='7',height='2',command=imprime)
        btpdf.place(x=100,y=450)
        btok=Button(Ventana_Top,text="ok",width='7',height='2',command=ok)
        btok.place(x=300,y=450)      
    #botones
    Boton1=Button(Ventana_C,text="Iniciar Juego",width='11',height='3',font=("Arial",15),bg='red',fg="black",command=lambda:jugar(Nombre_text.get(),var.get(),var2.get(),var3.get()))
    Boton1.place(x=160,y=300)
    Boton2=Button(Ventana_C,text="Cargar Juego",width='11',height='3',font=("Arial",15),bg='#A1FBD5',fg="black",command=cargar)
    Boton2.place(x=310,y=300)
    Boton3=Button(Ventana_C,text="Top 10",width='11',height='3',font=("Arial",15),bg='#DBEB1C',fg="black",command=top)
    Boton3.place(x=460,y=300)
    def manual():#abre el manual
        os.startfile("Esteban_Granda_Urbina_manual_de_usuario_futoshiki_v2.pdf")
    Boton4=Button(Ventana_C,text="Ayuda",width='11',height='3',font=("Arial",15),bg='grey',fg="black",command=manual)
    Boton4.place(x=160,y=400)
    def info():#muestra la informacion del programa
        messagebox.showinfo("Acerca de","""
Nombre del programa: Futoshiki
Version: 1.0.0
Fecha de creaión: 20/07/20
Autor: Esteban Granda Urbina
""")
    Boton5=Button(Ventana_C,text="Acerca de",width='11',height='3',font=("Arial",15),bg='grey',fg="black",command=info)
    Boton5.place(x=310,y=400)
    def cerrar():#cierra la ventana
        Ventana_C.destroy()
    Boton6=Button(Ventana_C,text="Salir",width='11',height='3',font=("Arial",15),bg='grey',fg="black",command=cerrar)
    Boton6.place(x=460,y=400)
    Ventana_C.mainloop()
VentanaPrincipal()

