def main() -> None:
    x: float = float(input())
    y: float = float(input())

    while x != 0 or y != 0:
        if y < 0:
            y *= -1
        
        if (x / 3) < y < (3 * x):
            print(f"x={x:.2f} y={y:.2f} INTERIOR")
        else:
            print(f"x={x:.2f} y={y:.2f} EXTERIOR")
        x = float(input())
        y = float(input())
    

main()
