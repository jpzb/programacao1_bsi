def main():
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    
    if num1 > num2 or num1 > num3:
        if num2 < num3:
            aux = num1
            num1 = num2
            num2 = aux
        else:
            aux = num1
            num1 = num3
            num3 = aux
    if num2 > num3:
        aux = num2
        num2 = num3
        num3 = aux
    print(num1, num2, num3)


if __name__ == "__main__":
    main()
