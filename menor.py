def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    menor = num1

    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3

    print(menor)


if __name__ == "__main__":
    main()
