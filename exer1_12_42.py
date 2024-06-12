def main() -> None:
    x1: float = float(input())
    y1: float = float(input())
    x2: float = float(input())
    y2: float = float(input())

    while x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
        distancia: float = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        print(distancia)
        x1 = float(input())
        y1 = float(input())
        x2 = float(input())
        y2 = float(input())

main()
