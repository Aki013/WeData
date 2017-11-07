def cadenas_lisa(p_valeur_n, p_longueur_code):
    valeurs_possibles=[]
    for valeur_possible_a in range(1,10**(p_longueur_code-1)-1):
        for valeur_possible_b in range(1,10**(p_longueur_code-1)-1):
            #print('valeur_possible_a_b : ' + str(valeur_possible_a) + ' - ' + str(valeur_possible_b))  
            if(len(str(valeur_possible_a))+len(str(valeur_possible_b))==p_longueur_code)and valeur_possible_a * valeur_possible_a + 2 * valeur_possible_b == p_valeur_n:
                    valeurs_possibles.append(str(valeur_possible_a)+str(valeur_possible_b))
    if (len(valeurs_possibles) == 0):
        print('Zut !')
    else:
        valeurs_possibles.sort()
        for valeur_possible in valeurs_possibles:
            print(valeur_possible)
        
liste_inputs = [int(x) for x in input().split(' ')]
valeur_n = liste_inputs[0]
longueur_code = liste_inputs[1]


cadenas_lisa(valeur_n,longueur_code)
