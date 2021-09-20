def email(nome, sobrenome, mail, ru):                   #Criei a função usando os 4 parâmetros pedidos e concatenando eles
    res = nome.__getitem__(0) + sobrenome + ru + mail   # para criar o email
    return res


nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
ru = input('Digte os dois últimos digítos do seu RU:  ')
x = email(nome, sobrenome, '@algoritmos.com.br', ru)             #Depois utilizei Fstrings para formatar o print
print(f'Sr {nome}, seu email é: {x}')
