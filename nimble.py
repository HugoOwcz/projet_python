
from random import *


def newBoard(n, p):
	board = []
	for i in range(n):
		board.append(randint(0, p))
	return board


def display(board, n):
	for i in range(n):
		print(" "*(len(str(i+1))-1), board[i], sep="", end=" | ")
	print()
	for i in range(n):
		if len(str(board[i])) == 1:
			print("-"*4, end="")
		else:
			print("-"*(4+len(str(board[i]))), end="")
	print()
	for i in range(n):
		if len(str(board[i])) == 1:
			print(i+1, end=" | ")
		else:
			print(" ", i+1, sep="", end=" | ")
	print()


def possibleSquare(board, n, i):
	if type(i) != int:
		return False
	if not 2 <= i <= n:
		return False
	if board[i-1] == 0:
		return False
	return True


def selectSquare(board, n):
	case = input("Rentrer-une case : ")
	while not possibleSquare(board, n, case):
		case = input("Rentrer-une case : ")
	return case


def possibleDestination(board, n, i, j):
	if type(j) != int:
		return False
	if j > i:
		return False
	return True


def selectDestination(board, n, i):
	case = eval(input("Rentrer-une destination : "))
	while not possibleDestination(board, n, i, case):
		case = eval(input("Rentrer-une destination : "))
	return case


def move(board, n, i, j):
	board[i-1] -= 1
	board[j-1] += 1


def lose(board, n):
	for i in range(1, n):
		if board[i] != 0:
			return False
	return True


def nimble(n, p):
	board = newBoard(n, p)
	tour_de_jeu = 1
	while not lose(board, n):
		display(board, n)
		depart = selectSquare(board, n)
		arrive = selectDestination(board, n, depart)
		move(board, n, depart, arrive)
		if tour_de_jeu == 1:
			tour_de_jeu = 2
		else:
			tour_de_jeu = 1
	if tour_de_jeu == 1:
		print("Le joueur 2 a gagné.")
	else:
		print("Le joueur 1 a gagné.")
