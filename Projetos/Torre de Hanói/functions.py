# Módulo reservado para criação de funções pertinentes às interações do usuário com o sistema
import os # Importação da biblioteca os para implementação de comandos ao terminal
from classes import Pilha # Importação da classe Pilha para implementação de instâncias baseadas nesse


def cria_torres_com_disco(qtde_discos): # Implementação de uma função para printar uma torre que possui discos (pilha com valores)
    txt = ''
    posicao_pino = qtde_discos + 1 # Garante a estética da torre
    
    for p in range(posicao_pino - qtde_discos):    # Cria o restante do pino da torre acima dos discos
        for m in range(posicao_pino):
            if (qtde_discos - p - 1 < m):
                print('|', end='')
            else:
                print(' ', end='')
    
    print('\n', end='')  # Dá o espaço da linha da torre

    for i in range(qtde_discos):  # Posiciona metade do raio de cada disco do lado esquerdo do pino da torre
        for j in range(qtde_discos):
            if (qtde_discos - i - 2 < j):
                print('#', end='')
            else:
                print(' ', end='')
        
        print('|', end='') # Posiciona os pipes referente ao pino da torre
        
        for k in range(qtde_discos): # Faz a outra metade do raio
            
            if (qtde_discos - i - 1 > k):
                txt += ' '
            else:
                txt += '#'
            
        txt_reversed = txt[::-1] # Ele pega o resultado e o inverte na string para fechar o disco
        print(txt_reversed, end='')
        txt = '' # Reinicio a variável para inserção de uma nova linha com o disco
        print('\n', end='')

    for i in range((qtde_discos+1)*2): # Print da base da torre
        print('-', end='')
    
    print('\n', end='')

def cria_torres_sem_disco(qtde_discos): # Implementação da função para criação de torres sem discos (pilha vazia)
    posicao_pino = qtde_discos + 1 # Garante a estética da torre

    for l in range(qtde_discos):
        for p in range(posicao_pino - qtde_discos):    # Cria o restante do pino da torre acima dos discos
            for m in range(posicao_pino):
                if (qtde_discos - p - 1 < m):
                    print('|', end='')
                else:
                    print(' ', end='')
    
        print('\n', end='')  # Dá o espaço da linha da torre

    for i in range((qtde_discos+1)*2): # Print da base da torre
        print('-', end='')
    
    print('\n', end='')



def cria_pilhas(): # Função para receber o número de discos e criar pilhas com base nesse
    flag = 1
    while flag: # Flag pra garantir que o usuário digitou um inteiro
        answer = input('Insira a qtde. de discos que deseja inserir na torre de origem (em inteiro): ')
        print('\n', end='')
        try:
            answer_int = int(answer)
            flag = 0
        except ValueError:
            os.system('cls')
            print('Por favor, insira apenas valores inteiros. Tente novamente.')
        
        except Exception:
            os.system('cls')
            print('Erro desconhecido, por favor, reinicie o programa')
            break

    p1_tamanho = answer_int
    p2_tamanho = 0
    p3_tamanho = 0

    p1 = Pilha(p1_tamanho) # Criação das instância de cada pilha
    p2 = Pilha(p2_tamanho)
    p3 = Pilha(p3_tamanho)

    lista_tamanhos = [p1_tamanho, p2_tamanho, p3_tamanho] # Separação das lenght de cada pilha para realização do print
    print ('-=-=-=-=-=-==-=-=-=-=-=-=- Estado Inicial das Torres -=-=-=-=-=-==-=-=-=-=-=-=-')
    for i in range(len(lista_tamanhos)):
        if lista_tamanhos[i] == 0:
            cria_torres_sem_disco(max(lista_tamanhos))
        else:
            cria_torres_com_disco(lista_tamanhos[i])
    print('\n', end='')

    return p1, p2, p3

movements = 0 # Inicia a variável contadora de movimentos

def torre_hanoi(disc, torre_origem, torre_destino, torre_aux): # Criação do algoritmo de recursão para resolver o problema da Torre de Hanói
    global movements
    movements += 1

    
    if disc == 1: # Trata do caso básico, onde há apenas um disco
        disco_atual = torre_origem.desempilha()
        torre_destino.empilha(disco_atual)
        return len(torre_origem.dados), len(torre_destino.dados), len(torre_aux.dados), movements
    
    else: # Caso contrário, ele faz a recursão até chegar no ponto de que haja apenas um disco
        
        torre_hanoi(disc - 1, torre_origem, torre_aux, torre_destino)
        disco_atual = torre_origem.desempilha()
        torre_destino.empilha(disco_atual)
        torre_hanoi(disc - 1, torre_aux, torre_destino, torre_origem) 
        '''Por fim, faz o processo inverso e garante que os discos vão para a torre de
        destino especificado no início.'''

    return len(torre_origem.dados), len(torre_destino.dados), len(torre_aux.dados), movements
    # Retorno do tamanho de cada torre no final para realização do print

def main(): # Implementação de uma função main para realização de cada etapa do algoritmo
    p1, p2, p3 = cria_pilhas()

    tam1, tam3, tam2, movimentos = torre_hanoi(len(p1.dados), p1, p3, p2)

    lista_tamanhos = [tam1, tam2, tam3]
    print ('-=-=-=-=-=-==-=-=-=-=-=-=- Estado Final das Torres -=-=-=-=-=-==-=-=-=-=-=-=-')

    for i in range(len(lista_tamanhos)): # Loop utilizado para criar as devidas torres em suas características
        if lista_tamanhos[i] == 0:
            cria_torres_sem_disco(max(lista_tamanhos))
        else:
            cria_torres_com_disco(lista_tamanhos[i])

    print('\n', end='')

    print(f'Quantidade total de movimentos realizados: {movimentos} movimentos')



        
