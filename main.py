# Define boardsize and initialize board
boardSize = 8
board = [[0]*boardSize for _ in range(boardSize)]

# Function to check if it is possible to place the Queen
def isSafe(row, col):

	# Initialize flag, if it is raised, it means the Queen can be placed
	flag = 1

	# Check top
	for i in range(row):
		if board[i][col]:
			flag = 0
			break

	# Check top-left to bottom-right diagonal
	if flag:
		for i in range(-min(row, col), boardSize-max(row, col)):
			if board[row+i][col+i]:
				flag = 0
				break

	# Check top-right to bottom-left diagonal
	if flag:
		for i in range(-min(row, boardSize-1-col), min(boardSize-1-row, col)):
			if board[row+i][col-i]:
				flag = 0
				break

	return flag

# Procedure to print the board
def printBoard():
	for row in board:
		print(row)

# Recursive function to solve the placement of the Queen
def solve(nQueen, row):

	# If all Queens already placed
	if nQueen == 0:
		# Return true
		return 1
	else:
		# Iterate board, searching a cell to place the Queen
		for i in range(boardSize):
			if isSafe(row, i):
				# Place the Queen
				board[row][i] = 1

				# If the Queen can be placed
				# Solve it recursively by reducing the number of the Queen
				# And go to the next row
				if solve(nQueen-1, row+1):
					return 1
				else:
					# Take back the Queen
					board[row][i] = 0

		return 0

if __name__ == "__main__":
	if solve(boardSize, 0):
		printBoard()
	else:
		print("No solution")