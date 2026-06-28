from flask import Flask, render_template, redirect, request
from database import criar_tabela, inserir_log, buscar_log, contar_logs_por_tipo,buscar_logs_por_tipo, buscar_logs_por_ip
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

app = Flask(__name__)
app.secret_key = 'segredo123'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class Usuario(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def carregar_usuario(id):
    from database import buscar_usuario_por_id
    usuario = buscar_usuario_por_id(id)
    if usuario:
        return Usuario(usuario[0], usuario[1])
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    from flask import request
    from werkzeug.security import check_password_hash
    from database import buscar_usuario
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        usuario = buscar_usuario(username)
        if usuario and check_password_hash(usuario[2], password):
            user = Usuario(usuario[0], usuario[1])
            login_user(user)
            return redirect('/')
        return render_template("login.html", erro="Usuário ou senha incorreto!")
    return render_template("login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/')
@login_required
def index():
    tipo = request.args.get('tipo','')
    ip = request.args.get('ip','')
    if tipo:
        logs = buscar_logs_por_tipo(tipo)
    elif ip:
        logs = buscar_logs_por_ip(ip)
    else:
        logs = buscar_log()
    contagem = contar_logs_por_tipo()
    return render_template('index.html', logs=logs, contagem=contagem, tipo=tipo, ip=ip)

@app.route('/importar')
@login_required
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
@login_required
def deletar(id):
    from database import deletar_log
    deletar_log(id)
    return redirect('/')

@app.route('/editar/<int:id>')
@login_required
def editar(id):
    from database import buscar_log_por_id
    log = buscar_log_por_id(id)
    return render_template("editar.html", log=log)

@app.route('/inserir', methods=['POST'])
@login_required
def inserir():
    from flask import request
    date = request.form['date']
    hour = request.form['hour']
    type = request.form['type']
    ip = request.form['ip']
    message = request.form['message']
    inserir_log(date, hour, type, ip, message)
    return redirect('/')

@app.route('/atualizar/<int:id>', methods=['POST'])
@login_required
def atualizar(id):
    from flask import request
    from database import atualizar_log
    date = request.form['date']
    hour = request.form['hour']
    type = request.form['type']
    ip = request.form['ip']
    message = request.form['message']
    atualizar_log(id, date, hour, type, ip, message)
    return redirect('/')

if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)
