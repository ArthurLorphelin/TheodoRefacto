import unittest
from hokla import Drug, Inventory


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.items = [
            Drug("Normal Drug", 10, 20),
            Drug("Old bottle of wine", 2, 0),
            Drug("Normal Drug 2", 5, 7),
            Drug("Granny recipe", 0, 150),
            Drug("Granny recipe", -1, 80),
            Drug("Insulin vial", 15, 20),
            Drug("Insulin vial", 10, 49),
            Drug("Insulin vial", 5, 49),
            # this ARN Vaccine drug does not work properly yet
            Drug("ARN Vaccine", 3, 6)
        ]
        self.inventory = Inventory(self.items)

    def test_normal_drug(self):
        self.inventory.update_efficiency()
        normal_drug = self.items[0]
        self.assertEqual(normal_drug.name, "Normal Drug")
        self.assertEqual(normal_drug.use_before, 9)
        self.assertEqual(normal_drug.efficiency, 19)

    def test_old_bottle_of_wine(self):
        self.inventory.update_efficiency()
        old_bottle_of_wine = self.items[1]
        self.assertEqual(old_bottle_of_wine.name, "Old bottle of wine")
        self.assertEqual(old_bottle_of_wine.use_before, 1)
        self.assertEqual(old_bottle_of_wine.efficiency, 1)

    def test_normal_drug_2(self):
        self.inventory.update_efficiency()
        normal_drug = self.items[2]
        self.assertEqual(normal_drug.name, "Normal Drug 2")
        self.assertEqual(normal_drug.use_before, 4)
        self.assertEqual(normal_drug.efficiency, 6)

    def test_granny_recipe(self):
        self.inventory.update_efficiency()
        granny_recipe = self.items[3]
        self.assertEqual(granny_recipe.name, "Granny recipe")
        self.assertEqual(granny_recipe.use_before, 0)
        self.assertEqual(granny_recipe.efficiency, 150)

    def test_granny_recipe_2(self):
        self.inventory.update_efficiency()
        granny_recipe = self.items[4]
        self.assertEqual(granny_recipe.name, "Granny recipe")
        self.assertEqual(granny_recipe.use_before, -1)
        self.assertEqual(granny_recipe.efficiency, 80)

    def test_insulin_vial(self):
        self.inventory.update_efficiency()
        insulin_vial = self.items[5]
        self.assertEqual(insulin_vial.name, "Insulin vial")
        self.assertEqual(insulin_vial.use_before, 14)
        self.assertEqual(insulin_vial.efficiency, 18)

    def test_insulin_vial_2(self):
        self.inventory.update_efficiency()
        insulin_vial = self.items[6]
        self.assertEqual(insulin_vial.name, "Insulin vial")
        self.assertEqual(insulin_vial.use_before, 9)
        self.assertEqual(insulin_vial.efficiency, 47)

    def test_insulin_vial_3(self):
        self.inventory.update_efficiency()
        insulin_vial = self.items[7]
        self.assertEqual(insulin_vial.name, "Insulin vial")
        self.assertEqual(insulin_vial.use_before, 4)
        self.assertEqual(insulin_vial.efficiency, 46)

    def test_arn_vaccine(self):
        self.inventory.update_efficiency()
        arn_vaccine = self.items[8]
        self.assertEqual(arn_vaccine.name, "ARN Vaccine")
        self.assertEqual(arn_vaccine.use_before, 2)
        self.assertEqual(arn_vaccine.efficiency, 4)


if __name__ == '__main__':
    unittest.main()
