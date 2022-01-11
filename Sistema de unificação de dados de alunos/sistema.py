from itertools import groupby
 
alunos = []
media = []
 
 
def f_nota(): # Calcula média do aluno
    nota = []
    c_nota = 0
    while c_nota < 4:
     c_nota += 1
     d_nota =input('Digite as notas do aluno:')
     nota.append(d_nota)
     soma = sum([ float(s) for s in nota]) / 4
    media.append(soma)
 
 
 
 
def f_alunos(): # coleta o nome dos alunos
    c_aluno = 4
    while c_aluno % 4 == 0:
     c_aluno += 4
     aluno = input('Digite o nome do aluno: ')
     alunos.append(aluno)
     print(40*'*')
     f_nota()
     print(media)
     print(alunos)
     if c_aluno == 12:
         break
 
f_alunos()
 
 
base_de_dados = zip(alunos,media) #junta as 2 listas em uma unica base de dados
base_de_dados = list(base_de_dados)
funcao_anonima_media = lambda m:m [1] #função para ordernar as notas na base de dados
base_de_dados.sort(key=funcao_anonima_media)
 
valores_agrupados = groupby(base_de_dados,funcao_anonima_media) # agrupando a base de dados
 
for medias,grupo_alunos in valores_agrupados:
    print(30*'-')
 
    quant = len(list(grupo_alunos))
    print(f'{quant} alunos tiraram nota:{medias}')