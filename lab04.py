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
		if maze[x][y] == ' ': 
			return True 
		elif maze[x][y] == 'G': 
		
			goalFound = True
		else: 
	  		return False
        
     

	### Movement functions
	def moveForward(x, y):
		printMaze(maze)
		stack.push([x, y])
		global counter
		counter += 1
		maze[x][y] = counter
		checkCounterClockwise(x, y)

	def moveBackward():
		stack.peek() 
		
	def checkCounterClockwise(x, y):
		print("Checking around")
		def checkNorth():
			checkValid(x - 1, y)
			checkGoal(x - 1, y)
		def checkWest():
			checkValid(x, y - 1)
			checkGoal(x, y - 1)
		def checkSouth():
			checkValid(x + 1, y)
			checkGoal(x + 1, y)
		def checkEast():
			checkValid(x, y + 1)
			checkGoal(x, y + 1)
		if checkNorth() == True:
			print("Valid")
			moveForward(x + 1, y)
		elif checkWest() == True:
			moveForward(x, y - 1)
		elif checkSouth() == True:
			moveForward(x - 1, y)
		elif checkEast() == True:
			moveForward(x, y + 1)
		else:
			moveBackward()
   
 
	moveForward(startX, startY)
	printMaze(maze)
	# while goalFound == False:
 
solveMaze(maze, 4, 4)
		
			



