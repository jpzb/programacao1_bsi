"""
Feito por:
Gustavo Alves Caetano
João Pedro Zamborlini Barcellos
"""


def main() -> None:
    # Declaracao e inicializacao de variaveis
    a: float = float(input())
    b: float = float(input())
    area: float = 0

    while a != 0 or b != 0:
        if a == 0 or b == 0:
            print(f"A: {a}, B: {b}, ÁREA: 0")
        else:
            x_coordenada: float = (-b) / a
            y_ordenada: float = b

            if x_coordenada < 0:
                x_coordenada *= -1
            if y_ordenada < 0:
                y_ordenada *= -1
            
            area = (x_coordenada * y_ordenada) / 2

            print(f"A: {a}, B: {b}, ÁREA: {area}")
    
        a = float(input())
        b = float(input())


if __name__ == "__main__":
    main()
