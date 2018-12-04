import pyglet
import random

window_width = 800
window_height = 700

def checker(grid):
    score_o = 0
    score_x = 0

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


def hard_ai(grid_var, window_width, window_height):
    change = 0
    last_change = 0
    p1_score = 0
    ai_score = 0
    menu = False
    grid = grid_var[:]

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
        counter = lines.count('X')
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

    grid_var[hard_ai_row][hard_ai_col] = 'O'
    x = (hard_ai_col) * (window_width / 5) + window_width/10
    y = (hard_ai_row) * (window_height - window_height / 6) / 5 + window_height/6 + window_height/12
    return x, y, hard_ai_row, hard_ai_col

def wtf_ai(grid_var, window_width, window_height):
    grid = grid_var[:]
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
        counter = lines.count('X')
        if 'O' in lines:
            continue
        if counter > many:
            minicounter = 0
            for each in lines:
                if each == 'X' or each == 'O':
                    minicounter += 1
            if minicounter < 5:
                many = counter
                indexgrid = all_lines.index(lines)


    many2 = 0
    indexgrid2 = 0
    enemy_counter = 0
    for enemy_counter1 in all_lines:
        if 'X' in enemy_counter1:
            enemy_counter += 1
    for lines2 in all_lines:
        counter2 = lines2.count('O')
        if 'X' in lines2 and enemy_counter < len(all_lines):
            continue
        if counter2 > many2:
            minicounter2 = 0
            for each2 in lines2:
                if each2 == 'X' or each2 == 'O':
                    minicounter2 += 1
            if minicounter2 < 5:
                many2 = counter2
                indexgrid2 = all_lines.index(lines2)
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

    
    grid_var[hard_ai_row][hard_ai_col] = 'O'
    x = (hard_ai_col) * (window_width / 5) + window_width/10
    y = (hard_ai_row) * (window_height - window_height / 6) / 5 + window_height/6 + window_height/12
    return x, y, hard_ai_row, hard_ai_col

intro = pyglet.image.load_animation('as.gif')
intro_sprite = pyglet.sprite.Sprite(intro)

bg_game = pyglet.image.load_animation('bggame.gif')
bg_game_sprite = pyglet.sprite.Sprite(bg_game, 0, 0)
bg_game_sprite.scale = 0.741

bg_menu = pyglet.image.load_animation('bg-menu.gif')
bg_menu_sprite = pyglet.sprite.Sprite(bg_menu, 0, 0)
bg_menu_sprite.scale = 0.75

bg_score = pyglet.image.load_animation('scorebg.gif')
bg_score_sprite = pyglet.sprite.Sprite(bg_score, 0, -20)
bg_score_sprite.scale = 1

bg_username = pyglet.image.load_animation('frame.gif')
bg_username_sprite = pyglet.sprite.Sprite(bg_username, 0, 0)
bg_username_sprite.scale = 1

bg_leaderboards = pyglet.image.load_animation('leaderboards.gif')
bg_leaderboards_sprite = pyglet.sprite.Sprite(bg_leaderboards, 0, -50)
bg_leaderboards_sprite.scale = 1

Image_width = 80
Image_height = 80

# mouse press counter
ctr = 0
o_score = 0
x_score = 0

X_image = pyglet.resource.image('x.png')
X_image.width = Image_width
X_image.height = Image_height
X_image.anchor_x = Image_width / 2
X_image.anchor_y = Image_height / 2

O_image = pyglet.resource.image('o.png')
O_image.width = Image_width
O_image.height = Image_height
O_image.anchor_x = Image_width / 2
O_image.anchor_y = Image_height / 2

grid_image = pyglet.resource.image('grid.png')
grid_image.width = window_width
grid_image.height = window_height - window_height / 6

pvp_image = pyglet.resource.image('PVP.png')
pvp_image.width = Image_width * 3
pvp_image.height = Image_height
pvp_image.anchor_x = pvp_image.width / 2
pvp_image.anchor_y = Image_height / 2

ai_image = pyglet.resource.image('AI.png')
ai_image.width = Image_width * 1.5
ai_image.height = Image_height
ai_image.anchor_x = ai_image.width / 2
ai_image.anchor_y = Image_height / 2

ez_image = pyglet.resource.image('EZ.png')
ez_image.width = Image_width * 1.5
ez_image.height = Image_height
ez_image.anchor_x = ez_image.width / 2
ez_image.anchor_y = Image_height / 2

hard_image = pyglet.resource.image('HARD.png')
hard_image.width = Image_width * 3
hard_image.height = Image_height
hard_image.anchor_x = hard_image.width / 2
hard_image.anchor_y = Image_height / 2

