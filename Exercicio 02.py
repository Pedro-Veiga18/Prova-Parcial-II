""" 
    Uma empresa de software está desenvolvendo um novo navegador, chamado "Vhrome", 
    com o objetivo de competir no mercado. 
    Como parte do desenvolvimento inicial, você foi contratado para prototipar funcionalidades básicas 
    de navegação, com foco no gerenciamento do histórico de páginas acessadas.

    Nesse protótipo, o sistema deve permitir que o usuário:

    -Acesse uma nova página
    -Retorne à página anteriormente visitada
    -Visualize o histórico de navegação atual

    Considerando que se trata de uma versão simplificada, não será possível acessar diretamente 
    páginas específicas do histórico. 
    O usuário poderá apenas retornar sequencialmente às páginas anteriores, 
    sempre a partir da página atual.

    Esse comportamento segue o princípio LIFO (Last In, First Out), 
    no qual a última página acessada é a primeira a ser removida do histórico. 
    Dessa forma, a utilização de uma estrutura de dados do tipo pilha se torna a abordagem mais adequada para 
    representar esse cenário.
"""

""" 
    Exemplo de Entrada, onde o número do parenteses é a opção do menu que o usuário deve escolher:
    (1): Youtube
    (1): Google
    (1): Canvas
    (2)
    (3)
    
    Exemplo de Saída:
    Página atual: Youtube
    Página atual: Google
    Página atual: Canvas
    Página atual: Google
    HISTÓRICO DO NAVEGADOR VHROME:
    Google
    Youtube
    Menu do Vhrome
"""

from collections import deque

def gerar_menu():
    print('[1] Acessar nova página')
    print('[2] Retornar à página anterior')
    print('[3] Exibir histórico')
    print('[4] Sair')

def main():
    historico = deque()
    pagina_inicial = 'Menu do Vhrome'
    historico.append(pagina_inicial)
    
    while True:
        gerar_menu()
        
        print(f"Página atual: {historico[-1]}")
        
        opcao = int(input())
        
        match opcao:
            
            case 1:
                pagina_nova = input('Insira o nome da página que voce quer acessar: ')
                historico.append(pagina_nova)
             
            case 2:
                if len(historico) <= 1:
                    print('Não é possível retornar a uma página anterior')
                else:
                    historico.pop()
                         
            case 3:
                print()
                print('HISTÓRICO DO NAVEGADOR VHROME:')
                print()
                
                for i in range(len(historico) -1, -1, -1):
                    print(historico[i])
                print()
            
            case 4:
                print('Obrigado por usar nosso navegador')
                break
            
            case _:
                print('Opção inválida!')
                
#Programa principal                
if __name__ == '__main__':
    main()
                
                