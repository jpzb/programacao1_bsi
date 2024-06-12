def main():
    l1 = float(input())
    l2 = float(input())
    l3 = float(input())

    if l1 >= (l2 + l3) or l2 >= (l1 + l3) or l3 >= (l1 + l2):
        print("NAO EH TRIANGULO")
    else:
        if l1 == l2 and l1 == l3:
            print("EQUILATERO")
        elif l1 != l2 and l2 != l3 and l1 != l3:
            print("ESCALENO")
        else:
            print("ISOSCELES")
    return 0


if __name__ == "__main__":
    main()
