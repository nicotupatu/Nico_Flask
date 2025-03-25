from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return "holaaaa"

@app.route('/ecuacion/<int:x>/<int:z>')
def calcular_ecuacion(x, z):
    y = x * z + z + x
    return f"<h1>El resultado de la ecuación es: {y}</h1>"

@app.route('/tabla/<int:numero>')
def tabla_multiplicar(numero):
    tabla = [f"{numero} x {i} = {numero * i}" for i in range(1, 11)]
    return "<h1>Tabla de multiplicar del {}</h1><pre>{}</pre>".format(numero, "\n".join(tabla))

@app.route('/area/circulo/<float:radio>')
def area_circulo(radio):
    import math
    area = math.pi * radio**2
    return f"<h1>El área del círculo con radio {radio} es: {area:.2f}</h1>"

@app.route('/area/cuadrado/<float:lado>')
def area_cuadrado(lado):
    area = lado**2
    return f"<h1>El área del cuadrado con lado {lado} es: {area:.2f}</h1>"

@app.route('/area/triangulo/<float:base>/<float:altura>')
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return f"<h1>El área del triángulo con base {base} y altura {altura} es: {area:.2f}</h1>"

if __name__ == '__main__':
    app.run(debug=True)