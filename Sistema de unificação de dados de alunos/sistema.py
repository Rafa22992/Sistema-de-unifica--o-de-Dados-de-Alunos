from itertools import groupby

alunos = []
media = []
séries = []

print(74*'-')
print(30*' ','SISTEMA UNIFICADO ESCOLAR')
print(74*'-')

def quantidade():
    quant = input('Digite a quantidade de alunos: ')
    print(74*'-')
    return quant

def f_nota(): # Calcula média do aluno
    nota = []
    c_nota = 0
    while c_nota < 4:
     c_nota += 1
     d_nota =input('Digite as notas do aluno:')
     nota.append(d_nota)
     soma = sum([ float(s) for s in nota]) / 4
    media.append(soma)

quantidade_de_alunos = quantidade()

def f_alunos(): # coleta o nome dos alunos
    c_aluno = 0
    while c_aluno < int(quantidade_de_alunos): #<--- quant de alunos
     c_aluno += 1
     aluno = input('Digite o nome do aluno: ')
     alunos.append(aluno)
     print(40*'*')
     f_nota()
     print(media)
     print(alunos)

f_alunos()


base_de_dados = zip(alunos,media) #junta as 2 listas em uma unica base de dados
base_de_dados = list(base_de_dados)
funcao_anonima_media = lambda m:m [1] #função para ordernar as notas na base de dados
base_de_dados.sort(key=funcao_anonima_media)

valores_agrupados = groupby(base_de_dados,funcao_anonima_media) # agrupando a base de dados
#------------------------------------------------------------------------------------
 # EM DESENVOLVIMENTO
for a,objeto in valores_agrupados:
    print(a)