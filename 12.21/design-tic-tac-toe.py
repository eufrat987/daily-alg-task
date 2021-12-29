# Hi, here's your problem today. This problem was recently asked by Google:

# Design a Tic-Tac-Toe game played between two players on an n x n grid. A move is guaranteed to be valid, 
# and a valid move is one placed on an empty block in the grid. 
# A player who succeeds in placing n of their marks in a horizontal, diagonal, 
# or vertical row wins the game. Once a winning condition is reached, 
# the game ends and no more moves are allowed. Below is an example game which ends in a winning condition:

# Given n = 3, assume that player 1 is "X" and player 2 is "O" 
# board = TicTacToe(3);

# board.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |

# board.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |

# board.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|

# board.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|

# board.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|

# board.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|

# board.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|

# Here's a starting point:

class TicTacToe(object):
  def __init__(self, n):
      self.n = n
      self.b = [[0 for _ in range(n)] for _ in range(n)]
      self.p = 1
      self.end = False

  def move(self, row, col, player):
      if self.end: raise Exception('end game')
      if player != self.p: raise Exception('wrong p')
      else: self.p = 3 - player
      if self.b[row][col] != 0: raise Exception('non empty field')
      self.b[row][col] = player

      for i in range(self.n):
          c = 0
          cc = 0
          for j in range(self.n):
              if self.b[i][j] == player:
                  c += 1
              if self.b[j][i] == player:
                  cc += 1
              if c==self.n or cc==self.n: self.end = True
      c = 0
      for i in range(self.n):
          if self.b[i][i] == player:
              c+=1
      if c==self.n: self.end = True


      res = ''
      for i in range(self.n):
          res += '|'
          for j in range(self.n):
              c  = ' '
              v = self.b[i][j]
              if v == 1:
                  c = 'X'
              elif v == 2:
                  c = 'O'
              res += c + '|'
          res += '\n'
      if self.end: res += 'end'
      return res

board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))