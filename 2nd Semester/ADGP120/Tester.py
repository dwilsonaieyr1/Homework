import pygame
import Image
import random
from random import*
from Image import *
from pygame.locals import *
import time



# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.	
searchSpace = []
infoy = 0
HoldN = []
a = Node(-10, -10)
	
# Initialize pygame
pygame.init()
	

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = width, height = 600, 600
size = 180, 180
screen = pygame.display.set_mode(WINDOW_SIZE)

	
for r in range(0, 10):
		HoldN = []
		for i in range(0, 10):
			HoldN.append(Node(i * (a.width + a.space), infoy))
		searchSpace.append(HoldN)
		infoy += HoldN[0].height + HoldN[0].space
	#for x in range(cols):
		#for y in range(rows):
			#print x,",",y, "Index", id
			#n = Node(x, y)
			
			
			
			#cantreach = True if (x >= 5 and x <= 8 and y >= 3 and y >= 8) else False
			#print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.pos)
			
			
			
			
			
			
#Used to test functions			
MD = Algorithm(searchSpace[0],searchSpace,searchSpace[9])	####???
Node1 = Node (3,5)	#
Node2 = Node (5,8)	#
#Node3 = Node (x-1,y-1)
#MD.Mdist (Node1, Node2)
#MD.Adj (Node3)
	
Control = Algorithm(searchSpace[1][1], searchSpace, searchSpace[8][8])
	
for r in searchSpace:	# Generate unwalkable walls
		for n in r:
			rand = randrange(0,5)
			if(rand % 3 == 0) and (Control.currentNode != n) and (Control.goal != n):
				n.walkable = False
			n.Draw(screen)
			
Control.Draw(screen)
#If the goal is found.
if(Control.Star()):		#Control.Star is our loop
                #checks for goal in the open list.
		for n in Control.OPEN:
			if n != Control.goal:
				pygame.draw.rect(screen, [0,255,0,0],[(n.x,n.y),(n.width, n.height)])
		#checks for goal in the closed list
		for n in Control.CLOSED:
			if(n != Control.start) and (n != Control.goal):
				pygame.draw.rect(screen,[0,208, 32, 144],[(n.x, n.y), (n.width, n.height)])
		#checks through the searchspace for parent nodes.
		for l in Control.ss:
			for n in l:
				if n.parent != None:
					pygame.draw.line(screen,[255,65,105,225],n.center,n.parent.center, 5)
					pygame.draw.circle(screen,[255,65,105,225], n.center, 10, 0)
		#Draws path to the screen			
		Control.Path(screen)
#If the goal is not found	
else:
                #checks for goal in the open list
		for n in Control.OPEN:
			if n != Control.OPEN:
				if n != Control.goal:
					pygame.draw.rect(screen,[0, 255, 0, 0],[(n.x,n.y),(n.width, n.height)])
		#checks for goal in the closed list
		for n in Control.CLOSED:
			if(n != Control.start) and (n != Control.goal):
				pygame.draw.rect(screen, [0,0,255,255],[(n.x, n.y), (n.width, n.height)])
		#checks through the searchspace
                for l in Control.ss:
			for n in l:
				if n.parent != None:
					pygame.draw.line(screen, [255, 0, 255, 255], n.center, n.parent.center, 5)
					pygame.draw.circle(screen,[255,0,255,255], n.center, 2, 0)
			#pygame.draw.line(screen,[100,100,100,255],[0, 0], size, 10)

	
# Set title of screen
pygame.display.set_caption("ADGP120 A*")

# Loop until the user clicks the close button.
done = False
started = None




	# -------- Main Program Loop -----------
while not done:
		for event in pygame.event.get():  # User did something
			if event.type == pygame.QUIT:  # If user clicked close
				done = True				# Flag that we are done so we exit this loop
			elif event.type == pygame.K_ESCAPE:
				done = True
		
		
		
		
		
		
		
		
		
		
		pygame.display.flip()

