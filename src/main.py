import funcoes


while True:
    funcoes.clean_screen()


    print(f'\n[ ------------------------- ]\n'
          f'[ LOGIN E CADASTRO DE CONTA ]\n'
          f'[ ------------------------- ]\n')
    print(f'[1] - Criar uma conta. \n'
          f'[2] - Logar uma conta já criada. \n'
          f'[3] - Sair do programa.\n')
    

    opcao = str(input('Selecione uma opção:'))


    #CONDICAO SE FOR CRIAR CONTA

    if opcao == '1':
        funcoes.register_screen()
                     
    elif opcao == '2':
        funcoes.login_screen()       
    

    elif opcao == '3':
        break
    
    

    else:
        print( '\nERRO: Não há esta opção no programa. Por favor digite uma destas listadas.')