class Vehicule:
    """
    Cette classe représente un véhicule.
    Attention, c'est une classe abstraite.
    Elle est destinée à être étendue par des classes enfants.
    """

    # les variables déclarées directement dans la classe sont "des variables de classe"
    # le underscore permet d'indiquer que la variable est privée
    # Attention car elle reste tout de même accessible depuis l'extérieur
    _acceleration = 10

    def __init__(self, marque: str, modele: str, carburant: str, vitesse: int):
        self._marque = marque
        self._modele = modele
    def set_vitesse(self, vitesse: int):

     def accelerer(self):
        vitesse = self.get_vitesse()
        vitesse += 10
        vitesse += self._acceleration
        self.set_vitesse(vitesse)

    def ralentir(self):
        vitesse = self.get_vitesse()
        vitesse -= 10
        vitesse -= self._acceleration
        self.set_vitesse(vitesse)