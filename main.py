import pygame as p
import engine
WIDTH = HEIGHT = 600
DIM = 8
SQ_SIZE = WIDTH // DIM
MAX_FPS = 15
IMAGES = {}

def load_images():
  pieces = ['wP', 'wR', 'wH', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bH', 'bB', 'bQ', 'bK']
  for piece in pieces:
    IMAGES[piece] = p.transform.scale(p.image.load(f'images/{piece}.png'), (SQ_SIZE, SQ_SIZE))

def main():
  p.init()
  screen = p.display.set_mode((WIDTH, HEIGHT))
  clock  = p.time.Clock()
  screen.fill(p.Color('White'))
  gamestate = engine.state()
  load_images()
  running = True
  sq_selected = ()
  player_clicked = []
  while running:
    for event in p.event.get():
      if event.type == p.QUIT:
        running = False

      elif event.type == p.MOUSEBUTTONDOWN:
        loc = p.mouse.get_pos()
        col = loc[0] // SQ_SIZE
        row = loc[1] // SQ_SIZE
        if sq_selected == (row, col): #same square clicked twice
          sq_selected = ()
          player_clicked = []
        else:
          sq_selected = (row, col)
          player_clicked.append(sq_selected)

        if len(player_clicked) == 2:
          move = engine.Move(player_clicked[0], player_clicked[1], gamestate.board)
          print(move.notation())
          gamestate.make_move(move)
          sq_selected = ()
          player_clicked = []

      elif event.type == p.KEYDOWN:
        if event.key == p.K_u:
          
          #u key for undoing
          gamestate.undo()



    
    draw_state(screen, gamestate)
    clock.tick(MAX_FPS)
    p.display.flip()

def draw_state(screen, gamestate):
  drawBoard(screen)

  drawPieces(screen, gamestate.board)

def drawBoard(screen):
  colors = [p.Color('Light Yellow'), p.Color('Sea Green')]
  for r in range(DIM):
    for c in range(DIM):
      color = colors[((r+c) % 2)]
      p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
  for r in range(DIM):
    for c in range(DIM):
      piece = board[r][c]
      if piece != '--':
        screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
  main()