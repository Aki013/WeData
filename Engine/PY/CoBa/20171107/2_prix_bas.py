nb_produits = int(input())
produit_recherche = input()

prix_plus_bas = -10

for num_produit in range(0,nb_produits):
    input_detail_produit = input()
    nom_produit = input_detail_produit.split(' ',1)[0]
    prix_produit = int(input_detail_produit.split(' ',1)[1])

    if nom_produit == produit_recherche:
        if prix_plus_bas == -10:
            prix_plus_bas = prix_produit
        if prix_plus_bas > prix_produit:
            prix_plus_bas = prix_produit

print(prix_plus_bas)
