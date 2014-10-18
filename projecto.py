# Grupo 21: Nuno Anselmo (81900); Mariana Silva (81938)

import random
import math

def verifica_cc(num_cc): #N
    '''Funcao verifica_cc: int -> tuple ; caso erro: int -> string
       Recebe um inteiro (num_cc) correspondente a um possivel numero 
       de um cartao de credito.
       Devolve um tuplo contendo a categoria e a rede do cartao se o
       numero corresponder a um cartao de credito ou a cadeia de caracteres.
       Em caso contrario devolve uma string com 'Cartao Invalido'.'''
    
    # Todas as funcoes secundarias recebem strings, portanto converte-se
    num_cc = str(num_cc)
    
    resposta = (categoria(num_cc), valida_iin(num_cc))
    
    if (luhn_verifica(num_cc) and resposta[0] != '' and resposta[1] != ''):
        return resposta
    
    else:
        return 'cartao invalido'
    
    
def gera_num_cc(rede_em): #N
    '''Funcao gera_num_c: string -> int
       Recebe uma cadeia de carateres (rede_em) correspondente a
       abreviatura de uma rede emissora.
       Devolve um numero de cartao de credito valido, gerado aleatoriamente.'''
    
    cartao = 0
    num_digitos = 0
    
    # Tuplo que guarda a informacao das redes
    # Primeira entrada: abreviatura
    # Segunda entrada: tuplo com possiveis comprimentos
    # Terceira entrada: tuplo com possiveis primeiros digitos      
    
    tuplo_rede = (('AE', (15,), (34, 37)),
                 ('DCI', (14,), (309, 36, 38, 39)),
                 ('DC', (16,), (65,)),
                 ('M', (13, 19), (5018, 5020, 5038)),
                 ('MC', (16,), (50, 51, 52, 53, 54, 19)),
                 ('VE', (16,), (4026, 426, 4405, 4508)),
                 ('V', (13, 16), (4024, 4532, 4556)))
    
    for tuplo in tuplo_rede:
        if tuplo[0] == rede_em:
            num_digitos = tuplo[1][int(random.random() * 10) % len(tuplo[1])]
            cartao = tuplo[2][int(random.random() * 10) % len(tuplo[2])]
            
            num_digitos -= (int(math.log10(cartao)) + 1)
            
            while num_digitos > 1: # Deixar ultimo digito para o de verificacao
                cartao = (cartao * 10) + int(random.random() * 10)
                num_digitos -= 1
            
            # A funcao digito_verificacao recebe e devolve string, logo e
            # necessario converter para string o input e para int o output
            cartao = cartao*10 + int(digito_verificacao(str(cartao)))
        
    return cartao
    

def calc_soma(a_somar): #N
    '''Funcao calc_soma: string -> int
       Recebe uma cadeia de carateres (a_somar), representando um numero 
       de cartao, sem o ultimo digito. 
       Devolve a soma ponderada dos digitos de a_somar, calculada de 
       acordo com o algoritmo de Luhn.'''
    
    temp = []
    soma = 0
    
    for c in a_somar:
        temp = [int(c)] + temp
        
    for i in range(0, len(temp)):
        if i % 2 == 0:
            temp[i] = temp[i] * 2
            
            if temp[i] > 9:
                temp[i] -= 9
                
    for n in temp:
        soma += n
        
    return soma
    
    
def luhn_verifica(numero_cc): #M
    '''Funcao luhn_verifica: string -> bool
       Recebe uma cadeia de carateres (numero_cc) que representa 
       um numero de cartao.
       Devolve verdadeiro, se o numero passar o algoritmo de Luhn.
       Em caso contrario, devolve falso.'''    
    
    digito = int(numero_cc) % 10 # Guardar o ultimo digito do numero.
    numero_cc = numero_cc[:-1] # Retirar o ultimo digito do numero.
    
    return (calc_soma(numero_cc) + digito) % 10 == 0

def comeca_por(cad1,cad2): #M
    '''Funcao comeca_por: (string,string) -> bool
       Recebe duas cadeias de carateres, cad1 e cad2. 
       Devolve verdadeiro se cad1 comecar por cad2. 
       Caso contrario devolve falso.'''
    
    return cad2 in cad1[0:len(cad2)]
    
def comeca_por_um(cad,t_cads): #M
    '''Funcao comeca_por_um: (string,tuple) -> bool
       Recebe uma cadeia de carateres (cad) e um 
       tuplo de cadeias de caracteres (t_cads). 
       Devolve verdadeiro apenas se cad comecar por um 
       dos elementos do tuplo t_cads.'''
    
    for c in t_cads:
        if comeca_por(cad, c):
            return True
    return False
    
    
def valida_iin(input_string): #N
    '''Funcao valida_iin: string -> string
       Recebe uma cadeira de caracteres (input_string)
       que e um numero de cartao, e devolve a cadeia
       correspondente a rede emissora do cartao caso
       exista (devolve vazio caso nao exista)'''
    
    # Tuplo que guarda a composicao do IIN
    # Primeira entrada: nome
    # Segunda entrada: tuplo com possiveis comprimentos
    # Terceira entrada: tuplo com possiveis primeiros digitos
    
    tuplo_iins = (('American Express', (15,), ('34', '37')),
             ('Diners Club International', (14,), ('309', '36', '38', '39')),
             ('Discover Card', (16,), ('65',)),
             ('Maestro', (13, 19), ('5018', '5020', '5038')),
             ('Master Card', (16,), ('50', '51', '52', '53', '54', '19')),
             ('Visa Electron', (16,), ('4026', '426', '4405', '4508')),
             ('Visa', (13, 16), ('4024', '4532', '4556')))
    

    for tuplo in tuplo_iins:
        if len(input_string) in tuplo[1] and comeca_por_um(input_string, tuplo[2]):
            return tuplo[0]
        
    else:
        return ''
    
def categoria(numero): #M
    '''Funcao categoria: string -> string'''
      
    
    if 1 <= int(numero[0]) <= 9:
        
        categorias = ['Companhias aereas',
                      'Companhias aereas e outras tarefas futuras da industria',
                      'Viagens e entretenimento e bancario / financeiro',
                      'Servicos bancarios e financeiros',
                      'Servicos bancarios e financeiros',
                      'Merchandising e bancario / financeiro',
                      'Petroleo e outras atribuicoes futuras da industria',
                      'Saude, telecomunicacoes e outras atribuicoes futuras da industria',
                      'Atribuicao nacional'] 
        
        return categorias[int(numero[0])-1]   
    
    else:
        return ''
    

def digito_verificacao(numero_cc): #M
    '''Funcao digito_verificacao: string -> string
       Recebe uma cadeia de carateres (numero_cc), que representa um numero de 
       cartao, sem o ultimo digito.
       Devolve o digito de verificacao que lhe devera ser acrescentado, 
       de forma a obter um numero de cartao valido.'''
    
    # Obtem-se o digito de verificacao ao subtrair a 10 o valor das somas
    # o que vai "complementar" o ultimo digito 
    #
    # soma + dig = 10 => dig = 10 - soma
    #
    # Como apenas interessa o ultimo digito calcula-se o resto da divisao por 10 
    
    return str((10 - calc_soma(numero_cc)) % 10)