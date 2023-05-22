from tkinter import *
import random
import tkinter

# Variables globales
base = 460
altura = 470
radio = 50

#Funciones de la app

# Función para el boton arriba
def arriba():
    c.move(rana, 0, -10)

# Función para el boton abajo
def abajo():
    c.move(rana, 0, 10)

# Función para el boton de izquierda
def izquierda():
    c.move(rana, -10, 0)

# Función para el boton de derecha
def derecha():
    c.move(rana, 10, 0)




#Ventana principal
ventana_principal = Tk()
ventana_principal.title("GameArcade - La Rana Insana")
ventana_principal.geometry("500x800")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="Blue")

# Frame de graficación
frame_graficacion = Frame(ventana_principal, bg="yellow", width=480, height=500)
frame_graficacion.place(x=10, y=10)

# Creación del lienzo (canvas)
c = Canvas(frame_graficacion, width=base, height=altura, bg="green")
c.place(x=10, y=10)

#Carretera superior
c.create_rectangle(0, 75, 600, 140, fill="gray", outline="white", width=2)

#Carretera del medio
c.create_rectangle(0, 270, 600, 200, fill="gray", outline="white", width=2)

#Carretera Inferior
c.create_rectangle(0, 395, 600, 320, fill="gray", outline="white", width=2)


"""#Creacion de un segundo lienzo (Carretera sup)
c1 = Canvas(frame_graficacion, width=457, height=75, bg="gray")
c1.place(x=12, y=80)

#Creacion de un tercer lienzo (Carretera med)
c2 = Canvas(frame_graficacion, width=457, height=75, bg="gray")
c2.place(x=12, y=205)

#Creacion de un cuarto lienzo(carretera inf)
c3 = Canvas(frame_graficacion, width=457, height=75, bg="gray")
c3.place(x=12, y=330)"""

"""# Creación del lienzo para la rana(canvas)
c = Canvas(frame_graficacion, width=base, height=altura,background=c["bg"])"""

#Diseño de la rana
rana_image = tkinter.PhotoImage(file="img/rana.png")

# Dibujar la imagen de la rana en el lienzo
initial_position = (230, 435)
rana = c.create_image(initial_position[0], initial_position[1], image=rana_image)

# Frame de controles
frame_controles = Frame(ventana_principal, bg="Yellow", width=480, height=290)
frame_controles.place(x=10, y=500)

# Botón para mover hacia arriba
arriba_icon = PhotoImage(file="img/arriba.png")
bt_arriba = Button(frame_controles, image=arriba_icon, command=arriba)
bt_arriba.place(x=210, y=30, width=60, height=60)

# Botón para mover hacia abajo
abajo_icon = PhotoImage(file="img/abajo.png")
bt_abajo = Button(frame_controles, image=abajo_icon, command=abajo)
bt_abajo.place(x=210, y=170, width=60, height=60)

# Botón para mover hacia la izquierda
izquierda_icon = PhotoImage(file="img/izq.png")
bt_izquierda = Button(frame_controles, image=izquierda_icon, command=izquierda)
bt_izquierda.place(x=135, y=100, width=60, height=60)

# Botón para mover hacia la derecha
derecha_icon = PhotoImage(file="img/derecha.png")
bt_derecha = Button(frame_controles, image=derecha_icon, command=derecha)
bt_derecha.place(x=285, y=100, width=60, height=60)

# Vehiculos



#Run
ventana_principal.mainloop()