import psutil


def capturar_processos():
    processos = []
    for proc in psutil.process_iter(["pid", "name", "username"]):
        try:
            processos.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processos


def capturar_conexoes():
    return psutil.net_connections(kind="inet")
