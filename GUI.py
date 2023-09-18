
from tkinter import *
class Graph():
	def __init__(self, vertices):
		self.graph = [[0 for column in range(vertices)]
							for row in range(vertices)]
		self.V = vertices
	''' Check if this vertex is an adjacent vertex
		of the previously added vertex and is not
		included in the path earlier '''
	def isSafe(self, v, pos, path):
		if self.graph[ path[pos-1] ][v] == 0:
			return False
		for vertex in path:
			if vertex == v:
				return False
		return True
	def hamCycleUtil(self, path, pos):
		if pos == self.V:
			if self.graph[ path[pos-1] ][ path[0] ] == 1:
				return True
			else:
				return False
		for v in range(1,self.V):
			if self.isSafe(v, pos, path) == True:
				path[pos] = v
				if self.hamCycleUtil(path, pos+1) == True:
					return True
				path[pos] = -1
		return False
	def hamCycle(self):
		path = [-1] * self.V
		''' Let us put vertex 0 as the first vertex
			in the path. If there is a Hamiltonian Cycle,
			then the path can be started from any point
			of the cycle as the graph is undirected '''
		path[0] = 0
		if self.hamCycleUtil(path,1) == False:
			print ("Solution does not exist\n")
			return False
		self.printSolution(path)
		return True
	def printSolution(self, path):
		print ("Solution Exists: Following",
				"is one Hamiltonian Cycle")
		for vertex in path:
			print (vertex, end = " ")
		print (path[0], "\n")
''' Let us create the following graph
	(0)--(1)--(2)
	| / \ |
	| / \ |
	| /	 \ |
	(3)-------(4) '''
g1 = Graph(5)
g1.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
			[0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
			[0, 1, 1, 1, 0], ]

''' Let us create the following graph
	(0)--(1)--(2)
	| / \ |
	| / \ |
	| /	 \ |
	(3)	 (4) '''
g2 = Graph(5)
g2.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
		[0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],
		[0, 1, 1, 0, 0], ]


  
root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text = 'Red', fg ='red',command=g2.hamCycle)
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown',command=g1.hamCycle)
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)
root.mainloop()
