# Feito por Gustavo Alves Caetano e João Pedro Zamborlini Barcellos
def f_calcula_mdc(n: int, m: int) -> int:
    resto: int = 0
    while (n % m) > 0:
        resto = n % m
        n = m
        m = resto
    return m


def main() -> None:
    for _ in range(25):
        n1: int = int(input())
        n2: int = int(input())
        n3: int = int(input())

        mdc = f_calcula_mdc(n1, n2)
        mdc = f_calcula_mdc(mdc, n3)
        print(f"MDC({n1}, {n2}, {n3})={mdc}")


if __name__ == "__main__":
    main()
