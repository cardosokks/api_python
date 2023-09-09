from flask import Flask, jsonify

app = Flask(__name__)

frutas =  {
  "Abacaxi":  23,
  "Manga":  13,
  "Banana":  123,
  "Goiaba":  293
}

carros = {
  "Golf": "Azul",
  "Fusca": "Amarelo",
  "Ferrari": "Vermelha"
}  


@app.route('/')
def homepage():
    return ('''
  <h1>API ESTÁ ONLINE</h1>
  <p>Links Disponíveis Abaixo:</p>
  <a href="/frutas"> Frutas</a>
  <a href="/carros"> Carros</a>
  ''')


@app.route('/frutas')
def mostrarFrutas():
    return jsonify(frutas)


@app.route('/carros')
def mostrarCarros():
  return jsonify(carros)


app.run(host='0.0.0.0')