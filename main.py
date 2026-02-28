import time
from src import engine, exporter, collector


def rodar_guardian():
    exporter.inicializar_db()
    intervalo = 60  # 1 minuto

    print("Iniciando o Guardian...")

    while True:
        proxima_execucao = time.time() + intervalo
        processos = collector.capturar_processos()

        for proc in processos:
            score = engine.calcular_risco(
                nome=proc["name"],
                cpu_usage=proc.get("cpu_percent", 0),
                username=proc.get("username", "unknown"),
            )
            exporter.salvar_log("Processos", proc.get("name"), score)

        conexoes = collector.capturar_conexoes()
        for conn in conexoes:
            exporter.salvar_log(
                "Rede",
                f"IP: {conn['ip_destino']}, Porta: {conn['porta']}, Status: {conn['status']}",
                10,
            )
        print(f"✅ Ciclo de telemetria concluído às {time.strftime('%H:%M:%S')}")
        espera = proxima_execucao - time.time()
        if espera > 0:
            time.sleep(espera)
        else:
            continue


if __name__ == "__main__":
    rodar_guardian()
