import os
import platform
from email_validation import send_code, verification_code
from dbconnect import Dbconnect

from time import sleep




def clean_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

database = Dbconnect()
database.connect_database()
cursor = database.get_cursor()


def register_screen():  
    
    while True:
                clean_screen()

                print(f'\n[ ------------------------ ]\n'
                    f'[     TELA DE CADASTRO     ]\n'
                    f'[ -------------------------]\n')

                while True:
                    username_py = input('Digite o nome de usuário:').lower()


                    #CONDICOES DE ERRO

                    if not username_py.strip():
                        print('O nome de usuário não pode estar vazio.')

                    if ' ' in username_py:
                        print('O nome de usuário não pode ter espaços em branco.')
                    
                    else:
                        cmdcond = f'SELECT nome FROM usuarios WHERE nome LIKE "{username_py}"'
                        cursor.execute(cmdcond)
                        result = cursor.fetchall()
                        nome_existe = False
                        

                        for username_sql in result:
                            if username_sql[0] == username_py:
                                nome_existe = True
                                break


                        if nome_existe == False:

                            
                            while True:


                                #PEDINDO EMAIL

                                email_py = input('Digite seu endereço de email:')
                                

                                #CONDICOES DE ERRO

                                if not email_py.strip():
                                    print('O email não pode estar vazio.')

                                elif ' ' in email_py:
                                    print('O email não pode ter espaços em branco.')
                                
                                elif '@' not in email_py or '.com' not in email_py:
                                    print('O email digitado não é válido.')

                                    
                                else:
                                    #READING EMAIL
                                    cmdcond = f'SELECT email FROM usuarios WHERE email LIKE "{email_py}"'
                                    cursor.execute(cmdcond)
                                    result = cursor.fetchall()
                                    email_existe = False

                                    for email_sql in result:
                                        if email_sql[0] == email_py:
                                            email_existe = True
                                            break

                                    if email_existe == False:
                                        print('\nPor favor, confirme seu e-mail {}. Te enviaremos um código'.format(email_py))
                                        send_code(username_py, email_py)
                                        print('Código enviado!')

                                        while True:


                                            user_code = input('Digite o código:')


                                            #CASO DE EXECUCAO DE CONFIRMACAO DE EMAIL

                                            if user_code == verification_code:
                                                print('\nE-mail confirmado com sucesso!\n')
                                                sleep(0.7)
                                                while True:
                                                    password = input("Digite sua senha:")

                                                    #CONDICOES DE ERRO 

                                                    if len(password) < 6:
                                                        print('ERRO: A senha não pode conter menos que 6 caracteres')

                                                    if not password.strip():
                                                        print('A senha não pode estar vazia')

                                                    if ' ' in password:
                                                        print('A senha não pode ter espaços em branco.')


                                                    #CONDICOES DE EXECUCAO

                                                    if not len(password) < 6 and password.strip() and ' ' not in password:
                                                        comando = f'INSERT INTO loginscreen.usuarios (nome, senha, email) VALUES ("{username_py}", "{password}","{email_py}");'
                                                        cursor.execute(comando)
                                                        database.connection.commit()
                                                        clean_screen()
                                                        print(f'\n************************************************\n'
                                                            f'Digite o número [2] e faça o login da sua conta.\n'
                                                            f'************************************************\n')
                                                        sleep(1)

                                                        return


                                            #CASO DE ERRO DE CONFIRMACAO DE EMAIL

                                            else:
                                                print('ERRO: o código digitado não é igual ao código enviado')


                                    #CASO DE ERRO DE EXISTENCIA DE EMAIL

                                    else:
                                        print('ERRO: o email digitado já foi logado.')


                        #CONDICAO DE ERRO DE EXISTENCIA DE USERNAME

                        else:
                            print("ERRO: O nome de usuário já está em uso.")







def login_screen():
    clean_screen()

    print(f'\n[ ------------------------ ]\n'
            f'[ TELA DE LOGIN DE USUARIO ]\n'
            f'[ -------------------------]\n')
    while True:
        

        username_py = input('Digite o nome de usuário:').lower()


        if not username_py.strip():
            print('O nome de usuário não pode estar vazio.')

        if ' ' in username_py:
            print('O nome de usuário não pode ter espaços em branco.')
        comando = f'SELECT nome FROM usuarios WHERE nome LIKE "{username_py}"'
        cursor.execute(comando)
        result = cursor.fetchall()
        

        correct_name = False
        for nome in result:
            if nome[0] == username_py:
                correct_name = True
                break


        if correct_name == True:
            while True:


                password = input("Digite sua senha:")
                command = f'SELECT senha FROM usuarios WHERE senha LIKE "{password}"'
                cursor.execute(command)
                result = cursor.fetchall()

                correct_password = False


                for senha in result:
                    if senha[0] == password:
                        correct_password = True
                        break
                

                if correct_password == True:
                    while True:
                        clean_screen()
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
                            return
                        elif opcao == '3':

                            comando = f'DELETE FROM usuarios WHERE nome = "{username_py}" AND senha = "{password}"'
                            cursor.execute(comando)
                            database.connection.commit()

                            print('\nSua conta foi deletada com sucesso!')
                            sleep(0.5)
                            return
                        elif opcao == '2':

                            while True:

                                new_password = input('Digite sua nova senha:')

                                if len(new_password) < 6:
                                    print('ERRO: A senha não pode conter menos que 6 caracteres')

                                if not new_password.strip():
                                    print('ERRO: A senha não pode estar vazia')

                                if ' ' in new_password:
                                    print('ERRO: A senha não pode ter espaços em branco.')

                                if not len(new_password) < 6 and new_password.strip() and ' ' not in new_password:
                                    comando = f'UPDATE usuarios ' \
                                            f'SET senha = "{new_password}" ' \
                                            f'WHERE nome = "{username_py}"'

                                    cursor.execute(comando)
                                    database.connection.commit()

                                    print('\nSua senha foi alterado com sucesso!')
                                    sleep(0.5)
                                    
                                    break


                        else:
                            print('\nERRO: Não há esta opção no programa. Por favor digite uma destas listadas.')


                else:
                    print('ERRO: A senha digitada está incorreta.')


        else:
            print('ERRO: O nome de usuário "{}" não existe.'.format(username_py))