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


if __name__ == "__main__":
    inicializar_db()
    print("Banco de dados físico criado com sucesso em /data!")
