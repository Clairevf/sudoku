'''
Claire Van Fossen 
December 22, 2015
Messing around with the turtle module
'''

from __future__ import division, print_function

import turtle
import random

COLS = 5; 
ROWS = 5; 
boxWidth = 60; 

# ==== Create the class of each block ===== #

class Block:
	def __init__(self):
		self.val = 0
		self.xCord = -1
		self.yCord = -1
	
	def set_x(self, xUnit):
		self.xCord = xUnit
	
	def set_y(self, yUnit):
		self.yCord = yUnit
	
	def set_val(self, value):
		self.val = value
	
	def retPos(self):
		return (self.xCord, self.yCord)


# ==== Create the grid using the turtle module ===== #

def makeGrid(cols, rows, width):
	george = turtle.Turtle()
	screen = george.getscreen()
	george.speed(0)


	for x in range(COLS):
		for y in range(ROWS):
			george.up()
			george.setx(x * boxWidth - 175)
			george.sety(y * boxWidth - 175)
			george.down()
			for i in range(4):
				george.forward(boxWidth)
				george.left(90)

	# create the thick outside border


	for i in range(4):
		george.up()
		george.setx(-175 - i)
		george.sety(-175 - i)	
		george.down()
		for j in range(4):
			george.forward(boxWidth * COLS)
			george.left(90)	
	george.hideturtle()

	screen.exitonclick()


# time to generate the matrix of sudoku blocks 

def createMatrix():
	matrix = []
	for y in range(ROWS):
		colList = []
		for x in range(COLS):
			block = Block()
			block.set_x(x)
			block.set_y(y) 
			colList.append(block)
		matrix.append(colList)
	return matrix
	
def insertBlock(matrix, xpos, ypos):
	numList = []
	for i in range(COLS):	# create new numList for each row
		numList.append(i+1)
	# remove possible numbers already in the row or col
	currBlock = matrix[ypos][xpos]
	while(currBlock.xCord != 0):	# delete all possible values left of block
		currX = currBlock.xCord
		currY = currBlock.yCord
		delVal = matrix[currY][currX-1].val
		if(delVal in numList):
			numList.remove(delVal)
		currBlock = matrix[currY][currX-1]
	currBlock = matrix[ypos][xpos]
	while(currBlock.yCord != 0):	# delete all possible values below block
		currX = currBlock.xCord
		currY = currBlock.yCord
		delVal = matrix[currY-1][currX].val
		if(delVal in numList):
			numList.remove(delVal)
		currBlock = matrix[currY-1][currX]
	# assign correct values to the left over blocks in row
	if(len(numList) != 0):
		randIndex = random.randrange(0, len(numList))
		newNum = numList[randIndex]
		matrix[ypos][xpos].set_val(newNum)
		return matrix
	else: 
		return -1
		
def populateMatrix(matrix):
	for y in range(ROWS):
		for x in range(COLS):
			# append valid number to the row slot
			if(insertBlock(matrix, x, y) == -1):
				return -1
	return matrix

def main():
	mat = createMatrix()
	result = populateMatrix(mat)
	if(result == -1):
		print('need to recreate the matrix')
		main()
	else: 
		makeGrid(COLS, ROWS, boxWidth)
		stri = ''
		for y in range(ROWS):
			for x in range(COLS):
				if(x == COLS-1):
					stri += str(mat[y][x].val)
					print(stri)
					stri = ''
				else:
					stri += str(mat[y][x].val)		
			
main()
	
	
	
	
	
	
	
	
	
	
