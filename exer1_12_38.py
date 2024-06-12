import math

def main() -> None:
    x: float = float(input())
    e: float = x ** 0
    cont: int = 1
    exp: float = math.exp(x)
    diferenca: float = exp - e

    if diferenca < 0:
        diferenca *= -1

    while diferenca >= 0.0001:
        fatorial: float = 1
        for i in range(1, cont+1):
            fatorial *= i
        fracao: float = (x ** cont) / fatorial
        e += fracao
        cont += 1
        
        diferenca: float = exp - e

        if diferenca < 0:
            diferenca *= -1
    
    print(f"Por série: {e}. Por EXP: {exp}. X: {x}. Termos: {cont}")

if __name__ == "__main__":
    main()
