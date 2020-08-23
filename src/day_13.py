import random



def print_header():
    print('----------------------------------')
    print('Welcome to the "Rock Paper Scissors" thrilling game')
    print('-----------------------------------')
    



class Roll:
    def __init__(self, name):
        self.name = name
        self.wins = []
        self.loses = []
    def __str__(self):
        return(self.name)
    
    def define_wins_loses(self, wins_against, loses_against):
        """ wins_agains and loses against must be lists!"""
        self.wins+= wins_against
        self.loses+= loses_against
        

class Player:
    def __init__(self, name, computer):
        self.name = name
        self.rolls_history = []
        self.computer = computer

    def rolls(self):
        selection = None
        if self.computer is True:
            selection = random.choice(
                list(possible_rolls.keys()))
        else:
            while selection not in list(possible_rolls.keys()): 
                selection = input(
                    'Choose your next roll: [r]ock, [p]aper, [s]cissors ')
        value = possible_rolls[selection]
        self.rolls_history.append(selection)
        return(value)

rock = Roll('Rock')
scissors = Roll('Scissors')
paper = Roll('Paper')

rock.define_wins_loses([scissors], [paper])
scissors.define_wins_loses([paper], [rock])
paper.define_wins_loses([rock], [scissors])

possible_rolls = {'r': rock, 's': scissors, 'p': paper}


def main():
    print_header()
    jugador_1 = Player('Mathieu', False)
    jugador_2 = Player('Computer', True)
        
    jugador_1_results = 0
    jugador_2_results = 0
    number_attempts = 0
    while number_attempts < 5:
        jugador_1_roll = jugador_1.rolls()
        jugador_2_roll = jugador_2.rolls()
        print(f'{jugador_1.name} has played {jugador_1_roll.name}\n{jugador_2.name} has played {jugador_2_roll.name}')
        if jugador_1_roll in jugador_2_roll.wins:
            print(f'{jugador_2.name} wins against {jugador_1.name}')
            jugador_2_results += 1
        elif jugador_1_roll == jugador_2_roll:
            print(f'{jugador_2.name} and {jugador_1.name} draw')
        else:
            print(f'{jugador_1.name} wins against {jugador_2.name}')
            jugador_1_results += 1
        number_attempts += 1
    if jugador_1_results > jugador_2_results:
        print(f'{jugador_1.name} has won, {jugador_1_results} against {jugador_2_results}')
    elif jugador_1_results == jugador_2_results:
        print(f'{jugador_1.name} and {jugador_2.name} have drawn, {jugador_1_results} vs {jugador_2_results}')
    else:
        print(f'{jugador_2.name} has won, {jugador_2_results} against {jugador_1_results}')



if __name__ == "__main__":
    main()