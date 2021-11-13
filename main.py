#!/usr/local/bin/python3
size = 3

class board():
	"""sudoku board class"""
	cells = [[-1 for i in range(0, size*size)] for _ in range(0, size*size)]
	log = []

	def __init__(self):
		pass

	def set(self, cood, num):
		x = cood[0]
		y = cood[1]
		# set number on x, y
		self.cells[x][y] = num
		self.log.append((cood, num))

	def undo(self):
		l = self.log.pop()
		x = l[0][0]
		y = l[0][1]
		self.cells[x][y] = -1

	def is_blank(self, cood):
		if self.cells[cood[0]][cood[1]] == -1:
			return True
		else:
			return False

	def get_candidate(self, cood):
		x = cood[0]
		y = cood[1]
		# get candidate on x, y
		if not(self.is_blank(cood)):
			return set()
		st = set()
		# row, column
		for i in range(size*size):
			st.add(self.cells[x][i])
			st.add(self.cells[i][y])
		# block
		blockx = x//size
		blocky = y//size
		for i in range(size):
			for j in range(size):
				st.add(self.cells[blockx*size+i][blocky*size+j])
		return set([i for i in range(-1,size*size)]).difference(st)

	def get_blank(self):
		# get first blank
		for i in range(size*size):
			for j in range(size*size):
				if self.is_blank((i, j)):
					return (i,j)
		return None

	def stdin(self):
		tmp = input()
		inlist = tmp.split()
		# print(inlist)
		for i in range(len(self.cells)):
			for j in range(len(self.cells[i])):
				if inlist[size*size*i+j] != "-":
					self.cells[i][j] = int(inlist[size*size*i+j])

	def print(self):
		print("+-------------------+")
		for l in self.cells:
			print("| ", end='')
			for c in l:
				if c == -1:
					print(' ', end=' ')
				else:
					print(c, end=' ')
			print("|")
		print("+-------------------+")

def dfs(bd, nodecount):
	nodecount[0]+=1
	blank = bd.get_blank()
	if blank == None:
		# all blanks are filled, a solution found
		return True
	candidate = bd.get_candidate(blank)
	for cnd in list(candidate):
		bd.set(blank, cnd)
		if dfs(bd, nodecount):
			return True
		bd.undo()
	return False

bd = board()
bd.stdin()
bd.print()
nodecount = [0]
dfs(bd, nodecount)
bd.print()
print("node count: "+str(nodecount[0]))
