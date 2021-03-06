from Game import events 
from Game.phases import Phases


class Game:
    turn = -1

    phase = Phases.MYTHOS
    phase_hooks = {
        Phases.UPKEEP: [events.UseFocus, events.RefreshCards],
        Phases.MOVEMENT: [events.FightOrEvade, events.UseTomes, events.Move, events.FightOrEvade, events. UseTomes]
    }

    environment_modifiers = {}
    
    
    def roll(self, stat_name, stat_value, modifier):
        result = stat_value + modifier + self.environment_modifiers.get(stat_name, 0)
        return result if result > 0 else 0

    def next_phase(self):
        self.phase = Phases(((Phases(self.phase).value + 1) % len(Phases)))
        if self.phase.value == 0:
            self.turn += 1
            print('Starting turn %i' % self.turn)

    def set_environment_modifiers(self, **kwargs):
        self.environment_modifiers.clear()
        self.environment_modifiers.update(kwargs)

    def start(self):
        print('The game just started')
        while True:
            self.next_phase()
            events.UseFocus(self.phase)
            events.RefreshCards(self.phase)
            events.UseTomes(self.phase)
            events.Move(self.phase)
            events.FightOrEvade(self.phase)
