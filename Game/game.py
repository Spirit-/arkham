from phases import Phases

class Game:
    environment_modifiers = {}
    turn = -1
    phase = Phases.MYTHOS

    def roll(self, stat_name, stat_value, modifier):
        result = stat_value + modifier + self.environment_modifiers.get(stat_name, 0)
        return result if result > 0 else 0
