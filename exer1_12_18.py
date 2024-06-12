"""def calcula_pontuacao(tempo_padrao, tempo_equipe) -> float:
    diferenca = tempo_padrao - tempo_equipe
    
    if diferenca < 0:
        diferenca *= -1
    if diferenca < 3:
        return 100
    if 3 <= diferenca <= 5:
        return 80
    return 80 - (diferenca - 5) / 5"""


def main():
    tempo_padrao1: float = float(input())
    tempo_padrao2: float = float(input())
    tempo_padrao3: float = float(input())
    maior_pontuacao: float = 0
    numero_inscricao: str = input()

    while numero_inscricao != "9999":
        tempo_equipe1: float = float(input())
        tempo_equipe2: float = float(input())
        tempo_equipe3: float = float(input())
        pontuacao_total: float
        pontuacao_etapa1: float
        pontuacao_etapa2: float
        pontuacao_etapa3: float

        # pontuacao_etapa1 = calcula_pontuacao(tempo_padrao1, tempo_equipe1)

        diferenca_etapa1: float = tempo_padrao1 - tempo_equipe1
        if diferenca_etapa1 < 0:
            diferenca_etapa1 *= -1
        if diferenca_etapa1 < 3:
            pontuacao_etapa1 = 100
        elif 3 <= diferenca_etapa1 <= 5:
            pontuacao_etapa1 = 80
        else: 
            pontuacao_etapa1 = 80 - (diferenca_etapa1 - 5) / 5
        
        # pontuacao_etapa2 = calcula_pontuacao(tempo_padrao2, tempo_equipe2)

        diferenca_etapa2: float = tempo_padrao2 - tempo_equipe2
        if diferenca_etapa2 < 0:
            diferenca_etapa2 *= -1
        if diferenca_etapa2 < 3:
            pontuacao_etapa2 = 100
        elif 3 <= diferenca_etapa2 <= 5:
            pontuacao_etapa2 = 80
        else: 
            pontuacao_etapa2 = 80 - (diferenca_etapa2 - 5) / 5

        # pontuacao_etapa3 = calcula_pontuacao(tempo_padrao3, tempo_equipe3)

        diferenca_etapa3: float = tempo_padrao3 - tempo_equipe3
        if diferenca_etapa3 < 0:
            diferenca_etapa3 *= -1
        if diferenca_etapa3 < 3:
            pontuacao_etapa3 = 100
        elif 3 <= diferenca_etapa3 <= 5:
            pontuacao_etapa3 = 80
        else:
            pontuacao_etapa3 = 80 - (diferenca_etapa3 - 5) / 5
        

        pontuacao_total = pontuacao_etapa2 + pontuacao_etapa1 + pontuacao_etapa3

        if pontuacao_total > maior_pontuacao:
            maior_pontuacao = pontuacao_total
        

        print(f"Inscrição: {numero_inscricao}. Etapa 1: {pontuacao_etapa1}. Etapa 2: {pontuacao_etapa2}." + 
            f" Etapa 3: {pontuacao_etapa3}. Pontuação total: {pontuacao_total}")
        
        numero_inscricao = int(input())
    
    print(f"Maior pontuação: {maior_pontuacao}")



main()
