import random

# игровое поле
board_size = 6
board = [[' ' for x in range(board_size)] for y in range(board_size)]

# корабли
num_ships = 11
ship_coords = []
for i in range(num_ships):
    x = random.randint(0, board_size - 1)
    y = random.randint(0, board_size - 1)
    ship_coords.append((x, y))

# игровой цикл
while True:
    # ход игрока
    print('Твой ход!')
    guess_x = int(input('Угадай строку (0-5): '))
    while guess_x > 5:
        guess_x = int(input('За границами моря! Угадай строку (0-5): '))
    guess_y = int(input('Угадай столбец (0-5): '))
    while guess_y > 5:
        guess_y = int(input('За границами моря! Угадай столбец (0-5): '))
    if (guess_x, guess_y) in ship_coords:
        print('Попал!')
        board[guess_x][guess_y] = 'X'
        ship_coords.remove((guess_x, guess_y))
        if len(ship_coords) == 0:
            print('Поздравляем! Ты выиграл!')
            break
    else:
        print('Не попал!')
        board[guess_x][guess_y] = 'O'

    # ход компьютера
    print('Ход компьютера!')
    comp_guess_x = random.randint(0, board_size - 1)
    comp_guess_y = random.randint(0, board_size - 1)
    if (comp_guess_x, comp_guess_y) in ship_coords:
        print('Компьютер попал в ваш корабль на ({}, {})'.format(comp_guess_x, comp_guess_y))
        board[comp_guess_x][comp_guess_y] = 'X'
        ship_coords.remove((comp_guess_x, comp_guess_y))
        if len(ship_coords) == 0:
            print('Игра закончена! Компьютер выиграл!')
            break
    else:
        print('Компьютер непопал!')
        board[comp_guess_x][comp_guess_y] = 'O'

    # печатается доска
    print('Обновленная доска:')
    for row in board:
        print(row)
