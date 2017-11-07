def argent_de_poche(p_nb_notes, liste_notes):
    note_min = 0;
    note_max = 0;
    somme_notes = 0;
    for note in liste_notes:
        somme_notes = float(somme_notes) + note
        if(note > float(note_max)):
            note_max = note
        if(note < float(note_min)):
            note_min = note
    somme = (20-(max(liste_notes)-min(liste_notes)))*((float(sum(liste_notes))/len(liste_notes))*(float(sum(liste_notes))/len(liste_notes)))*0.01
    print("%.2f" % somme)
nb_notes = input()

input_notes = input()
liste_notes = [float(x) for x in input_notes.split(' ')]

argent_de_poche(nb_notes,liste_notes)
