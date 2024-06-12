def main() -> None:
    converte10_3()
    

def converte10_3() -> None:
    base10: int = int(input())
    while base10 != 0:
        base3: int = 0
        cont: int = 1
        aux: int = base10
        while aux > 0:
            resto: int = aux % 3
            base3 += resto * cont
            aux //= 3
            cont *= 10
        print(base10, base3)
        base10 = int(input())


def converte3_10() -> None:
    base3: int = int(input())
    while base3 != 0:
        base10: int = 0
        cont: int = 0
        aux: int = base3
        while aux > 0:
            alg: int = aux % 10
            base10 += (3 ** cont) * alg
            aux //= 10
            cont += 1
        print(base3, base10)
        base3 = int(input())


main()
