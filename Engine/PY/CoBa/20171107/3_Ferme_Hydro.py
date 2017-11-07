from contextlib import suppress

taille_carre = int(input())

ferme = [[['']*taille_carre]*taille_carre]
ferme = [[0 for x in range(taille_carre)] for y in range(taille_carre)]

for num_ligne in range(0,taille_carre):
    valeurs_ligne = input()
    for num_colonne in range(0,taille_carre):
        #print('num_ligne \ num_colonne : ' + str(num_ligne) + '\\' + str(num_colonne))
        #print('valeur : ' + valeurs_ligne[num_colonne])
        ferme[num_ligne][num_colonne] = valeurs_ligne[num_colonne]


for i in range(0, taille_carre):
    for j in range(0, taille_carre):
        if(ferme[i][j] == 'X'):
            if(i > 0):
                with suppress(Exception):
                    if(j > 0):
                        if(ferme[i-1][j-1]!='X'):
                            ferme[i-1][j-1] = 'X2'
                with suppress(Exception):
                    if(ferme[i-1][j]!='X'):
                        ferme[i-1][j] = 'X2'                    
                with suppress(Exception):
                    if(ferme[i-1][j+1]!='X'):
                        ferme[i-1][j+1] = 'X2'

            with suppress(Exception):
                    if(j > 0):
                        if(ferme[i][j-1]!='X'):
                            ferme[i][j-1] = 'X2'
            with suppress(Exception):
                if(ferme[i][j+1]!='X'):
                    ferme[i][j+1] = 'X2'

            with suppress(Exception):
                if(j > 0):
                    if(ferme[i+1][j-1]!='X'):
                        ferme[i+1][j-1] = 'X2'
            with suppress(Exception):
                if(ferme[i+1][j]!='X'):
                    ferme[i+1][j] = 'X2'
            with suppress(Exception):
                if(ferme[i+1][j+1]!='X'):
                    ferme[i+1][j+1] = 'X2'

#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
#     for row in ferme]))

'''for i in range(0, taille_carre):
    for j in range(0, taille_carre):
        if(ferme[i][j] == 'X2'):
            ferme[i][j] = 'X'''

cpt_cases = 0
for i in range(0, taille_carre):
    for j in range(0, taille_carre):        
        if(ferme[i][j] == 'X2'):
            cpt_cases = cpt_cases +1
print(cpt_cases)