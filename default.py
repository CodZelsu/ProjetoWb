from app.main import cliente
from app.connect import inserir
from app.default import Pessoa
from flask import Flask, render_template
import pandas as pd
from flask.globals import request
from tinydb import TinyDB

app = Flask(__name__)
@app.route('/')
def cadastro():
    mostrarTodos = ("pessoa")
    result = mostrarTodos()
    return render_template("cadastro.html", result = result)

app.route("/", methods=["POST", "GET"])
def cadastrar():
    nome = request.form["nome"]
    telefone = request.form["telefone"]
    email = request.form["email"]
    senha = request.form["senha"]
    pessoa = Pessoa(nome, telefone, email, senha)
    inserir(pessoa)
    return render_template("cadastro.html")
if __name__=="__main__":
    app.run(debug=True)