from Game.phases import Phases

class Game:
    environment_modifiers = {}
    turn = -1
    phase = Phases.MYTHOS

    def roll(self, stat_name, stat_value, modifier):
        result = stat_value + modifier + self.environment_modifiers.get(stat_name, 0)
        return result if result > 0 else 0

    def next_phase(self):
        self.phase = Phases(((Phases(self.phase).value + 1) % len(Phases)))
        if self.phase.value == 0:
            self.turn += 1

    def set_environment_modifiers(self, **kwargs):
        self.environment_modifiers.clear()
        self.environment_modifiers.update(kwargs)
