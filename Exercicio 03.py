""" 
    Uma empresa de delivery, chamada Vfood, está desenvolvendo um sistema para gerenciar os pedidos realizados pelos clientes.
    Nesse sistema, os pedidos são processados na ordem em que chegam, ou seja, 
    o primeiro pedido realizado deve ser o primeiro a ser atendido.

    Cada pedido possui um número, o nome do cliente e o valor total da compra.

    O sistema deve permitir:

    -Adicionar novos pedidos à fila
    -Processar (atender) o próximo pedido da fila
    -Visualizar todos os pedidos que ainda estão aguardando atendimento
    -Calcular o valor total dos pedidos já atendidos

    Como os pedidos devem ser atendidos exatamente na ordem em que são realizados, 
    não sendo possível alterar essa ordem, a utilização de uma estrutura de dados do tipo fila FIFO
    (First In, First Out) se torna a mais adequada para representar esse cenário.

"""

""" 
    Exemplo de Entrada, onde o número do parenteses é a opção do menu que o usuário deve escolher:
    (1): Veiga, 25
    (1): Selmini, 79.67
    (1): Carlos Rafael, 47
    (3)
    (2)
    (2)
    (4)
    (5)
    
    Exemplo de Saída:
    Pedido 1 adicionado com sucesso
    Pedido 2 adicionado com sucesso
    Pedido 3 adicionado com sucesso
    Fila de pedidos:
        Pedido 1 | Cliente: Veiga | Valor: R$ 25
        Pedido 2 | Cliente: Selmini | Valor: R$ 79.67
        Pedido 3 | Cliente: Carlos Rafael | Valor: R$ 47
    Pedido 1 atendido! - Valor: R$ 25
    Pedido 2 atendido! - Valor: R$ 79.67
    O faturamento total atual é de R$ 104.67
    Obrigado por usar o Vfood
    
"""

from collections import deque

class Pedido:
    def __init__(self, numero: int, cliente: str, valor: float):
        self.numero = numero
        self.cliente = cliente
        self.valor = valor    

def gerar_menu():
    print('[1] Novo pedido')
    print('[2] Atender pedido')
    print('[3] Ver fila de pedidos')
    print('[4] Ver faturamento total')
    print('[5] Sair do Vfood')
    
def main():
    fila = deque()
    faturamento_total = 0
    numero_pedido = 1
    
    while True:
        gerar_menu()
        
        opcao = int(input())
        
        match opcao:
            
            case 1:
                cliente = input("Nome do cliente: ")
                valor = float(input("Valor do pedido: "))
                
                novo_pedido = Pedido(numero_pedido, cliente, valor)
                
                fila.append(novo_pedido)
                
                print(f"Pedido {numero_pedido} adicionado com sucesso")
                
                numero_pedido += 1
                
            case 2:
                if len(fila) == 0:
                    print("Nenhum pedido na fila")
                else:
                    pedido_atendido = fila.popleft()
                    
                    faturamento_total += pedido_atendido.valor
                    
                    print(f"Pedido {pedido_atendido.numero} atendido! - Valor: R${pedido_atendido.valor:.2f}")
                    
            case 3:
                if len(fila) == 0:
                    print("Nenhum pedido na fila")
                else:
                    print("\nFila de pedidos: ")
                    
                    for pedido in fila:
                        print(f"Pedido {pedido.numero} | Cliente: {pedido.cliente} | Valor: R$ {pedido.valor:.2f}")
                        print()
                        
            case 4:
                print(f"O faturamento total atual é de R$ {faturamento_total:.2f}")
                
            case 5:
                print("Obrigado por usar o Vfood")
                break
            
            case _:
                print('Opção inválida!')

# programa principal
if __name__ == '__main__':
    main()