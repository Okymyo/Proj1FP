# Grupo 21: Nuno Anselmo (81900); Mariana Silva (81938)

def verifica_cc(num_cc):
    #NUNO
    #Input: int(num_cc)
    #Output 1: string(cat_em), string(rede_em)
    #Output 2: string('cartao invalido')
    print("!!!!!")

def gera_num_cc(rede_em):
    #NUNO
    #Input: string(rede_em)
    #Output 1: int(num_cc)
    #Output 2: string('emissor invalido')
    print("!!!!!")

def calc_soma(a_somar):
    #NUNO
    #Input: string(a_somar)
    #Output: int(soma)
    soma = 0
    for c in a_somar:
        soma += int(c)
        
    return soma

def luhn_verifica(numero_cc):
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

def comeca_por(cad1,cad2):
    '''Funcao comeca_por: (string,string) -> bool
       Recebe duas cadeias de carateres, cad1 e cad2. 
       Devolve verdadeiro se cad1 começar por cad2. 
       Caso contrario devolve falso.'''
    
    return cad2 in cad1[0:len(cad2)]
    
def comeca_por_um(cad,t_cads):
    '''Funcao comeca_por_um: (string,tuple) -> bool
       Recebe uma cadeia de carateres (cad) e um 
       tuplo de cadeias de caracteres (t_cads). 
       Devolve verdadeiro apenas se cad comecar por um 
       dos elementos do tuplo t_cads.'''
    
    for i in range(len(t_cads)):
        if t_cads[i] in cad[0:len(t_cads[i])]:
            return True
    return False
    
    
def valida_iin():
    #NUNO
    #Input: string()
    #Output 1: string()
    #Output 2: string('')
    print("!!!!!")

def categoria(numero):
    '''Funcao categoria: (string) -> string
    #Output 1: string(cat_em)
    #Output 2: string('categoria invalida')'''   
    
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
    
def digito_verificacao():
    #MARIANA
    #Input: string()
    #Output: string(dig_ver)
    print("!!!!!")
