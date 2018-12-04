import random
import os
os.system('cls')

def checker():
    score_o = 0
    score_x = 0
    global grid

    for horline in grid:
        if horline == ['O','O','O','O','O']:
            score_o += 1
            break
        if horline == ['X','X','X','X','X']:
            score_x += 1
            break

    for v1 in range(len(grid)):
        verline = []
        for v2 in range(len(grid)):
            point = grid[v2][v1]
            verline.append(point)
        if verline == ['O','O','O','O','O']:
            score_o += 1
            break
        if verline == ['X','X','X','X','X']:
            score_x += 1
            break

    dialine1 = []
    for d1 in range(len(grid)):
        point2 = grid[d1][d1]
        dialine1.append(point2)
    if dialine1 == ['O','O','O','O','O']:
        score_o += 1
    if dialine1 == ['X','X','X','X','X']:
        score_x += 1

    dialine2 = []
    for d2,d3 in zip(range(0,5), range(4,-1,-1)):
        point3 = grid[d2][d3]
        dialine2.append(point3)
    if dialine2 == ['O','O','O','O','O']:
        score_o += 1
    if dialine2 == ['X','X','X','X','X']:
        score_x += 1

    return score_o, score_x

def pvp():
    change = 0
    last_change = 0
    global grid
    p1_score = 0
    p2_score = 0
    menu = False
    while True:
        os.system('cls')
        grids = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
        if last_change != change:
            grid = grids
        print('Player 1 Score: {}'.format(p1_score))
        print('Player 2 Score: {}'.format(p2_score))
        for line in grid:
            print(line)

        print('*'*50)

        dot = -1
        while True:
            dot += 1
            if dot == 25:
                break
            while True:
                if change % 2 == 0:
                    if dot%2 == 0:
                        print("Player 1's Turn!")
                    elif dot%2 != 0:
                        print("Player 2's Turn!")
                if change % 2 != 0:
                    if dot%2 == 0:
                        print("Player 2's Turn!")
                    elif dot%2 != 0:
                        print("Player 1's Turn!")
                move1 = input('Input row number and column number |ex.[5 5]|: ')
                if move1 == 'MENU':
                    menu = True
                    break
                move = [int(q) for q in move1.split()]
                row = move[0] - 1
                col = move[1] - 1
                if row > 4 or col > 4:
                    os.system('cls')
                    print('Player 1 Score: {}'.format(p1_score))
                    print('Player 2 Score: {}'.format(p2_score))
                    for line in grid:
                        print(line)
                    print('*'*50)
                    print('Input should be within the grid range.')
                    continue
                if grid[row][col] == 'O' or grid[row][col] == 'X':
                    os.system('cls')
                    print('Player 1 Score: {}'.format(p1_score))
                    print('Player 2 Score: {}'.format(p2_score))
                    for line in grid:
                        print(line)
                    print('*'*50)
                    print('That tile is occupied.')
                else:
                    break
            if menu == True:
                break
            print('*'*50)
            os.system('cls')
            if change%2 == 0:
                if dot%2 == 0:
                    grid[row][col] = 'O'
                elif dot%2 != 0:
                    grid[row][col] = 'X'
            if change%2 != 0:
                if dot%2 == 0:
                    grid[row][col] = 'X'
                elif dot%2 != 0:
                    grid[row][col] = 'O'
            print('Player 1 Score: {}'.format(p1_score))
            print('Player 2 Score: {}'.format(p2_score))
            for line in grid:
                print(line)
            print('*'*50)
            score = checker()
            if score[0] != 0 or score[1] != 0:
                break
        if menu == True:
            break
        if score[0] != 0:
            print('Player 1 wins!')
            p1_score += 1
        elif score[1] != 0:
            print('Player 2 wins!')
            p2_score += 1
        else:
            print('Draw!')
        last_change = int(change)
        change += 1


