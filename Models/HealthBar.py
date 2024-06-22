from Views.HealthBars.HealthBar import HealthBarV


class HealthBar:
    def __init__(self, max_health, current_health):
        self.view = HealthBarV()
        self.health = current_health
        self.max_health = max_health