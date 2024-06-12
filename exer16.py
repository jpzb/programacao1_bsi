def main() -> None:
    num_base_3: int = int(input())
    
    while num_base_3 >= 0:
        num_base_10: int = 0
        
        auxiliar: int = num_base_3
        cont: int = 0
        while auxiliar > 0:
            resto: int = auxiliar % 10
            num_base_10 += (3 ** cont) * resto
            cont += 1
            auxiliar //= 10
        print(num_base_3, num_base_10)
        num_base_3 = int(input())


if __name__ == "__main__":
    main()
