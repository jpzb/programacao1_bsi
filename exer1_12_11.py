def main():
    codigo_curso: int = int(input())
    maior_candidato_vaga: int = 0
    codigo_curso_maior: int
    total_candidatos: int = 0


    while codigo_curso != 0:
        vagas: int = int(input())
        numero_homens: int = int(input())
        numero_mulheres: int = int(input())
        total: int = numero_homens + numero_mulheres
        total_candidatos += total

        porcentagem_mulheres: float = numero_mulheres / total
        
        candidato_vaga: float = total / vagas

        if maior_candidato_vaga < candidato_vaga:
            maior_candidato_vaga = candidato_vaga
            codigo_curso_maior = codigo_curso
        
        print(f"Código do curso: {codigo_curso}. Candidatos por vaga: {candidato_vaga}. Candidatos sexo feminino " +
            f"(%): {porcentagem_mulheres}")
        
        codigo_curso = int(input())

    print(f"Curso com maior numero de candidatos por vaga: {codigo_curso_maior}. Candidato por vaga: {maior_candidato_vaga}")
    print(f"Total de candidatos: {total_candidatos}")


main()