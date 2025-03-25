from flask import Flask

app = Flask(__name__)

## Ruta principal
@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"

## Ruta para calcular el promedio de notas
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0, nota2=0, nota3=0):
    resultado = (nota1 * 30) / 100 + (nota2 * 30) / 100 + (nota3 * 40) / 100
    return f"<h1>El resultado es: {resultado:.2f}</h1> <hr>"

## Ejecutar la app en modo debug
if __name__ == '__main__':
    app.run(debug=True)