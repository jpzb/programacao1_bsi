def main() -> None:
    sucessor: int = 1
    anterior: int = 1
    cont: int = 0
    soma: float = 0
    numerador: int = 5
    termo: float = numerador / anterior
    while abs(termo) > 0.000001:
        soma += termo
        cont += 1
        if numerador > 0:
            print(f"+ {numerador}/{anterior}")
        else:
            print(f"- {abs(numerador)}/{anterior}")
        aux: int = sucessor
        sucessor += anterior
        anterior = aux
        numerador *= -1
        termo = numerador / anterior
    print(f"Qtd termos somados = {cont}")
    print(f"Soma total = {soma:7f}")


if __name__ == "__main__":
    main()
