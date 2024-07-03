def verificaPosicao(x: float,  y:float) -> str:
    retorno: str = ""

    y1: float = 3 * x
    y2: float = x / 3

    if (y2 > y > y1) or (y2 < y < y1):
        retorno = "INTERIOR"
    else:
        retorno = "EXTERIOR"
    return retorno


def main() -> None:
    x: float = float(input())
    y: float = float(input())

    while x != 0 or y != 0:
        string: str = verificaPosicao(x, y)
        print(f"x={x:.2f} y={y:.2f} {string}")
        x = float(input())
        y = float(input())
    

if __name__ == "__main__":
    main()
