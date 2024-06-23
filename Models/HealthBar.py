from Views.HealthBars.HealthBar import HealthBarV


class HealthBar:
    def __init__(self, max_health: int, current_health: int):
        self.view: HealthBarV = HealthBarV()
        self.health: int = current_health
        self.max_health: int = max_health
