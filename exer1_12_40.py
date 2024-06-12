from math import cos as cosseno


def main() -> None:
    x: float = float(input())
    cont: int = 0
    cos: float = 0
    fatorial: int = 1
    multiplicador: int = 1

    for _ in range(20):
        fracao: float = (x ** cont) / fatorial
        cont += 2
        fatorial *= cont * (cont - 1)
        cos += fracao * multiplicador
        multiplicador *= -1
        print(cont, fatorial, fracao, cos)
    print(cos)
    print(cosseno(x))


if __name__ == "__main__":
    main()
