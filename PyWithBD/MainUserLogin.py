
from time import sleep
from EmailValidation import enviarcodigo
from EmailValidation import codigo_user
from ConnectBD import ConnectBD
import os

#DEFININDO CLS PARA APAGAR O TERMINAL

def cls():
    return os.system('cls')


#CONEXAO DO BD

bd = ConnectBD()
bd.conectar()


#FAZENDO REFERENCIA AO CURSOR DEFINIDO NO OUTRO ARQUIVO

cursor = bd.get_cursor()




while True:
    i1 = True
    i2 = True
    i3 = True
    i4 = True
    i5 = True
    i6 = True
    i7 = True
    #TELA INICIAL
    cls()
    print(f'\n[ ------------------------- ]\n'
          f'[ LOGIN E CADASTRO DE CONTA ]\n'
          f'[ ------------------------- ]\n')
    print(f'[1] - Criar uma conta. \n'
          f'[2] - Logar uma conta já criada. \n'
          f'[3] - Sair do programa.\n')
    opcao = str(input('Selecione uma opção:'))


    #CONDICAO SE FOR CRIAR CONTA

    if opcao == '1':

        while i2 == True:
            

            #TELA CADASTRO
            cls()
            print(f'\n[ ------------------------ ]\n'
                  f'[     TELA DE CADASTRO     ]\n'
                  f'[ -------------------------]\n')

            while i7 == True:
                Username = input('Digite o nome de usuário:').lower()


                #CONDICOES DE ERRO

                if not Username.strip():
                    print('O nome de usuário não pode estar vazio.')

                if ' ' in Username:
                    print('O nome de usuário não pode ter espaços em branco.')
                
                else:
                    #READING EMAIL
                    cmdcond = f'SELECT nome FROM usuarios WHERE nome LIKE "{Username}"'
                    cursor.execute(cmdcond)
                    result = cursor.fetchall()

                    nome_existe = False


                    #VERIFICANDO SE O USERNAME JÁ EXISTE DE ACORDO COM O SELECT DO BD

                    for nome in result:
                        if nome[0] == Username:
                            nome_existe = True
                            break


                    #CONDICAO DE EXECUCAO DE USERNAME

                    if nome_existe == False:

                        
                        while i6 == True:


                            #PEDINDO EMAIL

                            Email = input('Digite seu endereço de email:')
                            

                            #CONDICOES DE ERRO

                            if not Email.strip():
                                print('O email não pode estar vazio.')

                            elif ' ' in Email:
                                print('O email não pode ter espaços em branco.')

                                
                            else:
                                #READING EMAIL
                                cmdcond = f'SELECT email FROM usuarios WHERE email LIKE "{Email}"'
                                cursor.execute(cmdcond)
                                result = cursor.fetchall()

                                email_existe = False


                                #VERIFICANDO SE EMAIL JÁ EXISTE DE ACORDO COM O SELECT DO EMAIL

                                for edmail in result:
                                    if edmail[0] == Username:
                                        email_existe = True
                                        break
                                

                                #CONDICAO CASO EXECUCAO EMAIL

                                if email_existe == False:


                                    #ENVIANDO CODIGO PARA O EMAIL

                                    enviarcodigo(Username, Email)
                                    print('\nPor favor, confirme seu e-mail {}. Te enviaremos um código'.format(Email))

                                    while i5 == True:


                                        confcod = input('Digite o código:')


                                        #CASO DE EXECUCAO DE CONFIRMACAO DE EMAIL

                                        if confcod == codigo_user:
                                            print('\nE-mail confirmado com sucesso!\n')
                                            sleep(0.7)
                                            while True:
                                                Senha = input("Digite sua senha:")

                                                #CONDICOES DE ERRO 

                                                if len(Senha) < 6:
                                                    print('ERRO: A senha não pode conter menos que 6 caracteres')

                                                if not Senha.strip():
                                                    print('A senha não pode estar vazia')

                                                if ' ' in Senha:
                                                    print('A senha não pode ter espaços em branco.')


                                                #CONDICOES DE EXECUCAO

                                                if not len(Senha) < 6 and Senha.strip() and ' ' not in Senha:
                                                    comando = f'INSERT INTO usuarios (nome, senha, email) VALUES ("{Username}", "{Senha}","{Email}");'
                                                    cursor.execute(comando)
                                                    bd.mydb.commit()
                                                    cls()
                                                    print(f'\n************************************************\n'
                                                        f'Digite o número [2] e faça o login da sua conta.\n'
                                                        f'************************************************\n')
                                                    sleep(1)
                                                    i5 = False
                                                    i6 = False
                                                    i2 = False
                                                    i7 = False
                                                    break


                                        #CASO DE ERRO DE CONFIRMACAO DE EMAIL

                                        else:
                                            print('ERRO: o código digitado não é igual ao código enviado')


                                #CASO DE ERRO DE EXISTENCIA DE EMAIL

                                else:
                                    print('ERRO: o email digitado já foi logado.')


                    #CONDICAO DE ERRO DE EXISTENCIA DE USERNAME

                    else:
                        print("ERRO: O nome de usuário já está em uso.")


                                

            

                    

    #CONDICAO SE FOR FAZER LOGIN
    elif opcao == '2':
        cls()
        print(f'\n[ ------------------------ ]\n'
              f'[ TELA DE LOGIN DE USUARIO ]\n'
              f'[ -------------------------]\n')
        while i3 == True:
            
            #PEDINDO LOGIN

            UserLogin = input('Digite o nome de usuário:').lower()


            #CASOS DE ERRO NO USERNAME

            if not UserLogin.strip():
                print('O nome de usuário não pode estar vazio.')

            if ' ' in UserLogin:
                print('O nome de usuário não pode ter espaços em branco.')
            comando = f'SELECT nome FROM usuarios WHERE nome LIKE "{UserLogin}"'
            cursor.execute(comando)
            result = cursor.fetchall()
            

            #VERIFICANDO SE USERNAME ESTÁ CORRETO

            nome_correto = False
            for nome in result:
                if nome[0] == UserLogin:
                    nome_correto = True
                    break

            #USERNAME CORRETO

            if nome_correto == True:
                while i4 == True:


                    #PEDINDO SENHA

                    Senha = input("Digite sua senha:")
                    comando = f'SELECT senha FROM usuarios WHERE senha LIKE "{Senha}"'
                    cursor.execute(comando)
                    result = cursor.fetchall()

                    senha_correta = False


                    #CONDICAO SE SENHA ESTÁ CORRETA

                    for senha in result:
                        if senha[0] == Senha:
                            senha_correta = True
                            break
                    

                    #SENHA CORRETA

                    if senha_correta == True:
                        while i1 == True:
                            cls()
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
                                i1 = False
                                i4 = False
                                i3 = False
                            elif opcao == '3':

                                comando = f'DELETE FROM usuarios WHERE nome = "{UserLogin}" AND senha = "{Senha}"'
                                cursor.execute(comando)
                                bd.mydb.commit()

                                print('\nSua conta foi deletada com sucesso!')
                                sleep(0.5)
                                i4 = False
                                i1 = False
                                i3 = False
                            elif opcao == '2':
                                i5 = True

                                while i5 == True:

                                    NovaSenha = input('Digite sua nova senha:')

                                    if len(NovaSenha) < 6:
                                        print('ERRO: A senha não pode conter menos que 6 caracteres')

                                    if not NovaSenha.strip():
                                        print('ERRO: A senha não pode estar vazia')

                                    if ' ' in NovaSenha:
                                        print('ERRO: A senha não pode ter espaços em branco.')

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
                                        i3 = False


                            #CONDICAO DE QUE NÃO HÁ OPCAO NO PROGRAMA DENTRO DA CONTA
                            else:
                                print('\nERRO: Não há esta opção no programa. Por favor digite uma destas listadas.')


                    #SENHA ERRADA

                    else:
                        print('ERRO: A senha digitada está incorreta.')


            #USERNAME ERRADO

            else:
                print('ERRO: O nome de usuário "{}" não existe.'.format(UserLogin))
    

    #CONDICAO SE FOR SAIR DO PROGRAMA

    elif opcao == '3':
        break
    
    
    #CONDICAO DE QUE NAO HÁ A OPCAO NO PROGRAMA DA TELA INICIAL

    else:
        print( '\nERRO: Não há esta opção no programa. Por favor digite uma destas listadas.')