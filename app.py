from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "holaaaaa"

@app.route('/ruta1')
def saludo1():
    return "hola"

@app.route('/ruta2')
def saludo2():
    return "¡Hola! "

if __name__ == '__main__':
    app.run(debug=True)