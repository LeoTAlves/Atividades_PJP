from conexao import conectar

class Aluno:
    def __init__(self, nome_aluno, media, id_aluno):
        self.id = id
        self.nome_aluno = nome_aluno
        self.media = media

    def exibir(self):
        texto = f"""
        Matricula: {self.id}
        Aluno: {self.nome_aluno}
        Media: {self.media}
        """
        print(f"{texto}")

    def salvar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO aluno (nome_aluno) VALUES (%s)"
        cursor.execute(sql, (self.nome_aluno))

        conexao.commit()
        conexao.close()

def lista_alunos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "SELECT * FROM aluno"
    cursor.execute(sql)

    alunos = []
    for id_aluno, nome_aluno, media in cursor.fetchall():
        aluno = Aluno(nome_aluno, media, id_aluno)
        alunos.append(aluno)
        print(aluno)
    conexao.close()
    print(alunos)
    return alunos