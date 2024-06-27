def validar(num: str) -> bool:
    pos: int = 0

    """
    while pos < len(num) and valido:
        if num[pos] not in "012":
            return False
    return True
    """

    valido: bool = True
    while pos < len(num) and valido:
        if num[pos] not in "012":
            valido = False
        pos += 1
    return valido


def converte3_10_int(base3: int) -> int:
    base10: int = 0
    cont: int = 0
    while base3 > 0:
        alg: int = base3 % 10
        base10 += (3 ** cont) * alg
        base3 //= 10
        cont += 1
    return base10


def converte3_10(base3: str) -> int:
    potencia: int = 0
    num_base_10: int = 0

    base3 = base3[::-1]
    for i in base3:
        num_base_10 += (3 ** potencia) * int(i)
        potencia += 1  

    return num_base_10


def main() -> None:
    num_base_3: str = input()

    while num_base_3.strip()[0] != "-":

        if validar(num_base_3):
            num_base_10: int = converte3_10(num_base_3)
            print(f"Num3={num_base_3} Num10={num_base_10}")
        else:
            print(f"Num3={num_base_3} INVALIDO")
        num_base_3 = input()


if __name__ == "__main__":
    main()
