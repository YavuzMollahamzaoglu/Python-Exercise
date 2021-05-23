import random

comp_win = 0
player_win = 0

for i in range(3):

    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input('rock, paper or scissors?:').lower()

    if player == computer:
        print('computer:', computer)
        print('player:', player)
        print('Tie')

    elif player == 'rock':
        if computer == 'paper':
            print('computer:', computer)
            print('player:', player)
            print('You lose!')
            comp_win += 1
        if computer == 'scissors':
            print('computer:', computer)
            print('player:', player)
            print('You win!')
            player_win += 1

    elif player == 'scissors':
        if computer == 'paper':
            print('computer:', computer)
            print('player:', player)
            print('You win!')
            player_win += 1
        if computer == 'scissors':
            print('computer:', computer)
            print('player:', player)
            print('You lose!')
            comp_win += 1



    elif player == 'paper':
        if computer == 'scissors':
            print('computer:', computer)
            print('player:', player)
            print('You lose!')
            comp_win += 1
        if computer == 'rock':
            print('computer:', computer)
            print('player:', player)
            print('You win!')
            player_win += 1


print(player_win)
print(comp_win)

if comp_win == player_win:
    print('You got tie with computer !')

elif comp_win > player_win:
    print('Computer win against to you !')

else:
    print('You win against to computer !')



