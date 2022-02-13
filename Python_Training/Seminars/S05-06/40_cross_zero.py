# intro
# main game
# Game over
# Interface

def main_game():
    new_game(intro())
    game_over()
    return end()

def intro():
    print('Hello Friend! Let\'s play the cross-zero!')
    return 'x' if input('Enter character x or o') == 'x' else 'o'

def new_game(c):
    print('OK, Let\'s start!')
    c2 = 'x' if c == 'x' else 'o'
    cross = create_game()
    

def create_game():
    return {i: '' for i in range(1,10)}

def end():
    return input('Want to play new game? y/n').lower() == 'n'

while True:
    if main_game():
        break