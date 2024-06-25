def is_in_check(board):
 def find_king(board):
   for r, row in enumerate(board):
     for c, cell in enumerate(row):
       if cell == 'K':
         return r, c
   return None

 def check_pawn(board, king_pos):
   kr, kc = king_pos
   threats = [(kr+1, kc-1), (kr+1, kc+1)]
   for tr, tc in threats:
     if 0 <= tr < len(board) and 0 <= tc < len(board[0]) and board[tr][tc] == 'P':
       return True
   return False

 def check_straight_lines(board, king_pos):
   directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
   return check_directions(board, king_pos, directions, ['R', 'Q'])

 def check_diagonals(board, king_pos):
  directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
  return check_directions(board, king_pos, directions, ['B', 'Q'])

 def check_directions(board, king_pos, directions, pieces):
   kr, kc = king_pos
   for dr, dc in directions:
     r, c = kr + dr, kc + dc
     while 0 <= r < len(board) and 0 <= c < len(board[0]):
       if board[r][c] == 'K':
         break
       if board[r][c] in pieces:
         return True
       if board[r][c] != '.':
         break
       r += dr
       c += dc
   return False

 def is_king_in_check(board):
   king_pos = find_king(board)
   if not king_pos:
     return "Error: King not found"

   if check_pawn(board, king_pos):
     return "Success"
   if check_straight_lines(board, king_pos):
     return "Success"
   if check_diagonals(board, king_pos):
     return "Success"
   return "Fail"

 
 result = is_king_in_check(board)
 print(result)
board = [
 "........",
 "........",
 "........",
 "........",
 "........",
 "........",
 "........",
 "........"
]

is_in_check(board)