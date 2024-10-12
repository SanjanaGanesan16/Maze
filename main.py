import pygame
import csv
from time import sleep
import random

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
TILE_SIZE = 32

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def get_data(file):
	f = open(file, 'r')
	reader = csv.reader(f)
	data = []
	for line in reader:
		data.append(line)
	return data



def build_grid():
	grid = []
	i = 0
	j = 0
	for row in matrix:
		for value in row:
			if value == "0":
				data = {
					"x": j * TILE_SIZE,
					"y": i * TILE_SIZE
				}
				grid.append(data)
			j += 1
		i += 1
		j = 0
	return grid			


def render_grid(surface, grid, window):
	for i in range(len(grid)):
		window.blit(surface, (grid[i]["x"], grid[i]["y"]))


def checkWalls(move, grid):
	for i in range(len(grid)):
		if move[0] == grid[i]["x"] and move[1] == grid[i]["y"]:
			return True
	return False

def reachedGoal(matrix, move):
	i = 0
	j = 0
	for row in matrix:
		for value in row:
			if value == '2':
				goal = (j * TILE_SIZE, i * TILE_SIZE)
				if move == goal:
					return True
			j += 1
		i += 1
		j = 0
	return False



def execute(newPos):

	visited.append(newPos)
	solution.append(newPos)

	tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
	tile.fill((255, 0, 0))

	entity = pygame.Surface((TILE_SIZE, TILE_SIZE))
	entity.fill((0, 255, 0))

	render_grid(tile, grid, window)
	window.blit(entity, newPos)
	pygame.display.update()
	sleep(0.05)



	possible_moves = [
		(newPos[0], newPos[1] + TILE_SIZE),
		(newPos[0], newPos[1] - TILE_SIZE),
		(newPos[0] + TILE_SIZE, newPos[1]),
		(newPos[0] - TILE_SIZE, newPos[1])
	]


	random.shuffle(possible_moves)

	for move in possible_moves:
		if move [0] < 0 or move[1] < 0 or move[0] > 30*TILE_SIZE or move[1] > 20*TILE_SIZE:
			continue
		elif checkWalls(move, grid):
			continue
		elif move in visited:
			continue
		else:
			if reachedGoal(matrix, newPos):
				print("Solution has been found!")
				path = pygame.Surface((TILE_SIZE, TILE_SIZE))
				path.fill((0, 0, 255))
				for i in range(len(solution)):
					window.blit(path, solution[i])
					pygame.display.update()
					sleep(0.02)
				sleep(2)
				quit()
			newPos = move 
			execute(newPos)
			solution.pop()
			entity.fill(0)
			window.blit(entity, newPos)
			pygame.display.update()
			sleep(0.05)












window.fill(0)

matrix = get_data('./data')
print(matrix)
grid = build_grid()
start_position =  (0, TILE_SIZE*1)
visited = []
solution = []

execute(start_position)

pygame.display.update()
sleep(2)

