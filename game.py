import random


def show_rating(score):
    print(f'Your rating: {score}')


def winning_indices(options, index):
    """Winning indices for computer"""
    indices = []
    for i in range(len(options) // 2):
        indices.append((index + i + 1) % len(options))

    return indices


def main():
    options = ['rock', 'paper', 'scissors']
    name = input('Enter your name: ')

    # read score if an existing player
    score = 0
    with open('rating.txt', 'r') as ratings:
        for rating in ratings:
            if name in rating:
                print('Hello,', name)
                score = int(rating.split()[1])

    # get a list from user
    user_options_str = input()
    if user_options_str:
        options = user_options_str.split(',')
    print("Okay, let's start")

    # play game
    while True:
        player = input()
        comp = random.choice(options)
        if player == '!exit':
            print('Bye!')
            break
        if player == '!rating':
            show_rating(score)
            continue
        if player not in options:
            print('Invalid input')
            continue
        index = options.index(player)
        winner_indices = winning_indices(options, index)
        comp_index = options.index(comp)
        if comp == player:
            print(f'There is a draw ({comp})')
            score += 50
        elif comp_index not in winner_indices:
            print(f'Well done. The computer chose {comp} and failed')
            score += 100
        else:
            print(f'Sorry, but the computer chose {comp}')

    # update ratings
    with open('rating.txt', 'w+') as ratings:
        is_new_user = True
        for rating in ratings:
            if name in rating:
                print(f'{name} {score}', file=ratings)
                is_new_user = False
                break
            print(rating, file=ratings)

        if is_new_user:
            print(f'{name} {score}', file=ratings)


if __name__ == '__main__':
    main()