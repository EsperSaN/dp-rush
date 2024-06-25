def checkmate(board):

    type_piece_attack = {
    "P":"""\
.................
.................
.................
.................
.................
.................
.................
.......x.x.......
........P........
.................
.................
.................
.................
.................
.................
.................
.................\
""",

        "B":"""\
x...............x
.x.............x.
..x...........x..
...x.........x...
....x.......x....
.....x.....x.....
......x...x......
.......x.x.......
........B........
.......x.x.......
......x...x......
.....x.....x.....
....x.......x....
...x.........x...
..x...........x..
.x.............x.
x...............x\
""",

        "R":"""\
........x........
........x........
........x........
........x........
........x........
........x........
........x........
........x........
xxxxxxxxRxxxxxxxx
........x........
........x........
........x........
........x........
........x........
........x........
........x........
........x........\
""",

        "Q":"""\
x.......x.......x
.x......x......x.
..x.....x.....x..
...x....x....x...
....x...x...x....
.....x..x..x.....
......x.x.x......
.......xxx.......
xxxxxxxxQxxxxxxxx
.......xxx.......
......x.x.x......
.....x..x..x.....
....x...x...x....
...x....x....x...
..x.....x.....x..
.x......x......x.
x.......x.......x\
"""
    }

    board_lines = board.split()
    rows_of_board = len(board_lines)


    if rows_of_board == 0:

        return "ERROR"
    
    columns_of_board = len(board_lines[0])

    if not all(len(i) == columns_of_board for i in board_lines):

        return "ERROR"

    attack_board = [["." for _ in range(columns_of_board)] for _ in range(rows_of_board)]

    #Find King Position

    k_position = None

    for x in range(rows_of_board):

        for y in range(columns_of_board):

            if board_lines[x][y] == "K":

                k_position = (x,y)

                break
        
        if k_position:

            break
    
    if k_position is None:

        return "ERROR"

    #Mark Attack

    for x in range(rows_of_board):

        for y in range(columns_of_board):

            piece = board_lines[x][y] #หาตำแหน่งชนิดของเบี้ย

            if piece in type_piece_attack:

                attack_pattern = type_piece_attack[piece].split("\n")

                pattern_size = len(attack_pattern)

                center = pattern_size // 2

                for pos_x in range(pattern_size):

                    for pos_y in range(pattern_size):

                        if attack_pattern[pos_x][pos_y] == "x":

                            attack_x = x + (pos_x - center)

                            attack_y = y + (pos_y - center)

                            if 0 <= attack_x < rows_of_board and 0 <= attack_y < columns_of_board:

                                attack_board[attack_x][attack_y] = "x"


    if k_position:

        k_x, k_y = k_position

        if attack_board[k_x][k_y] == "x":

            return "Success"
        
        return "Fail"