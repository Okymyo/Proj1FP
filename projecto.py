# Grupo 21: Nuno Anselmo (81900); Mariana Silva (81938)

def verifica_cc(num_cc): #N
    '''Funcao verifica_cc: int -> tuple ; caso erro: int -> string
       Recebe um inteiro (num_cc) correspondente a um possivel numero 
       de um cartao de credito.
       Devolve um tuplo contendo a categoria e a rede do cartao se o
       numero corresponder a um cartao de credito ou a cadeia de caracteres.
       Em caso contrario devolve uam string com 'Cartao Invalido'.'''
    
    
def gera_num_cc(rede_em): #N
    '''Funcao gera_num_c: string -> int
       Recebe uma cadeia de carateres (rede_em) correspondente a
       abreviatura de uma rede emissora.
       Devolve um numero de cartao de credito valido, gerado aleatoriamente.'''
    

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
    numero_cc = int(numero_cc) // 10 # Retirar o ultimo digito do numero.
    
    # Inverter o numero, ja sem o ultimo digito:
    invertido = 0
    
    while int(numero_cc) > 0:
        invertido = invertido * 10 + int(numero_cc) % 10
        numero_cc = int(numero_cc) / 10
        
    # Multiplicar os digitos em posicoes impares por 2:    
    
        
    # Subtrair 9 a todos os numeros resultantes que sejam superiores a 9:
    
            
    # Adicionar todos os numeros, incluindo o numero de verificacao:
    calc_soma(invertido)
    
    return (soma + digito) % 10 == 0

def comeca_por(cad1,cad2): #M
    '''Funcao comeca_por: (string,string) -> bool
       Recebe duas cadeias de carateres, cad1 e cad2. 
       Devolve verdadeiro se cad1 começar por cad2. 
       Caso contrario devolve falso.'''
    
    return cad2 in cad1[0:len(cad2)]
    
def comeca_por_um(cad,t_cads): #M
    '''Funcao comeca_por_um: (string,tuple) -> bool
       Recebe uma cadeia de carateres (cad) e um 
       tuplo de cadeias de caracteres (t_cads). 
       Devolve verdadeiro apenas se cad comecar por um 
       dos elementos do tuplo t_cads.'''
    
    for i in range(len(t_cads)):
        if t_cads[i] in cad[0:len(t_cads[i])]:
            return True
    return False
    
    
def valida_iin(input_string): #N
    #Input: string()
    #Output 1: string()
    #Output 2: string('')
    
    # Tuplo que guarda a composicao do IIN
    # Primeira entrada: nome
    # Segunda entrada: tuplo com possiveis comprimentos
    # Terceira entrada: tuplo com possiveis primeiros digitos
    
    tuplo_iins = (('American Express', (15,), ('34', '37')),
             ('Diners Club International', (14,), ('309', '36', '38', '39')),
             ('Discover Card', (16,), ('65')),
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
        raise ValueError ('O primeiro digito so pode conter numeros de 1 e 9!')
    
def digito_verificacao(): #M
    #Input: string()
    #Output: string(dig_ver)
    print("!!!!!")