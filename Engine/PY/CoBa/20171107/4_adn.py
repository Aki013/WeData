nb_fragments = int(input())

liste_fragments = [0 for x in range(nb_fragments * nb_fragments)]

longueur_totale = 0
for num_fragment in range(0,nb_fragments):
    valeurs_fragment = input()
    longueur_totale = longueur_totale + len(valeurs_fragment)
    liste_fragments[num_fragment] = valeurs_fragment

longueur_brins = longueur_totale / 2

print('longueur_brins')

combinaisons_possibles = ['' for x in range(nb_fragments * nb_fragments)]

for it1 in range (0, nb_fragments):
    for it2 in range (it1+1, nb_fragments):
        if(len(liste_fragments[it1]) + len(liste_fragments[it2]) == longueur_brins):
            combinaisons_possibles.append(str(liste_fragments[it1]) + str(liste_fragments[it2]))
            

for it in range (0, len(combinaisons_possibles)):
    print(combinaisons_possibles[it])