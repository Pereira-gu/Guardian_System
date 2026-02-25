def calcular_risco(evento):
    score = 0
    if "powershell" in evento["name"].lower():
        score += 70

    elif "chrome" in evento["name"].lower() or "code" in evento["name"].lower():
        score += 5

    else:
        score += 20

    return score
