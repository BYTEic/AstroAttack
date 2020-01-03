import pygame
import time
run = False
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
def getscores_all():
    config = open('hightscores.txt','r')
    return config.read().splitlines()
def game_init__():
    global window_size_x
    window_size_x = 500
    global window_size_y
    window_size_y = 500
    global menuScores
    menuScores = False
    global ticks
    ticks = 30
    global clock
    clock = pygame.time.Clock()
    global run_menu
    run_menu = True
    pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=4096)
    pygame.init()
    global menu
    menu = pygame.display.set_mode((window_size_x,window_size_y))
    pygame.display.set_caption("Astro attack!")
    global background
    background = pygame.image.load('menuScreen.bmp')
    global basis33
    basis33 = pygame.font.Font('basis33.ttf',40)
    global press_b_text
    press_b_text = basis33.render('PRESS B FOR GET HIGHSCORES', True, (200,200,0), (0,0,50))
    global HIGHTSCORES
    HIGHTSCORES_list = getscores_all()
    HIGHTSCORES = basis33.render('HIGHSCORES', False, (200,200,0))
    global hight0
    hight0 = basis33.render(HIGHTSCORES_list[0],False, (0,250,0))
    global hight1
    hight1 = basis33.render(HIGHTSCORES_list[1],False, (0,250,0))
    global hight2
    hight2 = basis33.render(HIGHTSCORES_list[2],False, (0,250,0))
    pygame.mixer.music.load("sounds/menu.wav")
    global gameover_hud
    gameover_hud = pygame.image.load('gameover_hud.bmp')
    global music
    music = 0
game_init__()

def update_window_menu():
    global music
    menu.blit(background,(0,0))
    if music == 0:
        pygame.mixer.music.play(5,0)
    if music == 4000000:
        music = -1
    music += 1
    menu.blit(press_b_text,(0,0))
    if menuScores:
        menu.fill((0,0,0))
        menu.blit(HIGHTSCORES,(0,0))
        menu.blit(hight0,(50,50))
        menu.blit(hight1,(50,100))
        menu.blit(hight2,(50,150))
    clock.tick(ticks)
    pygame.display.update()
game_init__()
check_j = True
while run_menu:
    if check_j:
        try:
            J_but0 = joystick.get_button(0)
            J_but1 = joystick.get_button(1)
        except:
            J_but0 = False
            J_but1 = False
            check_j = False
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] or J_but0:
        try:
            import main_game
        except SystemExit:
            menu.blit(gameover_hud, (0,0))

        game_init__()

    if keys[pygame.K_x] or J_but1:
        if menuScores == False:
            menuScores = True
            time.sleep(0.2)
        else:
            menuScores = False
            time.sleep(0.2)

    update_window_menu()
import menu
