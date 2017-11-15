from itertools import combinations
from itertools import permutations
from math import *

'''nb_fragments = int(input())


liste_fragments = ['' for x in range(nb_fragments * nb_fragments)]

longueur_totale = 0
for num_fragment in range(0,nb_fragments:
    valeurs_fragment = input()
    longueur_totale = longueur_totale + len(valeurs_fragment)
    liste_fragments[num_fragment] = valeurs_fragment'''



nb_fragments = int(4)
longueur_totale = 12
liste_fragments = ['' for x in range(nb_fragments)]
liste_fragments.append('CGTG')
liste_fragments.append('GCAC')
liste_fragments.append('TC')
liste_fragments.append('AG')

longueur_brins = longueur_totale / 2

print('longueur_brins : ' + str(longueur_brins))

tour_restant = nb_fragments

liste_combinaisons_possibles = ['' for x in range(factorial(nb_fragments))]

for num_fragment1 in range(0,tour_restant):    
    liste_combinaisons_possibles.append(liste_fragments[num_fragment1])
    tour_restant = nb_fragments -1
    print('num_fragment1 : ' + str(num_fragment1+1))
    if tour_restant > 0:        
        for num_fragment2 in range(0,tour_restant):    
            liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments[num_fragment2])
            tour_restant = tour_restant - 1   
            print('num_fragment2 : ' + str(num_fragment2+1))
            if tour_restant > 0:       
                for num_fragment3 in range(0,tour_restant):   
                    liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments[num_fragment2] + ' ' + liste_fragments[num_fragment3]) 
                    tour_restant = tour_restant -1 
                    print('num_fragment3 : ' + str(num_fragment3+1))
                    if tour_restant > 0:       
                        for num_fragment4 in range(0,tour_restant):    
                            liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments[num_fragment2] + ' ' + liste_fragments[num_fragment3] + ' ' + liste_fragments[num_fragment4]) 
                            tour_restant = tour_restant -1
                            print('num_fragment4 : ' + str(num_fragment4+1))
                            if tour_restant > 0: 
                                for num_fragment5 in range(0,tour_restant):  
                                    liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments[num_fragment2] + ' ' + liste_fragments[num_fragment3] + ' ' + liste_fragments[num_fragment4] + ' ' + liste_fragments[num_fragment5])  
                                    tour_restant = tour_restant -1 
                                    print('num_fragment5 : ' + str(num_fragment5))
                                    if tour_restant > 0:                
                                        for num_fragment6 in range(0,tour_restant): 
                                            liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments[num_fragment2] + ' ' + liste_fragments[num_fragment3] + ' ' + liste_fragments[num_fragment4] + ' ' + liste_fragments[num_fragment5]  + ' ' + liste_fragments[num_fragment6])   
                                            tour_restant = tour_restant -1
                                            print('num_fragment6 : ' + str(num_fragment6+1))
                                            if tour_restant > 0:      
                                                for num_fragment7 in range(0,tour_restant):  
                                                    liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments[num_fragment2] + ' ' + liste_fragments[num_fragment3] + ' ' + liste_fragments[num_fragment4] + ' ' + liste_fragments[num_fragment5]  + ' ' + liste_fragments[num_fragment6]  + ' ' + liste_fragments[num_fragment7])     
                                                    tour_restant = tour_restant -1   
                                                    print('num_fragment7 : ' + str(num_fragment7+1))                                                   
                                                    if tour_restant > 0:                   
                                                        for num_fragment8 in range(0,tour_restant):  
                                                            liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments[num_fragment2] + ' ' + liste_fragments[num_fragment3] + ' ' + liste_fragments[num_fragment4] + ' ' + liste_fragments[num_fragment5]  + ' ' + liste_fragments[num_fragment6]  + ' ' + liste_fragments[num_fragment7]  + ' ' + liste_fragments[num_fragment8])   
                                                            tour_restant = tour_restant -1
                                                            print('num_fragment8 : ' + str(num_fragment8+1)) 

for idx_combinaison in range(0, len(liste_combinaisons_possibles)):
    if(len(liste_combinaisons_possibles[idx_combinaison])> 0):
        print('combinaison ' + str(idx_combinaison) + ' : ' + liste_combinaisons_possibles[idx_combinaison])

print('C est fini')

'''for i in range(0, len(liste_fragments)+1:
        for subset in permutations(liste_fragments, i:
               print(subset)'''