
class state():
  def __init__(self):
    self.board = [
      ['bR', 'bH', 'bB', 'bQ', 'bK', 'bB', 'bH', 'bR'],
      ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
      ['--', '--', '--', '--', '--', '--', '--', '--'],
      ['--', '--', '--', '--', '--', '--', '--', '--'],
      ['--', '--', '--', '--', '--', '--', '--', '--'],
      ['--', '--', '--', '--', '--', '--', '--', '--'],
      ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
      ['wR', 'wH', 'wB', 'wQ', 'wK', 'wB', 'wH', 'wR']
    ]
    self.whiteMove = True
    self.movelog = []
    self.move_functions = {'P': self.pawn_moves,
                           'R': self.rook_moves,
                           'Q': self.queen_moves,
                           'H': self.knight_moves,
                           'K': self.king_moves,
                           'B': self.bishop_moves,
                           }

  def make_move(self, move):
    self.board[move.start_row][move.start_col] = '--'
    self.board[move.end_row][move.end_col] = move.piece_moved
    self.movelog.append(move)
    self.whiteMove = not self.whiteMove #simple turn switching


  def undo(self):
    if len(self.movelog) != 0:
      move = self.movelog.pop()
      self.board[move.start_row][move.start_col] = move.piece_moved
      self.board[move.end_row][move.end_col] = move.piece_captured
      self.whiteMove = not self.whiteMove 

  def valid_moves(self):
    return self.possible_moves()

#Produces all possible moves for a given piece
  def possible_moves(self):
    moves = []
    for r in range(len(self.board)):
      for c in range(len(self.board[r])):
        chance = self.board[r][c][0] #for info regarding who's turn
        if (chance == 'w' and self.whiteMove) or (chance == 'b'and not self.whiteMove):
          piece = self.board[r][c][1] #info regarding what piece is selected
          self.move_functions[piece](r, c, moves)
    return moves

#MOVE FUNCTIONS FOR ALL REPSECTIVE PIECES
  def pawn_moves(self, r, c, moves):
    if self.whiteMove:
      if self.board[r-1][c] == '--':
        moves.append(Move((r,c),(r-1, c), self.board))
        if r == 6 and self.board[r-2][c] == '--':
          moves.append(Move((r,c),(r-2, c), self.board))
      
      if c - 1 >= 0:
        if self.board[r-1][c-1][0] == 'b':
          moves.append(Move((r, c), (r-1, c-1), self.board))
      if c + 1 <= 7:
        if self.board[r-1][c+1][0] == 'b':
          moves.append(Move((r, c), (r-1, c+1), self.board))

    if not self.whiteMove:
      if self.board[r+1][c] == '--':
        moves.append(Move((r,c),(r+1, c), self.board))
        if r == 1 and self.board[r+2][c] == '--':
          moves.append(Move((r,c),(r+2, c), self.board))
      
      if c - 1 >= 0:
        if self.board[r+1][c-1][0] == 'w':
          moves.append(Move((r, c), (r+1, c-1), self.board))
      if c + 1 <= 7:
        if self.board[r+1][c+1][0] == 'w':
          moves.append(Move((r, c), (r+1, c+1), self.board))


  def rook_moves(self, r, c, moves):
    directions = ((1,0), (0,1),
                  (-1,0), (0,-1))
    rival = 'b' if self.whiteMove else 'w'
    for d in directions:
      for i in range(1,8):
        end_row = r + d[0]*i
        end_col = c + d[1]*i
        if 0 <= end_row < 8 and 0 <= end_col < 8:
          end_piece = self.board[end_row][end_col]
          if end_piece == '--':
            moves.append(Move((r,c), (end_row,end_col), self.board))
          elif end_piece[0] == rival:
            moves.append(Move((r,c), (end_row,end_col), self.board))
            break
          else:
            break

        else:
          break


  def king_moves(self, r, c, moves):
    directions = ((2, 1), (1, 2)
                  (-2, 1), (2, -1)
                  (-1, 2), (1, -2)
                  (-1,-2), (-2, -1))
    
    colour = 'w' if  self.whiteMove else 'b'
    for d in directions:
      end_row = r + d[0]
      end_col = c + d[1]
      if 0<=end_row<8 and 0<=end_col<8:
        end_piece = self.board[end_row][end_col]
        if end_piece != colour:
          moves.append(Move((r,c), (end_row,end_col), self.board))
        else:
          break

  def knight_moves(self, r, c, moves):
    pass
  def queen_moves(self, r, c, moves):
    pass
  def bishop_moves(self, r, c, moves):
    directions = ((1,1), (1,-1),
                  (-1,1), (-1,-1))
    rival = 'b' if self.whiteMove else 'w'
    for d in directions:
      for i in range(1,8):
        end_row = r + d[0]*i
        end_col = c + d[1]*i
        if 0 <= end_row < 8 and 0 <= end_col < 8:
          end_piece = self.board[end_row][end_col]
          if end_piece == '--':
            moves.append(Move((r,c), (end_row,end_col), self.board))
          elif end_piece[0] == rival:
            moves.append(Move((r,c), (end_row,end_col), self.board))
            break
          else:
            break

        else:
          break

 
  

class Move():
#labelling of rows and columns
  ranks_to_rows = {'1': 7, '2': 6, '3': 5, '4': 4,
                   '5': 3, '6': 2, '7': 1, '8': 0}
  rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}
  files_to_cols = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                   'e': 4, 'f': 5, 'g': 6, 'h': 7}
  cols_to_files = {v: k for k, v in files_to_cols.items()}
  
  def __init__(self, start, end, board):
    self.start_row, self.start_col = start[0], start[1]
    self.end_row, self.end_col = end[0], end[1]
    self.piece_moved = board[self.start_row][self.start_col]
    self.piece_captured = board[self.end_row][self.end_col]
    self.move_id = self.start_row*1000 + self.start_col*100 + self.end_row*10 + self.end_col

  def __eq__(self, other):
    if isinstance(other, Move):
      return self.move_id == other.move_id
    return False

  def notation(self):
    return self.rank_file(self.start_row, self.start_col) + self.rank_file(self.end_row, self.end_col)

  def rank_file(self, r, c):
    return self.cols_to_files[c] + self.rows_to_ranks[r]
