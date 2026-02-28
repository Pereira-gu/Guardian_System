import time
from src import engine, exporter, collector

pids_processados = set()


def rodar_guardian():
    exporter.inicializar_db()
    print("Iniciando o Guardian...")

    while True:
        processos = collector.capturar_processos()

        for proc in processos:
            pid = proc["pid"]
            score = engine.calcular_risco(
                nome=proc["name"],
                cpu_usage=proc.get("cpu_percent", 0),
                username=proc.get("username", "unknown"),
            )

            if pid not in pids_processados:
                pids_processados.add(pid)

                exporter.salvar_log("Processos", proc["name"], score)
                print(f"Monitorando: {proc['name']} | Risco: {score}% | Salvo No BD")

        print("-" * 30)
        time.sleep(60)


if __name__ == "__main__":
    rodar_guardian()
