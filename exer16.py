def main() -> None:
    num_base_3: int = int(input())

    while num_base_3 >= 0:
        num_base_10: int = 0
        
        auxiliar: int = num_base_3
        erro: bool = False
        cont: int = 0
        while auxiliar > 0 and not erro:
            resto: int = auxiliar % 10
            if str(resto) not in "012":
                erro = True
            num_base_10 += (3 ** cont) * resto
            cont += 1
            auxiliar //= 10
        if erro:
            print(f"Num3={num_base_3} INVALIDO")
        else:
            print(f"Num3={num_base_3} Num10={num_base_10}")
        num_base_3 = int(input())


if __name__ == "__main__":
    main()
