def main():
    marco1: float = float(input())
    marco2: float = float(input())

    while marco1 != marco2:
        distancia: float = marco2 - marco1
        velocidade: int = 20
        for i in range(6):
            tempo: float = distancia / velocidade
            if tempo > 2:
                print(f"Marco 1: {marco1}. Marco 2: {marco2}. Velocidade {velocidade}. Tempo decorrido (h): {tempo}")
            velocidade += 10
        marco1 = float(input())
        marco2 = float(input())


main()
