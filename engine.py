from move import Move

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
    pass

  def possible_moves(self):
    pass


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


  def notation(self):
    return self.rank_file(self.start_row, self.start_col) + self.rank_file(self.end_row, self.end_col)

  def rank_file(self, r, c):
    return self.cols_to_files[c] + self.rows_to_ranks[r]