def ai():
    change = 0
    last_change = 0
    global grid
    p1_score = 0
    ai_score = 0
    menu = False
    while True:
        os.system('cls')
        grids = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
        if last_change != change:
            grid = grids
        print('Player Score: {}'.format(p1_score))
        print('AI Score: {}'.format(ai_score))
        for line in grid:
            print(line)

        print('*'*50)

        dot = -1
        while True:
            dot += 1
            if dot == 25:
                break
            if change%2 == 0:
                if dot%2 == 0:
                    note = 0
                elif dot%2 != 0:
                    note = 1
            elif change%2 != 0:
                if dot%2 == 0:
                    note = 1
                elif dot%2 != 0:
                    note = 0

            while note == 0:
                print('---Player Turn---')
                move1 = input('Input row number and column number |ex.[5 5]|: ')
                if move1 == 'MENU':
                    menu = True
                    break
                move = [int(q) for q in move1.split()]
                row = move[0] - 1
                col = move[1] - 1
                if row > 4 or col > 4:
                    os.system('cls')
                    print('Player Score: {}'.format(p1_score))
                    print('AI Score: {}'.format(ai_score))
                    for line in grid:
                        print(line)
                    print('*'*50)
                    print('Input should be within the grid range.')
                    continue
                if grid[row][col] == 'O' or grid[row][col] == 'X':
                    os.system('cls')
                    print('Player Score: {}'.format(p1_score))
                    print('AI Score: {}'.format(ai_score))
                    for line in grid:
                        print(line)
                    print('*'*50)
                    print('That tile is occupied.')
                else:
                    break

            while note == 1:
                ai_choose = [0,1,2,3,4]
                ai_row = random.choice(ai_choose)
                ai_col = random.choice(ai_choose)
                if grid[ai_row][ai_col] == 'O' or grid[ai_row][ai_col] == 'X':
                    continue
                else:
                    break
            if menu == True:
                break
            print('*'*50)
            os.system('cls')
            if change%2 == 0:
                if dot%2 == 0:
                    grid[row][col] = 'O'
                elif dot%2 != 0:
                    grid[ai_row][ai_col] = 'X'
            elif change%2 != 0:
                if dot%2 != 0:
                    grid[row][col] = 'O'
                elif dot%2 == 0:
                    grid[ai_row][ai_col] = 'X'
            print('Player Score: {}'.format(p1_score))
            print('AI Score: {}'.format(ai_score))
            for line in grid:
                print(line)
            print('*'*50)
            score = checker()
            if score[0] != 0 or score[1] != 0:
                break

        if menu == True:
            break
        if score[0] != 0:
            print('Player wins!')
            p1_score += 1
        elif score[1] != 0:
            print('AI wins!')
            ai_score += 1
        else:
            print('Draw!')
        last_change = int(change)
        change += 1


