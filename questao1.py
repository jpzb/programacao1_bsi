def main() -> None:
    nome_candidato1: str = input()
    nome_candidato2: str = input()
    nome_candidato3: str = input()

    cont_candidato1: int = 0
    cont_candidato2: int = 0
    cont_candidato3: int = 0
    cont_branco: int = 0
    cont_nulo: int = 0

    voto: int = int(input())
    

    while voto != 0:
        if voto < 0 or voto > 5:
            print("VOTO INVALIDO")
        else:
            if voto == 1:
                cont_candidato1 += 1
            elif voto == 2:
                cont_candidato2 += 1
            elif voto == 3:
                cont_candidato3 += 1
            elif voto == 4:
                cont_branco += 1
            else:
                cont_nulo += 1
        voto = int(input())

    soma_votos_validos: int = cont_candidato1 + cont_candidato2 + cont_candidato3 + cont_branco
    if soma_votos_validos <= cont_nulo:
        print("ELEICAO INVALIDA")
    else:
        print(f"{nome_candidato1} {cont_candidato1} votos {(cont_candidato1/soma_votos_validos)*100:.2f}%")
        print(f"{nome_candidato2} {cont_candidato2} votos {(cont_candidato2/soma_votos_validos)*100:.2f}%")
        print(f"{nome_candidato3} {cont_candidato3} votos {(cont_candidato3/soma_votos_validos)*100:.2f}%")
        print(f"{cont_branco} votos em branco")
        print(f"{cont_nulo} votos nulos")

        if cont_candidato1 > cont_candidato2 and cont_candidato1 > cont_candidato3:
            print(f"VENCEDOR = {nome_candidato1}")
        elif cont_candidato2 > cont_candidato3:
            print(f"VENCEDOR = {nome_candidato2}")
        else:
            print(f"VENCEDOR = {nome_candidato3}")


if __name__ == "__main__":
    main()
