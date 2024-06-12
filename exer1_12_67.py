def main() -> None:
    for num in range(5000, 7001):
        cont: int = 0
        for i in range(1, (num//2) + 1):
            if num % i == 0:
                cont += 1
        if cont == 1:
            print(num)

main()
