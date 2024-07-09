def calcula_arranjo(m: int, p: int) -> float:
    fatorial_m: int = calcula_fatorial(m)
    fatorial_mp: int = calcula_fatorial(m - p)
    return fatorial_m / fatorial_mp


def calcula_combinacao(p: int, arranjo: float) -> float:
    fatorial_p: int = calcula_fatorial(p)
    return arranjo / fatorial_p


def calcula_fatorial(n: int) -> int:
    fatorial: int = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial


def main() -> None:
    m: int = int(input())
    p: int = int(input())
    while m != 0 and p != 0:
        if m < p:
            arranjo: int  = 0
            combinacao: int = 0
        else:
            arranjo: float = calcula_arranjo(m, p)
            combinacao: float = calcula_combinacao(p, arranjo)

        print(f"Para M={m} e P={p} => Arranjo={arranjo} Combinacao={combinacao}")
        m = int(input())
        p = int(input())


if __name__ == "__main__":
    main()