wtf_image = pyglet.resource.image('WTF.png')
wtf_image.width = Image_width * 3
wtf_image.height = Image_height
wtf_image.anchor_x = wtf_image.width / 2
wtf_image.anchor_y = Image_height / 2

continue_image = pyglet.resource.image('continue.png')
continue_image.anchor_x = continue_image.width / 2
continue_image.anchor_y = continue_image.height / 2

menu_image = pyglet.resource.image('menu.png')
menu_image.anchor_x = menu_image.width / 2
menu_image.anchor_y = menu_image.height / 2

draw_intro = True
draw_mode = False
draw_AI_levels = False
game = False
draw_outro = False
someone_won = False
mode = None
cont = False
menu = False
placeholder = False
draw_leaderboards = False
ok = False
ok1 = False
input_username = False
confirm = False
ai_level = None
temporary = []
loss = False



grid = [[None for i in range(5)] for i in range(5)]

game_batch = pyglet.graphics.Batch()
mode_batch = pyglet.graphics.Batch()
AI_levels_batch = pyglet.graphics.Batch()

game_sprites = []

class Button(pyglet.sprite.Sprite):
    def __init__(self, img, *args, **kwargs):
        super().__init__(img, *args, **kwargs)
        self.x = window_width/2
        self.anchor_x = self.x/2
        self.anchor_y = self.y/2


pvp_sprite = Button(pvp_image, y=window_height*(2/3), batch=mode_batch)
ai_sprite = Button(ai_image, y=window_height*(1/3), batch=mode_batch)

ez_sprite = Button(ez_image, y=window_height*(3/4), batch=AI_levels_batch)
hard_sprite = Button(hard_image, y=window_height*(1/2), batch=AI_levels_batch)
wtf_sprite = Button(wtf_image, y=window_height*(1/4), batch=AI_levels_batch)

menu_sprite = Button(menu_image, y=window_height*(1/3))
continue_sprite = Button(continue_image, y=window_height*(2/3),)




def start():
    global draw_intro
    global game
    global draw_mode
    global draw_AI_levels
    global game_sprites
    draw_intro = False
    draw_mode = False
    draw_AI_levels = False
    game = True
    del game_sprites
    game_sprites = []
    game_sprites.append(pyglet.sprite.Sprite(grid_image, 0, window_height / 6, batch=game_batch))
    player_turn(ctr)


def ai():
    global ctr
    global score
    global game_over
    global grid

    ctr += 1

    if ai_level == 'ez':
        while True:
            col = random.choice([0, 1, 2, 3, 4])
            row = random.choice([0, 1, 2, 3, 4])
            if grid[row][col] == None:
                grid[row][col] = 'O'
                break

        x = col * (window_width / 5) + window_width / 10
        y = row * (window_height - window_height / 6) / 5 + window_height / 6 + window_height / 12
    elif ai_level == 'hard':
        coordinates = hard_ai(grid, window_width, window_height)
        x = int(coordinates[0])
        y = int(coordinates[1])
        row = coordinates[2]
        col = coordinates[3]
        grid[row][col] = 'O'
    elif ai_level == 'wtf':
        coordinates = wtf_ai(grid, window_width, window_height)
        x = int(coordinates[0])
        y = int(coordinates[1])
        row = coordinates[2]
        col = coordinates[3]
        grid[row][col] = 'O'

    game_sprites.append(pyglet.sprite.Sprite(O_image, x, y, batch=game_batch))
    score = checker(grid)
    game_over = player_blank_wins(score)

def menu():
    global draw_mode
    global draw_AI_levels
    global game
    global draw_outro
    draw_mode = True
    draw_AI_levels = False
    game = False
    draw_outro = False


def change():
    global draw_outro
    global placeholder
    draw_outro = False
    placeholder = True

def go_to_leaderboards():
    global input_username
    global draw_leaderboards
    input_username = False
    draw_leaderboards = True



def back_to_menu():
    global grid
    global someone_won
    global ctr
    global ok
    global placeholder
    global draw_mode
    global o_score
    global x_score
    global cont
    global menu
    global mode
    global ok1
    global temporary
    global ai_level
    global loss
    ctr = 0
    grid = [[None for i in range(5)] for i in range(5)]
    mode = None
    someone_won = False
    ok = False
    ok1 = False
    placeholder = False
    draw_mode = True
    cont = False
    menu = False
    o_score = 0
    x_score = 0
    temporary = []
    ai_level = None
    loss = False

def go_to_username():
    global placeholder
    global input_username
    global ok
    global confirm
    ok = False
    confirm = False
    placeholder = False
    input_username = True

def put_username_in_file():
    global temporary
    global x_score
    if ai_level == 'ez':
        file = open('leaderboards_ez.txt','a')
    elif ai_level == 'hard':
        file = open('leaderboards_hard.txt','a')
    elif ai_level == 'wtf':
        file = open('leaderboards_wtf.txt','a')
    finalusername = ''.join(temporary)
    file.write(",{}/{}".format(x_score, finalusername))
    file.close()


