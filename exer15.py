def main() -> None:
    num: int = int(input())

    while num > 0:
        cont_divisores: int = 0
        soma_divisores: int = 0
        for div in range(1, (num // 2)):
            if num % div == 0:
                cont_divisores += 1
                soma_divisores += div
        print(f"Num={num} Media Divisores={soma_divisores/cont_divisores}")
        num = int(input())


if __name__ == "__main__":
    main()
