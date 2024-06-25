import numpy
def checkmate(board):
    # check square
    K_chk = -1 #No king
    bb = numpy.array(board)
    row_board,col_board = bb.shape

    if row_board == col_board:
        sqr_chk = 1
    else:
        sqr_chk = -1
        print("This board is not a square board.")

    cnt_K = 0
    if sqr_chk == 1:
        # check King
        for i in range(0,col_board):
            for j in range(0,row_board):
                if board[j][i]=="K":
                    K_row = j
                    K_col = i
                    cnt_K = cnt_K + 1 # count King
                    K_chk = 1 # king
        if cnt_K > 1 or cnt_K == 0:
            print("Error")

    if K_chk == 1 and sqr_chk == 1 and cnt_K == 1:
        row_set_p = []
        col_set_p = []
        row_set_b = []
        col_set_b = []
        row_set_r = []
        col_set_r = []
        row_set_q = []
        col_set_q = []
        for i in range(0,col_board):
            for j in range(0,row_board):
                if i==0 and j==0:
                    b_chk = -1
                    p_chk = -1
                    r_chk = -1
                    q_chk = -1
                # find P
                if board[j][i]=="P":
                    P_row = j
                    P_col = i
                    # find  path P
                    p_chk = 1
                    if P_row != 0 and P_col != 0 and P_col != col_board:
                        row_set_p.append(P_row - 1)
                        row_set_p.append(P_row - 1)
                        col_set_p.append(P_col-1)
                        col_set_p.append(P_col+1)
                    elif P_col == 0 and P_row != 0:
                        row_set_p.append(P_row - 1)
                        col_set_p.append(P_col + 1)
                    elif P_col == col_board and P_row != 0:
                        row_set_p.append(P_row - 1)
                        col_set_p.append(P_col - 1)
                    # check in
                    P_SF = "Fail"
                    if p_chk != -1:
                        len_inx_p = len(row_set_p)
                        for i1 in range(0,len_inx_p):
                            if K_row == row_set_p[i1] and K_col == col_set_p[i1]:
                                P_SF = "Success"
                # find B
                if board[j][i]=="B":
                    B_row = j
                    B_col = i
                    # find  path B

                    if B_row != 0 and B_row != row_board-1 and B_col != 0 and B_col != col_board-1:
                        # top-Left
                        a = len(range(0,B_row))
                        b = len(range(0,B_col))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(B_row - c,B_row):
                            row_set_b.append(i1)
                        for i1 in range(B_col - c,B_col):
                            col_set_b.append(i1)
                        # top-right
                        a = len(range(B_row-1,-1,-1))
                        b = len(range(B_col+1,col_board))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(B_row-1,B_row-c-1,-1):
                            row_set_b.append(i1)
                        for i1 in range(B_col+1,B_col + c + 1):
                            col_set_b.append(i1)
                        # down-Left
                        a = len(range(B_row+1,row_board))
                        b = len(range(B_col-1,-1,-1))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(B_row+1,B_row + c + 1):
                            row_set_b.append(i1)
                        for i1 in range(B_col-1,B_col-c-1,-1):
                            col_set_b.append(i1)
                        # down-right
                        a = len(range(B_row+1,row_board))
                        b = len(range(B_col+1,col_board))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(B_row+1,B_row + c + 1):
                            row_set_b.append(i1)
                        for i1 in range(B_col+1,B_col + c + 1):
                            col_set_b.append(i1)
                        b_chk = 1
                    if B_row == 0:
                        if B_col == 0:
                            # down-right
                            a = len(range(B_row+1,row_board))
                            b = len(range(B_col+1,col_board))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(B_row+1,B_row + c + 1):
                                row_set_b.append(i1)
                            for i1 in range(B_col+1,B_col + c + 1):
                                col_set_b.append(i1)
                        if B_col == col_board-1:
                            # down-Left
                            a = len(range(B_row+1,row_board))
                            b = len(range(B_col-1,-1,-1))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(B_row+1,B_row + c + 1):
                                row_set_b.append(i1)
                            for i1 in range(B_col-1,B_col-c-1,-1):
                                col_set_b.append(i1)
                        if B_col != 0 and B_col != col_board-1:
                            # down-right
                            a = len(range(B_row+1,row_board))
                            b = len(range(B_col+1,col_board))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(B_row+1,B_row + c + 1):
                                row_set_b.append(i1)
                            for i1 in range(B_col+1,B_col + c + 1):
                                col_set_b.append(i1)
                            # down-Left
                            a = len(range(B_row+1,row_board))
                            b = len(range(B_col-1,-1,-1))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(B_row+1,B_row + c + 1):
                                row_set_b.append(i1)
                            for i1 in range(B_col-1,B_col-c-1,-1):
                                col_set_b.append(i1)
                        b_chk = 1
                    if B_row == row_board-1:
                        if B_col == 0:
                            # top-right
                            a = len(range(B_row-1,-1,-1))
                            b = len(range(B_col+1,col_board))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(B_row-1,B_row-c-1,-1):
                                row_set_b.append(i1)
                            for i1 in range(B_col+1,B_col + c + 1):
                                col_set_b.append(i1)
                        if B_col == col_board-1:
                            # top-Left
                            a = len(range(0,B_row))
                            b = len(range(0,B_col))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(B_row - c,B_row):
                                row_set_b.append(i1)
                            for i1 in range(B_col - c,B_col):
                                col_set_b.append(i1)

                        if B_col != 0 and B_col != col_board-1:
                            # top-right
                            a = len(range(B_row-1,-1,-1))
                            b = len(range(B_col+1,col_board))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(B_row-1,B_row-c-1,-1):
                                row_set_b.append(i1)
                            for i1 in range(B_col+1,B_col + c + 1):
                                col_set_b.append(i1)
                            # top-Left
                            a = len(range(0,B_row))
                            b = len(range(0,B_col))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(B_row - c,B_row):
                                row_set_b.append(i1)
                            for i1 in range(B_col - c,B_col):
                                col_set_b.append(i1)
                        b_chk = 1
                    if B_col == 0 and B_row != 0 and B_row != row_board-1:
                        # top-right
                        a = len(range(B_row-1,-1,-1))
                        b = len(range(B_col+1,col_board))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(B_row-1,B_row-c-1,-1):
                            row_set_b.append(i1)
                        for i1 in range(B_col+1,B_col+c+1):
                            col_set_b.append(i1)
                        a = len(range(B_row+1,row_board))
                        b = len(range(B_col+1,col_board))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        # down-right
                        for i1 in range(B_row+1,B_row+c+1):
                            row_set_b.append(i1)
                        for i1 in range(B_col+1,B_col+c+1):
                            col_set_b.append(i1)
                        b_chk = 1
                    if B_col == col_board-1 and B_row != 0 and B_col != row_board-1:
                        # top-Left
                        a = len(range(0,B_row))
                        b = len(range(0,B_col))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(B_row-c,B_row):
                            row_set_b.append(i1)
                        for i1 in range(B_col-c,B_col):
                            col_set_b.append(i1)
                        # down-Left
                        a = len(range(B_row+1,row_board))
                        b = len(range(B_col-1,-1,-1))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(B_row+1,B_row + c + 1):
                            row_set_b.append(i1)
                        for i1 in range(B_col-1,B_col - c -1,-1):
                            col_set_b.append(i1)
                        b_chk = 1
                    # check in
                    B_SF = "Fail"
                    if b_chk != -1:
                        len_inx_b = len(row_set_b)
                        for i1 in range(0,len_inx_b):
                            if K_row == row_set_b[i1] and K_col == col_set_b[i1]:
                                B_SF = "Success"
                # find R
                if board[j][i] == "R":
                    R_row = j
                    R_col = i

                    #find path R
                    for i1 in range(0,row_board):
                        if i1 != R_row:
                            row_set_r.append(i1)
                            col_set_r.append(R_col)
                    for i1 in range(0,col_board):
                        if i1 != R_col:
                            row_set_r.append(R_row)
                            col_set_r.append(i1)
                    r_chk = 1
                    # check in
                    R_SF = "Fail"
                    if r_chk != -1:
                        len_inx_r = len(row_set_r)
                        for i1 in range(0, len_inx_r):
                            if K_row == row_set_r[i1] and K_col == col_set_r[i1]:
                                R_SF = "Success"
                #find Q
                if board[j][i] == "Q":
                    Q_row = j
                    Q_col = i
                    #find path Q

                    for i1 in range(0,row_board):
                        if i1 != Q_row:
                            row_set_q.append(i1)
                            col_set_q.append(Q_col)
                    for i1 in range(0,col_board):
                        if i1 != Q_col:
                            row_set_q.append(Q_row)
                            col_set_q.append(i1)
                    if Q_row != 0 and Q_row != row_board - 1 and Q_col != 0 and Q_col != col_board - 1:
                        # top-Left
                        a = len(range(0, Q_row))
                        b = len(range(0, Q_col))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(Q_row - c, Q_row):
                            row_set_q.append(i1)
                        for i1 in range(Q_col - c, Q_col):
                            col_set_q.append(i1)
                        # top-right
                        a = len(range(Q_row - 1, -1, -1))
                        b = len(range(Q_col + 1, col_board))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(Q_row - 1, Q_row - c - 1, -1):
                            row_set_q.append(i1)
                        for i1 in range(Q_col + 1, Q_col + c + 1):
                            col_set_q.append(i1)
                            # down-Left
                        a = len(range(Q_row + 1, row_board))
                        b = len(range(Q_col - 1, -1, -1))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(Q_row + 1, Q_row + c + 1):
                            row_set_q.append(i1)
                        for i1 in range(Q_col - 1, Q_col - c - 1, -1):
                            col_set_q.append(i1)
                            # down-right
                        a = len(range(Q_row + 1, row_board))
                        b = len(range(Q_col + 1, col_board))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(Q_row + 1, Q_row + c + 1):
                            row_set_q.append(i1)
                        for i1 in range(Q_col + 1, Q_col + c + 1):
                            col_set_q.append(i1)
                        q_chk = 1
                    if Q_row == 0:
                        if Q_col == 0:
                            # down-right
                            a = len(range(Q_row + 1, row_board))
                            b = len(range(Q_col + 1, col_board))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(Q_row + 1, Q_row + c + 1):
                                row_set_q.append(i1)
                            for i1 in range(Q_col + 1, Q_col + c + 1):
                                col_set_q.append(i1)
                        if Q_col == col_board - 1:
                            # down-Left
                            a = len(range(Q_row + 1, row_board))
                            b = len(range(Q_col - 1, -1, -1))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(Q_row + 1, Q_row + c + 1):
                                row_set_q.append(i1)
                            for i1 in range(Q_col - 1, Q_col - c - 1, -1):
                                col_set_q.append(i1)
                        if Q_col != 0 and Q_col != col_board - 1:
                            # down-right
                            a = len(range(Q_row + 1, row_board))
                            b = len(range(Q_col + 1, col_board))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(Q_row + 1, Q_row + c + 1):
                                row_set_q.append(i1)
                            for i1 in range(Q_col + 1, Q_col + c + 1):
                                col_set_q.append(i1)
                                # down-Left
                            a = len(range(Q_row + 1, row_board))
                            b = len(range(Q_col - 1, -1, -1))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(Q_row + 1, Q_row + c + 1):
                                row_set_q.append(i1)
                            for i1 in range(Q_col - 1, Q_col - c - 1, -1):
                                col_set_q.append(i1)
                        q_chk = 1
                    if Q_row == row_board - 1:
                        if Q_col == 0:
                            # top-right
                            a = len(range(Q_row - 1, -1, -1))
                            b = len(range(Q_col + 1, col_board))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(Q_row - 1, Q_row - c - 1, -1):
                                row_set_q.append(i1)
                            for i1 in range(Q_col + 1, Q_col + c + 1):
                                col_set_q.append(i1)
                        if Q_col == col_board - 1:
                            # top-Left
                            a = len(range(0, Q_row))
                            b = len(range(0, Q_col))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(Q_row - c, Q_row):
                                row_set_q.append(i1)
                            for i1 in range(Q_col - c, Q_col):
                                col_set_q.append(i1)
                        if Q_col != 0 and Q_col != col_board - 1:
                            # top-right
                            a = len(range(Q_row - 1, -1, -1))
                            b = len(range(Q_col + 1, col_board))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(Q_row - 1, Q_row - c - 1, -1):
                                row_set_q.append(i1)
                            for i1 in range(Q_col + 1, Q_col + c + 1):
                                col_set_q.append(i1)
                            # top-Left
                            a = len(range(0, Q_row))
                            b = len(range(0, Q_col))
                            if a <= b:
                                c = a
                            else:
                                c = b
                            for i1 in range(Q_row - c, Q_row):
                                row_set_q.append(i1)
                            for i1 in range(Q_col - c, Q_col):
                                col_set_q.append(i1)
                        q_chk = 1
                    if Q_col == 0 and Q_row != 0 and Q_row != row_board - 1:
                        # top-right
                        a = len(range(Q_row - 1, -1, -1))
                        b = len(range(Q_col + 1, col_board))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(Q_row - 1, Q_row - c - 1, -1):
                            row_set_q.append(i1)
                        for i1 in range(Q_col + 1, Q_col + c + 1):
                            col_set_q.append(i1)
                        a = len(range(Q_row + 1, row_board))
                        b = len(range(Q_col + 1, col_board))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        # down-right
                        for i1 in range(Q_row + 1, Q_row + c + 1):
                            row_set_q.append(i1)
                        for i1 in range(Q_col + 1, Q_col + c + 1):
                            col_set_q.append(i1)
                        q_chk = 1
                    if Q_col == col_board - 1 and Q_row != 0 and Q_col != row_board - 1:
                        # top-Left
                        a = len(range(0, Q_row))
                        b = len(range(0, Q_col))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(Q_row - c, Q_row):
                            row_set_q.append(i1)
                        for i1 in range(Q_col - c, Q_col):
                            col_set_q.append(i1)
                        # down-Left
                        a = len(range(Q_row + 1, row_board))
                        b = len(range(Q_col - 1, -1, -1))
                        if a <= b:
                            c = a
                        else:
                            c = b
                        for i1 in range(Q_row + 1, Q_row + c + 1):
                            row_set_q.append(i1)
                        for i1 in range(Q_col - 1, Q_col - c - 1, -1):
                            col_set_q.append(i1)
                        q_chk = 1
                    # check in
                    Q_SF = "Fail"
                    if q_chk != -1:
                        len_inx_q = len(row_set_q)
                        for i1 in range(0, len_inx_q):
                            if K_row == row_set_q[i1] and K_col == col_set_q[i1]:
                                Q_SF = "Success"





        if p_chk == 1 or b_chk == 1 or r_chk == 1 or q_chk == 1:
            if p_chk == -1:
                P_SF = "Fail"
            if b_chk == -1:
                B_SF = "Fail"
            if r_chk == -1:
                R_SF = "Fail"
            if q_chk == -1:
                Q_SF = "Fail"
            if B_SF == "Success":
                if p_chk == 1:
                    if K_row < B_row and P_row > K_row and P_row < B_row and K_col > B_col and K_col > P_col and P_col > B_col:
                        B_SF = "Fail"
                    if K_row > B_row and P_row < K_row and P_row > B_row and K_col > B_col and K_col > P_col and P_col > B_col:
                        B_SF = "Fail"
                    if K_row < B_row and P_row > K_row and P_row < B_row and K_col < B_col and K_col < P_col and P_col < B_col:
                        B_SF = "Fail"
                    if K_row > B_row and P_row < K_row and P_row > B_row and K_col < B_col and K_col < P_col and P_col < B_col:
                        B_SF = "Fail"
            if B_SF == "Success":
                if r_chk == 1:
                    if K_row < B_row and R_row > K_row and R_row < B_row and K_col > B_col and K_col > R_col and R_col > B_col:
                        B_SF = "Fail"
                    if K_row > B_row and R_row < K_row and R_row > B_row and K_col > B_col and K_col > R_col and R_col > B_col:
                        B_SF = "Fail"
                    if K_row < B_row and R_row > K_row and R_row < B_row and K_col < B_col and K_col < R_col and R_col < B_col:
                        B_SF = "Fail"
                    if K_row > B_row and R_row < K_row and R_row > B_row and K_col < B_col and K_col < R_col and R_col < B_col:
                        B_SF = "Fail"
            if R_SF == "Success":
                if p_chk == 1:
                    if K_row < P_row and R_row > K_row and P_row < R_row:
                        R_SF = "Fail"
                    elif K_row > P_row and R_row < K_row and P_row > R_row:
                        R_SF = "Fail"
                    elif K_col > P_col and K_col > R_col and P_col > R_col:
                        R_SF = "Fail"
                    elif K_col < P_col and K_col < R_col and P_col < R_col:
                        R_SF = "Fail"
            if R_SF == "Success":
                if b_chk == 1:
                    if K_row < B_row and R_row > K_row and B_row < R_row:
                        R_SF = "Fail"
                    if K_row > B_row and R_row < K_row and B_row > R_row:
                        R_SF = "Fail"
                    if K_col > B_col and K_col > R_col and B_col > R_col:
                        R_SF = "Fail"
                    if K_col < B_col and K_col < R_col and B_col < R_col:
                        R_SF = "Fail"
            if Q_SF == "Success":
                if p_chk == 1:
                    if K_row < Q_row and P_row > K_row and P_row < Q_row and K_col > Q_col and K_col > P_col and P_col > Q_col:
                        Q_SF = "Fail"
                    if K_row > Q_row and P_row < K_row and P_row > Q_row and K_col > Q_col and K_col > P_col and P_col > Q_col:
                        Q_SF = "Fail"
                    if K_row < Q_row and P_row > K_row and P_row < Q_row and K_col < Q_col and K_col < P_col and P_col < Q_col:
                        Q_SF = "Fail"
                    if K_row > Q_row and P_row < K_row and P_row > Q_row and K_col < Q_col and K_col < P_col and P_col < Q_col:
                        Q_SF = "Fail"
                    if K_row < P_row and Q_row > K_row and P_row < Q_row:
                        Q_SF = "Fail"
                    if K_row > P_row and Q_row < K_row and P_row > Q_row:
                        Q_SF = "Fail"
                    if K_col > P_col and K_col > Q_col and P_col > Q_col:
                        Q_SF = "Fail"
                    if K_col < P_col and K_col < Q_col and P_col < Q_col:
                        Q_SF = "Fail"
            if Q_SF == "Success":
                if r_chk == 1:
                    if K_row < Q_row and R_row > K_row and R_row < Q_row and K_col > Q_col and K_col > R_col and R_col > Q_col:
                        Q_SF = "Fail"
                    if K_row > Q_row and R_row < K_row and R_row > Q_row and K_col > Q_col and K_col > R_col and R_col > Q_col:
                        Q_SF = "Fail"
                    if K_row < Q_row and R_row > K_row and R_row < Q_row and K_col < Q_col and K_col < R_col and R_col < Q_col:
                        Q_SF = "Fail"
                    if K_row > Q_row and R_row < K_row and R_row > Q_row and K_col < Q_col and K_col < R_col and R_col < Q_col:
                        Q_SF = "Fail"
            if Q_SF == "Success":
                if b_chk == 1:
                    if K_row < B_row and Q_row > K_row and B_row < Q_row:
                        Q_SF = "Fail"
                    if K_row > B_row and Q_row < K_row and B_row > Q_row:
                        Q_SF = "Fail"
                    if K_col > B_col and K_col > Q_col and B_col > Q_col:
                        Q_SF = "Fail"
                    if K_col < B_col and K_col < Q_col and B_col < Q_col:
                        Q_SF = "Fail"



            if P_SF == "Success" or B_SF == "Success" or R_SF == "Success" or Q_SF == "Success":
                check_in = "Success"
            else:
                check_in = "Fail"

            print(check_in )
        else:
            print("Error")













