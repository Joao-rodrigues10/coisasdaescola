def menu_principal():
    print('Menu principal')
    print('Digite o código do menu:')
    print('1: Opção 1')
    print('2: Opção 2')
    print('3: Opção 3')
    print('5: Sair')


def submenu(opcao):
    print('########################')
    print(f'Você está na {opcao}')
    print('1: Fazer algo nessa sub opção')
    print('2: Voltar ao menu anterior')
    print('3: Sair')
    print('########################')


def main():
    while True:
        menu_principal()
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            while True:
                submenu('Opção 1')
                sub_menu = input('Escolha uma ação: ')
                
                if sub_menu == '1':
                    print('Você fez algo na opção 1')
                elif sub_menu == '2':
                    break 
                elif sub_menu == '3':
                    exit()  
                else:
                    print('Opção inválida!')
        
        elif opcao == '2':
            while True:
                submenu('Opção 2')
                sub_menu = input('Escolha uma ação: ')
                
                if sub_menu == '1':
                    print('Você fez algo na opção 2')
                elif sub_menu == '2':
                    break
                elif sub_menu == '3':
                    exit()
                else:
                    print('Opção inválida!')
        
        elif opcao == '3':
            while True:
                submenu('Opção 3')
                sub_menu = input('Escolha uma ação: ')
                
                if sub_menu == '1':
                    print('Você fez algo na opção 3')
                elif sub_menu == '2':
                    break
                elif sub_menu == '3':
                    exit()
                else:
                    print('Opção inválida!')
        
        elif opcao == '5':
            print("Sair!!!")
            break
        
        else: 
            print("Opção inválida")


main()
