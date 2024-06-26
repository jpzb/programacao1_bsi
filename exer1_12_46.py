def verificaPosicao(x: float,  y:float) -> str:
    if y < 0:
        y *= -1
    
    retorno: str = ""

    if (x / 3) < y < (3 * x):
        retorno = f"x={x:.2f} y={y:.2f} INTERIOR"
    else:
        retorno = f"x={x:.2f} y={y:.2f} EXTERIOR"
    return retorno


def main() -> None:
    x: float = float(input())
    y: float = float(input())

    while x != 0 or y != 0:
        print(verificaPosicao(x, y))
        x = float(input())
        y = float(input())
    

if __name__ == "__main__":
    main()
