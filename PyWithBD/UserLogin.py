
from time import sleep
from EmailValidation import enviarcodigo
from EmailValidation import codigo
from ConnectBD import ConnectBD

#CONEXAO DO BD

bd = ConnectBD()
bd.conectar()


#FAZENDO REFERENCIA AO CURSOR DEFINIDO NO OUTRO ARQUIVO

cursor = bd.get_cursor()

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
i1 = True
i2 = True
i3 = True
i4 = True
i5 = True
i6 = True

while True:

    print(f'\n[ ------------------------- ]\n'
          f'[ LOGIN E CADASTRO DE CONTA ]\n'
          f'[ ------------------------- ]\n')
    print(f'[1] - Criar uma conta. \n'
          f'[2] - Logar uma conta já criada. \n'
          f'[3] - Sair do programa.\n')
    opcao = str(input('Selecione uma opção:'))

    if opcao == '1':

        while i2 == True:
            print(f'\n[ ------------------------ ]\n'
                  f'[     TELA DE CADASTRO     ]\n'
                  f'[ -------------------------]\n')

            Username = input('Digite o nome de usuário:').lower()


            if not Username.strip():
                print('O nome de usuário não pode estar vazio.')

            if ' ' in Username:
                print('O nome de usuário não pode ter espaços em branco.')


            cmdcond = f'SELECT nome FROM usuarios WHERE nome LIKE "{Username}"'
            cursor.execute(cmdcond)
            result = cursor.fetchall()

            nome_existe = False

            for nome in result:
                if nome[0] == Username:
                    nome_existe = True
                    break


            if nome_existe == False:

                while i6 == True:
                    Email = input('Digite seu endereço de email:')
                    if not Email.strip():
                        print('O email não pode estar vazio.')

                    if ' ' in Email:
                        print('O email não pode ter espaços em branco.')

                    cmdcond = f'SELECT email FROM usuarios WHERE email LIKE "{Email}"'
                    cursor.execute(cmdcond)
                    result = cursor.fetchall()

                    email_existe = False

                    for edmail in result:
                        if edmail[0] == Username:
                            email_existe = True
                            break

                    if email_existe == False:
                        enviarcodigo(Username, Email)
                        print('\nPor favor, confirme seu e-mail {}. Te enviaremos um código'.format(Email))
                        while i5 == True:
                            confcod = input('Digite o código:')

                            if confcod == codigo:
                                print('\nE-mail confirmado com sucesso!\n')
                                sleep(0.7)
                                while True:
                                    Senha = input("Digite sua senha:")
                                    if len(Senha) < 6:
                                        print(RED + 'ERRO: A senha não pode conter menos que 6 caracteres')

                                    if not Senha.strip():
                                        print('A senha não pode estar vazia')

                                    if ' ' in Senha:
                                        print('A senha não pode ter espaços em branco.')

                                    if not len(Senha) < 6 and Senha.strip() and ' ' not in Senha:
                                        comando = f'INSERT INTO usuarios (nome, senha, email) VALUES ("{Username}", "{Senha}","{Email}");'
                                        cursor.execute(comando)
                                        bd.mydb.commit()
                                        print(f'\n************************************************\n'
                                              f'Digite o número [2] e faça o login da sua conta.\n'
                                              f'************************************************\n')
                                        i5 = False
                                        i6 = False
                                        i2 = False
                                        break


                            else:
                                print(RED + 'ERRO: o código digitado não é igual ao código enviado')




            else:
                print(RED + "ERRO: O nome de usuário já está em uso.")


    elif opcao == '2':
        print(f'\n[ ------------------------ ]\n'
              f'[ TELA DE LOGIN DE USUARIO ]\n'
              f'[ -------------------------]\n')
        while i3 == True:

            UserLogin = input('Digite o nome de usuário:').lower()

            if not UserLogin.strip():
                print('O nome de usuário não pode estar vazio.')

            if ' ' in UserLogin:
                print('O nome de usuário não pode ter espaços em branco.')
            comando = f'SELECT nome FROM usuarios WHERE nome LIKE "{UserLogin}"'
            cursor.execute(comando)
            result = cursor.fetchall()

            nome_correto = False
            for nome in result:
                if nome[0] == UserLogin:
                    nome_correto = True
                    break

            if nome_correto == True:
                i3 = False

                while i4 == True:
                    Senha = input("Digite sua senha:")
                    comando = f'SELECT senha FROM usuarios WHERE senha LIKE "{Senha}"'
                    cursor.execute(comando)
                    result = cursor.fetchall()

                    senha_correta = False

                    for senha in result:
                        if senha[0] == Senha:
                            senha_correta = True
                            break
                    while i1 == True:
                        if senha_correta == True:
                            print(f'\n[ ------------------ ]\n'
                                f'[ LOGADO COM SUCESSO ]\n'
                                f'[ ------------------ ]\n')
                            print('[1] Sair da conta.\n'
                                '[2] Alterar sua senha.\n'
                                '[3] Deletar conta.')

                            opcao = str(input('Digite uma das opções:'))

                            if opcao == '1':
                                print('\nSaindo da conta...')
                                sleep(0.5)
                                i4 = False

                            elif opcao == '3':

                                comando = f'DELETE FROM usuarios WHERE nome = "{UserLogin}" AND senha = "{Senha}"'
                                cursor.execute(comando)
                                bd.mydb.commit()

                                print('\nSua conta foi deletada com sucesso!')
                                sleep(0.5)
                                i4 = False

                            elif opcao == '2':
                                i5 = True

                                while i5 == True:

                                    NovaSenha = input('Digite sua nova senha:')

                                    if len(NovaSenha) < 6:
                                        print(RED + 'ERRO: A senha não pode conter menos que 6 caracteres')

                                    if not NovaSenha.strip():
                                        print('A senha não pode estar vazia')

                                    if ' ' in NovaSenha:
                                        print('A senha não pode ter espaços em branco.')

                                    if not len(NovaSenha) < 6 and NovaSenha.strip() and ' ' not in NovaSenha:
                                        comando = f'UPDATE usuarios ' \
                                                f'SET senha = "{NovaSenha}" ' \
                                                f'WHERE nome = "{UserLogin}"'

                                        cursor.execute(comando)
                                        bd.mydb.commit()

                                        print('\nSua senha foi alterado com sucesso!')
                                        sleep(0.5)
                                        i5 = False
                                        i4 = False
                                        i1 = False

                            else:
                                print('\nERRO: Não há esta opção no programa. Por favor digite uma destas listadas.')
                        else:
                            print('\nERRO: Não há esta opção no programa. Por favor digite uma destas listadas.')
                    else:
                        print('ERRO: A senha digitada está incorreta.')
                        
            else:
                print('ERRO: O nome de usuário "{}" não existe.'.format(UserLogin))

    elif opcao == '3':
        break

    else:
        print( '\nERRO: Não há esta opção no programa. Por favor digite uma destas listadas.')