def main():
    massa_inicio: float = float(input())
    massa_fim: float = 0.5
    segundos: int = 0
    minutos: int = 0
    horas: int = 0
    
    while massa_inicio > massa_fim:
        massa_inicio /= 2
        segundos += 50
        if segundos > 60:
            segundos -= 60
            minutos += 1
        if minutos > 60:
            minutos -= 60
            horas += 1

    print(f"Demorou {horas}:{minutos}:{segundos}")


if __name__ == "__main__":
    main()