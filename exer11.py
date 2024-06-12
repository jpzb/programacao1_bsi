import math

def main() -> None:
    qtd: int = int(input())

    for _ in range(qtd):
        num: float = float(input())
        e: float = 0
        cont: int = 0
        fatorial: int = 1
        exp: float = math.exp(num)
        diferenca: float = exp - e
        if diferenca < 0:
            diferenca *= -1

        while diferenca >= 0.0001:
            fracao: float = (num ** cont) / fatorial
            cont += 1
            fatorial *= cont
            e += fracao
            diferenca: float = exp - e
            if diferenca < 0:
                diferenca *= -1
        print(f"x={num:.10f} Exponencial Serie={e:.10f} Exponencial Funcao={exp:.10f} Qtd Termos={cont}")


if __name__ == "__main__":
    main()
