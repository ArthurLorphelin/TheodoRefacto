class Inventory(object):
    def __init__(self, drugs):
        self.drugs = drugs

    def update_efficiency(self):
        for drug in self.drugs:
            match drug.name:
                case "Normal Drug":
                    self.update_normal_drug_use_before(drug)
                    self.update_normal_drug_efficiency(drug)




    def update_normal_drug_use_before(self, drug):
        drug.use_before -= 1

    def update_normal_drug_efficiency(self, drug):
        if drug.use_before >= 0:
            drug.efficiency = max(drug.efficiency - 1, 0)
        else:
            drug.efficiency = max(drug.efficiency - 2, 0)


class Drug:
    def __init__(self, name, use_before, efficiency):
        self.name = name
        self.use_before = use_before
        self.efficiency = efficiency

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.use_before, self.efficiency)
