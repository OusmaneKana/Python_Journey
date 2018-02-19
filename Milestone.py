#My first milestone project
from __future__ import print_function

from IPython.display import clear_output
board = [1,2,3,4,5,6,7,8,9]
def display_board(board):
	clear_output()
	print("+---------+---------+---------+")
	print("|         |         |         |")
	print("|         |         |         |")
	print("|         |         |         |")
	print("|         |         |         |")
	print("+---------+---------+---------+")
	print("|         |         |         |")
	print("|         |         |         |")
	print("|         |         |         |")
	print("|         |         |         |")
	print("+---------+---------+---------+")
	print("|         |         |         |")
	print("|         |         |         |")
	print("|         |         |         |")
	print("|         |         |         |")
	print("+---------+---------+---------+")

def player_input():
	pass

def place_marker(board, marker, position):
	pass

def win_check(board, mark):
	pass

import random
def space_check(board, position):
	pass

def full_board_check(board):
	pass

def player_choice(board):
	pass

def replay():
	pass

print('Welcome to Tic Tac Toe!')
display_board(board)