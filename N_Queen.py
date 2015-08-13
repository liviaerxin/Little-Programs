########################################################################################
def InitialBoard(n):
	board=[]
	row = []
	for i in range(0,n):
		row.append(0)
	for i in range(0,n):
		board.append(row)
	return board

def ShowBoard(constrants):
	n = len(constrants)
	for i in range(n):
		row = constrants[i][0]
		col = constrants[i][1]
		board = [0] * n
		board[col] = 1
		print board

board = InitialBoard(4)


results=[]
constrants = []  # constrants is set of point(row,col) is chose


# return available cols in the chosen row
def GetColumn(constrants, row_i, n): # n = 4, 8 
	default_list=[]
	for i in range(n):
		default_list.append(i)
	default_set = set(default_list)

	constrants_list = []
	for i in range(len(constrants)):
		constrants_list.append(constrants[i][1])
		constrants_list.append(constrants[i][1] + constrants[i][0] - row_i)
		constrants_list.append(constrants[i][1] - constrants[i][0] + row_i)
	constrants_set = set(constrants_list)

	r = default_set - constrants_set
	if (len(r) == 0):
		return None
	else:
		return r

import sys
sys.setrecursionlimit(2500)

count = 0

def PlaceQueen(board, row_i, n): # n = 4, 8
	# successful find the queen board
	if (row_i == n):
		ShowBoard(constrants)
		print "constrants:", constrants
		global count
		count = count +1
		constrants.pop()
		return 1

	usable_col = GetColumn(constrants, row_i, n)
	#print "usable_col:%s" % usable_col
	if usable_col:
		for i in usable_col:
			#print "chosen row col:(%s,%s)" % (row_i,i)
			#print "add", row_i
			new_constrant = []
			new_constrant.append(row_i)
			new_constrant.append(i)
			constrants.append(new_constrant)
			#print "constrants:", constrants
			PlaceQueen(board, row_i + 1, n)
		#print "remove", row_i
		if constrants:
			constrants.pop()
		#print "constrants:", constrants
		
	else:
		#print "remove", row_i - 1
		constrants.pop()
		#print "constrants:", constrants
		return False

PlaceQueen(board,0,10)
print count