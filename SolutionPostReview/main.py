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
        self.assertEqual(self.items[0].name, "Normal Drug")
        self.assertEqual(self.items[0].use_before, 9)
        self.assertEqual(self.items[0].efficiency, 19)

    def test_old_bottle_of_wine(self):
        self.inventory.update_efficiency()
        self.assertEqual(self.items[1].name, "Old bottle of wine")
        self.assertEqual(self.items[1].use_before, 1)
        self.assertEqual(self.items[1].efficiency, 1)

    def test_normal_drug_2(self):
        self.inventory.update_efficiency()
        self.assertEqual(self.items[2].name, "Normal Drug 2")
        self.assertEqual(self.items[2].use_before, 4)
        self.assertEqual(self.items[2].efficiency, 6)

    def test_granny_recipe(self):
        self.inventory.update_efficiency()
        self.assertEqual(self.items[3].name, "Granny recipe")
        self.assertEqual(self.items[3].use_before, 0)
        self.assertEqual(self.items[3].efficiency, 150)

    def test_granny_recipe_2(self):
        self.inventory.update_efficiency()
        self.assertEqual(self.items[4].name, "Granny recipe")
        self.assertEqual(self.items[4].use_before, -1)
        self.assertEqual(self.items[4].efficiency, 80)

    def test_insulin_vial(self):
        self.inventory.update_efficiency()
        self.assertEqual(self.items[5].name, "Insulin vial")
        self.assertEqual(self.items[5].use_before, 14)
        self.assertEqual(self.items[5].efficiency, 18)

    def test_insulin_vial_2(self):
        self.inventory.update_efficiency()
        self.assertEqual(self.items[6].name, "Insulin vial")
        self.assertEqual(self.items[6].use_before, 9)
        self.assertEqual(self.items[6].efficiency, 47)

    def test_insulin_vial_3(self):
        self.inventory.update_efficiency()
        self.assertEqual(self.items[7].name, "Insulin vial")
        self.assertEqual(self.items[7].use_before, 4)
        self.assertEqual(self.items[7].efficiency, 46)


if __name__ == '__main__':
    unittest.main()
