import math


def calcula_area(raio):
    return math.pi * (raio ** 2)


def calcula_perimetro(raio):
    return math.pi * raio * 2


def main():
    try:
        raio = float(input())
    except ValueError as err:
        print(f"Erro: {err}")
    
    peri = calcula_perimetro(raio)
    
    area = calcula_area(raio)
    
    print(f"Raio = {raio: .4f}")
    print(f"Perimetro = {peri: .4f}")
    print(f"Area = {area: .4f}")


if __name__ == "__main__":
    main()