# Simple Rock, paper, scissors game.
# This program choose Rock, paper, scissors for an enemy
# And you choose your move.

# random import to sort the enemy choices.
import random

# sys import to exit the game.
import sys

# Match point
wins = 0
losses = 0
ties = 0

# Player is a person
player = ''

# Enemy is your AI enemy
enemy = 0

# Match is the game result
match = ''

#A simple gameIntro
def gameIntro():
    print('## Rock, paper, scissors Game ##')
    print('built by Alvaro Costa')

#A simple gameExit
def gameExit():
    print('Game Ended.')
    print('Your scores:')
    print(str(wins) + ' Wins - ' + str(losses) + ' Losses - ' + str(ties) + ' Ties ')
    print('Press enter to quit')
    player = input()
    sys.exit()


#Execute the gameIntro
gameIntro()

#Game Loop
while True:
    #Sorting the enemy moviment
    enemy = random.randint(1,3)

    #Showing scores
    print('Your scores:')
    print(str(wins) + ' Wins - ' + str(losses) + ' Losses - ' + str(ties) + ' Ties ')

    #Player Choice
    #Here you, the person, choose your moviment.
    #You should choose one valid answer.
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        player = input()

        #Validating the valid answer.
        if player == 'r' or player == 'p' or player == 's':
            #Print your choice
            if player == 'r':
                print('ROCK versus...')
            if player == 'p':
                print('PAPER versus...')
            if player == 's':
                print('SCISSORS versus...')
            if enemy == 1:
                print('ROCK')
            if enemy == 2:
                print('PAPER')
            if enemy == 3:
                print('SCISSORS')

            #Game result assignment
            match = player + str(enemy)
            break
        elif player == 'q':
            gameExit()
        else:
            print('Type a valid choice.')
            continue

    #Looking the game result.
    #When Ties
    if match == 'r1' or match == 'p2' or match == 's3':
        print('Ties')
        ties = ties + 1

    #When Losses
    if match == 'r2' or match == 'p3' or match == 's1':
        print('You lose')
        losses = losses + 1

    # When Wins
    if match == 'r3' or match == 'p1' or match == 's2':
        print('You Win.')
        wins = wins + 1



