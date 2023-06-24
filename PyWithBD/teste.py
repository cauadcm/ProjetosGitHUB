from time import sleep
from EmailValidation import enviarcodigo
from EmailValidation import codigo
from ConnectBD import ConnectBD

#CONEXAO DO BD

bd = ConnectBD()
bd.conectar()


#FAZENDO REFERENCIA AO CURSOR DEFINIDO NO OUTRO ARQUIVO

cursor = bd.get_cursor()


def teladecadastro():

    while True:
        print(f'\n[ ------------------------ ]\n'
              f'[     TELA DE CADASTRO     ]\n'
              f'[ -------------------------]\n')

        Username = input('Digite o nome de usuário:').lower()

        if not Username.strip():
            print('O nome de usuário não pode estar vazio.')

        elif ' ' in Username:
            print('O nome de usuário não pode ter espaços em branco.')

        else:
            cmdcond = f'SELECT nome FROM usuarios WHERE nome LIKE "{Username}"'
            cursor.execute(cmdcond)
            result = cursor.fetchall()

            nome_existe = False

            for nome in result:
                if nome[0] == Username:
                    nome_existe = True
                    break

            if nome_existe == False:

                while True:
                    Email = input('Digite seu endereço de email:')

                    if not Email.strip():
                        print('O email não pode estar vazio.')

                    if ' ' in Email:
                        print('O email não pode ter espaços em branco.')

                    else:

                        cmdcond = f'SELECT email FROM usuarios WHERE email LIKE "{Email}"'
                        cursor.execute(cmdcond)
                        result = cursor.fetchall()

                        email_existe = False

                        for edmail in result:
                            if edmail[0] == Email:
                                email_existe = True
                                break

                        if email_existe == False:
                            enviarcodigo(Username, Email)
                            print('\nPor favor, confirme seu e-mail {}. Te enviaremos um código'.format(Email))
                            while True:
                                confcod = input('Digite o código:')

                                if confcod == codigo:
                                    print('\nE-mail confirmado com sucesso!\n')
                                    sleep(0.7)
                                    while True:
                                        Senha = input("Digite sua senha:")
                                        if len(Senha) < 6:
                                            print('ERRO: A senha não pode conter menos que 6 caracteres')

                                        elif not Senha.strip():
                                            print('A senha não pode estar vazia')

                                        elif ' ' in Senha:
                                            print('A senha não pode ter espaços em branco.')

                                        else:
                                            comando = f'INSERT INTO usuarios (nome, senha, email) VALUES ("{Username}", "{Senha}","{Email}");'
                                            cursor.execute(comando)
                                            bd.mydb.commit()
                                            print(f'\n************************************************\n'
                                                  f'Digite o número [2] e faça o login da sua conta.\n'
                                                  f'************************************************\n')



                                else:
                                    print('ERRO: o código digitado não é igual ao código enviado')

                        else:
                            print('ERRO: o email digitado já existe')


            else:
                print("ERRO: O nome de usuário já está em uso.")



teladecadastro()