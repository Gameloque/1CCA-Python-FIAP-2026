from Aluno import Aluno
from Disciplina import Disciplina

#Criar / Instanciar 1 aluno
aluno1 = Aluno("João", "123456", "Sciêmncia das Computações")
#print(aluno1)

#Criar / Instanciar 2 Disciplinas
sers = Disciplina("Soluções Renováveis", "Tritiack")
model_mat = Disciplina("Modelagem Matemática", "Roberto")

# print(sers.nome)
# model_mat_exibir_infos()

# Matricular o aluno nas 2 disciplinas
aluno1.matricular(model_mat)
aluno1.matricular(sers)
# print(aluno1.disciplinas[1].professor)

# Adicionar as notas referente às disciplina
aluno1.adicionar_nota(model_mat, 10)
aluno1.adicionar_nota(model_mat, 7)
aluno1.adicionar_nota(sers, 6)
aluno1.adicionar_nota(sers, 8)
# print(aluno1.notas_por_disciplina)
print(aluno1.calcular_media_d(model_mat))