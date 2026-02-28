import psutil


def capturar_processos():
    processos = []
    for proc in psutil.process_iter(
        ["pid", "name", "username", "cpu_percent", "memory_percent"]
    ):
        try:
            processos.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processos


def capturar_conexoes():
    conexoes = []
    for conn in psutil.net_connections(kind="inet"):
        if conn.status == "ESTABLISHED" and conn.raddr:
            conexoes.append(
                {
                    "ip_destino": conn.raddr.ip,
                    "porta": conn.raddr.port,
                    "status": conn.status,
                }
            )
    return conexoes