def hard_ai():
    change = 0
    last_change = 0
    global grid
    p1_score = 0
    ai_score = 0
    menu = False
    while True:
        os.system('cls')
        grids = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
        if last_change != change:
            grid = grids
        print('Player Score: {}'.format(p1_score))
        print('AI Score: {}'.format(ai_score))
        for line in grid:
            print(line)

        print('*'*50)

        dot = -1
        while True:
            dot += 1
            if dot == 25:
                break
            if change%2 == 0:
                if dot%2 == 0:
                    note = 0
                elif dot%2 != 0:
                    note = 1
            elif change%2 != 0:
                if dot%2 == 0:
                    note = 1
                elif dot%2 != 0:
                    note = 0

            while note == 0:
                print('---Player Turn---')
                move1 = input('Input row number and column number |ex.[5 5]|: ')
                if move1 == 'MENU':
                    menu = True
                    break
                move = [int(q) for q in move1.split()]
                row = move[0] - 1
                col = move[1] - 1
                if row > 4 or col > 4:
                    os.system('cls')
                    print('Player Score: {}'.format(p1_score))
                    print('AI Score: {}'.format(ai_score))
                    for line in grid:
                        print(line)
                    print('*'*50)
                    print('Input should be within the grid range.')
                    continue
                if grid[row][col] == 'O' or grid[row][col] == 'X':
                    os.system('cls')
                    print('Player Score: {}'.format(p1_score))
                    print('AI Score: {}'.format(ai_score))
                    for line in grid:
                        print(line)
                    print('*'*50)
                    print('That tile is occupied.')
                else:
                    break

            if menu == True:
                break

            if note == 1:
                all_lines = []
                all_lines_index = []

                for horlines1 in range(len(grid)):
                    horlines = []
                    horlines_index = []
                    for horlines2 in range(len(grid)):
                        horlines3 = grid[horlines1][horlines2]
                        horlines.append(horlines3)
                        horlines_index.append('{} {}'.format(horlines1, horlines2))
                    all_lines.append(horlines)
                    all_lines_index.append(horlines_index)

                for v1s in range(len(grid)):
                    verlines = []
                    verlines_index = []
                    for v2s in range(len(grid)):
                        point = grid[v2s][v1s]
                        verlines.append(point)
                        verlines_index.append('{} {}'.format(v2s, v1s))
                    all_lines.append(verlines)
                    all_lines_index.append(verlines_index)

                dialine1s = []
                dialine1s_index = []
                for d1s in range(len(grid)):
                    point2s = grid[d1s][d1s]
                    dialine1s.append(point2s)
                    dialine1s_index.append('{} {}'.format(d1s,d1s))
                all_lines.append(dialine1s)
                all_lines_index.append(dialine1s_index)

                dialine2s = []
                dialine2s_index = []
                for d2s,d3s in zip(range(0,5), range(4,-1,-1)):
                    point3s = grid[d2s][d3s]
                    dialine2s.append(point3s)
                    dialine2s_index.append('{} {}'.format(d2s,d3s))
                all_lines.append(dialine2s)
                all_lines_index.append(dialine2s_index)

                many = 0
                indexgrid = 0
                for lines in all_lines:
                    counter = lines.count('O')
                    if counter > many:
                        minicounter = 0
                        for each in lines:
                            if each == 'X' or each == 'O':
                                minicounter += 1
                        if minicounter < 5:
                            many = counter
                            indexgrid = all_lines.index(lines)

                line_many = all_lines_index[indexgrid]

                while True:
                    hard_ai_choose = random.choice(line_many)
                    hard_ai_row = int(hard_ai_choose[0])
                    hard_ai_col = int(hard_ai_choose[2])
                    if grid[hard_ai_row][hard_ai_col] == 'O' or grid[hard_ai_row][hard_ai_col] == 'X':
                        continue
                    else:
                        break

            print('*'*50)
            os.system('cls')
            if change%2 == 0:
                if dot%2 == 0:
                    grid[row][col] = 'O'
                elif dot%2 != 0:
                    grid[hard_ai_row][hard_ai_col] = 'X'
            if change%2 != 0:
                if dot%2 != 0:
                    grid[row][col] = 'O'
                elif dot%2 == 0:
                    grid[hard_ai_row][hard_ai_col] = 'X'
            print('Player Score: {}'.format(p1_score))
            print('AI Score: {}'.format(ai_score))
            for line in grid:
                print(line)
            print('*'*50)
            score = checker()
            if score[0] != 0 or score[1] != 0:
                break

        if menu == True:
            break
        if score[0] != 0:
            print('Player wins!')
            p1_score += 1
        elif score[1] != 0:
            print('AI wins!')
            ai_score += 1
        else:
            print('Draw!')
        last_change = int(change)
        change += 1


