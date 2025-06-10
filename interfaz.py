import sqlite3
import tkinter as tk



def crearAnime():
  app.withdraw()  # Ocultar la ventana principal
  ventana=tk.Tk()
  ventana.title("Crear Anime")
  # Configurar el tamaño de la ventana
  ventana.geometry("500x500")
  # Crear etiquetas y campos de entrada
  etiquetaNombre = tk.Label(ventana, text="Nombre del Anime:")
  etiquetaNombre.pack(pady=5)
  entradaNombre = tk.Entry(ventana)
  entradaNombre.pack(pady=5)
  etiquetaGenero = tk.Label(ventana, text="Género del Anime:")
  etiquetaGenero.pack(pady=5)
  entradaGenero = tk.Entry(ventana)
  entradaGenero.pack(pady=5)
  etiquetaDescripcion = tk.Label(ventana, text="Descripción del Anime:")
  etiquetaDescripcion.pack(pady=5)
  entradaDescripcion = tk.Entry(ventana)
  entradaDescripcion.pack(pady=5)
  etiquetaCapitulos = tk.Label(ventana, text="Cantidad de Episodios:")
  etiquetaCapitulos.pack(pady=5)
  entradaCapitulos = tk.Entry(ventana)
  entradaCapitulos.pack(pady=5)
  # Crear un botón para guardar el anime


  def guardarAnime():
    nombre=entradaNombre.get()
    genero=entradaGenero.get()
    descripcion=entradaDescripcion.get()
    capitulos=int(entradaCapitulos.get())
  

 
    #conectar a la base de datos
    conexion=sqlite3.connect("animes.db")
      #crear un cursor
    if conexion:
          print("conexion exitosa")
    cursor=conexion.cursor()

      #crear la tabla
    insertarAnime="INSERT INTO animes (nombre,genero,descripcion,capitulos) VALUES (?,?,?,?)" 
    cursor.execute(insertarAnime,(nombre,genero,descripcion,capitulos))
    conexion.commit()
    print("anime creado con exito")
      #cerrar la conexion
    conexion.close()
  def volver():
    ventana.destroy()  # Cerrar la ventana de creación de anime
    app.deiconify()  # Mostrar la ventana principal nuevamente
  crearAnime = tk.Button(ventana, text="guardar anime", command=guardarAnime)
  crearAnime.pack(pady=10)
  volverButton = tk.Button(ventana, text="Volver", command=volver)
  volverButton.pack(pady=10)
def mostrarAnimes():
  ventanaMostrar = tk.Tk()
  ventanaMostrar.title("Mostrar Animes")
  # Configurar el tamaño de la ventana
  ventanaMostrar.geometry("500x500")

  # Crear una etiqueta para mostrar los animes

  #conectar a la base de datos
  conexion=sqlite3.connect("animes.db")
  #crear un cursor
  cursor=conexion.cursor()
  #consultar la tabla
  cursor.execute("SELECT * FROM animes")
  animes=cursor.fetchall()
  for fila in range(len(animes)):
      for columna in range(len(animes[fila])):
          etiqueta = tk.Label(ventanaMostrar, text=animes[fila][columna])
          etiqueta.grid(row=fila, column=columna, padx=10, pady=5)
    
  conexion.close()
 

def buscarAnime():
    #conectar a la base de datos
    ventanaBuscar = tk.Tk()
    ventanaBuscar.title("Buscar Anime")
    # Configurar el tamaño de la ventana
    ventanaBuscar.geometry("500x500")
    # Crear etiquetas y campos de entrada
    etiquetaNombre = tk.Label(ventanaBuscar, text="Nombre del Anime:")
    etiquetaNombre.pack(pady=5)
    entradaNombre = tk.Entry(ventanaBuscar)
    entradaNombre.pack(pady=5)
    def buscarAnimeEnDB(nombre):
          conexion=sqlite3.connect("animes.db")
    #crear un cursor
          cursor=conexion.cursor()
    #consultar la tabla
          
          cursor.execute("SELECT * FROM animes WHERE nombre=?", (nombre,))
          animes=cursor.fetchall()
          for anime in animes:
              print(anime)
          #cerrar la conexion
          conexion.close()

    # Crear un botón para buscar el anime
    buscarButton = tk.Button(ventanaBuscar, text="Buscar Anime", command=lambda: buscarAnimeEnDB(entradaNombre.get()))
    buscarButton.pack(pady=10)  
    # Crear un botón para volver a la ventana principal
    def volver():
        ventanaBuscar.destroy()
        app.deiconify()  # Mostrar la ventana principal nuevamente
    volverButton = tk.Button(ventanaBuscar, text="Volver", command=volver)
    volverButton.pack(pady=10)
 


