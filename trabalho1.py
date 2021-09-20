# Escreva um programa que leia o nome de um aluno e sua nota final. Em seguida,
# informe o conceito conforme a tabela abaixo. A saída do programa deve exibir na tela uma
# frase com o padrão descrito a seguir:
# Nome do aluno: Fábio José
# Nota final: 73.4
# Frase a ser exibida: O aluno Fabio José tirou nota 3.5 e se enquadra no conceito D
# Nota Conceito
# De 0,0 a 2,9 E
# De 3,0 a 4,9 D
# De 5,0 a 6,9 C
# De 7 a 8,9 B
# De 9,0 a 10 A

while True:                                                        # Usei o laço de repitição while, para o número
    sair = input('Deseja inciar o programa? [S]im ou [N]ão: ')     # indefinido de loops

    if sair == 'N' or sair == 'n':                                 #Condição para terminar o laço.
        print('Encerrando programa. ')
        break

    nome = input('Digite o nome do aluno: ')                    #Entrada de dados para o programa.
    nota = float(input('Digite a nota do aluno: '))

    if nota > 10.0:
        print('Digite uma nota entre 0.0 a 10.0 ')
        print()
        continue

    elif nota <= 2.9:                                           #As condições para achar o conceito de acordo com as notas.
        print(f'Nome do aluno: {nome}')
        print(f'Nota final: {nota}')
        print(f'O aluno {nome} tirou a nota {nota} e se enquadra no conceito E. ')


    elif nota > 2.9 and nota <= 4.9:
        print(f'Nome do aluno: {nome}')
        print(f'Nota final: {nota}')
        print(f'O aluno {nome} tirou a nota {nota} e se enquadra no conceito D. ')


    elif nota > 4.9 and nota <= 6.9:
        print(f'Nome do aluno: {nome}')
        print(f'Nota final: {nota}')
        print(f'O aluno {nome} tirou a nota {nota} e se enquadra no conceito C. ')


    elif nota > 6.9 and nota <= 8.9:
        print(f'Nome do aluno: {nome}')
        print(f'Nota final: {nota}')
        print(f'O aluno {nome} tirou a nota {nota} e se enquadra no conceito B. ')


    elif nota > 8.9 and nota <= 10:
        print(f'Nome do aluno: {nome}')
        print(f'Nota final: {nota}')
        print(f'O aluno {nome} tirou a nota {nota} e se enquadra no conceito A. ')
