import math


def funcao_f(x: float) -> float:
    return 1/ (1 + x ** 2)


def funcao_g(x: float) -> float:
    return x ** 2


def funcao_h(x: float) -> float:
    return math.sin(x)
    

def calcula_integral(n: int) -> float:
    h: float = 1 / n
    area_total: float = 0.0
    for i in range(n):
        area_trapezio: float = calcula_area_trapezio(funcao_f(h * i), funcao_f(h * (i + 1)), h)
        area_total += area_trapezio
    return area_total


def calcula_area_trapezio(base_menor: float, base_maior: float, h: float) -> float:
    return (base_maior + base_menor) * h / 2


def main() -> None:
    n: int = int(input())

    while n > 0:
        area: float = calcula_integral(n)
        pi: float = area * 4
        print(f"n={n} area={pi:.6f}")
        n = int(input())


if __name__ == "__main__":
    main()
