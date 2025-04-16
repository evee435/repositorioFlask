from flask import Flask, url_for
import sqlite3
app = Flask(__name__)
db=None

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