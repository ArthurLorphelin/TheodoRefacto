class Inventory(object):
    def __init__(self, drugs):
        self.drugs = drugs

    def update_efficiency(self):
        for drug in self.drugs:
            if drug.efficiency < 0:
                raise Exception("Efficiency must be positive")
            match drug.name:
                case "Old bottle of wine":
                    self.update_old_wine_bottle(drug)
                case "Granny recipe":
                    self.update_granny_recipe()
                case "Insulin vial":
                    self.update_insulin_vial(drug)
                case "ARN Vaccine":
                    self.update_arn_vaccine(drug)
                case default:
                    self.update_normal_drug(drug)


    def update_use_before(self, drug):
        drug.use_before -= 1

    def update_normal_drug(self, drug):
        self.update_use_before(drug)
        self.update_normal_drug_efficiency(drug)

    def update_normal_drug_efficiency(self, drug):
        if drug.use_before >= 0:
            drug.efficiency = max(drug.efficiency - 1, 0)
        else:
            drug.efficiency = max(drug.efficiency - 2, 0)

    def update_old_wine_bottle(self, drug):
        self.update_use_before(drug)
        self.update_old_bottle_of_wine_efficiency(drug)

    def update_old_bottle_of_wine_efficiency(self, drug):
        drug.efficiency += 1

    def update_granny_recipe(self):
        pass

    def update_insulin_vial(self, drug):
        self.update_use_before(drug)
        self.update_insulin_vial_efficiency(drug)

    def update_insulin_vial_efficiency(self, drug):
        if drug.use_before < 0:
            drug.efficiency = 0
        elif drug.use_before <= 7:
            drug.efficiency = max(drug.efficiency - 3, 0)
        elif drug.use_before <= 30:
            drug.efficiency = max(drug.efficiency - 2, 0)
        else:
            drug.efficiency = max(drug.efficiency - 1, 0)

    def update_arn_vaccine(self, drug):
        self.update_use_before(drug)
        self.update_arn_vaccine_efficiency(drug)

    def update_arn_vaccine_efficiency(self, drug):
        if drug.use_before >= 0:
            drug.efficiency = max(drug.efficiency - 2, 0)
        else:
            drug.efficiency = max(drug.efficiency - 4, 0)


class Drug:
    def __init__(self, name, use_before, efficiency):
        self.name = name
        self.use_before = use_before
        self.efficiency = efficiency

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.use_before, self.efficiency)
