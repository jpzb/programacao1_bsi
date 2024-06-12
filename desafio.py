def main():
    a = float(input())
    b = float(input())

    b += a
    a = b - a
    b = b - a
    print(a, b)


if __name__ == "__main__":
    main()
