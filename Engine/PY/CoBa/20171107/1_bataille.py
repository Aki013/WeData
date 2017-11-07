nb_tours = int(input())

points_j1 = 0
points_j2 = 0

for num_tour in range(0,nb_tours):
    input_cartes = input()
    carte_j1 = int(input_cartes.split(' ',1)[0])
    carte_j2 = int(input_cartes.split(' ',1)[1])
    if carte_j1 > carte_j2:
        points_j1 = points_j1 +1
    if carte_j2 > carte_j1:
        points_j2 = points_j2 +1
        
if points_j2 > points_j1:
    print('B')
if points_j1 > points_j2:
    print('A')