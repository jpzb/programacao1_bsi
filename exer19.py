def calc_perimetro(l1: float, l2: float, l3: float) -> float:
    return l1 + l2 + l3


def calc_area(l1: float, l2: float, l3: float, perimetro: float) -> float:
    semi_perimetro: float = perimetro / 2
    area: float = (semi_perimetro * (semi_perimetro - l1) * (semi_perimetro - l2) * (semi_perimetro - l3)) ** 0.5
    return area
    

def type_triangulo(l1: float, l2: float, l3: float) -> str:
    if l1 == l2 == l3:
        return 'EQUILATERO'
    if l1 != l2 and l1 != l3 and l2 != l3:
        return 'ESCALENO'
    return 'ISOSCELES'


def is_triangulo(l1: float, l2: float, l3: float) -> bool:
    return l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2)


def main() -> None:
    l1: float = float(input())
    l2: float = float(input())
    l3: float = float(input())

    maior_area: float = 0
    l1_maior: float = 0
    l2_maior: float = 0
    l3_maior: float = 0
    
    soma_perimetro_escaleno: float = 0
    soma_perimetro_equilatero: float = 0
    soma_perimetro_isosceles: float = 0

    cont_escaleno: int = 0
    cont_isosceles: int = 0
    cont_equilatero: int = 0
    cont_triangulo: int = 0
    cont_nao_triangulo: int = 0
    cont_total: int = 0

    while l1 != 0 or l2 != 0 or l3 != 0:
        if is_triangulo(l1, l2, l3):
            cont_triangulo += 1
            tipo_triangulo: str = type_triangulo(l1, l2, l3)
            perimetro: float = calc_perimetro(l1, l2, l3)
            area: float = calc_area(l1, l2, l3, perimetro)

            if tipo_triangulo == "EQUILATERO":
                cont_equilatero += 1
                soma_perimetro_equilatero += perimetro
            elif tipo_triangulo == "ESCALENO":
                cont_escaleno += 1
                soma_perimetro_escaleno += perimetro
            else:
                cont_isosceles += 1
                soma_perimetro_isosceles += perimetro

            if area > maior_area:
                maior_area = area
                l1_maior = l1
                l2_maior = l2
                l3_maior = l3

            print(f"AREA = {area:.2f} PERIMETRO = {perimetro:.2f} TIPO = {tipo_triangulo}")
        else:
            print('NAO TRIANGULO')
            cont_nao_triangulo += 1
        l1 = float(input())
        l2 = float(input())
        l3 = float(input())
        cont_total += 1

    if cont_total:
        
        print(f"A maior area = {maior_area:.2f} eh do triangulo: lado1 = {l1_maior:.2f}, lado2 = {l2_maior:.2f} e lado3 = {l3_maior}")
        
        if cont_equilatero:
            perimetro_medio_equilateros: float = soma_perimetro_equilatero / cont_equilatero
            print(f"{perimetro_medio_equilateros:.2f} eh o perimetro medio dos triangulos equilateros")
        else:
            print("0.00 eh o perimetro medio dos triangulos equilateros")
          
        if cont_isosceles: 
            perimetro_medio_isosceles: float = soma_perimetro_isosceles / cont_isosceles
            print(f"{perimetro_medio_isosceles:.2f} eh o perimetro medio dos triangulos isosceles")
        else:
            print("0.00 eh o perimetro medio dos triangulos isosceles")
    
        if cont_escaleno:
            perimetro_medio_escalenos: float = soma_perimetro_escaleno / cont_escaleno
            print(f"{perimetro_medio_escalenos:.2f} eh o perimetro medio dos triangulos escalenos")
        else:
            print("0.00 eh o perimetro medio dos triangulos escalenos")

        print(f"Percentual de triangulos = {cont_triangulo * 100 / cont_total:.2f}")
        print(f"Percentual de nao triangulos = {cont_nao_triangulo * 100 / cont_total:.2f}")


if __name__ == "__main__":
    main()
