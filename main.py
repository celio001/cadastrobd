from conexaobd import ConsultaUsuarios
import os

class Menu():
    def __init__(self):
        os.system('cls')

    def menu1(self):
        print('Bem-vindo ao sistema UserRegistry \n')
        self.opcaomn1 = int(input('Digite o número do que deseja fazer: \n (1)logar\n (2)Sair\n'))
        while self.opcaomn1 <= 0 or self.opcaomn1 >= 3:
            print('!! Digitar uma opção valida !!')
            self.opcaomn1 = input('Digite o número do que deseja fazer: \n (1)logar\n (2)Sair\n')

        if self.opcaomn1 == 1:
            self.login()
        elif self.opcaomn1 == 2:
            exit()

    def login(self):
        print('Bem-vindo a area de registro!')
        self.email = input('Inserir e-mail:')
        self.senha = input('Inserir senha:')
    
    def exibirusUsuarios(self):
        consulta = ConsultaUsuarios()
        return consulta.Usuariosdb()
    
    def cadastrarUsuarios(self):
        print('[ Area de cadastro de usuarios ]')
        self.nome = input('Nome: ')
        self.email = input('E-mail: ')
        self.senha = input('Senha: ')
        self.cpf = input('CPF: ')
        self.cargo = input('Cargo: ')
        
        self.cadastrar = ConsultaUsuarios
        self.cadastrar.cadastrarUsuario(self.nome,self.email,self.senha,self.cpf, self.cargo)

iniciar = Menu()
iniciar.cadastrarUsuarios()
