import pygame
import sys, getopt
import numpy as np
import time

#Constants
size_win_x = 600
size_win_y = 600
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
rgb = [red,green,blue]
coord = [[[76,77],[[79,94],[58,65],[94,60]]],
		 [[299,77],[[302,94],[281,65],[317,60]]],
		 [[522,77],[[525,94],[504,65],[540,60]]],
		 [[76,302],[[79,319],[58,290],[94,285]]],
		 [[299,302],[[302,319],[281,290],[317,285]]],
		 [[522,302],[[525,319],[504,290],[540,285]]],
		 [[76,525],[[79,542],[58,513],[94,508]]],
		 [[299,525],[[302,542],[281,513],[317,508]]],
		 [[522,525],[[525,542],[504,513],[540,508]]]
		]

circles = []
screen = []

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            	return

def init_gui():
	global screen
	pygame.init()
	screen = pygame.display.set_mode((size_win_x,size_win_y))
	image = pygame.image.load("graph.gif")
	screen.blit(image, [0, 0])
	draw_circles()
	pygame.display.update()
	wait()

def draw_circles():
	global circles
	for i in range(0,9):
		circles.append([])
		x,y = (coord[i][0][0]+2, coord[i][0][1]+1)
		circles[i].append(pygame.draw.circle(screen, black, (x,y),50,1))
		circles[i].append([])
		for j in range(0,3):
			x,y = (coord[i][1][j][0]+2, coord[i][1][j][1]+1)
			circles[i][1].append(pygame.draw.circle(screen, rgb[j], (x,y),15,0))

def circle_assigment(id,value):
	global circles
	color = {'R':red, 'B': blue, 'G':green}
	x,y = (coord[id][0][0]+2, coord[id][0][1]+1)
	circles[id][0] = pygame.draw.circle(screen, color[value], (x,y),50,0)	
	pygame.display.update()

def circle_unassigment(id):
	global circles
	x,y = (coord[id][0][0]+2, coord[id][0][1]+1)
	circles[id][0] = pygame.draw.circle(screen, white, (x,y),50,0)
	circles[id][0] = pygame.draw.circle(screen, black, (x,y),50,1)
	for j in range(0,3):
			x,y = (coord[id][1][j][0]+2, coord[id][1][j][1]+1)
			circles[id][1][j] = pygame.draw.circle(screen, black, (x,y),15,1)
	pygame.display.update()

def update_assign_domain(id,domain,has_assigment):
	global circles
	if has_assigment==False:
		if 'R' in domain:		
			x,y = (coord[id][1][0][0]+2, coord[id][1][0][1]+1)
			circles[id][1][0] = pygame.draw.circle(screen, red, (x,y),15,0)
		else:
			x,y = (coord[id][1][0][0]+2, coord[id][1][0][1]+1)
			circles[id][1][0] = pygame.draw.circle(screen, white, (x,y),15,0)
		if 'G' in domain:		
			x,y = (coord[id][1][1][0]+2, coord[id][1][1][1]+1)
			circles[id][1][1] = pygame.draw.circle(screen, green, (x,y),15,0)
		else:
			x,y = (coord[id][1][1][0]+2, coord[id][1][1][1]+1)
			circles[id][1][1] = pygame.draw.circle(screen, white, (x,y),15,0)
		if 'B' in domain:		
			x,y = (coord[id][1][2][0]+2, coord[id][1][2][1]+1)
			circles[id][1][2] = pygame.draw.circle(screen, blue, (x,y),15,0)
		else:
			x,y = (coord[id][1][2][0]+2, coord[id][1][2][1]+1)
			circles[id][1][2] = pygame.draw.circle(screen, white, (x,y),15,0)
	else:
		if 'R' in domain:
			x,y = (coord[id][1][0][0]+2, coord[id][1][0][1]+1)
			circles[id][1][0] = pygame.draw.circle(screen, red, (x,y),15,0)
			x,y = (coord[id][1][1][0]+2, coord[id][1][1][1]+1)
			circles[id][1][1] = pygame.draw.circle(screen, red, (x,y),15,0)
			x,y = (coord[id][1][2][0]+2, coord[id][1][2][1]+1)
			circles[id][1][2] = pygame.draw.circle(screen, red, (x,y),15,0)
		if 'G' in domain:
			x,y = (coord[id][1][0][0]+2, coord[id][1][0][1]+1)
			circles[id][1][0] = pygame.draw.circle(screen, green, (x,y),15,0)
			x,y = (coord[id][1][1][0]+2, coord[id][1][1][1]+1)
			circles[id][1][1] = pygame.draw.circle(screen, green, (x,y),15,0)
			x,y = (coord[id][1][2][0]+2, coord[id][1][2][1]+1)
			circles[id][1][2] = pygame.draw.circle(screen, green, (x,y),15,0)
		if 'B' in domain:
			x,y = (coord[id][1][0][0]+2, coord[id][1][0][1]+1)
			circles[id][1][0] = pygame.draw.circle(screen, blue, (x,y),15,0)
			x,y = (coord[id][1][1][0]+2, coord[id][1][1][1]+1)
			circles[id][1][1] = pygame.draw.circle(screen, blue, (x,y),15,0)
			x,y = (coord[id][1][2][0]+2, coord[id][1][2][1]+1)
			circles[id][1][2] = pygame.draw.circle(screen, blue, (x,y),15,0)

	pygame.display.update()





# init_gui()
# circle_assigment(0,'G')
# wait()
# circle_unassigment(0)
# wait()







