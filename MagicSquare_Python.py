import numpy as np
import random as rd
import heapq

#Q2

#TIME AND SPACE COMPEXITY:
#TIME COMPLEXITY: A* search has a time complexity of O(b^d) where b is the branching factor (i.e., the maximum number of valid moves from any given board state) and d is the depth of the shallowest goal state. In this case, the branching factor can be up to 4 and the depth of the goal state is at most SIZE^2, so the worst-case time complexity is O(4^(SIZE^2)). 
#SPACE COMPLEXITY: The maximum depth of the search tree is SIZE^2, so the maximum space complexity is O(bSIZE^2). The maximum branching factor is 4, so the actual space complexity is much less than O(4*SIZE^2).


#CHECKS IF GIVEN BOARD IS A VALID SOL TO THE MAGIC SQUARE PROBLEM
#COMPUTS SUM OF DIAGNOLS AND ROWS AND COLUMNS

def isSolved(board):
    diagonalSum1 = 0
    diagonalSum2 = 0
    for i in range(SIZE):
        diagonalSum1 += board[i][i]
        diagonalSum2 += board[i][SIZE - i - 1]
    if diagonalSum1 != Target or diagonalSum2 != Target:
        return False

    for i in range(SIZE):
        rowSum = 0
        colSum = 0
        for j in range(SIZE):
            rowSum += board[i][j]
            colSum += board[j][i]
        if rowSum != Target or colSum != Target:
            return False

    return True

#RETURNS LIST OF ALL VALID MOVES

def getMoves(board, movableIndex):
    i, j = movableIndex
    moves = []
    if i > 0:
        moves.append((i-1, j))
    if i < SIZE-1:
        moves.append((i+1, j))
    if j > 0:
        moves.append((i, j-1))
    if j < SIZE-1:
        moves.append((i, j+1))
    return moves

#CHECKS IF BOARDS ARE EQUAL

def isEqual(board1, board2):
    for i in range(SIZE):
        for j in range(SIZE):
            if board1[i][j] != board2[i][j]:
                return False
    return True

#IF BOARD HAS BEEN VISITED BEFORE

def isVisited(board, stack):
    for i in range(len(stack)):
        if isEqual(board, stack[i]):
            return True
    return False

#USED DFS TO FIND SOLUTION

def solveMagicSquare(board, movableIndex):
    visited = []
    stack = [(board, movableIndex)]

    while stack:
        curr_board, curr_movableIndex = stack.pop()
        visited.append(curr_board.copy())

        if isSolved(curr_board):
            return curr_board

        moves = getMoves(curr_board, curr_movableIndex)
        rd.shuffle(moves)

        for move in moves:
            i, j = move
            next_board = curr_board.copy()
            next_board[i][j], next_board[curr_movableIndex[0]][curr_movableIndex[1]
                                                               ] = next_board[curr_movableIndex[0]][curr_movableIndex[1]], next_board[i][j]
            if isSolved(next_board):
                print(next_board)
                return next_board
            if not isVisited(next_board, visited):
                stack.append((next_board, move))

    return None

#USES HEURISTIC TO FIND THE SOLUTION

def rowSumsHeuristic(board):
    row_sums = [sum(row) for row in board]
    return sum(abs(Target - s) for s in row_sums)

#USES A* ALGO TO SEARCH STATE SPACE

def solveMagicSquareAstar(board, movableIndex):
    visited = []
    heap = [(rowSumsHeuristic(board), board, movableIndex)]

    while heap:
        _, curr_board, curr_movableIndex = heapq.heappop(heap)
        visited.append(curr_board.copy())

        if isSolved(curr_board):
            return curr_board

        moves = getMoves(curr_board, curr_movableIndex)
        rd.shuffle(moves)

        for move in moves:
            i, j = move
            next_board = curr_board.copy()
            next_board[i][j], next_board[curr_movableIndex[0]][curr_movableIndex[1]
                                                               ] = next_board[curr_movableIndex[0]][curr_movableIndex[1]], next_board[i][j]
            if isSolved(next_board):
                return next_board
            if not isVisited(next_board, visited):
                heapq.heappush(
                    heap, (rowSumsHeuristic(next_board), next_board, move))

    return None


SIZE = 3
Target = 15

#INPUT OF CHOICE GOES HERE

board = [
    [6, 9, 8],
    [7, 1, 3],
    [2, 5, 4]
]


#board = [
 #   [2, 5, 6],
  #  [9, 7, 1],
   # [4, 3, 8]
#]

print("Solution where sum = 15 for all diagnols and sides:")

board = np.array(board)
movableIndex = (0, 1)
solveMagicSquare(board, movableIndex)