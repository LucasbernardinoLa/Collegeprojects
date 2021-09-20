# Um canal de jogos do youtube está fazendo um sorteio para angariar doações para
# pessoas em situação de vulnerabilidade social. A cada 10,00 doado o nome da
# pessoa é inserido em uma lista de sorteio, por exemplo:
# Ruth doou 20,00;
# Maria doou 30,00;
# Fernando doou 50,00;
# A lista de sorteio estará com os valores:
# listaSorteio = [‘Ruth’, ‘Ruth’, ’Maria’, ’Maria’, ’Maria’, ’Fernando’, ’Fernando’,
# ’Fernando’, ’Fernando’, ’Fernando’]
# Implemente um programa para cadastrar o nome das pessoas que doaram. O
# programa deve embaralhar a lista, sortear o ganhador e imprimir o seu nome.
# Imprima na tela um teste do seu programa utilizando como primeiro doador o seu
# nome e os dois últimos dígitos do seu RU para o valor doado. Não se esqueça de
# imprimir também a lista de sorteio.


import random
listaSort = []                          #lista vazia para receber valores.


def mult10(num):                        #Função para achar o número que multiplica as Strings com o
    res = num // 10                     # resultado da divisão do valor doado.
    return res


def sorteio():
    random.shuffle(listaSort)                  #Função para embaralhar e escolher o ganhador do sorteio
    print(f'lista embaralhada: {listaSort}')
    print()
    return random.choice(listaSort)


while True:                                                   # laço de repitição while, para loops infinitos
    print()
    cadastro = input('Deseja cadastrar um doador? sim - 1 // não - 0:  ')       #condição para cadastro

    if cadastro == '1' or cadastro == 'sim':
        print()
        valor = float(input('digite o valor doado: '))                             #dados a para inserção
        print()
        nome = (input('Digite o nome do doador: '))
        listaSort.extend(((nome + ' ') * int(mult10(valor))).split())           #Extend para jogar os valores no final
                                                                                #da lista. nome + str vazia para separar
    elif cadastro == '0' or cadastro == 'não':                                  #vezes a função de multiplicação de strs
        sorteiostart = input('Deséja iniciar o sorteio? sim - 1 // não - 0: ')  #e split para separar todas as strs
        print()

        if sorteiostart == '1' or sorteiostart == 'sim':
            print(f'esta é a lista do sorteio: {listaSort} ')           # condição para iniciar o sorteio
            print()
            print(f'O ganhador do concurso é :{sorteio()} ')

        else:
            encerrar = input('Deséja encerrar o programa? sim - 1 // não - 0: ')     # conidição para terminar o program

            if encerrar == '1' or encerrar == 'sim':                                  #caso não seja satisfeita, continue
                print('encerrando o programa..')
                break

            else:
                continue
