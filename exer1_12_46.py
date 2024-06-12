def main() -> None:
    x: float = float(input())
    y: float = float(input())

    while x != 0 or y != 0:
        if y < 0:
            y *= -1
        
        if (x / 3) < y < (3 * x):
            print("INTERIOR")
        else:
            print("EXTERIOR")
        x = float(input())
        y = float(input())
    

main()
