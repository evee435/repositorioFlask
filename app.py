from flask import Flask

app = Flask(__name__)

@app.route("/")  #devuelve lo q ve en el navegador
def principal():
    return """  
        <a href='/buenos dias'>buenos dias</a>
        <a href='/buenas noches'>buenas noches</a>
    """

@app.route("/buenos dias") #si se presiona hola se muestra holanda
def hello_world(): 
    return "<p>como amaneciste!</p>"

@app.route("/buenas noches") #pero si se presiona chau muestra chau
def despedir():
    return "<p>descansa</p>"
#dos rutas y dos links

@app.route("/hola")
def saludar():
    return "<h2>Hola!</h2>"
@app.route("/hola/<string:nombre>") #el argumento nombre, se pasa por parametro en la ruta.
def saludar_con_nombre (nombre):
    return f"<h2>Hola {nombre}!</h2>"