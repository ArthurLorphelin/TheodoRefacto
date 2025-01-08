import unittest
from hokla import Drug, Inventory


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.drugs = [
            Drug("Normal Drug", 10, 20),
            Drug("Normal Drug 2", -3, 7),
            Drug("Old bottle of wine", 2, 0),
            Drug("Granny recipe", 0, 150),
            Drug("Granny recipe", -1, 80),
            Drug("Insulin vial", 55, 20),
            Drug("Insulin vial", 30, 49),
            Drug("Insulin vial", 18, 37),
            Drug("Insulin vial", 7, 78),
            Drug("Insulin vial", 4, 21),
            Drug("Insulin vial", 0, 12),
            Drug("Insulin vial", -9, 12),
            Drug("ARN Vaccine", 3, 6),
            Drug("ARN Vaccine", -6, 14)
        ]
        self.inventory = Inventory(self.drugs)

    def test_normal_drug_positive_use_before(self):
        self.inventory.update_efficiency()
        normal_drug = self.drugs[0]
        self.assertEqual(normal_drug.name, "Normal Drug")
        self.assertEqual(normal_drug.use_before, 9)
        self.assertEqual(normal_drug.efficiency, 19)

    def test_normal_drug_negative_use_before(self):
        self.inventory.update_efficiency()
        normal_drug = self.drugs[1]
        self.assertEqual(normal_drug.name, "Normal Drug 2")
        self.assertEqual(normal_drug.use_before, -4)
        self.assertEqual(normal_drug.efficiency, 5)

    def test_old_bottle_of_wine(self):
        self.inventory.update_efficiency()
        old_bottle_of_wine = self.drugs[2]
        self.assertEqual(old_bottle_of_wine.name, "Old bottle of wine")
        self.assertEqual(old_bottle_of_wine.use_before, 1)
        self.assertEqual(old_bottle_of_wine.efficiency, 1)

    def test_granny_recipe(self):
        self.inventory.update_efficiency()
        granny_recipe = self.drugs[3]
        self.assertEqual(granny_recipe.name, "Granny recipe")
        self.assertEqual(granny_recipe.use_before, 0)
        self.assertEqual(granny_recipe.efficiency, 150)

    def test_granny_recipe_2(self):
        self.inventory.update_efficiency()
        granny_recipe = self.drugs[4]
        self.assertEqual(granny_recipe.name, "Granny recipe")
        self.assertEqual(granny_recipe.use_before, -1)
        self.assertEqual(granny_recipe.efficiency, 80)

    def test_insulin_vial_more_than_30_days_use_before(self):
        self.inventory.update_efficiency()
        insulin_vial = self.drugs[5]
        self.assertEqual(insulin_vial.name, "Insulin vial")
        self.assertEqual(insulin_vial.use_before, 54)
        self.assertEqual(insulin_vial.efficiency, 19)

    def test_insulin_vial_30_days_use_before(self):
        self.inventory.update_efficiency()
        insulin_vial = self.drugs[6]
        self.assertEqual(insulin_vial.name, "Insulin vial")
        self.assertEqual(insulin_vial.use_before, 29)
        self.assertEqual(insulin_vial.efficiency, 47)

    def test_insulin_vial_between_30_and_7_days_use_before(self):
        self.inventory.update_efficiency()
        insulin_vial = self.drugs[7]
        self.assertEqual(insulin_vial.name, "Insulin vial")
        self.assertEqual(insulin_vial.use_before, 17)
        self.assertEqual(insulin_vial.efficiency, 35)

    def test_insulin_vial_7_days_use_before(self):
        self.inventory.update_efficiency()
        insulin_vial = self.drugs[8]
        self.assertEqual(insulin_vial.name, "Insulin vial")
        self.assertEqual(insulin_vial.use_before, 6)
        self.assertEqual(insulin_vial.efficiency, 75)

    def test_insulin_vial_between_0_and_7_days_use_before(self):
        self.inventory.update_efficiency()
        insulin_vial = self.drugs[9]
        self.assertEqual(insulin_vial.name, "Insulin vial")
        self.assertEqual(insulin_vial.use_before, 3)
        self.assertEqual(insulin_vial.efficiency, 18)

    def test_insulin_vial_0_days_use_before(self):
        self.inventory.update_efficiency()
        insulin_vial = self.drugs[10]
        self.assertEqual(insulin_vial.name, "Insulin vial")
        self.assertEqual(insulin_vial.use_before, -1)
        self.assertEqual(insulin_vial.efficiency, 0)

    def test_insulin_vial_negative_days_use_before(self):
        self.inventory.update_efficiency()
        insulin_vial = self.drugs[11]
        self.assertEqual(insulin_vial.name, "Insulin vial")
        self.assertEqual(insulin_vial.use_before, -10)
        self.assertEqual(insulin_vial.efficiency, 0)

    def test_arn_vaccine(self):
        self.inventory.update_efficiency()
        arn_vaccine = self.drugs[12]
        self.assertEqual(arn_vaccine.name, "ARN Vaccine")
        self.assertEqual(arn_vaccine.use_before, 2)
        self.assertEqual(arn_vaccine.efficiency, 4)

    def test_arn_vaccine_negative_use_before(self):
        self.inventory.update_efficiency()
        arn_vaccine = self.drugs[13]
        self.assertEqual(arn_vaccine.name, "ARN Vaccine")
        self.assertEqual(arn_vaccine.use_before, -7)
        self.assertEqual(arn_vaccine.efficiency, 10)

    def test_normal_drug_negative_efficiency(self):
        drugs = [Drug("Normal drug 3", 10, -10)]
        inventory = Inventory(drugs)
        with self.assertRaises(Exception) as context:
            inventory.update_efficiency()
        self.assertEqual(str(context.exception), "Efficiency must be positive")

    def test_old_bottle_of_win_negative_efficiency(self):
        drugs = [Drug("Old bottle of wine", 10, -10)]
        inventory = Inventory(drugs)
        with self.assertRaises(Exception) as context:
            inventory.update_efficiency()
        self.assertEqual(str(context.exception), "Efficiency must be positive")

    def test_granny_recipe_negative_efficiency(self):
        drugs = [Drug("Granny recipe", 10, -10)]
        inventory = Inventory(drugs)
        with self.assertRaises(Exception) as context:
            inventory.update_efficiency()
        self.assertEqual(str(context.exception), "Efficiency must be positive")

    def test_insulin_vial_negative_efficiency(self):
        drugs = [Drug("Insulin vial", 10, -10)]
        inventory = Inventory(drugs)
        with self.assertRaises(Exception) as context:
            inventory.update_efficiency()
        self.assertEqual(str(context.exception), "Efficiency must be positive")

    def test_arn_vaccine_negative_efficiency(self):
        drugs = [Drug("ARN Vaccine", 10, -10)]
        inventory = Inventory(drugs)
        with self.assertRaises(Exception) as context:
            inventory.update_efficiency()
        self.assertEqual(str(context.exception), "Efficiency must be positive")


if __name__ == '__main__':
    unittest.main()
