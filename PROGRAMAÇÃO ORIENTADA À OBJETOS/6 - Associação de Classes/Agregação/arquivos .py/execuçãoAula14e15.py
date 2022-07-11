from Aula14e15 import *;

ufpi = Universidade('UFPI', 'Universidade Federal do Piauí', 'Federal')
uespi = Universidade('UESPI', 'Universidade Estadual do Piauí', 'Estadual')
pucsp = Universidade('PUC-SP', 'Pontificia Universicade Católica de São Paulo', 'Privada')

maria = Aluno('48952036547', 'Maria', 'SISU')
joao = Aluno('120368945236', 'João', 'PROUNI')
eva = Aluno('87423001598', 'Eva', 'SISU')
carlos = Aluno('02211568747', 'Carlos', 'Portador de diploma')

ufpi.cadastrarAluno(maria)
uespi.cadastrarAluno(carlos)
pucsp.cadastrarAluno(joao)
uespi.cadastrarAluno(eva)

print(ufpi)
print(uespi)
print(pucsp)