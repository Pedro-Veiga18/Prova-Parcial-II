""" 
    Uma empresa de tecnologia está desenvolvendo um novo aplicativo de música chamado Veiga Music, 
    com o objetivo de oferecer uma experiência mais interativa na criação e gerenciamento de playlists.

    Nesse app, cada música da playlist possui um nome, o nome do compositor e sua duração em minutos. 
    As músicas devem ser organizadas de forma que o usuário possa navegar livremente entre elas, 
    podendo avançar para a próxima música ou retornar para a música anterior.

    O sistema deve permitir:

    -Adicionar novas músicas à playlist
    -Remover músicas existentes da playlist
    -Visualizar todas as músicas da playlist
    -Buscar uma música pelo nome
    -Navegar para a próxima música
    -Navegar para a música anterior
    -Calcular a duração total da playlist

    Como o usuário pode percorrer a playlist nos dois sentidos, é necessário que cada música mantenha uma 
    referência tanto para a música anterior quanto para a próxima. 
    Dessa forma, a utilização de uma lista linear duplamente encadeada se torna a estrutura mais adequada 
    para representar esse cenário, pois permite acesso aos elementos vizinhos em ambas as direções.
"""

""" 
    Exemplo de Entrada, onde o número do parenteses é a opção do menu que o usuário deve escolher:
    (1): Use Somebody, Kings of Leon, 4
    (1): Black Sheep, Metric, 5
    (1): Ask, The Smiths, 3
    (5)
    (3)
    (3)
    (6)
    (7)
    
    Exemplo de Saída:
    Música adicionada com sucesso
    Música adicionada com sucesso
    Música adicionada com sucesso
    Tocando agora: Use Somebody - Kings of Leon
    Fim da reprodução
    Playlist:
        Música: Use Somebody | Compositor: Kings of Leon | Duração: 4 min
        Música: Black Sheep | Compositor: Metric | Duração: 5 min
        Música: Ask | Compositor: The Smiths | Duração: 3 min
    Duração total da playlist --> 12 min
    Obrigado por usar Veiga Music
"""

class Musica:
    def __init__(self, nome: str, compositor: str, duracao: int):
        self.nome = nome
        self.compositor = compositor
        self.duracao = duracao
        self.esq = None
        self.dir = None
        
        
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    
    def adicionar_musica(self, nome, compositor, duracao): 
        novo = Musica(nome, compositor, duracao)
        if self.tamanho == 0: 
            self.inicio = novo
            self.fim = novo
            novo.dir = novo
            novo.esq = novo
            self.tamanho += 1
        else:                 
            self.fim.dir = novo
            novo.esq = self.fim
            self.fim = novo
            novo.dir = self.inicio
            self.inicio.esq = novo
            self.tamanho += 1
    
    
    def buscar_musica(self, nome): 
        aux = self.inicio
        while aux:
            if aux.nome == nome:
                
                return aux
            aux = aux.dir
            if aux == self.inicio:
                break
        return None
    
    
    def remover_musica(self, nome): 
        aux = self.buscar_musica(nome) 
        
        if aux:
            if self.tamanho == 1: 
                self.inicio = None
                self.fim = None
            elif aux == self.inicio:
                self.inicio = aux.dir
                self.inicio.esq = self.fim
                self.fim.dir = self.inicio
            elif aux == self.fim: 
                self.fim = aux.esq
                self.fim.dir = self.inicio
                self.inicio.esq = self.fim
            else:
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
                aux.esq = None
                aux.dir = None
            aux = None
            self.tamanho -= 1
            
            return True
        
        else: 
            return False
            
       
    def imprimir(self): 
        if self.tamanho == 0:
            print("Playlist vazia")
            return
        
        aux = self.inicio
        while aux: 
            print(f"Música: {aux.nome} | Compositor: {aux.compositor} | Duração: {aux.duracao} min")
            print()
            aux = aux.dir
            if aux == self.inicio:
                break
         
            
    def duracao_total(self):
        aux = self.inicio
        duracao_total_minutos = 0
        while aux:
            duracao_total_minutos += aux.duracao
            aux = aux.dir
            if aux == self.inicio:
                break
        
        return duracao_total_minutos
        

def gerar_menu():
    print('[1] Adicionar música')
    print('[2] Remover música')
    print('[3] Visualizar playlist')
    print('[4] Buscar música na playlist')
    print('[5] Tocar playlist')
    print('[6] Visualizar duração total da playlist')
    print('[7] Sair do Veiga Music')
    
def gerar_submenu():
    print('[1] Avançar música')
    print('[2] Música anterior')
    print('[3] Parar playlist')
    
def main():
    while True:
        gerar_menu()
        opcao = int(input())
        
        match opcao:
            case 1:
                nome = input('Nome da música: ')
                compositor = input('Nome do compositor da música: ')
                duracao = int(input('Duração, em minutos, da música: '))
                
                playlist.adicionar_musica(nome, compositor, duracao)
                print('Música adicionada com sucesso.')
                
            case 2:
                nome = input('Nome da música a ser removida: ')
                
                resposta = playlist.remover_musica(nome)
                
                if resposta:
                    print('Música removida com sucesso')
                else:
                    print('Música não encontrada')
                
            case 3:
                print('\nPlaylist:')
                playlist.imprimir()
                print()
            
            case 4:
                nome = input('Nome da música a ser buscada: ')
                
                resposta = playlist.buscar_musica(nome)
                
                if resposta is not None:
                    print()
                    print('Música encontrada!')
                    print(f"Música: {resposta.nome} | Compositor: {resposta.compositor} | Duração: {resposta.duracao} min")
                    print()
                    
                else:
                    print('Música não encontrada')
                  
            case 5:
                musica_atual = playlist.inicio
                while True:
                    if playlist.tamanho == 0:
                        print("Playlist vazia")
                        break
                    gerar_submenu()
                    print(f"Tocando agora: {musica_atual.nome} - {musica_atual.compositor} ")
                    opcao2 = int(input())
                        
                    match opcao2:
                        case 1:
                            musica_atual = musica_atual.dir
                        case 2:
                            musica_atual = musica_atual.esq
                        case 3:
                            print('Fim da reprodução')
                            break
                        case _:
                            print('Opção inválida')
                            
                
            case 6:
                print(f"Duração total da playlist --> {playlist.duracao_total()} min")
                print()
            
            case 7:
                print('Obrigado por usar Veiga Music')
                break
                
            case _:
                print('Opção inválida')
                
# Programa principal
playlist = Lista()

if __name__ == '__main__':
    main()