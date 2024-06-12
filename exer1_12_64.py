def main() -> None:
    for j in range(100):
        soma_div: int = 0
        num: int = int(input())
        for i in range(1, num//2 + 1):
            if num % i == 0:
                soma_div += i
        if soma_div == num:
            print(f"Número perfeito: {num}")
        else:
            print(f"Número não perfeito: {num}")


if __name__ == "__main__":
    main()
