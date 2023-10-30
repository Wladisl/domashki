from random import choice


class Player:
    def __init__(self, name=None):
        if name is not None:
            self.name = name
        else:
            self.name = input("Enter player name: ")

    def get_figure(self, *args, **kwargs):
        return self._get_figure(*args, **kwargs)

    def _get_figure(self, *args, **kwargs):
        raise NotImplementedError


class HumanPlayer(Player):
    name = 'Human'

    def _get_figure(self, options: list):
        names = [obj.name for obj in options]
        while True:
            user_input = input(f'Enter one of {names}: ')
            if user_input not in names:
                print('Wrong input')
                continue

            for obj in options:
                if obj.name == user_input:
                    return obj


class AIPlayer(Player):
    name = 'AI'

    def _get_figure(self, options: dict):
        ai_choice = choice(options)
        print(f'HINT {ai_choice.name}')
        return ai_choice


class BaseGameFigure:

    def __eq__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError

        return type(self) == type(other)


class Rock(BaseGameFigure):
    name = 'Rock'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if type(other) in (Lizard, Scissors):
            return True
        else:
            return False


class Scissors(BaseGameFigure):
    name = 'Scissors'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if type(other) in (Paper, Lizard):
            return True
        else:
            return False


class Paper(BaseGameFigure):

    name = 'Paper'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if type(other) in (Spock, Rock):
            return True
        else:
            return False


class Lizard(BaseGameFigure):
    name = 'Lizard'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if type(other) in (Paper, Spock):
            return True
        else:
            return False


class Spock(BaseGameFigure):
    name = 'Spock'

    def __gt__(self, other):
        if not isinstance(other, BaseGameFigure):
            raise TypeError
        if type(other) in (Scissors, Rock):
            return True
        else:
            return False


class RSPGame:
    game_name = 'Rock Scissors Paper Lizard Spock'
    player1 = None
    player2 = None
    rules = [Scissors(), Paper(), Rock(), Lizard(), Spock()]

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        print(f'{self.game_name} started for 1 time play')
        self._play()

    def _play(self):
        f1 = self.player1.get_figure(self.rules)
        f2 = self.player2.get_figure(self.rules)

        if f1 == f2:
            print('Draw')
        elif f1 > f2:
            print(f'Player {self.player1.name} wins with {f1.name}')
        else:
            print(f'Player {self.player2.name} wins with {f2.name}')

    def play_3_times(self):
        print(f'{self.game_name} started for 3 time play')
        for _ in range(3):
            self._play()


ai_player1 = AIPlayer('AI')
human_player1 = HumanPlayer()

game = RSPGame(ai_player1, human_player1)

game.play()
