import random


class Game:
    def __init__(self):
        self.computer_pick = self.get_computer_pick()
        self.user_pick = self.get_user_pick()
        self.result = self.get_result()

    def get_computer_pick(self):
        random_number = random.randint(1, 3)
        options= {1: 'pedra', 2: 'papel', 3: 'tesoura'}
        return options[random_number]

    def get_user_pick(self):
        while True:
            user_pick = input('Digite pedra/papel/tesoura: ')
            user_pick = user_pick.lower()

            if user_pick in ('pedra', 'papel', 'tesoura'):
                break
            else:
                print('Entrada errada!')
        return user_pick

    def get_result(self):
        if self.computer_pick == self.user_pick:
            return 'Empatou'
        elif self.user_pick == 'papel' and self.computer_pick == 'tesoura':
            return 'Venceu'
        elif self.user_pick == 'pedra' and self.computer_pick == 'tesoura':
            return "Venceu"
        elif self.user_pick == 'tesoura' and self.computer_pick == 'papel':
            return "Venceu"
        else:
            return 'Perdeu'

    def print_result(self):
        print(f'Escolha do computador: {self.computer_pick}')
        print(f'Sua escolha: {self.user_pick}')
        print(f'Você {self.result}')


while True:
    game = Game()
    game.print_result()

    play_again = input('Deseja continuar jogando? (y/n): ').lower()

    if play_again != 'y':
        break
