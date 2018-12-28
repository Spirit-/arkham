from Game.phases import Phases

class Event:
    phase = None
    description = ""

    def __init__(self, phase):
        if self.phase and self.phase == phase:
            print(self.description)
            if input('Proceed?'):
                return


class UseFocus(Event):
    phase = Phases.UPKEEP
    description = "Use focus for adjusting skills"


class RefreshCards(Event):
    phase = Phases.UPKEEP
    description = "Refresh used cards if possible"


class UseTomes(Event):
    phase = Phases.MOVEMENT
    description = "Spend movement points to use Tomes"


class Move(Event):
    phase = Phases.MOVEMENT
    description = "Spend movement points to move"


class FightOrEvade(Event):
    phase = Phases.MOVEMENT
    description = "Fight or evade monster"
