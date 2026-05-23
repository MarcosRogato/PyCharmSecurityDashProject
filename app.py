from flask import Flask, render_template, redirect
from database import criar_tabela, inserir_log, buscar_log
import requests

app = Flask(__name__)

@app.route('/')
def index():
    logs = buscar_log()
    return render_template("index.html", logs=logs)

@app.route('/importar')
def importar():
    with open("logs_v2.log", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split()
            date = partes[0]
            hour = partes[1]
            type = partes[2]
            ip = partes[3]
            message = " ".join(partes[4:])
            inserir_log(date, hour, type, ip, message)
    return "Logs importados com sucesso!"

@app.route('/deletar/<int:id>')
def deletar(id):
    from database import deletar_log
    deletar_log(id)
    return redirect('/')

@app.route('/editar/<int:id>')
def editar(id):
    from database import buscar_log_por_id
    log = buscar_log_por_id(id)
    return render_template("editar.html", log=log)

@app.route('/inserir', methods=['POST'])
def inserir():
    from flask import request
    date = request.form['date']
    hour = request.form['hour']
    type = request.form['type']
    ip = request.form['ip']
    message = request.form['message']
    inserir_log(date, hour, type, ip, message)
    return redirect('/')


if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)