def ask_username():
    global temporary
    finalusernametemp = ''.join(temporary)
    title = pyglet.text.Label('ENTER NAME',
                              font_size=55,
                              x=window_width / 2, y= window_height - window_height / 7,
                              anchor_x='center', anchor_y='center')
    username = pyglet.text.Label(finalusernametemp,
                                 font_size=30,
                                 x=window_width / 2, y=window_height / 2,
                                 anchor_x='center', anchor_y='center')
    okay = pyglet.text.Label('OK',
                             font_size=40,
                             x=window_width / 2, y=window_height / 3,
                             anchor_x='center', anchor_y='center')

    title.draw()
    username.draw()
    okay.draw()


def final_score():
    global x_score
    global o_score
    x_score_dis = int(x_score)
    score_x = pyglet.text.Label(str(x_score_dis),
                                font_size=80,
                                x=window_width / 3.7, y=2*window_height/5.5,
                                anchor_x='center', anchor_y='center')
    o_score_dis = int(o_score)
    score_o = pyglet.text.Label(str(o_score_dis),
                                font_size=80,
                                x=3 * window_width / 4.1, y=2*window_height/5.5,
                                anchor_x='center', anchor_y='center')
    score_x.draw()
    score_o.draw()


# prints which player's turn it is
def player_turn(ctr):
    if ctr % 2 == 0:
        label = pyglet.text.Label("X's turn!",
                                  font_size=30,
                                  x=window_width / 2, y=window_height / 6 / 2,
                                  anchor_x='center', anchor_y='center')
    else:
        if mode == 'AI':
            return
        label = pyglet.text.Label("O's turn!",
                                  font_size=30,
                                  x=window_width / 2, y=window_height / 6 / 2,
                                  anchor_x='center', anchor_y='center')

    label.draw()


def show_score():
    global x_score
    global o_score
    if mode == 'AI':
        x_score_dis = "P1's Score: {}".format(x_score)
        label_o = pyglet.text.Label(x_score_dis,
                                    font_size=20,
                                    x=window_width / 5, y=window_height / 6 / 2,
                                    anchor_x='center', anchor_y='center')
        o_score_dis = "AI's Score: {}".format(o_score)
        label_x = pyglet.text.Label(o_score_dis,
                                    font_size=20,
                                    x=4 * window_width / 5, y=window_height / 6 / 2,
                                    anchor_x='center', anchor_y='center')
    else:
        o_score_dis = "O's Score: {}".format(o_score)
        label_o = pyglet.text.Label(o_score_dis,
                                    font_size=20,
                                    x=window_width / 5, y=window_height / 6 / 2,
                                    anchor_x='center', anchor_y='center')
        x_score_dis = "X's Score: {}".format(x_score)
        label_x = pyglet.text.Label(x_score_dis,
                                    font_size=20,
                                    x=4 * window_width / 5, y=window_height / 6 / 2,
                                    anchor_x='center', anchor_y='center')
    label_o.draw()
    label_x.draw()


def winner_screen():
    global game
    global draw_outro
    game = False
    draw_outro = True


def player_blank_wins(score):
    global someone_won
    if score[0] == 0 and score[1] == 0 and ctr != 25:
        return False
    someone_won = True
    winner_screen()
    return True

def know_loss():
    global mode
    global loss
    if mode == 'AI':
        if score[0] != 0:
            loss = True

def player_display():
    global o_score
    global x_score
    global continue_sprite
    global menu_sprite
    if score[0] != 0:
        label = pyglet.text.Label("--Player O wins!--",
                                  font_size=36,
                                  x=window_width / 2, y=window_height / 6 / 2,
                                  anchor_x='center', anchor_y='center')
    elif score[1] != 0:
        label = pyglet.text.Label("--Player X wins!--",
                                  font_size=36,
                                  x=window_width / 2, y=window_height / 6 / 2,
                                  anchor_x='center', anchor_y='center')
    else:
        label = pyglet.text.Label("--Draw!--",
                                  font_size=36,
                                  x=window_width / 2, y=window_height / 6 / 2,
                                  anchor_x='center', anchor_y='center')
    if mode != 'AI' or (mode == 'AI' and loss == False):
        continue_sprite.draw()
        menu_sprite.draw()
    elif mode == 'AI' and loss == True:
        menu_sprite.draw()

    label.draw()

