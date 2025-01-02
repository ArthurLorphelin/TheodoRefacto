# On crée une classe parente, générique pour tous les médicaments "normaux".
# On crée la méthode de mise à jour quotidienne de leur date de péremption et efficacité
class Drug:
    # On définit un médicament par son nom, sa date de péremption et son efficacité
    def __init__(self, name, use_before, efficiency):
        self.name = name
        self.use_before = use_before
        self.efficiency = efficiency

    # Fonction qui permet d'afficher les informations sur le médicament
    def __repr__(self):
        return f'Drug : name = "{self.name}", use before = {self.use_before}, efficiency = {self.efficiency}%'

    # Fonction de mise à jour
    def daily_update(self):
        # Tant que l'efficacité du médicament n'est pas nulle, elle diminue de 1 tous les jours
        if self.efficiency > 0:
            self.efficiency -= 1
        # De même, la date de péremption (use_before) se rapproche tous les jours
        self.use_before -= 1
        # Si la date de péremption est passée, le médicament se dégrade 2 fois plus vite
        # Sauf si son efficacité est déjà nulle, alors elle reste à 0
        if self.use_before < 0:
            if self.efficiency > 0:
                self.efficiency -= 1
            else:
                self.efficiency = 0


# On crée une sous-classe de Drug, nommée InsulineFlask,
# parce que la mise à jour quotidienne est différente des médicaments normaux.
class InsulineFlask(Drug):
    def daily_update(self):
        # Tant que l'efficacité n'est pas nulle, elle diminue de 1 tous les jours
        if self.efficiency > 0:
            self.efficiency -= 1
            # Si la date de péremption est inférieure à 30 jours ou moins, le médicament se dégrade de fois plus vite
            if self.use_before <= 30:
                self.efficiency -= 1
            # Si la date de péremption est inférieure à 7 jours ou moins, le médicament se dégrade 3 fois plus vite
            if self.use_before <= 7:
                self.efficiency -= 1
        # De même, la date de péremption (use_before) se rapproche tous les jours
        self.use_before -= 1
        # Si la date de péremption est passée, l'efficacité retombe à 0
        if self.use_before < 0:
            self.efficiency = 0


# # On crée une sous-classe de Drug, nommée GrandMaRecipe,
# # parce que la mise à jour quotidienne est différente des médicaments normaux.
class GrandMaRecipe(Drug):
    def daily_update(self):
        # Les recettes de grand-mère n'ont pas de date de péremption, et ne perdent jamais en efficacité.
        # Il n'y a donc pas de mise à jour quotidienne de la condition du médicament
        pass


# On crée une sous-classe de Drug, nommée WineBottle,
# parce que la mise à jour quotidienne est différente des médicaments normaux.
class WineBottle(Drug):
    def daily_update(self):
        # Les bouteilles de vin augmentent leur efficacité chaque jour
        self.efficiency += 1
        self.use_before -= 1


# On crée une sous-classe de Drug, nommée ARNVaccine,
# parce que la mise à jour quotidienne est différente des médicaments normaux.
class ARNVaccine(Drug):
    def daily_update(self):
        # Tant que l'efficacité n'est pas nulle, elle se dégrade deux fois plus vite que les médicaments normaux
        if self.efficiency > 0:
            self.efficiency -= 2
        # La date de péremption se rapproche tous les jours
        self.use_before -= 1
        # Les vaccins ARN se dégradent 2 fois plus vite que la normale, donc après la date de péremption aussi
        if self.use_before < 0:
            if self.efficiency > 1:
                self.efficiency -= 2
            else:
                self.efficiency = 0
