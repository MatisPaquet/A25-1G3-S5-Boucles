import pytest
from ExDebug1 import environnement_optimal

def test_environnement_optimal_2():
    #Arrange : préparer des variables d'entrées et le résultat attendu
    temperature = 30
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Environnement non optimal"

    #Act: appeler la fonction à tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    #Assert: vérifier le résultat
    assert resultat_attendu == resultat_obtenu
