import unittest
from drug_inventory import Inventory
from drug import Drug, InsulineFlask, GrandMaRecipe, WineBottle, ARNVaccine


class MyTestCase(unittest.TestCase):
    # Fonction qui permet de poser les bases et contours pour bien effectuer les tests
    def setUp(self):
        # On crée une liste de médicaments pour effectuer les tests unitaires
        self.drugs = [
            Drug("Médicament normal", 10, 80),
            InsulineFlask("Flacon d'insuline", 45, 90),
            GrandMaRecipe("Recette de grand-mère", 60, 60),
            WineBottle("Bouteille de vin", 15, 15),
            ARNVaccine("Vaccin ARN", 30, 30)
        ]
        # On crée une variable pour appeler la classe Inventory
        self.inventory = Inventory(self.drugs)

    # On crée la fonction qui teste qu'un médicament normal se met correctement à jour selon sa logique
    def test_regular_drug_update(self):
        # Le médicament normal correspond au premier élément de la liste créée au-dessus
        regular_drug = self.drugs[0]
        self.inventory.update_efficiency()
        self.assertEqual(regular_drug.use_before, 9)
        self.assertEqual(regular_drug.efficiency, 79)

    # On crée la fonction qui teste qu'un flacon d'insuline se met correctement à jour selon sa logique
    def test_insuline_flask_update(self):
        # Le flacon d'insuline correspond au deuxième élément de la liste crée au-dessus
        insuline_flask = self.drugs[1]
        self.inventory.update_efficiency()
        self.assertEqual(insuline_flask.use_before, 44)
        self.assertEqual(insuline_flask.efficiency, 89)

    # On crée la fonction qui teste qu'une recette de grand-mère se met correctement à jour selon sa logique
    def test_grand_ma_recipe_update(self):
        # La recette de grand-mère correspond au troisième élément de la liste crée au-dessus
        grand_ma_recipe = self.drugs[2]
        self.inventory.update_efficiency()
        self.assertEqual(grand_ma_recipe.use_before, 60)
        self.assertEqual(grand_ma_recipe.efficiency, 60)

    # On crée la fonction qui teste qu'une bouteille de vin se met correctement à jour selon sa logique
    def test_win_bottle_update(self):
        # La bouteille de vin correspond au quatrième élément de la liste crée au-dessus
        wine_bottle = self.drugs[3]
        self.inventory.update_efficiency()
        self.assertEqual(wine_bottle.use_before, 14)
        self.assertEqual(wine_bottle.efficiency, 16)

    # On crée la fonction qui teste qu'un vaccin ARN se met correctement à jour selon sa logique
    def test_ARN_vaccine_update(self):
        # Le vaccin ARN correspond au cinquième élément de la liste crée au-dessus
        arn_vaccine = self.drugs[4]
        self.inventory.update_efficiency()
        self.assertEqual(arn_vaccine.use_before, 29)
        self.assertEqual(arn_vaccine.efficiency, 28)

    # On crée la fonction qui teste si un flacon d'insuline à moins de 30 jours de péremption se met bien à jour.
    def test_insuline_flask_less_than_30_days_update(self):
        insuline_flask = InsulineFlask("Flacon d'insuline", 25, 70)
        inventory = Inventory([insuline_flask])
        inventory.update_efficiency()
        self.assertEqual(inventory.drugs[0].use_before, 24)
        self.assertEqual(inventory.drugs[0].efficiency, 68)

    # On crée la fonction qui teste si un flacon d'insuline à moins de 7 jours de péremption se met bien à jour.
    def test_insuline_flask_less_than_7_days_update(self):
        insuline_flask = InsulineFlask("Flacon d'insuline", 6, 70)
        inventory = Inventory([insuline_flask])
        inventory.update_efficiency()
        self.assertEqual(inventory.drugs[0].use_before, 5)
        self.assertEqual(inventory.drugs[0].efficiency, 67)

    # On crée la fonction qui teste si un médicament normal, dont la date de péremption est passée, se met bien à jour.
    def test_regular_drug_negative_use_before_update(self):
        regular_drug = Drug("Médicament", -1, 50)
        inventory = Inventory([regular_drug])
        inventory.update_efficiency()
        self.assertEqual(inventory.drugs[0].use_before, -2)
        self.assertEqual(inventory.drugs[0].efficiency, 48)

    # On teste si l'efficacité d'un flacon d'insuline tombe à 0 la date de péremption passée
    def test_insuline_flask_negative_use_before_update(self):
        insuline_flask = InsulineFlask("Flacon d'insuline", -1, 50)
        inventory = Inventory([insuline_flask])
        inventory.update_efficiency()
        self.assertEqual(inventory.drugs[0].use_before, -2)
        self.assertEqual(inventory.drugs[0].efficiency, 0)

    # On crée la fonction qui teste si un vaccin ARN, dont la date de péremption est passée, se met bien à jour.
    def test_ARN_vaccine_negative_use_before_update(self):
        arn_vaccine = ARNVaccine("ARN Vaccine", -1, 50)
        inventory = Inventory([arn_vaccine])
        inventory.update_efficiency()
        self.assertEqual(inventory.drugs[0].use_before, -2)
        self.assertEqual(inventory.drugs[0].efficiency, 46)

    # On crée la fonction pour vérifier ce qu'il se passe si plusieurs mises à jour ont lieu
    def test_multiple_updates(self):
        # Pour 2 mises à jour
        regular_drug = self.drugs[0]
        self.inventory.update_efficiency()
        self.inventory.update_efficiency()
        self.assertEqual(regular_drug.use_before, 8)
        self.assertEqual(regular_drug.efficiency, 78)

        # Pour 4 mises à jour
        insuline_flask = self.drugs[1]
        self.inventory.update_efficiency()
        self.inventory.update_efficiency()
        self.assertEqual(insuline_flask.use_before, 41)
        self.assertEqual(insuline_flask.efficiency, 86)

        # Pour 6 mises à jour
        grand_ma_recipe = self.drugs[2]
        wine_bottle = self.drugs[3]
        arn_vaccine = self.drugs[4]
        self.inventory.update_efficiency()
        self.inventory.update_efficiency()
        self.assertEqual(grand_ma_recipe.use_before, 60)
        self.assertEqual(grand_ma_recipe.efficiency, 60)
        self.assertEqual(wine_bottle.use_before, 9)
        self.assertEqual(wine_bottle.efficiency, 21)
        self.assertEqual(arn_vaccine.use_before, 24)
        self.assertEqual(arn_vaccine.efficiency, 18)


if __name__ == '__main__':
    unittest.main()
