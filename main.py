import Visuallize
import pygame
import random
import sys
from Utils import createState, print_boards, generateNewState
from Board import Board
from Button import Button
from level1 import DFS, UCS, IDS, BFS, GBFS, Asearch,DLS
from level3 import A_star_search,gbfs
from level2 import Asearch2,UCS_2
from level4 import A_star_search_lv4
if __name__ == "__main__":
    Visuallize.menu()






    # matrix,time,fuel = Visuallize.read_file("input_level4_3.txt")
    # board = Board(matrix, time, fuel)
    # initialize_board = board.copy() # Pass to visualize to draw 
    # #Call search function here

    # #Visualize map 
    # #print(limit)
    # vehicles = 4
    # Boards = createState(board, vehicles) 
    # # coordinate = (1,3)
    # # new_board = generateNewState(Boards[1], 1,  coordinate)
    # # new_board.print_board()
    # # print_boards(Boards)
    # A_star_search_lv4(Boards)
    # Visuallize.start_lv4_clone(Boards, initialize_board)

