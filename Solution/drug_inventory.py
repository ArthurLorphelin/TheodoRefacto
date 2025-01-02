# -*- coding: utf-8 -*-

from drug import InsulineFlask
from drug import GrandMaRecipe
from drug import WineBottle
from drug import ARNVaccine


class Inventory(object):
    def __init__(self, drugs):
        self.drugs = drugs

    def update_efficiency(self):
        # On parcourt la liste des médicaments, et on effectue leur mise à jour quotidienne
        # Comme chaque type de médicament a une logique spécifique, isinstance permet de différencier ces
        # types de médicaments, parce qu'on ne connaît pas le type dans la classe Inventory.
        # Ainsi, on s'assure que les bonnes méthodes de mise à jour sont effectuées pour chaque médicament
        for drug in self.drugs:
            if isinstance(drug, InsulineFlask):
                drug.daily_update()
            elif isinstance(drug, GrandMaRecipe):
                drug.daily_update()
            elif isinstance(drug, WineBottle):
                drug.daily_update()
            elif isinstance(drug, ARNVaccine):
                drug.daily_update()
            # Ici, le else correspond au cas où le médicament n'est pas d'un type particulier.
            # Donc, on applique la méthode daily_update() de la classe Druf
            else:
                drug.daily_update()
