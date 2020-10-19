import tkinter as tkinter
from tkinter import messagebox
import pygame
import random, math

width = 500
height = 500
rows = 20

class cube():
	def __init__(self):
		pass
	def draw(self, surface):
		pass


#class snake

def drawGrid(surface):
	global width, height, rows
	wx = width // rows
	wy = height // rows

	x = 0
	y = 0

	for i in range(rows):
		x = x + wx
		y = y + wy

		pygame.draw.line(surface,(255,255,255),(0,y),(width,y))
		pygame.draw.line(surface,(255,255,255),(x,0),(x,width))

def redrawWindow(surface):
	global width, height, rows
	surface.fill((0,0,0))
	drawGrid(surface)
	pygame.display.update()


def main():
	global width, height, rows
	win = pygame.display.set_mode((width, height))

#	s = snake((255,0,0), (10,10))
	flag = True
#	clock = pygame.time.Clock()

	while flag:
#		pygame.time.delay(50)
#		clock.tick(10)

		redrawWindow(win)

main()