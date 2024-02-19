import sqlite3 

class ConsultaUsuarios:
    def __init__(self):
        self.conexao = sqlite3.connect('usuarios.db')
        self.sql = self.conexao.cursor()
    
    def Usuariosdb(self):
        self.usuarios =  self.sql.execute('select * from usuario;')

        for self.usuario in self.usuarios:
            nome, email, senha, telefone, cargo = self.usuario
            print('\n')
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Senha: ******")
            print(f"CPF: {******}")
            print(f"Cargo: {cargo}") 

if __name__ == '__main__':
    iniciar = ConsultaUsuarios()
    iniciar.Usuariosdb()