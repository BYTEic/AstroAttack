import pygame
import random
try:
    pygame.joystick.init()
except:
    pass
def getscores(row):
    config = open('hightscores.txt','r')
    lines = config.read().splitlines()
    return lines[row]
def setscores(lines):
	with open("hightscores.txt", "w") as file:
		for  line in lines:
			file.write(line + '\n')
window_size_x = 500
window_size_y = 500
pygame.mixer.init(frequency=44100, size=-16, channels=1, buffer=4096)
pygame.init()
game = pygame.display.set_mode((window_size_x,window_size_y))
pygame.display.set_caption("Astro attack!")
gameover = False
x = (500//2)-(32//2)
y = 450
width = 32
height = 32
speed = 5
ticks = 30
run = True
left = False
right = False
up = False
down = False
level = 0
backX = 0
backY = -500
lives_int = 3

bullets = []
dummies = []

boom_sprite = pygame.image.load('sprites/boom.bmp')

class bullet_obj():
	def __init__(self,x,y,facing,radius,color):
		self.x = x
		self.y = y
		self.facing = facing
		self.vel = 8 * facing
		self.radius = radius
		self.color = color
	def draw(self, game):
		pygame.draw.circle(game,self.color, (self.x,self.y),self.radius)

class dummie_obj():
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.vel = 2
	def draw(self, game):
		game.blit(dummie,(self.x,self.y))
	def isCollide(self,x,y,width,height):
		if (self.x < (x + width) and (self.x + 32) > x and self.y < (y + height) and (32 + self.y) > y):
			return True
		else:
			return False
	def boom(self,game):
		game.blit(boom_sprite,(self.x,self.y))
		pygame.display.update()

score_hud = pygame.image.load('score_hud.bmp')

lives_hud = pygame.image.load('Lives_hud.bmp')

RightFrame = pygame.image.load('sprites/right.bmp')

LeftFrame = pygame.image.load('sprites/left.bmp')

ForwardFrame = pygame.image.load('sprites/up.bmp')

BackwardFrame = pygame.image.load('sprites/down.bmp')

IDLEframe = pygame.image.load('sprites/SpaceShip1.bmp')

background = pygame.image.load('space.bmp')

dummie = pygame.image.load('sprites/SpaceShip2.bmp')
chance_dummie_do_not_spawn = 0.9
basis33 = pygame.font.Font('basis33.ttf',50)
score_int = 0
clock = pygame.time.Clock()
score_ = basis33.render(str(score_int), False, (0,0,250))
lives_ = basis33.render(str(lives_int), False, (200,0,0))
score_RectObj = score_.get_rect()
score_RectObj.center = (140, 18)
music = 0
j_check = True

pygame.mixer.music.load("sounds/m1.wav")
def update_window():
	global chance_dummie_do_not_spawn
	global music
	global backX
	global backY
	global score_RectObj
	chance_dummie_do_not_spawn -= 0.0000001
	game.blit(background,(backX,backY))
	if music == 0:
		pygame.mixer.music.play(99999999,0)
	if music == 9100:
		music = -1
	music += 1

	backY += 0.5
	if backY == 1:
		backY = -500
	for bullet in bullets:
		bullet.draw(game)
	for dummie_ in dummies:
		dummie_.draw(game)
	if left:
		game.blit(LeftFrame,(x,y))
	elif right:
		game.blit(RightFrame,(x,y))
	elif up:
		game.blit(ForwardFrame,(x,y))
	elif down:
		game.blit(BackwardFrame,(x,y))
	else:
		game.blit(IDLEframe,(x,y))
	score_ = basis33.render(str(score_int), True, (0,0,250))
	lives_ = basis33.render(str(lives_int), False, (200,0,0))
	game.blit(lives_, (480,-5))
	game.blit(lives_hud,(350,0))
	game.blit(score_, score_RectObj)
	game.blit(score_hud,(0,0))
	clock.tick(ticks)
	pygame.display.update()

while run == True:
	if j_check:
		try:
			J_but0 = joystick.get_button(0)
			J_but1 = joystick.get_button(1)
		except:
			J_but0 = False
			J_but1 = False
			j_check = False
	keys = pygame.key.get_pressed()
	joystick_count = pygame.joystick.get_count()
	for i in range(joystick_count):
		joystick = pygame.joystick.Joystick(i)
		joystick.init()
		# Get the name from the OS for the controller/joystick
		name = joystick.get_name()
		# Usually axis run in pairs, up/down for one, and left/right for
		# the other.
		axes = joystick.get_numaxes()
		for i in range(axes):
			axis = joystick.get_axis(i)

		buttons = joystick.get_numbuttons()

		for i in range(buttons):
			button = joystick.get_button(i)
			#if button[pygame.j]

		# Hat switch. All or nothing for direction, not like joysticks.
		# Value comes back in an array.
		hats = joystick.get_numhats()


		for i in range(hats):
			hat = joystick.get_hat(i)
	horiz_axis_pos= round(joystick.get_axis(0))
	vert_axis_pos= round(joystick.get_axis(1))


	if (keys[pygame.K_z] or J_but0):
		if len(bullets) <= 5:
			bullets.append(bullet_obj(round(x + width // 2),round(y + height // 2),1,3,(random.randint(0,255),random.randint(0,255),random.randint(0,255))))
	if (keys[pygame.K_LEFT] or horiz_axis_pos == -1) and x > 0:
		x -=speed
		left = True
		right = False
		up = False
		down = False
		lastMove = "left"
	elif (keys[pygame.K_RIGHT] or horiz_axis_pos == 1) and x < window_size_x - width:
		x +=speed
		left = False
		right = True
		up = False
		down = False
		lastMove = "right"
	elif (keys[pygame.K_DOWN] or vert_axis_pos == 1) and y < window_size_y - height:
		y+=speed
		left = False
		right = False
		up = False
		down = True
		lastMove = "down"
	elif (keys[pygame.K_UP] or vert_axis_pos == -1) and y > 0:
		y -=speed
		left = False
		right = False
		up = True
		down = False
		lastMove = "up"
	else:
		left = False
		right = False
		up = False
		down = False
		animCount = 0
	if random.random() > chance_dummie_do_not_spawn:
		dummies.append(dummie_obj(random.randint(5,500),-40))
	for event in pygame.event.get():
		if event == pygame.QUIT:
			run = False
	for bullet in bullets:
		if bullet.y < 500 and bullet.y > 0:
			bullet.y -= bullet.vel
		else:
			bullets.pop(bullets.index(bullet))
	for dummie_ in dummies:
		if dummie_.y < 500 and dummie_.y > -50:
			dummie_.y += dummie_.vel
		else:
			dummies.pop(dummies.index(dummie_))
		if dummie_.isCollide(x,y,width,height):
			dummie_.boom(game)
			dummies.pop(dummies.index(dummie_))
			if lives_int == 1:
				if score_int < int(getscores(0)):
					if score_int < int(getscores(1)):
						if score_int < int(getscores(2)):
							lines = [getscores(0),getscores(1),getscores(2)]
							setscores(lines)
						else:
							lines = [getscores(0),getscores(1),str(score_int)]
							setscores(lines)
					else:
						lines = [getscores(0),str(score_int),getscores(1)]
						setscores(lines)
				else:
					lines = [str(score_int),getscores(0),getscores(1)]
					setscores(lines)
				raise SystemExit
			else:
				lives_int -= 1
		for bullet in bullets:
			if dummie_.isCollide(bullet.x,bullet.y,32,32):
				dummie_.boom(game)
				try:
					dummies.pop(dummies.index(dummie_))
					bullets.pop(bullets.index(bullet))
				except ValueError:
					print(u'Не обращайте внимание, это предупреждение о том что сразу две пули попали в объект((((')
				score_int += 1
	update_window()
run = False
