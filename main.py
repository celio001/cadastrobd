from conexaobd import ConsultaUsuarios
import os

class Menu():
    def __init__(self):
        os.system('cls')
        self.db = ConsultaUsuarios()

    def menu1(self):
        print('Bem-vindo ao sistema UserRegistry \n')
        self.opcaomn1 = int(input('Digite o número do que deseja fazer: \n (1)logar\n (2)Cadastrar\n (3)Sair\n Digite: '))
        while self.opcaomn1 <= 0 or self.opcaomn1 >= 3:
            print('!! Digitar uma opção valida !!')
            self.opcaomn1 = input('Digite o número do que deseja fazer: \n (1)logar\n (2)Sair\n')

        if self.opcaomn1 == 1:
            self.login()
        elif self.opcaomn1 == 2:
            pass

    def login(self):
        print('\nBem-vindo a area de login!')
        self.email = input('Inserir e-mail:')
        self.senha = input('Inserir senha:')
        self.relogin = self.db.logar(self.email, self.senha)
        if not self.relogin:#Se o banco não retornar valor
            self.tentativas = 3
            #Laço de tentativas de login
            for self.tentativa in range (self.tentativas):
                self.tentativa+=1
                if not self.relogin:
                    if self.tentativa <= 2:
                        print('\n[ Usuario não encontrado ]')
                        self.email = input('Inserir e-mail:')
                        self.senha = input('Inserir senha:')
                        self.relogin = self.db.logar(self.email, self.senha)
                else:
                    pass
        else:
            print('Login realizado com sucesso!')
    
    def exibirusUsuarios(self):
        return self.db.Usuariosdb()
    
    def cadastrarUsuarios(self):
        print('[ Area de cadastro de usuarios ]')
        self.nome = input('Nome: ')
        self.email = input('E-mail: ')
        self.senha = input('Senha: ')
        self.cpf = input('CPF: ')
        self.cpfverificado = self.verificarCpf(self.cpf)
        self.cargo = input('Cargo: ')
        
        self.db.cadastrarUsuario(self.nome,self.email,self.senha,self.cpf, self.cargo)
        
    def verificarCpf(self, cpf):
            self.cpf = cpf
            while self.cpf.isdigit() is not True:
                if not self.cpf.isdigit():
                    print('Digitar apenas números!')
                self.cpf = input('CPF: ')
                     
            while True:
                if len(self.cpf) == 11:
                    break
                else:
                    print('O cpf conter apenas 11 digitos')
                    self.cpf = input('CPF: ')
            return int(self.cpf)
    
    def consultarUsuario(self):
        print('[ Area consulta de usuario ]')
        self.usuario = input('Digitar cpf do usuario para consulta')
        self.cpfvalido = self.verificarCpf(self.usuario)
        self.db.exibirUsuario(self.cpfvalido)



if __name__ == '__main__':
    iniciar = Menu()
    iniciar.menu1()