def top_five():
    global ai_level
    if ai_level == 'ez':
        file = open('leaderboards_ez.txt')
    elif ai_level == 'hard':
        file = open('leaderboards_hard.txt')
    elif ai_level == 'wtf':
        file = open('leaderboards_wtf.txt')
    boards_scores = file.read()
    boards_scores = boards_scores.split(',')
    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0
    ind_first = ''
    ind_second = ''
    ind_third = ''
    ind_fourth = ''
    ind_fifth = ''
    for name_score in boards_scores:
        individual_score = [q for q in name_score.split('/')]
        score = int(individual_score[0])
        individual = individual_score[1]
        if score > fifth:
            fifth = score
            ind_fifth = individual
        if score > fourth:
            fifth = fourth
            fourth = score
            ind_fifth = ind_fourth
            ind_fourth = individual
        if score > third:
            fourth = third
            third = score
            ind_fourth = ind_third
            ind_third = individual
        if score > second:
            third = second
            second = score
            ind_third = ind_second
            ind_second = individual
        if score > first:
            second = first
            first = score
            ind_second = ind_first
            ind_first = individual
    name_1 = pyglet.text.Label(ind_first,
                               font_size=20,
                               x=window_width/3, y=6*window_height/8 - 40,
                               anchor_y='center')
    name_2 = pyglet.text.Label(ind_second,
                               font_size=20,
                               x=window_width/3, y=5*window_height/8 - 40,
                               anchor_y='center')
    name_3 = pyglet.text.Label(ind_third,
                               font_size=20,
                               x=window_width/3, y=4*window_height/8 - 40,
                               anchor_y='center')
    name_4 = pyglet.text.Label(ind_fourth,
                               font_size=20,
                               x=window_width/3, y=3*window_height/8 - 40,
                               anchor_y='center')
    name_5 = pyglet.text.Label(ind_fifth,
                               font_size=20,
                               x=window_width/3, y=2*window_height/8 - 40,
                               anchor_y='center')
    score_1 = pyglet.text.Label(str(first),
                                font_size=20,
                                x=2*window_width/3 + 40, y=6*window_height/8 - 40,
                                anchor_x='center', anchor_y='center')
    score_2 = pyglet.text.Label(str(second),
                                font_size=20,
                                x=2*window_width/3 + 40, y=5*window_height/8 - 40,
                                anchor_x='center', anchor_y='center')
    score_3 = pyglet.text.Label(str(third),
                                font_size=20,
                                x=2*window_width/3 + 40, y=4*window_height/8 - 40,
                                anchor_x='center', anchor_y='center')
    score_4 = pyglet.text.Label(str(fourth),
                                font_size=20,
                                x=2*window_width/3 + 40, y=3*window_height/8 - 40,
                                anchor_x='center', anchor_y='center')
    score_5 = pyglet.text.Label(str(fifth),
                                font_size=20,
                                x=2*window_width/3 + 40, y=2*window_height/8 - 40,
                                anchor_x='center', anchor_y='center')
    number_1 = pyglet.text.Label("1. ",
                                 font_size=40,
                                 x=window_width/4, y=6*window_height/8 - 40,
                                 anchor_x='center', anchor_y='center')
    number_2 = pyglet.text.Label("2. ",
                                 font_size=40,
                                 x=window_width/4, y=5*window_height/8 - 40,
                                 anchor_x='center', anchor_y='center')
    number_3 = pyglet.text.Label("3. ",
                                 font_size=40,
                                 x=window_width/4, y=4*window_height/8 - 40,
                                 anchor_x='center', anchor_y='center')
    number_4 = pyglet.text.Label("4. ",
                                 font_size=40,
                                 x=window_width/4, y=3*window_height/8 - 40,
                                 anchor_x='center', anchor_y='center')
    number_5 = pyglet.text.Label("5. ",
                                 font_size=40,
                                 x=window_width/4, y=2*window_height/8 - 40,
                                 anchor_x='center', anchor_y='center')
    ok_leaderboard = pyglet.text.Label("OK",
                                       font_size=30, italic=True,
                                       x=window_width/2, y=1*window_height/8 - 20,
                                       anchor_x='center', anchor_y='center')
    file.close()
    name_1.draw()
    name_2.draw()
    name_3.draw()
    name_4.draw()
    name_5.draw()
    score_1.draw()
    score_2.draw()
    score_3.draw()
    score_4.draw()
    score_5.draw()
    number_1.draw()
    number_2.draw()
    number_3.draw()
    number_4.draw()
    number_5.draw()
    ok_leaderboard.draw()

def GAMEOVER():
    global grid
    global someone_won
    global ctr
    global cont
    ctr = 0
    grid = [[None for i in range(5)] for i in range(5)]
    someone_won = False
    cont = False
    start()

import sys
class Shape(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super(Shape,self).__init__(*args,**kwargs)
    def draw_triangle(self):
        pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v2i', (365,275,380,305,395,275)))
    def on_draw(self):
        sys.stdout.flush()
        self.draw_triangle()