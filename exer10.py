def main() -> None:
    base10: int = int(input())
    letras_basehex: str = "0123456789ABCDEF"

    while base10 >= 0:
        basehex: str = ""
        auxiliar: int = base10

        if auxiliar == 0:
            basehex = "0"
        while auxiliar > 0:
            resto: int = auxiliar % 16
            basehex = letras_basehex[resto] + basehex
            auxiliar //= 16
        
        print(f"Num10 = {base10} Num16 = {basehex}")
        base10: int = int(input())



if __name__ == "__main__":
    main()
