def main() -> None:
    somatorio: int = 1
    for i in range(2, 65):
        somatorio +=  (2 ** i)
    print(somatorio)


if __name__ == "__main__":
    main()
