import Stack 

class Stack():
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return self.items == []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)

maze = [
	['+','+','+','+','+','+'],
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

	### Trackers and Counters
	global goalFound 
	goalFound = False 
	global noSolution
	noSolution = False
	global counter 
	counter = 0

	### Maze checker 'G', '', '|'
	def checkValid(coord):
		x, y = coord
		print(f'Checking [{x},{y}]')
		if maze[x][y] == " ": 
			return True 

	def checkGoal(coord):
		x, y = coord
		if maze[x][y] == 'G': 
			global goalFound
			goalFound = True
			return True
		
        
	### Movement functions
	def moveForward(coord):
		x, y = coord
		print(f'Moved to [{x},{y}]')
		stack.push([x, y])
		# Marks the step taken
		global counter
		counter += 1
		maze[x][y] = counter
		printMaze(maze)
		checkCounterClockwise(x, y)

	def moveBackward():
		stack.pop()
		lastStep = stack.peek() 
		print("Last coord:", lastStep)
		x, y = lastStep
		checkCounterClockwise(x, y)
			
	def checkCounterClockwise(x, y):
		north = [x - 1 , y]
		west = [x, y - 1]
		south = [x + 1, y]
		east = [x, y + 1]
		if stack.size() == 0:
			print(stack.peek())
			global noSolution
			noSolution = True
		elif checkGoal(north) == True:
			return True
		elif checkGoal(west) == True:
			return True
		elif checkGoal(south) == True:
			return True
		elif checkGoal(east) == True:
			return True
		elif checkValid(north) == True:
			moveForward(north)
		elif checkValid(west) == True:
			moveForward(west)
		elif checkValid(south) == True:
			moveForward(south)
		elif checkValid(east) == True:
			moveForward(east)
		else:
			moveBackward()
   
	while goalFound == False and noSolution == False:
		moveForward([startX, startY])
	else:
		print("Maze is finished")
		return True
	
 
solveMaze(maze, 4, 4)
		
			



