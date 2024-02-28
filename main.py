from conexaobd import ConsultaUsuarios
import os

class Menu():
    def __init__(self):
        os.system('cls')
        self.db = ConsultaUsuarios()

    def menu1(self):
        print('Bem-vindo ao sistema UserRegistry \n')
        self.opcaomn1 = int(input('Digite o número do que deseja fazer: \n (1)logar\n (2)Mostrar usuarios\n (3)Sair\n Digite: '))
        while self.opcaomn1 <= 0 or self.opcaomn1 >= 3:
            print('!! Digitar uma opção valida !!')
            self.opcaomn1 = input('Digite o número do que deseja fazer: \n (1)logar\n (2)Sair\n')

        if self.opcaomn1 == 1:
            self.login()
        elif self.opcaomn1 == 2:
            self.exibirusUsuarios1()
        elif self.opcaomn1 == 3:
            exit()

    def menu2(self):
        print('[ Seja bem vindo ]')
        self.opcaomn2 = int(input('Digite o número do que deseja fazer: \n (1)Cadastrar usuario\n (2)Consultar usuario\n (3)Consultar usuarios\n Digite: '))
        while self.opcaomn2 <= 0 or self.opcaomn2 >= 3:
            print('!! Digitar uma opção valida !!')
            self.opcaomn1 = input('Digite o número do que deseja fazer: \n (1)Cadastrar usuario\n (2)Consultar usuario\n (3)Consultar usuarios\n Digite:')

        if self.opcaomn1 == 1:
            self.cadastrarUsuarios()
        elif self.opcaomn1 == 2:
            self.consultarUsuario()
        elif self.opcaomn1 == 3:
            self.exibirusUsuarios2()


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
                    self.menu2()
        else:
            print('Login realizado com sucesso!')
            self.menu2()

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
    
    def exibirusUsuarios1(self):
        return self.db.Usuariosdb1()
    
    def exibirusUsuarios2(self):
        return self.db.Usuariosdb2()
    
    def cadastrarUsuarios(self):
        print('[ Area de cadastro de usuarios ]')
        self.nome = input('Nome: ')
        self.email = input('E-mail: ')
        self.senha = input('Senha: ')
        self.cpf = input('CPF: ')
        self.cpfverificado = self.verificarCpf(self.cpf)
        self.cargo = input('Cargo: ')
        
        self.db.cadastrarUsuario(self.nome,self.email,self.senha,self.cpf, self.cargo)
    
    def resetSenha(self):
        print('[ Informar CPF do usuario ]')
        self.cpf = input('Digite:')
        self.cpfverificado = self.verificarCpf(self.cpf)
        self.novasenha = input('Digitar nova senha:')
        self.db.resetSenha(self.cpfverificado, self.novasenha)
        self.menu2()

    def deletarUsuario(self):
        print('[ Area de exclusão de usuario]\n Informar CPF do usuario')
        self.user = input('Digitar:')
        self.userVerificado = self.verificarCpf(self.user)
        self.db.deletarUser(self.userVerificado)

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
    iniciar.deletarUsuario()