def eliminarAnime():
    ventanaEliminar = tk.Tk()
    ventanaEliminar.title("Eliminar Anime")
    # Configurar el tamaño de la ventana
    ventanaEliminar.geometry("500x500")
    # Crear etiquetas y campos de entrada
    etiquetaNombre = tk.Label(ventanaEliminar, text="Nombre del Anime:")
    etiquetaNombre.pack(pady=5)
    entradaNombre = tk.Entry(ventanaEliminar)
    entradaNombre.pack(pady=5)
    def eliminarAnimeEnDB(nombre):
    #conectar a la base de datos
      conexion=sqlite3.connect("animes.db")
      #crear un cursor
      cursor=conexion.cursor()
      #consultar la tabla
      
      cursor.execute("DELETE FROM animes WHERE nombre=?", (nombre,))
      conexion.commit()
      print("anime eliminado con exito")
      #cerrar la conexion
      conexion.close()
    # Crear un botón para eliminar el anime
    eliminarButton = tk.Button(ventanaEliminar, text="Eliminar Anime", command=lambda: eliminarAnimeEnDB(entradaNombre.get()))
    eliminarButton.pack(pady=10)
    # Crear un botón para volver a la ventana principal
    volverButton = tk.Button(ventanaEliminar, text="Volver", command=volver)
    volverButton.pack(pady=10)
    def volver():
        ventanaEliminar.destroy()
        app.deiconify()  # Mostrar la ventana principal nuevamente

def actualizarAnime():
    ventanaActualizar = tk.Tk()
    ventanaActualizar.title("Actualizar Anime")
    # Configurar el tamaño de la ventana
    ventanaActualizar.geometry("500x500")
    # Crear etiquetas y campos de entrada
    etiquetaNombre = tk.Label(ventanaActualizar, text="Nombre del Anime:")
    etiquetaNombre.pack(pady=5)
    entradaNombre = tk.Entry(ventanaActualizar)
    entradaNombre.pack(pady=5)
    etiquetaNuevoNombre = tk.Label(ventanaActualizar, text="Nuevo Nombre del Anime:")
    etiquetaNuevoNombre.pack(pady=5)
    entradaNuevoNombre = tk.Entry(ventanaActualizar)
    entradaNuevoNombre.pack(pady=5)
    etiquetaNuevoGenero = tk.Label(ventanaActualizar, text="Nuevo Género del Anime:")
    etiquetaNuevoGenero.pack(pady=5)
    entradaNuevoGenero = tk.Entry(ventanaActualizar)
    entradaNuevoGenero.pack(pady=5)
    etiquetaNuevaDescripcion = tk.Label(ventanaActualizar, text="Nueva Descripción del Anime:") 
    etiquetaNuevaDescripcion.pack(pady=5)
    entradaNuevaDescripcion = tk.Entry(ventanaActualizar)
    entradaNuevaDescripcion.pack(pady=5)
    etiquetaNuevosCapitulos = tk.Label(ventanaActualizar, text="Nueva Cantidad de Episodios:")
    etiquetaNuevosCapitulos.pack(pady=5)
    entradaNuevosCapitulos = tk.Entry(ventanaActualizar)
    entradaNuevosCapitulos.pack(pady=5)
    def actualizarAnimeEnDB(nombre, nuevoNombre, nuevoGenero, nuevaDescripcion, nuevosCapitulos):
    #conectar a la base de datos
      conexion=sqlite3.connect("animes.db")
      #crear un cursor
      cursor=conexion.cursor()
      #consultar la tabla
     
      cursor.execute("UPDATE animes SET nombre=?, genero=?, descripcion=?, capitulos=? WHERE nombre=?", (nuevoNombre,nuevoGenero,nuevaDescripcion,nuevosCapitulos,nombre))
      conexion.commit()
      print(" actualizado con exito")
      #cerrar la conexion
      conexion.close()
    # Crear un botón para actualizar el anime
    # actualizarButton = tk.Button(ventanaActualizar, text="Actualizar Anime", command=lambda: actualizarAnimeEnDB(entradaNombre.get(), entradaNuevoNombre.get(), entradaNuevoGenero.get(), entradaNuevaDescripcion.get(), int(entradaNuevosCapitulos.get())))
    actualizarButton = tk.Button(ventanaActualizar, text="Actualizar Anime", command=lambda: actualizarAnimeEnDB(
        entradaNombre.get(),
        entradaNuevoNombre.get(),
        entradaNuevoGenero.get(),
        entradaNuevaDescripcion.get(),
        int(entradaNuevosCapitulos.get())
    ))
    actualizarButton.pack(pady=10)
    # Crear un botón para volver a la ventana principal
    def volver():
        ventanaActualizar.destroy()
        app.deiconify()  # Mostrar la ventana principal nuevamente  

    volverButton = tk.Button(ventanaActualizar, text="Volver", command=volver)
    volverButton.pack(pady=10)

app = tk.Tk()
app.title("Selecciona la opcion que deseas realizar")
# Crear botones para cada opción
botonCrear = tk.Button(app, text="Crear Anime", command=crearAnime)
botonCrear.pack(pady=10)
botonMostrar = tk.Button(app, text="Mostrar Animes", command=mostrarAnimes)
botonMostrar.pack(pady=10)
botonBuscar = tk.Button(app, text="Buscar Anime", command=buscarAnime)
botonBuscar.pack(pady=10)
botonEliminar = tk.Button(app, text="Eliminar Anime", command=eliminarAnime)
botonEliminar.pack(pady=10)
botonActualizar = tk.Button(app, text="Actualizar Anime", command=actualizarAnime)
botonActualizar.pack(pady=10)
# Configurar el tamaño de la ventana
#ancho X alto
app.geometry("500x500")

app.mainloop()
