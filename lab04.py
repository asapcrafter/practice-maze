import Stack 

maze = [
	['+','+','+','+','G','+'],
	['+',' ','+',' ',' ','+'],
	['+',' ',' ',' ','+','+'],
	['+',' ','+','+',' ','+'],
	['+',' ',' ',' ',' ','+'],
	['+','+','+','+','+','+'] ]

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return

def solveMaze(maze, startX, startY):
	stack = Stack()
	stack.push([startX, startY])

	# Stops the program once the goal is reached
	goalFound = False 
	# Keeps track of how many valid steps were taken in the maze
	counter = 0

	def checkGoal(x, y):
		if maze[x][y] == 'G': goalFound = True; return False
	def checkValid(x, y):
		if maze[x][y] == ' ': return True; return False

	def moveForward(x, y):
		counter += 1
		maze[x][y] = counter


	def moveBackward(x, y):
		return

	def checkCounterClockwise(x, y):
		def checkNorth():
			checkValid(x + 1, y)
			checkGoal(x + 1, y)
		def checkWest():
			checkValid(x, y - 1)
			checkGoal(x, y - 1)
		def checkSouth():
			checkValid(x - 1, y)
			checkGoal(x - 1, y)
		def checkEast():
			checkValid(x, y + 1)
			checkGoal(x, y + 1)

		if checkNorth() == True:
			moveForward(x + 1, y)
		elif checkWest() == True:
			moveForward(x, y - 1)
		elif checkSouth() == True:
			moveForward(x - 1, y)
		elif checkEast() == True:
			moveForward(x, y + 1)
		
			



