def media_divisores(num: int) -> float:
    soma: int = num
    cont: int = 1
    for i in range(1, num//2 + 1):
        if num % i == 0:
            cont += 1
            soma += i
    return soma / cont


def main() -> None:
    num: int = int(input())
    while num > 0:
        print(f"Num={num} Media Divisores={media_divisores(num)}")
        num = int(input())


if __name__ == "__main__":
    main()
