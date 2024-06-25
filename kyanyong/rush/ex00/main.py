#!usr/bin/env python3

import checkmate

def main():
# Chessboard instance
    board = [
    ['-', '-', '-', '-', 'k', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', 'R', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-', '-']
]             


    result = checkmate.checkBoard(board)
    if result:
        print("king's in danger")
    else:
        print("king's safe") 

if __name__ == "__main__":
    main()



