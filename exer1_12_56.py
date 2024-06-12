def main() -> None:
    for x in range(1, 11):
        x **= 2
        for y in range(6):
            denominador: int = (x * y) - (5 * y) - (3 * x) + 15
            if denominador:
                numerador: int = (x ** 2) + (3 * x) + (y ** 2)
                print(f"x={x} y={y} f({x}, {y})={numerador/denominador:.5f}")
            else:
                print(f"x={x} y={y} f({x}, {y})=indeterminado")


if __name__ == "__main__":
    main()
