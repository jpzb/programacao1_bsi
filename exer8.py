def main() -> None:
    # Declaração de variáveis
    num_base_10: int = int(input())

    # Processamento
    while num_base_10 > 0:
        # Declaração de variáveis
        num_base_2: int = 0
        multiplicador: int = 1
        auxiliar: int = num_base_10

        # Processamento
        while auxiliar > 0:
            resto: int = auxiliar % 2
            num_base_2 += resto * multiplicador
            auxiliar //= 2
            multiplicador *= 10
        
        # Saída de dados
        print(f"Num10 = {num_base_10} Num2 = {num_base_2}")
        num_base_10 = int(input())


if __name__ == "__main__":
    main()
