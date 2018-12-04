import pyglet
from pyglet.window import key
import engine

from typing import List, Any



window = pyglet.window.Window(engine.window_width, engine.window_height)

@window.event
def on_draw():
    global score
    global o_score
    global x_score
    window.clear()
    if engine.draw_intro:
        engine.intro_sprite.draw()
        engine.Shape.draw_square()
        #engine.music()
        #engine.have_music()
    elif engine.draw_mode:
        window.clear()
        engine.bg_menu_sprite.draw()
        engine.mode_batch.draw()
    elif engine.draw_AI_levels:
        window.clear()
        engine.bg_menu_sprite.draw()
        engine.AI_levels_batch.draw()
    elif engine.game:
        window.clear()
        engine.bg_game_sprite.draw()
        engine.game_batch.draw()
        engine.score = engine.checker(engine.grid)
        engine.game_over = engine.player_blank_wins(engine.score)
        if not (engine.game_over):
            engine.player_turn(engine.ctr)
            engine.show_score()
    elif engine.draw_outro:
        window.clear()
        engine.bg_game_sprite.draw()
        engine.game_batch.draw()
        engine.player_display()
        engine.know_loss()
        if engine.mode != 'AI':
            if engine.cont == True:
                if engine.score[0] != 0:
                    engine.o_score += 1
                if engine.score[1] != 0:
                    engine.x_score += 1
                engine.GAMEOVER()
            elif engine.menu == True:
                if engine.score[0] != 0:
                    engine.o_score += 1
                if engine.score[1] != 0:
                    engine.x_score += 1
                engine.change()
        elif engine.mode == 'AI' and engine.loss == False:
            if engine.cont == True:
                if engine.score[0] != 0:
                    engine.o_score += 1
                if engine.score[1] != 0:
                    engine.x_score += 1
                engine.GAMEOVER()
            elif engine.menu == True:
                if engine.score[0] != 0:
                    engine.o_score += 1
                if engine.score[1] != 0:
                    engine.x_score += 1
                engine.change()
        elif engine.mode == 'AI' and engine.loss == True:
            if engine.menu == True:
                if engine.score[0] != 0:
                    engine.o_score += 1
                if engine.score[1] != 0:
                    engine.x_score += 1
                engine.change()
    elif engine.placeholder:
        window.clear()
        engine.bg_score_sprite.draw()
        engine.final_score()
        if engine.ok == True:
            if engine.confirm == True:
                engine.go_to_username()
            elif engine.confirm == False:
                engine.back_to_menu()
    elif engine.input_username:
        window.clear()
        engine.bg_username_sprite.draw()
        engine.ask_username()
        if engine.ok1 == True:
            engine.put_username_in_file()
            engine.go_to_leaderboards()
    elif engine.draw_leaderboards:
        window.clear()
        engine.bg_leaderboards_sprite.draw()
        engine.top_five()

@window.event
def on_key_press(symbol, modifiers):
    global draw_intro
    global draw_mode
    global temporary
    global input_username
    global ok1
    global draw_leaderboards
    global ok
    global confirm
    if engine.draw_intro:
        if symbol == key.ENTER:
            engine.draw_intro = False
            engine.draw_mode = True
    elif engine.placeholder:
        if symbol == key.ENTER:
            engine.ok = True
            if engine.mode == 'AI':
                engine.confirm = True
    elif engine.input_username and len(engine.temporary) < 8:
        if symbol == key.A:
            engine.temporary.append('A')
        elif symbol == key.B:
            engine.temporary.append('B')
        elif symbol == key.C:
            engine.temporary.append('C')
        elif symbol == key.D:
            engine.temporary.append('D')
        elif symbol == key.E:
            engine.temporary.append('E')
        elif symbol == key.F:
            engine.temporary.append('F')
        elif symbol == key.G:
            engine.temporary.append('G')
        elif symbol == key.H:
            engine.temporary.append('H')
        elif symbol == key.I:
            engine.temporary.append('I')
        elif symbol == key.J:
            engine.temporary.append('J')
        elif symbol == key.K:
            engine.temporary.append('K')
        elif symbol == key.L:
            engine.temporary.append('L')
        elif symbol == key.M:
            engine.temporary.append('M')
        elif symbol == key.N:
            engine.temporary.append('N')
        elif symbol == key.O:
            engine.temporary.append('O')
        elif symbol == key.P:
            engine.temporary.append('P')
        elif symbol == key.Q:
            engine.temporary.append('Q')
        elif symbol == key.R:
            engine.temporary.append('R')
        elif symbol == key.S:
            engine.temporary.append('S')
        elif symbol == key.T:
            engine.temporary.append('T')
        elif symbol == key.U:
            engine.temporary.append('U')
        elif symbol == key.V:
            engine.temporary.append('V')
        elif symbol == key.W:
            engine.temporary.append('W')
        elif symbol == key.X:
            engine.temporary.append('X')
        elif symbol == key.Y:
            engine.temporary.append('Y')
        elif symbol == key.Z:
            engine.temporary.append('Z')
    elif engine.draw_leaderboards:
        if symbol == key.ENTER:
            engine.back_to_menu()
    if engine.input_username:
        if symbol == key.BACKSPACE:
            if len(engine.temporary) > 0:
                del engine.temporary[-1]
        elif symbol == key.ENTER:
            engine.ok1 = True

