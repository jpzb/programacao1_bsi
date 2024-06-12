def verifica(num):
    try:
        num = int(num)
        if num > 0:
            return f"O {num} é positivo"
        if num < 0:
            return f"O {num} é negativo"
        return f"O {num} é nulo"
    except ValueError as err:
        return f"Precisa ser um valor numérico. {err}"


def main():
    num = input()
    print(verifica(num))
    return 0


if __name__ == "__main__":
    main()
