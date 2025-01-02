# -*- coding: utf-8 -*-

from hokla import Drug, Inventory

class InventoryTest():
  def test_foo(self):
    items = [
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
    
    inventory = Inventory(items)
    inventory.update_efficiency()
    assert items[0].name == "fix me"
    print('fix me')

if __name__ == '__main__':
  test = InventoryTest()
  test.test_foo()
