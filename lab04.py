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

	### Trackers and Counters
	global goalFound 
	goalFound = False 
	global counter 
	counter = 0

	### Maze checker 'G', '', '|'
	def checkValid(x, y):
		print("Checking", x, y)
		if maze[x][y] == " ": 
			return True 
		elif maze[x][y] == 'G': 
			global goalFound
			goalFound = True
		else: 
			return False
        
	### Movement functions
	def moveForward(x, y):
		print("Moved to:", x, y)
		stack.push([x, y])
  
		global counter
		counter += 1
		maze[x][y] = counter
		printMaze(maze)
  
		checkCounterClockwise(x, y)

	def moveBackward():
		lastStep = stack.peek() 
		print("Last coord:", lastStep)
		
	def checkCounterClockwise(x, y):
		def checkNorth():
			return checkValid(x - 1, y)
		def checkWest():
			return checkValid(x, y - 1)
		def checkSouth():
			return checkValid(x + 1, y)
		def checkEast():
			return checkValid(x, y + 1)
		if checkNorth() == True:
			moveForward(x - 1, y)
		elif checkWest() == True:
			moveForward(x, y - 1)
		elif checkSouth() == True:
			moveForward(x + 1, y)
		elif checkEast() == True:
			moveForward(x, y + 1)
		else:
			moveBackward()
   
 
	moveForward(startX, startY)
	# while goalFound == False:
 
solveMaze(maze, 4, 4)
		
			



