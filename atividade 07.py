## Atividade 07 do Projeto Integrador - Por Ana Beatriz Martins

'''
Olá. Este é o exercício 07 do projeto integrador dos Cursos de Ciências de Dados e Bioinformática do 
Centro Universitário Metodista Izabela Hendrix. Neste exercício, vamos começar a trabalhar com python.
'''

''' 1. Em comentários, explique o que cada comando faz: '''

5 + 5 # soma os valores 5 e 5
8 - 6 # subtrai 6 de 8
12 * 5 # multiplica 12 por 5
4**2 # calcula a raiz quadrada de 4
27**(1/3) # calcula a raiz cubica de 27
27 / 3 # divide 27 por 4
27 // 4 # mostra o quociente da divisão de 27 por 4
27 % 4  #mostra o resto da divisão de 27 por 4

print('Este exercício é muito legal!') # printa a frase "Este exercicio é muito legal"
x = 7 # atribui o 7 ao X
print('O exercício ' + str(x) + ' é muito fácil!') # printa na tela a frase "O exercício 7 é muito fácil!", transformando a variavel x em texto/string
x, y = 5, 6 # atribui os valores 5 e 6 à X e Y, respectivamente
print(x, y) # printa na tela os valores de X e Y, separados por um espaço
print('Aprendi na escola que o {} vem antes do {}'.format(x, y)) # printa a frase "Aprendi na escola que o 5 vem antes do 6"

meuNome = 'Neylson Crepalde' # atribui Neylson Crepalde ao objeto meuNome
print(meuNome[:8]) #printa até o oitavo item de meuNome
print(meuNome[8:]) # printa a partir do oitavo item de meuNome

galera = ['Neylson', 'Edésio', 'Layla', 'Gerson', 'Iago','Ester', 'Juliany', 'Marcos', 'Patrick', 
          'Bia', 'Fabiano', 'Larissa', 'Sávio', 'Túlio', 'Vanessa', 'Numiá', 'Adelvan', 'Nelson', 
          'Warley', 'Vladimir'] # cria a lista Galera, com os nomes indicados

galera[1] # printa o segundo item da lista, Édesio
galera[0] # printa o primeiro item da lista, Neylson
galera[:5] # printa os cinco primeiros itens da lista
galera[10:] # printa a partir do decimo primeiro item da lista, Fabiano 
galera[6:15] # printa do sétimo ao decimo quinto nome da lista



'''
2. Crie três listas. A primeira deve conter o nome de 5 amigos de infância. 
A segunda deve conter o nome e 5 animais de estimação.
A terceira deve conter três pratos que você adora comer (use a criatividade). Exiba o conteúdo das listas.
'''
amigos = ['Caroline', 'Amanda', 'Emanuelle', 'Priscila', 'Franciele']
animais = ['Melanie', 'Izzie', 'Yang', 'Happy', 'Harry']
pratos = ['Lua Blanco', 'Lasanha', 'Pizza']

print(amigos, animais, pratos)



''' 3. Printe o nome do terceiro amigo da lista. '''
amigos [2]

''' 4. Bole uma frase bonitinha para chamar um bicho e insira nesse frase o nome do último bicho de estimação.
Printe a frase na tela.'''

print(f'Ei, {animais[4]}, meu neneeeem, vem aqui, vem!')



'''5. Exiba na tela uma frase perguntando o que você quer comer no jantar essa noite e dê três opções: o segundo, terceiro e 
quarto pratos. (dica, use os comandos print e .format)'''

print(f'Boa noite! Você ja decidiu o que comer? Se não, tenho três excelentes opções! \n \
1){pratos[0]} \n \
2){pratos[1]} \n \
3){pratos[2]}')

 ''' 6. Crie um objeto chamado nomeCompleto e atribua a ele o seu nome completo como uma string. '''
 
 nomeCompleto = 'Ana Beatriz Martins de Oliveira'


''' 7. Usando apenas slices (subsettings de um dado de texto) exiba apenas seu primeiro nome, apenas seu nome do meio e apenas seu
sobrenome, um por vez.'''

print(nomeCompleto[:3])
print(nomeCompleto[11:19])
print(nomeCompleto[11:])

'''
8. Crie um dicionário com dados sobre a sua casa. Pense em dados que seriam interessantes de serem usados numa pesquisa de
verdade - quantidade de moradores, bairro de localização, nomes das pessoas que moram, idade, cor, sexo, tipo de moradia
(casa ou apartamento) e mais quatro campos. Use a criatividade!!! Lembre-se de que num dicionário, os valores podem ser
qualquer tipo de dado (string, int, float, listas, dicionários, etc.) e podem também ser de qualquer tamanho.
 '''
casa = {'quantidade de moradores': 4,
        'quantidade de animais': 10,
        'bairro': 'Vale das Acácias',
        'nomes': ['Ana', 'Augusto', 'Maria', 'José'],
        'idades': [18, 28, 52, 60],
        'cor': ['Branca(o)','Branca(o)','Branca(o)','Preta(o)'],
        'sexo': ['Feminino','Masculino', 'Feminino', 'Masculino'],
        'tipo de moradia': ['Casa'],
        'estado civil': ['Solteira(o), Solteira(o), Casada(o)', 'Casada(o)'],
        'horas em casa por dia': [16, 5, 24, 10],
        'horas no celular por dia': [8, 7, 10, 24],
        }


''' 9. Exiba apenas as chaves do dicionário. Exiba apenas os valores do dicionário.'''
casa.keys()
casa.values()

''' 10.Exiba apenas o nome da segunda pessoa que mora na sua casa.'''

casa['nomes'][1]

''' 11. Escolha mais duas informações relevantes e exiba no console.'''

casa ['quantidade de moradores']
casa ['bairro']