import sqlite3 

class ConsultaUsuarios:
    def __init__(self):
        self.conexao = sqlite3.connect('usuarios.db')
        self.sql = self.conexao.cursor()
    
    #Extraindo e mostrando os usuarios da tabela
    def Usuariosdb(self):
        self.usuarios =  self.sql.execute('select * from usuario;')

        for self.usuario in self.usuarios:
            nome, email, senha, cpf, cargo = self.usuario
            print('\n')
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Senha: ******")
            print(f"CPF: *****")
            print(f"Cargo: {cargo}")
        self.conexao.close()
    
    #Adicionando usuario a nossa tabela de usuarios
    def cadastrarUsuario(self, nome: str, email: str, senha: str, cpf: int, cargo: str):
        self.cadastrar = []
        self.cadastrar.extend([nome, email, senha,cpf, cargo])

        self.sql.execute('insert into usuario values(?,?,?,?,?)', self.cadastrar)
    
        self.conexao.commit()
        self.conexao.close()

if __name__ == '__main__':
    iniciar = ConsultaUsuarios()
    iniciar.cadastrarUsuario()