
import tkinter as tk 

#Importar los módulos restantes de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox

from Usuario import *
from Conexion import *

class FormularioClientes:

    global textBoxComentario
    textBoxComentario =None
    
    global groupBox
    groupBox =None

    global tree
    tree =None

    global textBoxId
    textBoxId =None

    global combo 
    combo =None
    

def Formulario():

        global textBoxComentario
        global tree
        global groupBox
        global textBoxId
        global combo 

        try:
            base = Tk()
            base.geometry("1200x300")
            base.title("Comentarios Python")
            
            groupBox = LabelFrame(base,text= "Información  del comentario",padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            labelId=Label(groupBox,text="Id:",width=13,font=("arial",12)).grid(row=0,column=0) 
            textBoxId = Entry(groupBox)
            textBoxId.grid(row=0,column=1)

            labelAsunto=Label(groupBox,text="Asunto:",width=13,font=("arial",12)).grid(row=1,column=0) 
            seleccionAsunto = tk.StringVar()
            combo = ttk.Combobox(groupBox,values=["Hueco","Tala de arboles","Desechos","Quema indiscriminada","Salubridad"],textvariable=seleccionAsunto)
            combo.grid(row=1,column=1)
            seleccionAsunto.set("Hueco")
  
            labelComentario=Label(groupBox,text="Comentario:",width=13,font=("arial",12)).grid(row=2,column=0) 
            textBoxComentario = Entry(groupBox)
            textBoxComentario.grid(row=2,column=1)
                        


            Button(groupBox,text="Enviar",width=10,command=enviarUsuario).grid(row=3,column=0)
            Button(groupBox,text="Modificar",width=10,command=editarUsuario).grid(row=3,column=1)
            Button(groupBox,text="Eliminar",width=10,command=eliminarUsuario).grid(row=3,column=2)            
            
            groupBox = LabelFrame(base,text="Comentarios",padx=5,pady=5)
            groupBox.grid(row=1,column=0,padx=0,pady=0)
            #Crear un Treeview

            #Configurar las columnas

            tree = ttk.Treeview(groupBox,columns=("Id","Asunto","Comentario"),show='headings',height=5)
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1",text="Id")
            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2",text="Asunto")
            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3",text="Comentario")
 
            #Agregar los datos a la tabla
            #Mostrar la tabla

            for row in CAsunto.mostrarAsunto():
                 tree.insert("","end",values=row)


            #Ejecutar la función de hacer click
            tree.bind("<<TreeviewSelect>>",seleccionarRegistro)

            tree.pack()

            base.mainloop()


        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}". format(error))

def enviarUsuario():
        global combo,textBoxId,textBoxComentario,tree,groupBox

        try:
            #Verificar si los widgets están inicializados
            if textBoxComentario is None or combo is None:
                print ("Los widgets no están inicializados")
                return
            comentario =textBoxComentario.get()
            asunto =combo.get()

            CAsunto.ingresarAsunto(asunto,comentario)
            messagebox.showinfo("Información", "Los datos fueron guardados")

            actualizarTreeView()

            #Limpiamos los campos

            textBoxComentario.delete(0,END)
            combo.delete(0,END)

        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def editarUsuario():
    global textBoxId,textBoxComentario,combo,tree,groupBox

    try:
            #Verificar si los widgets están inicializados
            if textBoxComentario is None or combo is None or textBoxId is None:
                print ("Los widgets no están inicializados")
                return
            comentario =textBoxComentario.get()
            asunto =combo.get()
            id =textBoxId.get()


            CAsunto.editarAsunto(id,asunto,comentario)
            messagebox.showinfo("Información", "Los datos fueron actualizados")

            actualizarTreeView()

            #Limpiamos los campos

            textBoxId.delete(0,END)
            textBoxComentario.delete(0,END)
            combo.delete(0,END)

    except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def eliminarUsuario():
    global textBoxId,textBoxComentario,combo,tree,groupBox

    try:
            #Verificar si los widgets están inicializados
            if textBoxComentario is None or combo is None or textBoxId is None:
                print ("Los widgets no están inicializados")
                return
            
            id =textBoxId.get()


            CAsunto.eliminarAsunto(id)
            messagebox.showinfo("Información", "Los datos fueron eliminados")

            actualizarTreeView()

            #Limpiamos los campos

            textBoxId.delete(0,END)
            textBoxComentario.delete(0,END)
            combo.delete(0,END)

    except ValueError as error:
            print("Error al eliminar los datos {}".format(error))

def actualizarTreeView():
    global tree

    try:
          #Borrar todos los elementos actuales del TreeView (manual)
          tree.delete(*tree.get_children())
          #Obtener los nuevos datos a mostrar
          datos = CAsunto.mostrarAsunto()
          #Insertar nuevos datos en el TreeView
          for row in CAsunto.mostrarAsunto():
            tree.insert("","end",values=row)
    except ValueError as error:
          print("Error al actualizar los datos {}".format(error))
           
def seleccionarRegistro(event):
     try:
          itemSelect = tree.focus()

          if itemSelect:
               #Obtener los valores por columna
               values = tree.item(itemSelect)['values']
               #Establecer los valores en los widgets Entry
               textBoxId.delete(0,END)
               textBoxId.insert(0,values[0])
               combo.delete(0,END)
               combo.insert(0,values[1])
               textBoxComentario.delete(0,END)
               textBoxComentario.insert(0,values[2])

               #Obtener el asunto del elemento seleccionado

     except ValueError as error:
          print("Error al seleccionar registro {}".format(error))
Formulario()

