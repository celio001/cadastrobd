import sqlite3 

class ConsultaUsuarios:
    def __init__(self):
        self.conexao = sqlite3.connect('usuarios.db')
        self.sql = self.conexao.cursor()
    
    #Extraindo e mostrando os usuarios da tabela
    def Usuariosdb1(self):
        self.usuarios =  self.sql.execute('select nome, email, cargo from usuario;')

        for self.usuario in self.usuarios:
            nome, email, cargo = self.usuario
            print('\n')
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Cargo: {cargo}")
        self.conexao.close()
    
    def Usuariosdb2(self):
        self.usuarios =  self.sql.execute('select * from usuario;')

        for self.usuario in self.usuarios:
            nome, email,senha, cpf, cargo = self.usuario
            print('\n')
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"senha: {senha}")
            print(f"cpf: {cpf}")
            print(f"Cargo: {cargo}")
        self.conexao.close()
    
    #Adicionando usuario a nossa tabela de usuarios
    def cadastrarUsuario(self, nome: str, email: str, senha: str, cpf: int, cargo: str):
        self.cadastrar = []
        self.cadastrar.extend([nome, email, senha,cpf, cargo])

        self.sql.execute('insert into usuario values(?,?,?,?,?)', self.cadastrar)
    
        self.conexao.commit()
        self.conexao.close()
    
    def exibirUsuario(self, cpf):
        #comando de pesquisa no banco
        self.usuario = self.sql.execute(f'select * from usuario where CPF="{cpf}"')
        self.resultado = self.usuario.fetchall()# recuperar todas as linhas do resultado
        if not self.resultado:  # Verifica se a lista de resultados está vazia
            return print('Nenhum usuário encontrado para o CPF fornecido.')
        else:
            for self.a in self.resultado:
                    nome, email, senha, cpf, cargo = self.a
                    print('\n')
                    print(f"Nome: {nome}")
                    print(f"Email: {email}")
                    print(f"Senha: {senha}")
                    print(f"CPF: {cpf}")
                    print(f"Cargo: {cargo}")
                    self.conexao.close()

    def logar(self, email, senha):
        self.usuario = self.sql.execute(f'select * from usuario where EMAIL="{email}" and SENHA="{senha}";')
        self.resultado = self.usuario.fetchall()
        self.conexao.close()
        return self.resultado
    
    
    def resetSenha(self, cpf, senha):
        self.usuario = self.sql.execute(f'select * from usuario where CPF="{cpf}"')
        self.resultado = self.usuario.fetchall()# recuperar todas as linhas do resultado
        if not self.resultado:  # Verifica se a lista de resultados está vazia
            return print('Nenhum usuário encontrado para o CPF fornecido.')

        self.sql.execute(f'update usuario set senha="{senha}" where cpf={cpf};')
        self.conexao.commit()
        self.conexao.close()
        return print('Reset realizado com sucesso')
    
    def deletarUser(self, cpf):
        self.usuario = self.sql.execute(f'select * from usuario where CPF="{cpf}"')
        self.resultado = self.usuario.fetchall()# recuperar todas as linhas do resultado
        if not self.resultado:  # Verifica se a lista de resultados está vazia
            return print('Nenhum usuário encontrado para o CPF fornecido.')
        self.sql.execute(f'delete from usuario where CPF={cpf};')
        



if __name__ == '__main__':
    iniciar = ConsultaUsuarios()
    iniciar.resetSenha(80289002087, 'Guis@123')