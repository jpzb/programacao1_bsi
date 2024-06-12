def main():
    maior_nota: float = 0
    menor_nota: float = 100
    media_turma: float
    soma_notas: float = 0
    reprovados: int = 0
    reprovados_por_faltas: int = 0

    for i in range(100):
        matricula: int = int(input())
        nota1: float = float(input())
        nota2: float = float(input())
        nota3: float = float(input())
        codigo: str
        aulas_frequentadas: int = int(input())
        
        nota_final: float = (nota1 + nota2 + nota3) / 3
        soma_notas += nota_final

        if nota_final > maior_nota:
            maior_nota = nota_final
        elif nota_final < menor_nota:
            menor_nota = nota_final
            
        if nota_final < 60:
            reprovados += 1
            codigo = "reprovado"
        elif aulas_frequentadas < 40:
            reprovados += 1
            reprovados_por_faltas += 1
            codigo = "reprovado"
        else:
            codigo = "aprovado"
        
        print(f"Matrícula: {matricula}. Frequência: {aulas_frequentadas}. Nota final: {nota_final}. Código: {codigo}")
    
    media_turma = soma_notas / 100
    print(f"Média da turma: {media_turma}")

    
main()
