import array # Importação da biblioteca array

class PilhaCheiaErro(Exception): # Implementação de classes para tratamento de erros
    pass

class PilhaVaziaErro(Exception):
    pass

class DiscoInvalidoErro(Exception):
    pass

class Pilha: # Implementação da Classe Pilha conforme especificado
    def __init__(self, qtde_discos):
        self.dados = array.array('i', [k+1 for k in range(qtde_discos)][::-1])  # 'i' para representar que é um array de inteiros
                                        # List comprehesion para criar a stack com os raios certos de cada disco

    def empilha(self, raio_disco): # Criação de uma função empilha para colocar o disco na torre especificada
        if len(self.dados) == 0: # Caso a torre não tenha discos, a função o aplica na torre
            self.dados.append(raio_disco)
        elif self.dados[len(self.dados) - 1] > raio_disco: # Caso o menor disco seja maior, pode aplicar o disco especificado
            self.dados.append(raio_disco)
        else: # Caso contrário, retorna erro falando que o disco maior não pode ser colocado em cima de um menor
            raise DiscoInvalidoErro('O disco que está querendo colocar acima desse é inválido')
        
    def desempilha(self): # Criação de uma função desempilha para retirar o menor disco de uma torre
        if not self.pilha_esta_vazia(): # Se a torre não estiver vazia, ele pega o primeiro disco
            return self.dados.pop()
        else: # Caso contrário, ele retorna um erro avisando que a torre está vazia de fato
            raise PilhaVaziaErro('A pilha está vazia')
    
    def pilha_esta_vazia(self): # Função para entender se uma pilha está vazia ou não
        return len(self.dados) == 0
    
    def pilha_esta_cheia(self): # Função para entender se a pilha está cheia
        return len(self.dados) == self.capacidade
    
    def tamanho(self): # Função para ver a quantidade de discos que uma pilha possui
        return len(self.dados)

