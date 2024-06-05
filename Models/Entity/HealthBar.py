from Views.Entity.HealthBar import HealthBarV


class HealthBar:
    def __init__(self, max_health):
        self.view = HealthBarV()
        self.health = max_health
        self.max_health = max_health