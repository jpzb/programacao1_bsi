def f_calcula_area_triangulo(a: float, b: float) -> float:
    area: float = 0.0
    if a != 0 and b != 0:
        x_coordenada: float = (-b) / a
        y_ordenada: float = b

        if x_coordenada < 0:
            x_coordenada *= -1
        if y_ordenada < 0:
            y_ordenada *= -1
        
        area = (x_coordenada * y_ordenada) / 2

    return area


def main() -> None:
    # Declaracao e inicializacao de variaveis
    a: float = float(input())
    b: float = float(input())

    while a != 0 or b != 0:
        area: float = f_calcula_area_triangulo(a, b)
        print(f"AREA={area:.5f} A={a:.5f} B={b:.5f}")
    
        a = float(input())
        b = float(input())


if __name__ == "__main__":
    main()
