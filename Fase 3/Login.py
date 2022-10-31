import hashlib
import json
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename 
from PIL import Image,ImageTk
from Doble import doble
from Doble_Items import doble_items
from Doble_Usuarios import doble_usuarios
from merkle import MerkleTree
from Matriz import matriz
from tabla_hash import HashTable
global usuarios
global tienda
global hashtable_1
usuarios = doble_usuarios()
tienda = doble_items()
hashtable_1 = HashTable(13,20,80)
#Método tienda 
def creatienda():
    global shop
    shop = Toplevel(pantalla)
    shop.title("Tienda")
    shop.geometry("1200x600")
    image1 = Image.open("Loguin.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(shop,image=test)
    label1.image = test
    label1.place(x=0,y=0)
    image2 = Image.open("carrito.png").resize((50,50))
    test2 = ImageTk.PhotoImage(image2)
    label2 = Button(shop,command=merk,image=test2)
    label2.image = test2
    label2.place(x=10,y=10)
    usuarios.settienda(tienda)
    crearbotones()

#Método que muestra el arbol merkle
def merk():
    global merkrep
    merkrep = Toplevel(pantalla)
    merkrep.title("Reporte Merkle y tabla Hash")
    merkrep.geometry("1300x700")
    image1 = Image.open("./imagenes/Arbol_Merkle.png").resize((900,700))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(merkrep,image=test)
    label1.image = test
    label1.place(x=0,y=0)
    image2 = Image.open("./imagenes/Tabla_Hash.png").resize((400,700))
    test2 = ImageTk.PhotoImage(image2)
    label2 = Label(merkrep,image=test2)
    label2.image = test2
    label2.place(x=900,y=0)

#Método que agrega los botones a la tienda 
def crearbotones():
    x = 1200
    y = 700
    xi = 5
    yi = 120
    cantidad = tienda.cantidad()
    for i in range(cantidad): #Poner antes del text el nombre de la ventana
        datos = tienda.retornaritem(i+1)

        locals()[f'b{i}'] = Button(shop,text=datos[0]+"\n Precio: "+str(datos[2]) + "\n Categoría: " +datos[3],command=lambda a = [datos[0],str(datos[1])]:comprar(a),width=15,height=3)
        locals()[f'b{i}'].place(x=xi,y=yi) 
        if xi+120 < x:
            xi+=120 
        else:
            xi =5
            yi+=100
    lab = Label(shop,text = 0)
    lab.place(x=70,y=10,width=55,height=55)

#Método que agrega items a la tienda
def comprar(lista):
    encriptar = hashlib.sha256(contra_l.get().encode('utf-8')).hexdigest()
    lista2 = usuarios.obtener(nombre_l.get(),encriptar,lista[1],lista[0])
    id = usuarios.getidhash(nombre_l.get(),encriptar)
    hashtable_1.agregar(str(id)+str(lista[1]),lista[0])
    m = MerkleTree(lista2)
    m.graficar(nombre_l.get())
    hashtable_1.drawHashTable(nombre_l.get())
    actualizar_tokens()

#Método que actualiza los tokens en la tienda
def actualizar_tokens():
    encriptar = hashlib.sha256(contra_l.get().encode('utf-8')).hexdigest()
    
    lab2 = Label(shop,text=str(usuarios.actualizartokens(nombre_l.get(),encriptar)))
    lab2.place(x=1100,y=10,width=55,height=55)

#Pantalla al loguearse
def logueado(nombre,contrasena):
    global logued
    pantalla.withdraw()
    logued = Toplevel(pantalla)
    logued.title("Bienvenido: "+nombre)
    logued.geometry("400x400")
    image1 = Image.open("Logueado.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(logued,image=test)
    label1.image = test
    label1.place(x=0,y=0)
    a = Button(logued,text="Partida 1vs1",command=versus,width=25,height=2)
    a.place(x=110,y=50)
    b = Button(logued,text="Tienda",command=creatienda,width=25,height=2)
    b.place(x=110,y=100)
    c = Button(logued,text="Reporte ultima partida",command=reporte1vs1,width=25,height=2)
    c.place(x=110,y=150)
    d = Button(logued,text="Cerrar sesion",command=cerrar,width=25,height=2)
    d.place(x=110,y=200)

#Cerrar loguin
def cerrar():
    pantalla.deiconify()
    logued.destroy()

#Cerrar admin
def cerraradmin():
    pantalla.deiconify()
    padmin.destroy()
#1vs1
def versus():
    global vrs,inv,nu,map,tm,bt,tamano,u2
    u2 = StringVar()
    tamano = StringVar()
    vrs = Toplevel(pantalla)
    vrs.title("1VS1")
    vrs.geometry("1000x1200")
    vrs.configure(bg="#A5907E")
    inv = Label(vrs,text="Nombre usuario invitado")
    inv.place(x=185,y=40)
    nu = Entry(vrs,textvariable=u2)
    nu.place(x=150,y=70)
    map = Label(vrs,text="Tamano del mapa")
    map.place(x=185,y=110)
    tm = Entry(vrs,textvariable=tamano)
    tm.place(x=150,y=150)
    bt = Button(vrs,text="Iniciar",width=10,height=1,command=iniciar)
    bt.place(x=175,y=220)

#Inicio del 1vs1
def iniciar():
    global P1,P2,n2
    tam = int(tamano.get())
    x = StringVar()
    y = StringVar()
    x2 = StringVar()
    y2 = StringVar()
    n2 = u2.get()
    inv.destroy()
    nu.destroy()
    map.destroy()
    tm.destroy()
    bt.destroy()
    P1 = matriz()
    P2 = matriz()
    P1.Agregarbarcos(tam)
    P2.Agregarbarcos(tam)
    P1.tablero(tam,nombre_l.get())
    P2.tablero(tam,n2)
    P1x = Label(vrs,text="Coordenada x")
    P1x.place(x=10,y=610)
    Pixp = Entry(vrs,textvariable=x)
    Pixp.place(x=90,y=610)
    P1y = Label(vrs,text="Coordenada y")
    P1y.place(x=10,y=640)
    P1yp = Entry(vrs,textvariable=y)
    P1yp.place(x=90,y=640)
    Bd1 = Button(vrs,text="Disparar",width=30,height=1,command=lambda:[P2.MarcarDisparo(int(y.get()),int(x.get()),tam),actualizar()])
    Bd1.place(x=10,y=670)
    P2x = Label(vrs,text="Coordenada x")
    P2x.place(x=510,y=610)
    P2xp = Entry(vrs,textvariable=x2)
    P2xp.place(x=590,y=610)
    P2y = Label(vrs,text="Coordenada y")
    P2y.place(x=510,y=640)
    P2yp = Entry(vrs,textvariable=y2)
    P2yp.place(x=590,y=640)
    Bd2 = Button(vrs,text="Disparar",width=30,height=1,command=lambda:[P1.MarcarDisparo(int(y2.get()),int(x2.get()),tam),actualizar()])
    Bd2.place(x=510,y=670)
    image1 = Image.open("./imagenes/tablero"+nombre_l.get()+".png").resize((500,590))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(vrs,image=test)
    label1.image = test
    label1.place(x=0,y=0)
    image2 = Image.open("./imagenes/tablero"+n2+".png").resize((500,590))
    test2 = ImageTk.PhotoImage(image2)
    label2 = Label(vrs,image=test2)
    label2.image = test2
    label2.place(x=500,y=0)
    btp = Button(vrs,text="Reiniciar juego",width=30,height=2,command=repetir,bg="#E6E8E6")
    btp.place(x=730,y=610)
    btv = Button(vrs,text="Regresar al menu",width=20,height=2,command=vic)
    btv.place(x=350,y=610)

#Metodo para actualizar el mapa 
def actualizar():
    if P1.victoria()==1:
        usuarios.aumentatoken(nombre_l.get(),contra_l.get(),P2.comprobargolpes())
        tam = int(tamano.get())
        P1.tablero(tam,nombre_l.get())
        P2.tablero(tam,n2)
        P1.dob.Destruidos(nombre_l.get())
        image1 = Image.open("./imagenes/tablero"+nombre_l.get()+".png").resize((500,590))
        test = ImageTk.PhotoImage(image1)
        label1 = Label(vrs,image=test)
        label1.image = test
        label1.place(x=0,y=0)
        image2 = Image.open("./imagenes/tablero"+n2+".png").resize((500,590))
        test2 = ImageTk.PhotoImage(image2)
        label2 = Label(vrs,image=test2)
        label2.image = test2
        label2.place(x=500,y=0)
    elif P2.victoria()==1: #El método victoria indica que ya no le quedan barcos al jugador
        usuarios.aumentavictoria(nombre_l.get(),contra_l.get())
        usuarios.aumentatoken(nombre_l.get(),contra_l.get(),P2.comprobargolpes())
        tam = int(tamano.get())
        P1.tablero(tam,nombre_l.get())
        P2.tablero(tam,n2)
        P1.dob.Destruidos(nombre_l.get())
        image1 = Image.open("./imagenes/tablero"+nombre_l.get()+".png").resize((500,590))
        test = ImageTk.PhotoImage(image1)
        label1 = Label(vrs,image=test)
        label1.image = test
        label1.place(x=0,y=0)
        image2 = Image.open("./imagenes/tablero"+n2+".png").resize((500,590))
        test2 = ImageTk.PhotoImage(image2)
        label2 = Label(vrs,image=test2)
        label2.image = test2
        label2.place(x=500,y=0)
    else:
        tam = int(tamano.get())
        P1.tablero(tam,nombre_l.get())
        P2.tablero(tam,n2)
        P1.dob.Destruidos(nombre_l.get())
        image1 = Image.open("./imagenes/tablero"+nombre_l.get()+".png").resize((500,590))
        test = ImageTk.PhotoImage(image1)
        label1 = Label(vrs,image=test)
        label1.image = test
        label1.place(x=0,y=0)
        image2 = Image.open("./imagenes/tablero"+n2+".png").resize((500,590))
        test2 = ImageTk.PhotoImage(image2)
        label2 = Label(vrs,image=test2)
        label2.image = test2
        label2.place(x=500,y=0)

#Metodo tras ganar partida
def vic():
    vrs.destroy()

#Método para reiniciar la partida
def repetir():
    iniciar()

#Método para mostrar el reporte de la ultima partida
def reporte1vs1():
    global reporte
    reporte = Toplevel(pantalla)
    reporte.title("Reporte")
    reporte.geometry("1200x600")
    image1 = Image.open("./imagenes/reporte"+nombre_l.get()+".png").resize((600,600))
    test = ImageTk.PhotoImage(image1)
    label1 = Label(reporte,image=test)
    label1.image = test
    label1.place(x=600,y=0)
    image2 = Image.open("./imagenes/Lista_Adyacencia.png").resize((300,600))
    test2 = ImageTk.PhotoImage(image2)
    label2 = Label(reporte,image=test2)
    label2.image = test2
    label2.place(x=0,y=0)
    image3 = Image.open("./imagenes/grafo.png").resize((300,600))
    test3= ImageTk.PhotoImage(image3)
    label3 = Label(reporte,image=test3)
    label3.image = test3
    label3.place(x=300,y=0)
#Método para registrar usuarios manualmente
def registrar_usuario():
    id = 0
    nombre_u = nombrer.get()
    contra_u = contrar.get()
    contra_u = hashlib.sha256(contra_u.encode('utf-8')).hexdigest()
    edad_u = edadr.get()
    a = Label(pantalla1,text="Registro exitoso",fg="green")
    a.place(x=170,y=260)
    nombre_usuario.delete(0,END)
    contra_usuario.delete(0,END)
    edad_usuario.delete(0,END)
    id = usuarios.getid()
    usuarios.agregar(nombre_u,0,id,contra_u,edad_u)

#Pantalla de registro
def registrar():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.title("Registrarse")
    pantalla1.geometry("400x400")
    image1 = Image.open("Loguin.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(pantalla1,image=test)
    label1.image = test
    label1.place(x=0,y=0)
    global nombrer
    global contrar
    global edadr
    global nombre_usuario
    global contra_usuario
    global edad_usuario
    nombrer = StringVar()
    edadr = StringVar()
    contrar = StringVar()
    a = Label(pantalla1,text="Ingrese su usuario y contraseña")
    a.place(x=130,y=10)
    b = Label(pantalla1,text="Nombre *")
    b.place(x=185,y=40)
    nombre_usuario = Entry(pantalla1,textvariable=nombrer)
    nombre_usuario.place(x=150,y=70)
    c = Label(pantalla1,text="Contrasena *")
    c.place(x=175,y=100)
    contra_usuario = Entry(pantalla1,textvariable=contrar)
    contra_usuario.place(x=150,y=130)
    d = Label(pantalla1,text="Edad *")
    d.place(x=195,y=160)
    edad_usuario = Entry(pantalla1,textvariable = edadr)
    edad_usuario.place(x=150,y=190)
    e = Button(pantalla1,text="Registrarse",width=10,height=1,command=registrar_usuario)
    e.place(x=175,y=220)

#Pantalla de admin
def admin():
    global padmin
    padmin = Toplevel(pantalla)
    padmin.title("Administracion")
    padmin.geometry("400x400")

    image1 = Image.open("Loguin.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(padmin,image=test)
    label1.image = test
    label1.place(x=0,y=0)
    a = Button(padmin,text="Carga masiva",command=Carga_masiva,width=25,height=2)
    a.place(x=110,y=50)
    b = Button(padmin,text="Crear bloque",command=None,width=25,height=2)
    b.place(x=110,y=100)
    c = Button(padmin,text="Cambiar prueba de trabajo",command=None,width=25,height=2)
    c.place(x=110,y=150)
    d = Button(padmin,text="Tiempo de creación de bloque",command=None,width=25,height=2)
    d.place(x=110,y=200)
    e = Button(padmin,text="Cerrar sesion",command=cerraradmin,width=25,height=2)
    e.place(x=110,y=250)

#metodo de carga masiva
def Carga_masiva():
        ruta = askopenfilename(title="Seleccione archivo", filetypes=[("Ficheros json", "*.json"), ("todos los archivos", "*.*")])
        contenido = None
        contra = ""
        i = 0
        if (ruta != ""):
            with open(ruta, mode="r", encoding="utf-8") as file:
                contenido = json.load(file)

            for user in contenido['usuarios']:
                i+=1
                contra = hashlib.sha256(user['password'].encode('utf-8')).hexdigest()
                usuarios.agregar(user["nick"], user['monedas'],user['id'],contra, user["edad"])
                
            for article in contenido['articulos']:
                tienda.agregar(article["id"],"Disponible", article["nombre"],article["categoria"], article["precio"], article["src"])


#Pantalla de logueo

def Login():
    global pantalla2
    global contra_l,nombre_l
    pantalla2 = Toplevel(pantalla)
    pantalla2.title("Login")
    pantalla2.geometry("400x400")
    image1 = Image.open("Loguin.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(pantalla2,image=test)
    label1.image = test
    label1.place(x=0,y=0)
    nombre_l = StringVar()
    contra_l = StringVar()
    a = Label(pantalla2,text="Ingrese su usuario y contraseña")
    a.place(x=130,y=10)
    b = Label(pantalla2,text="Nombre *")
    b.place(x=185,y=40)
    nombre_usuario_l = Entry(pantalla2,textvariable=nombre_l)
    nombre_usuario_l.place(x=150,y=70)
    c = Label(pantalla2,text="Contrasena *")
    c.place(x=175,y=100)
    contra_usuario_l = Entry(pantalla2,textvariable=contra_l)
    contra_usuario_l.place(x=150,y=130)
    print(contra_l.get())

    d = Button(pantalla2,text="Iniciar sesión",width=10,height=1,command=verificar)
    d.place(x=175,y=160)
def verificar():
    contrasena =  hashlib.sha256(contra_l.get().encode('utf-8')).hexdigest()
    nome = nombre_l.get()
    if  usuarios.login(nome,contrasena) == True:
        logueado(nome,contrasena)
        pantalla2.destroy()
    elif nombre_l.get() == "EDD" and contrasena ==  hashlib.sha256("edd123".encode('utf-8')).hexdigest():
        admin()
        pantalla2.destroy()
    else:
        messagebox.showinfo("Error","Ingrese un usuario y contraseña correctos")
        pantalla2.destroy()

#Ventana principal
def Ventana_principal():

    global pantalla
    pantalla = Tk()
    image1 = Image.open("fondo.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test
    label1.place(x=0,y=0)
    pantalla.geometry("800x800")
    pantalla.title("Pantalla principal")
    a = Label(text="Bienvenido a Battleship",font = ("Arial",14)).place(x=300,y=20)
    #a.place(x=300,y=20)
    b = Button(text="Login",command=Login,width=50,height=2)
    b.place(x=225,y=70)
    c = Button(text="Registrarse",command=registrar,width=50,height=2)
    c.place(x=225,y=120)
    
    pantalla.mainloop()

Ventana_principal()

