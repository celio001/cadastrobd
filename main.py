from conexaobd import ConsultaUsuarios

class Menu():
    def __init__(self):
        pass

    def menu(self):
        print('Bem-vindo ao sistema UserRegistry \n')
        #self.opcaomn = input('Digite o número do que deseja fazer: \n (1)logar\n (2)Consultar Usuarios\n (3)Cadastrar usuario\n')
        #self.login()
        self.exibirusUsuarios()
    
    def login(self):
        print('Bem-vindo a area de registro!')
        email = input('Inserir e-mail:')
        senha = input('Inserir senha:')
    
    def exibirusUsuarios(self):
        consulta = ConsultaUsuarios()
        return consulta.Usuariosdb()

iniciar = Menu()
iniciar.exibirusUsuarios()
