from itertools import combinations
from itertools import permutations
from math import *


def generate_groups(lst, n):
    if not lst:
        yield []
    else:
        for group in (((lst[0],) + xs) for xs in combinations(lst[1:], n-1)):
            for groups in generate_groups([x for x in lst if x not in group], n):
                yield [group] + groups


'''nb_fragments = int(input())


liste_fragments = ['' for x in range(nb_fragments * nb_fragments)]

longueur_totale = 0
for num_fragment in range(0,nb_fragments:
    valeurs_fragment = input()
    longueur_totale = longueur_totale + len(valeurs_fragment)
    liste_fragments[num_fragment] = valeurs_fragment'''



nb_fragments = int(4)
longueur_totale = 12
liste_fragments = ['' for x in range(0)]
#liste_fragments.append('CGTG')
#liste_fragments.append('GCAC')
#liste_fragments.append('TC')
#liste_fragments.append('AG')
liste_fragments.append('A')
liste_fragments.append('B')
liste_fragments.append('C')
liste_fragments.append('D')

longueur_brins = longueur_totale / 2

print('longueur_brins : ' + str(longueur_brins))

tour_restant = nb_fragments

liste_combinaisons_possibles = ['' for x in range(factorial(nb_fragments))]

for num_fragment1 in range(0,tour_restant):    
    liste_combinaisons_possibles.append(liste_fragments[num_fragment1])
    tour_restant = nb_fragments - 1
    print(liste_fragments)
    print('num_fragment1 : ' + str(num_fragment1+1) + ' -> ' + str(liste_fragments[num_fragment1]))
    if len(liste_fragments)-1 > 0: 
        liste_fragments2 = liste_fragments.copy()
        liste_fragments2.remove(str(liste_fragments[num_fragment1]))      
        for num_fragment2 in range(0,tour_restant):    
            liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments2[num_fragment2])
            tour_restant = len(liste_fragments2)-1
            print('num_fragment2 : ' + str(num_fragment2+1) + ' -> ' + str(liste_fragments2[num_fragment2]))
            if  tour_restant > 0:      
                liste_fragments3 = liste_fragments2.copy()
                liste_fragments3.remove(str(liste_fragments2[num_fragment2]))   
                for num_fragment3 in range(0,tour_restant):   
                    liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments2[num_fragment2] + ' ' + liste_fragments3[num_fragment3])
                    tour_restant = len(liste_fragments3)-1   
                    print('num_fragment3 : ' + str(num_fragment3+1) + ' -> ' + str(liste_fragments3[num_fragment3]))
                    if tour_restant > 0:  
                        liste_fragments4 = liste_fragments3.copy()
                        liste_fragments4.remove(str(liste_fragments3[num_fragment3]))       
                        for num_fragment4 in range(0,tour_restant):    
                            liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments2[num_fragment2] + ' ' + liste_fragments3[num_fragment3] + ' ' + liste_fragments4[num_fragment4]) 
                            tour_restant = len(liste_fragments4)-1
                            print('num_fragment4 : ' + str(num_fragment4+1) + ' -> ' + str(liste_fragments4[num_fragment4]))
                            if tour_restant > 0:
                                liste_fragments5 = liste_fragments4.copy()
                                liste_fragments5.remove(str(liste_fragments4[num_fragment4]))    
                                for num_fragment5 in range(0,tour_restant):  
                                    liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments2[num_fragment2] + ' ' + liste_fragments3[num_fragment3] + ' ' + liste_fragments4[num_fragment4] + ' ' + liste_fragments5[num_fragment5])  
                                    tour_restant = len(liste_fragments5)-1
                                    print('num_fragment5 : ' + str(num_fragment5))
                                    if tour_restant > 0:  
                                        liste_fragments6 = liste_fragments5.copy()
                                        liste_fragments6.remove(str(liste_fragments5[num_fragment5]))               
                                        for num_fragment6 in range(0,tour_restant): 
                                            liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments2[num_fragment2] + ' ' + liste_fragments3[num_fragment3] + ' ' + liste_fragments4[num_fragment4] + ' ' + liste_fragments5[num_fragment5]  + ' ' + liste_fragments6[num_fragment6])   
                                            tour_restant = len(liste_fragments6)-1
                                            print('num_fragment6 : ' + str(num_fragment6+1))
                                            if tour_restant > 0:
                                                liste_fragments7 = liste_fragments6.copy()
                                                liste_fragments7.remove(str(liste_fragments6[num_fragment6]))        
                                                for num_fragment7 in range(0,tour_restant):  
                                                    liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments2[num_fragment2] + ' ' + liste_fragments3[num_fragment3] + ' ' + liste_fragments4[num_fragment4] + ' ' + liste_fragments5[num_fragment5]  + ' ' + liste_fragments6[num_fragment6]  + ' ' + liste_fragments7[num_fragment7])     
                                                    tour_restant = len(liste_fragments7)-1  
                                                    print('num_fragment7 : ' + str(num_fragment7+1))                                                   
                                                    if tour_restant > 0:
                                                        liste_fragments8 = liste_fragments7.copy()
                                                        liste_fragments8.remove(str(liste_fragments7[num_fragment7]))                    
                                                        for num_fragment8 in range(0,tour_restant):  
                                                            liste_combinaisons_possibles.append(liste_fragments[num_fragment1] + ' ' + liste_fragments2[num_fragment2] + ' ' + liste_fragments3[num_fragment3] + ' ' + liste_fragments4[num_fragment4] + ' ' + liste_fragments5[num_fragment5]  + ' ' + liste_fragments6[num_fragment6]  + ' ' + liste_fragments7[num_fragment7]  + ' ' + liste_fragments8[num_fragment8])   
                                                            tour_restant = tour_restant -1
                                                            print('num_fragment8 : ' + str(num_fragment8+1))



#print(list(generate_groups(liste_fragments, 1)))
#print(list(generate_groups(liste_fragments, 2)))
#print(list(generate_groups(liste_fragments, 3)))
#print(list(generate_groups(liste_fragments, 4)))

#[liste_combinaisons_possibles.append(str(i)+str(j)+str(k)+str(l)) for i in liste_fragments for j in liste_fragments for k in liste_fragments for l in liste_fragments]

for combinaison_possible in liste_combinaisons_possibles:
    #if(len(combinaison_possible) == longueur_brins):
    print('ligne - ' + combinaison_possible)

print('C est fini')
