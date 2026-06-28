import sqlite3

def conectar():
    conn = sqlite3.connect('database.db')
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            hour INTEGER,
            type TEXT,
            ip TEXT,
            message TEXT
            )    
        ''')
    conn.commit()
    conn.close()

def inserir_log(date, hour, type, ip, message):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO logs (date, hour, type, ip, message)
    VALUES (?, ?, ?, ?, ?)''', (date, hour, type, ip, message))
    conn.commit()
    conn.close()

def buscar_log():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    logs = cursor.fetchall()
    conn.close()
    return logs

def atualizar_log(id,date, hour, type, ip, message):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE logs SET date = ?, hour = ?, type = ?, ip = ?, message = ? WHERE id = ?''', (date, hour, type, ip, message, id))
    conn.commit()
    conn.close()

def deletar_log(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM logs WHERE id = ?''', (id,))
    conn.commit()
    conn.close()

def buscar_log_por_id(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs WHERE id = ?", (id,))
    log = cursor.fetchone()
    conn.close()
    return log

def criar_tabela_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios 
    ( id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def buscar_usuario(username):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def inserir_usuario(username, password):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO usuarios (username, password)
                   VALUES (?, ?)''', (username, password))
    conn.commit()
    conn.close()

def buscar_usuario_por_id(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def contar_logs_por_tipo():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''SELECT type, COUNT(*) FROM logs GROUP BY type''')
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def buscar_logs_por_tipo(tipo):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs WHERE type = ?", (tipo,))
    logs = cursor.fetchall()
    conn.close()
    return logs

def buscar_logs_por_ip(ip):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs WHERE ip = ?", (ip,))
    logs = cursor.fetchall()
    conn.close()
    return logs
