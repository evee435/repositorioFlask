from flask import Flask, url_for
import sqlite3
app = Flask(__name__)
db=None

#fetchone=proximo registro / usr=cursor.fetchone()
#fetchall=todos los registros que quedan en una lista y un elemento / cursor.fetchall()
#se guardan en variables
#delet borra uno o mas registros de la tabla, si no pones where se borra todo, ? se guarda el nro

@app.route("/insertar/<string:mail>/<string:email>")
def testDB(usuario, email)
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("INSERT INTO usuario (usuarios, email) VALUES (?, ?)",(usuario, email))
    db.commit() 
    cursor.execute("SELECT COUNT(*) as cant FROM usuarios")
    res = cursor.fetchone() #obtiene el resultado de la consulta 
    nombre = res["usuario"]
    registros = res["cant"]
    cerrarConexion() #cierra conexion en la base de datos
    return f"nombre: {nombre}, mail: {email}"

@app.route("/borrar/<int:id>")
def borrar_usuarios(id):
    abrirConexion() #abre conexion en la base de datos
    db.execute(" DELETE FROM usuarios WHERE id=? ; ", (id,)) # ambos hacen lo mismo en el fondo: enviar comandos SQL a una base de datos y devolver los resultados. en este caso es mas facil db ya que esta definido
    db.commit() #guarda cambios realizados en la base de datos
    cerrarConexion() #cierra conexion en la base de datos
    return f"borre {id} de la tabla usuarios"

@app.route("/detalle/<int:id>")
def usuarios(id):
    abrirConexion()
    cursor = db.cursor() #crea un cursor para ejecutar la consulta en sql
    cursor.execute("SELECT usuario, email FROM usuarios WHERE id = ? ; ", (id,))    
    res = cursor.fetchone() #obtiene el resultado de la consulta 
    nombre = res["usuario"]
    mail = res["email"]
    db.commit() 
    cerrarConexion() #cierra conexion en la base de datos
    return f"nombre: {nombre}, mail: {mail}"

#ultima consgina

def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite") #se ve el resultad
   db.row_factory = dict_factory


def cerrarConexion(): #cierra conexion y vuelve aponer la conecion en none
   global db
   db.close()
   db = None


@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor() #ve los resultados
   cursor.execute("SELECT usuarios, email FROM usuarios; ") #ejecuta una consulta como en sql
   res = cursor.fetchone() #porque se sabe que solo hay un elemento
   registros = res["cant"] #diccionario, corchete cantidad devuelve dos
   cerrarConexion() #guarda en variable
   return f"Hay {registros} registros en la tabla usuarios" #arma mensaje que incluye numeros



#------------------CONEXION A BASE DE DATOS

def abrirConexion():
    global db
    db = sqlite3.connect('instance/datos.sqlite')
    db.row_factory = sqlite3.Row
    return db

def cerrarConexion(): 
    global db
    if db is not None:
        db.close()
        db=None

@app.route("/usuarios/")
def obtenerGente():
    global db
    conexion = abrirConexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor.fetchall()
    cerrarConexion()
    fila = [dict(row) for row in resultado]
    return str(fila)


#-----------------------------------------------------------------------------------------------------


@app.route("/")  #devuelve lo q ve en el navegador, ruta
def principal():
    url_hola = url_for("hello_world")
    #url_dado = url_for("dado", caras=6)
    url_logo = url_for("static", filename="img/badbo.jpeg")
    return """  
        <a href='/buenos dias'>buenos dias</a>
        <a href='/buenas noches'>buenas noches</a>
         <a href="{url_hola}">Hola</a>
        <br>
        <a href="{url_for("despedir")}">Chau</a>
         <br>
        <a href="{url_logo}">Logo</a> 
        <br>
        <a href="{url_dado}">Tirar_dado</a>
    """

@app.route("/buenos dias") #si se presiona hola se muestra holanda
def hello_world(): 
    return "<p>como amaneciste!</p>"

@app.route("/buenas noches") #hello_worldpero si se presiona chau muestra chau
def despedir():
    return "<p>descansa</p>"
#dos rutas y dos links

@app.route("/hola")
def saludar():
    return "<h2>Hola!</h2>"


@app.route("/hola/<string:nombre>") #el argumento nombre, se pasa por parametro en la ruta.
def saludar_con_nombre (nombre):
    return f"<h2>Hola {nombre}!</h2>"

def main():
    url_hola = url_for("hello_world") #es una variable, llama lo que esta en el def
    url_dado = url_for("dado", caras=6)
    url_logo = url_for("static", filename="img/badbo.jpeg")

    return f"""
    <a href="{url_hola}">Hola</a> #NN not null, sin valor
    <br>
    <a href="{url_for("despedir")}">Chau</a>
    <br>
    <a href="{url_logo}">Logo</a> 
    <br>
    <a href="{url_dado}">Tirar_dado</a>
    """