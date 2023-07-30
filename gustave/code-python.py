
# SAMOURA Amadou 'Developpeur Informatique '
# Exercice Technique GUSTAVE


class Tache:
    def __init__(self, debut, fin):
        self.debut = debut
        self.fin = fin


def trouver_trajets_optimises(liste_taches):
    trajets_optimises = []

    while len(liste_taches) > 0:
        trajet_actuel = []
        temps_restant_trajet_actuel = 30

        while len(liste_taches) > 0 and temps_restant_trajet_actuel > 0:
            tache_optimale = None
            distance_min = float('inf')

            for tache in liste_taches:
                distance = temps_restant_trajet_actuel - (tache.debut - tache.fin)
                if distance >= 0 and distance < distance_min:
                    distance_min = distance
                    tache_optimale = tache

            if tache_optimale is not None:
                trajet_actuel.append(tache_optimale)
                liste_taches.remove(tache_optimale)
                temps_restant_trajet_actuel -= distance_min

        trajets_optimises.append(trajet_actuel)

    return trajets_optimises


# les données des trajets indiqué dans le tableau
taches = [
    Tache(9, 11),
    Tache(13, 15),
    Tache(8.15, 10.15),
    Tache(14.30, 16.30),
    Tache(15.10, 17.10),
    Tache(12.30, 14.30),
    Tache(13.40, 15.40),
    Tache(17.00, 19.00),
    Tache(20.15, 22.15),
    Tache(18.15, 20.15),
]

# Appel de la fonction pour obtenir les trajets optimisés

resultat_trajets = trouver_trajets_optimises(taches)

# Affichage des résultats

print("Résultat de l'algorithme :")
for i, trajet in enumerate(resultat_trajets):
    print(f"Trajet {i + 1} :", ', '.join([f"Tâche {taches.index(tache) + 1}" for tache in trajet]),
          f"(Temps total = {sum([tache.fin + tache.debut for tache in trajet])} heures)")

print("Nombre total de trajets :", len(resultat_trajets))
