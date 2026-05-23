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