
def checkBoard(board):
    # Find the position of the black king
    for i in range(8):
        for j in range(8):
            # Check for all pieces which can attack the white King
            if board[i][j] == 'k':
                # Check for Pawn uppercase = black 
                if lookForp(board, 'P', i, j):
                    return True
                # Check for Rook
                if lookForr(board, 'R', i, j):
                    return True
                # Check for Bishop
                if lookForb(board, 'B', i, j):
                    return True
                # Check for Queen
                if lookForq(board, 'Q', i, j):
                    return True
            
    return False

# Function to check if Queen can attack the King
def lookForq(board, c, i, j):
    # Queen's moves are a combination of both the Bishop and the Rook
    if lookForb(board, c, i, j) or lookForr(board, c, i, j):
        return True
    return False

# Function to check if bishop can attack the king
def lookForb(board, c, i, j):
    # Check the lower right diagonal
    k = 1
    while inBounds(i + k, j + k):
        if board[i + k][j + k] == c:
            return True
        if board[i + k][j + k] != '-':
            break
        k += 1

    # Check the lower left diagonal
    k = 1
    while inBounds(i + k, j - k):
        if board[i + k][j - k] == c:
            return True
        if board[i + k][j - k] != '-':
            break
        k += 1

    # Check the upper right diagonal
    k = 1
    while inBounds(i - k, j + k):
        if board[i - k][j + k] == c:
            return True
        if board[i - k][j + k] != '-':
            break
        k += 1

    # Check the upper left diagonal
    k = 1
    while inBounds(i - k, j - k):
        if board[i - k][j - k] == c:
            return True
        if board[i - k][j - k] != '-':
            break
        k += 1

    return False

# Check if rook can attack the king
def lookForr(board, c, i, j):
    # Check downwards
    k = 1
    while inBounds(i + k, j):
        if board[i + k][j] == c:
            return True
        if board[i + k][j] != '-':
            break
        k += 1

    # Check upwards
    k = 1
    while inBounds(i - k, j):
        if board[i - k][j] == c:
            return True
        if board[i - k][j] != '-':
            break
        k += 1

    # Check right
    k = 1
    while inBounds(i, j + k):
        if board[i][j + k] == c:
            return True
        if board[i][j + k] != '-':
            break
        k += 1

    # Check left
    k = 1
    while inBounds(i, j - k):
        if board[i][j - k] == c:
            return True
        if board[i][j - k] != '-':
            break
        k += 1

    return False

# Function to check if pawn can attack the king
def lookForp(board, c, i, j):
    # Check for white pawn
    if inBounds(i + 1, j - 1) and board[i + 1][j - 1] == c:
        return True
    if inBounds(i + 1, j + 1) and board[i + 1][j + 1] == c:
        return True
    return False


# Check if the indices are within the matrix or not
def inBounds(i, j):
    # Checking boundary conditions
    return i >= 0 and i < 8 and j >= 0 and j < 8







