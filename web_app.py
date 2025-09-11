from flask import Flask, render_template
from app import carregar_tarefas

app = Flask(__name__)

@app.route("/")

def index():

    tarefas_atuais = carregar_tarefas()
    return render_template("index.html", lista_de_tarefas=tarefas_atuais)