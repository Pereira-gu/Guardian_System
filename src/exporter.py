import sqlite3
import os

DB_PATH = "data/database.db"


def inicializar_db():
    if not os.path.exists("data"):
        os.makedirs("data")

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Tabela de Processos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs_seguranca (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                modulo TEXT,
                descricao TEXT,
                score_risco INTEGER
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS logs_rede (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                ip_destino TEXT,
                porta INTEGER,
                status TEXT
            )
        """)
        conn.commit()


def salvar_log(modulo, descricao, score):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO logs_seguranca (modulo, descricao, score_risco) VALUES (?, ?, ?)",
                (modulo, descricao, score),
            )
            conn.commit()
    except sqlite3.OperationalError:
        print("⚠️ Banco ocupado (Power BI lendo?). Tentando novamente na próxima volta.")


def salvar_rede(ip, porta, status):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO logs_rede (ip_destino, porta, status) VALUES (?, ?, ?)",
                (ip, porta, status),
            )
            conn.commit()
    except sqlite3.OperationalError:
        pass
