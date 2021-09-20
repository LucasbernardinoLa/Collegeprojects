# Exercício 4:
# Considere a tabela a seguir referente a produtos armazenados em um
# depósito, em que são considerados o estoque atual de cada produto e o estoque
# mínimo necessário.
# Código Estoque Mínimo
# 1 35 20
# 5 75 50
# 2 43 45
# 3 26 18
# 20 35 20
# Armazene as informações acima em uma estrutura de lista com dicionário,
# substituindo a primeira linha com os dados: no campo código coloque o primeiro
# digito do seu RU, no estoque os dois dígitos seguintes de seu RU, e no campo
# mínimo os dois últimos dígitos do seu RU.
# Por exemplo, tendo o RU: 123456
# Código Estoque Mínimo
# 1 23 56
# 5 75 50
# 2 43 45
# 3 26 18
# 20 35 20
# As informações devem ser inseridas no dicionário via teclado. Ao digitar o código 0
# (zero), o programa interrompe a leitura e se encerra. Ordene os produtos em ordem
# crescente de código. Imprima na tela um teste do seu programa usando como
# primeiro cadastro o primeiro digito do seu RU, como estoque os dois dígitos
# seguintes de seu RU, e como mínimo os dois últimos dígitos do seu RU.
from operator import itemgetter

dicio = {}                                      #lista e dict vazios
lista = []

for i in range(5):                        # laço for para 5 iterções
    dicio['Código'] = int(input('Digite o código do produto ou 0 para enecerrar o programa: '))
    print()
    if dicio['Código'] == '0':                 # input de dados com as chaves do dicts e condição para fechar o programa
        break
    dicio['Estoque'] = int(input('Digite a quantidade de itens no estoque: '))
    print()
    dicio['Mínimo'] = int(input('Digite a quantidade mínima necessária do estoque: '))
    print()
    lista.append(dicio.copy())            #inserção de dados do dict copiado para lista

listaordenada = sorted(lista, key=itemgetter('Código'))        #var de de organização do dict
print(listaordenada)                                           #dict organizado