@window.event
def on_mouse_press(x, y, button, modifiers):
    global ctr
    global draw_AI_levels
    global draw_mode
    global mode
    global ai_level
    global score
    global game_over
    global draw_outro
    global cont
    global menu
    global placeholder
    global ok
    global ok1
    global input_username
    global confirm
    global draw_leaderboards
    global music_ctr
    if engine.draw_intro:
        if x < engine.window_width/5 and y > (9*engine.window_height/10):
            engine.music_ctr += 1
            engine.music()
    elif engine.game and not (engine.someone_won):
        engine.player_turn(engine.ctr)
        if y < engine.window_height / 6:
            return

        col = int(x // (engine.window_width / 5))
        row = int(y // ((engine.window_height - engine.window_height / 6) / 5)) - 1
        x_coordinate = col * (engine.window_width / 5) + engine.window_width / 10
        y_coordinate = (row + 1) * ((engine.window_height - engine.window_height / 6) / 5) + (engine.window_height - engine.window_height / 6) / 10

        if engine.grid[row][col] != None and engine.mode == 'AI' and engine.ctr % 2 == 1:
            engine.ai()
        if engine.grid[row][col] != None:
            print("Tile occupied!")
            return
        engine.ctr += 1
        if engine.ctr % 2 == 0:
            engine.game_sprites.append(pyglet.sprite.Sprite(engine.O_image, x_coordinate, y_coordinate, batch=engine.game_batch))
            engine.grid[row][col] = 'O'

        if engine.ctr % 2 == 1:
            engine.game_sprites.append(pyglet.sprite.Sprite(engine.X_image, x_coordinate, y_coordinate, batch=engine.game_batch))
            engine.grid[row][col] = 'X'
            if engine.mode == 'AI':
                engine.score = engine.checker(engine.grid)
                engine.game_over = engine.player_blank_wins(engine.score)
                if not (engine.game_over):
                    engine.ai()
    elif engine.draw_mode:
        if (2 * engine.window_height / 3 - 50) < y < (2 * engine.window_height / 3 + 50):
            engine.start()
        elif (engine.window_height / 3 - 50) < y < (engine.window_height / 3 + 50):
            engine.draw_mode = False
            engine.draw_AI_levels = True
            engine.mode = 'AI'
    elif engine.draw_AI_levels:
        if (3 * engine.window_height / 4 - 50) < y < (3 * engine.window_height / 4 + 50):
            engine.ai_level = 'ez'
            engine.start()
        elif (engine.window_height / 2 - 50) < y < (engine.window_height / 2 + 50):
            engine.ai_level = 'hard'
            engine.start()
        elif (engine.window_height / 4 - 50) < y < (engine.window_height / 4 + 50):
            engine.ai_level = 'wtf'
            engine.start()
    elif engine.draw_outro:
        if (2 * engine.window_height / 3 - 25) < y < (
                2 * engine.window_height / 3 + 25) and engine.window_width / 2 - 130 < x < engine.window_width / 2 + 130:
            engine.cont = True
        if (engine.window_height / 3 - 25) < y < (
                engine.window_height / 3 + 25) and engine.window_width / 2 - 80 < x < engine.window_width / 2 + 80:
            engine.menu = True
    elif engine.placeholder:
        #if window_height / 3 - 45 < y < window_height / 3 + 45 and window_width / 2 - 60 < x < window_width / 2 + 60:
        if y < engine.window_height/3:
            engine.ok = True
            if engine.mode == 'AI':
                engine.confirm = True
    elif engine.input_username:
        if engine.window_height / 3 - 25 < y < engine.window_height / 3 + 25 and engine.window_width / 2 - 40 < x < engine.window_width / 2 + 40:
            engine.ok1 = True
    elif engine.draw_leaderboards:
        if y < engine.window_height/8:
            engine.back_to_menu()

# increases font on mouse hover
@window.event
def on_mouse_motion(x, y, dx, dy):
    if engine.draw_mode:
        if (2 * engine.window_height / 3 - 50) < y < (2 * engine.window_height / 3 + 50):
            engine.pvp_sprite.scale = 1.5
            engine.ai_sprite.scale = 1
        elif (engine.window_height / 3 - 50) < y < (engine.window_height / 3 + 50):
            engine.ai_sprite.scale = 1.5
            engine.pvp_sprite.scale = 1
        else:
            engine.pvp_sprite.scale = 1
            engine.ai_sprite.scale = 1
    elif engine.draw_AI_levels:
        if (3 * engine.window_height / 4 - 50) < y < (3 * engine.window_height / 4 + 50):
            engine.ez_sprite.scale = 1.5
            engine.hard_sprite.scale = 1
            engine.wtf_sprite.scale = 1
        elif (engine.window_height / 2 - 50) < y < (engine.window_height / 2 + 50):
            engine.hard_sprite.scale = 1.5
            engine.ez_sprite.scale = 1
            engine.wtf_sprite.scale = 1
        elif (engine.window_height / 4 - 50) < y < (engine.window_height / 4 + 50):
            engine.wtf_sprite.scale = 1.5
            engine.ez_sprite.scale = 1
            engine.hard_sprite.scale = 1
        else:
            engine.ez_sprite.scale = 1
            engine.hard_sprite.scale = 1
            engine.wtf_sprite.scale = 1
    elif engine.draw_outro:
        if engine.window_width / 2 - 165 < x < engine.window_width / 2 + 165 and engine.window_height * (2 / 3) - 40 < y < engine.window_height * (2 / 3) + 40:
            engine.continue_sprite.scale = 1.5
            engine.menu_sprite.scale = 1
        elif engine.window_width / 2 - 105 < x < engine.window_width / 2 + 105 and engine.window_height * (1 / 3) - 40 < y < engine.window_height * (1 / 3) + 40:
            engine.continue_sprite.scale = 1
            engine.menu_sprite.scale = 1.5
        else:
            engine.continue_sprite.scale = 1
            engine.menu_sprite.scale = 1




pyglet.app.run()
