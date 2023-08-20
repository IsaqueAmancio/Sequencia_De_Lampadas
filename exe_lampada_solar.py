# a função pega uma sequencia e faz a contagem de quantas lampadas solares podem ser incluidas e tambem mostra como vai ficar a sequencia de lampadas após a alteração
#lampada eletrica = 0 e lampada solar = 1 
def sequencia_e_qtd_lamp(sequencia):
    n_lamp = 0
    li_lamp = []                    
    cont = 0
    for x in sequencia:
        li_lamp.append(x)   #transforma a string da sequencia em uma lista que contém a sequencia de lampadas 
    print(li_lamp) 
    for i in li_lamp:       
        if cont < 0:        #transforma o contador em positivo caso não exista uma lampada anterior 
            cont = cont*-1      
        if i == "1":
            atual_lamp = False      
            n_lamp = n_lamp + 1           #confere se a lampada é alimentada com energia solar ou eletrica 
        elif i == "0":
            atual_lamp = True
        if atual_lamp == True and li_lamp[cont - 1] != "1" and li_lamp[cont + 1] != "1":
            n_lamp = n_lamp + 1                         # se a lampada for eletrica e não possuir uma lampada solar antes ou depois adiciona uma lampada solar e atualiza a sequencia
            li_lamp[cont] = "1"                         
        cont = cont + 1
    print(f"Nova sequencia: {li_lamp}")
    return print(f"numero de lampadas solares : {n_lamp}")
sequencia = input() 
sequencia_e_qtd_lamp(sequencia)