def wtf_ai():
    change = 0
    last_change = 0
    global grid
    p1_score = 0
    ai_score = 0
    menu = False
    while True:
        grids = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
        if last_change != change:
            grid = grids
        os.system('cls')
        print('Player Score: {}'.format(p1_score))
        print('AI Score: {}'.format(ai_score))
        for line in grid:
            print(line)

        print('*'*50)

        dot = -1
        while True:
            dot += 1
            if dot == 25:
                break
            if change%2 == 0:
                if dot%2 == 0:
                    note = 0
                elif dot%2 != 0:
                    note = 1
            elif change%2 != 0:
                if dot%2 == 0:
                    note = 1
                elif dot%2 != 0:
                    note = 0

            while note == 0:
                print('---Player Turn---')
                move1 = input('Input row number and column number |ex.[5 5]|: ')
                if move1 == 'MENU':
                    menu = True
                    break
                move = [int(q) for q in move1.split()]
                row = move[0] - 1
                col = move[1] - 1
                if row > 4 or col > 4:
                    os.system('cls')
                    print('Player Score: {}'.format(p1_score))
                    print('AI Score: {}'.format(ai_score))
                    for line in grid:
                        print(line)
                    print('*'*50)
                    print('Input should be within the grid range.')
                    continue
                if grid[row][col] == 'O' or grid[row][col] == 'X':
                    os.system('cls')
                    print('Player Score: {}'.format(p1_score))
                    print('AI Score: {}'.format(ai_score))
                    for line in grid:
                        print(line)
                    print('*'*50)
                    print('That tile is occupied.')
                else:
                    break

            if menu == True:
                break

            if note == 1:
                all_lines = []
                all_lines_index = []

                for horlines1 in range(len(grid)):
                    horlines = []
                    horlines_index = []
                    for horlines2 in range(len(grid)):
                        horlines3 = grid[horlines1][horlines2]
                        horlines.append(horlines3)
                        horlines_index.append('{} {}'.format(horlines1, horlines2))
                    all_lines.append(horlines)
                    all_lines_index.append(horlines_index)

                for v1s in range(len(grid)):
                    verlines = []
                    verlines_index = []
                    for v2s in range(len(grid)):
                        point = grid[v2s][v1s]
                        verlines.append(point)
                        verlines_index.append('{} {}'.format(v2s, v1s))
                    all_lines.append(verlines)
                    all_lines_index.append(verlines_index)

                dialine1s = []
                dialine1s_index = []
                for d1s in range(len(grid)):
                    point2s = grid[d1s][d1s]
                    dialine1s.append(point2s)
                    dialine1s_index.append('{} {}'.format(d1s,d1s))
                all_lines.append(dialine1s)
                all_lines_index.append(dialine1s_index)

                dialine2s = []
                dialine2s_index = []
                for d2s,d3s in zip(range(0,5), range(4,-1,-1)):
                    point3s = grid[d2s][d3s]
                    dialine2s.append(point3s)
                    dialine2s_index.append('{} {}'.format(d2s,d3s))
                all_lines.append(dialine2s)
                all_lines_index.append(dialine2s_index)

                many = 0
                indexgrid = 0
                for lines in all_lines:
                    counter = lines.count('O')
                    if 'X' in lines:
                        continue
                    if counter > many:
                        minicounter = 0
                        for each in lines:
                            if each == 'X' or each == 'O':
                                minicounter += 1
                        if minicounter < 5:
                            many = counter
                            indexgrid = all_lines.index(lines)

                print(many)
                print(indexgrid)

                many2 = 0
                indexgrid2 = 0
                enemy_counter = 0
                for enemy_counter1 in all_lines:
                    if 'O' in enemy_counter1:
                        enemy_counter += 1
                for lines2 in all_lines:
                    counter2 = lines2.count('X')
                    if 'O' in lines2 and enemy_counter < len(all_lines):
                        continue
                    if counter2 > many2:
                        minicounter2 = 0
                        for each2 in lines2:
                            if each2 == 'X' or each2 == 'O':
                                minicounter2 += 1
                        if minicounter2 < 5:
                            many2 = counter2
                            indexgrid2 = all_lines.index(lines2)
                print(len(all_lines))
                print(many2)
                print(indexgrid2)
                if many > many2:
                    line_many = all_lines_index[indexgrid]
                elif many2 >= many:
                    line_many = all_lines_index[indexgrid2]

                while True:
                    hard_ai_choose = random.choice(line_many)
                    hard_ai_row = int(hard_ai_choose[0])
                    hard_ai_col = int(hard_ai_choose[2])
                    if grid[hard_ai_row][hard_ai_col] == 'O' or grid[hard_ai_row][hard_ai_col] == 'X':
                        continue
                    else:
                        break

            print('*'*50)
            os.system('cls')
            if change%2 == 0:
                if dot%2 == 0:
                    grid[row][col] = 'O'
                elif dot%2 != 0:
                    grid[hard_ai_row][hard_ai_col] = 'X'
            if change%2 != 0:
                if dot%2 != 0:
                    grid[row][col] = 'O'
                elif dot%2 == 0:
                    grid[hard_ai_row][hard_ai_col] = 'X'
            print('Player Score: {}'.format(p1_score))
            print('AI Score: {}'.format(ai_score))
            for line in grid:
                print(line)
            print('*'*50)
            score = checker()
            if score[0] != 0 or score[1] != 0:
                break

        if menu == True:
            break
        if score[0] != 0:
            print('Player wins!')
            p1_score += 1
        elif score[1] != 0:
            print('AI wins!')
            ai_score += 1
        else:
            print('Draw!')
        last_change = int(change)
        change += 1



while True:
    grid = [['','','','',''],['','','','',''],['','','','',''],['','','','',''],['','','','','']]
    x = input('PVP or AI: ')
    if x == 'PVP':
        pvp()
    elif x == 'AI':
        xx = input('EZ or HARD or WTF: ')
        if xx == 'EZ':
            ai()
        elif xx == 'HARD':
            hard_ai()
        elif xx == 'WTF':
            wtf_ai()
    else:
        continue
