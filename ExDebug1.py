def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"


if __name__ == "__main__":
    #TODO : Créer 3 listes
  #  liste_temperature = [temp]
  #  liste_poussiere = [poussiere]
   # liste_humidite = [humidite]

    #TODO : Pour 3 ordinateur
#def
        #TODO : Demander temp, poussière, humidite
        #TODO : Mettres les 3 valeurs dans leurs listes

    temp = float(input("Entrez la température: "))
    poussiere = input("Entrez le niveau de poussière: ")
    humidite = float(input("Entrez l'humidité: "))

    # TODO : Pour les 3 ordi
        #TODO : utiliser la fonction et afficher le résultat
    print(environnement_optimal(temp, poussiere, humidite))





