def main():
    num = 4
    pi = 4
    pa = 1
    sinal = -1
    cont = 0
    while num >= 0.0001:
        pa += 2
        num = 4 / pa
        pi += num * sinal
        cont += 1
        sinal *= -1
    print(pi)
    print(cont)


if __name__ == "__main__":
    main()
