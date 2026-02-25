import sqlite3


def inicializar_db():
    conn = sqlite3.connect("data/database.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs_seguranca (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            modulo TEXT,
            descricao TEXT,
            score_risco FLOAT
        )
    """)
    conn.commit()
    conn.close()


def salvar_log(modulo, descricao, score_risco):
    """insere um novo registro de monitoramento no banco de dados"""
    try:
        conn = sqlite3.connect("data/database.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO logs_seguranca (modulo, descricao, score_risco)
            VALUES (?, ?, ?)
        """,
            (modulo, descricao, score_risco),
        )
        conn.commit()
    except Exception as e:
        print(f"Erro ao salvar log: {e}")


if __name__ == "__main__":
    inicializar_db()
    print("Banco de dados físico criado com sucesso em /data!")
