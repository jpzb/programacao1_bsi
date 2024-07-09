def calcula_diaria(diaria: int, aumento: int, n: int) -> int:
    if n <= 14:
        valor_diario: int = diaria + (n - 1) * aumento
    else:
        valor_diario: int = diaria + 14 * aumento
    total: int = valor_diario * (32 - n)
    return total


def main() -> None:
    diaria: int = int(input())
    aumento: int = int(input())
    n: int = int(input())
    print(calcula_diaria(diaria, aumento, n))


if __name__ == "__main__":
    main()
