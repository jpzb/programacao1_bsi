def main() -> None:
    n: int = int(input())
    m: int = int(input())

    string: str = f"N = {n} M = {m} \n"
    while n <= m:
        for i in range(1, 11):
            string += f"{n} x {i} = {n * i} \n"
        n += 1
    
    print(string)


if __name__ == "__main__":
    main()
