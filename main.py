import time
from src import colletor, engine, exporter


def rodar_guardian():
    exporter.inicializar_db()
    print("Iniciando o Guardian...")

    while True:
        processos = colletor.capturar_processos()

        for proc in processos[:10]:
            score = engine.calcular_risco(proc)

            print(f"Monitorando: {proc['name']} | Risco: {score}%")
        time.sleep(60)


if __name__ == "__main__":
    rodar_guardian()
