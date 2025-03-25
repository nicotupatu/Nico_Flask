from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores, columnas, filas=0):
    if filas == 0:
        arreglo = np.random.randint(0, valores, size=columnas)  # Vector
    else:
        arreglo = np.random.randint(0, valores, size=(filas, columnas))  # Matriz

    return f"<h1>El arreglo aleatorio es:</h1> <pre>{arreglo}</pre>"

if __name__ == '__main__':
    app.run(debug=True)