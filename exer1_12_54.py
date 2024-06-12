def main() -> None:
    y: float = float(input())
    aproximacao: float = y / 2

    print(f"Raiz quadrada de {y:.2f} aproximacao 1 = {aproximacao:.2f}")
    for i in range(2, 21): 
        aproximacao = ((aproximacao ** 2) + y) / (2 * aproximacao)
        print(f"Raiz quadrada de {y:.2f} aproximacao {i} = {aproximacao:.2f}")


if __name__ == "__main__":
    main()
