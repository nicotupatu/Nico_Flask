from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Verificador de Edad</h1>"

@app.route("/edad")
@app.route("/edad/<int:edad>")
def verificar_edad(edad=0):
    if edad < 18:
        mensaje = "Menor de edad"
    elif edad < 60:
        mensaje = "Adulto"
    else:
        mensaje = "Adulto mayor"
    
    return f"<h1>La persona tiene {edad} años y es: {mensaje}</h1> <hr>"

if __name__ == '__main__':
    app.run(debug=True)