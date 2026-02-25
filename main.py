import time
from src import collector
from src import engine, exporter


def rodar_guardian():
    exporter.inicializar_db()
    print("Iniciando o Guardian...")

    while True:
        processos = collector.capturar_processos()

        for proc in processos[:10]:
            score = engine.calcular_risco(proc)

            exporter.salvar_log(
                modulo="Monitoramento de Processos",
                descricao=f"Processo: {proc['name']} | PID: {proc['pid']}",
                score_risco=score,
            )

            print(f"Monitorando: {proc['name']} | Risco: {score}% | Salvo No BD")
        print("-" * 30)
        time.sleep(60)


if __name__ == "__main__":
    rodar_guardian()
