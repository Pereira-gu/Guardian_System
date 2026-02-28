def calcular_risco(nome, cpu_usage=0, username="unknown"):
    score = 0
    nome_low = nome.lower()

    processos_criticos = {
        "powershell.exe": 60,
        "cmd.exe": 40,
        "regedit.exe": 50,
        "vbc.exe": 70,
    }

    score = processos_criticos.get(nome_low, 10)

    if cpu_usage > 70:
        score += 20
    elif cpu_usage > 30:
        score += 10

    privilegiados = ["root", "admin", "system"]

    user = (username or "unknown").lower()
    if user in privilegiados:
        score += 15

    return max(0, min(score, 100))
