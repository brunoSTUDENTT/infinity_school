'''O sistema de avaliação de uma determinada disciplina obedece aos seguintes critérios:
Durante o semestre são dadas três notas;
A nota final é obtida pela média aritmética das três notas;
É considerado aprovado o aluno que obtiver a nota final superior ou igual a 6 e que tiver comparecido
 a um mínimo de 40 aulas.'''

media_nota = 0
i = 0
soma_nota = 0
pres = int(input('informe qtas h/aula foram assistidas: '))
while i < 3:
    nota = int(input('informe a nota: '))
    i += 1
    soma_nota += nota
    media_nota = soma_nota / i

if pres >= 40 and media_nota >= 6:
    print(f' pres = {pres} e media = {media_nota}. o aluno esta aprovado')
else:
    print (f' pres = {pres} e media = {media_nota}. o aluno esta aprovado')

print(soma_nota, media_nota)
