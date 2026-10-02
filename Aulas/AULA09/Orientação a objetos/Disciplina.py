class Disciplina():
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
    def exibir_info(self):
        print(f"|Disciplina: {self.nome}    |Professor: {self.professor}|")


# TEMPORÁRIO
# cs = Disciplina( "Computer Science", "MauMau")
# cs.exibir_info()

