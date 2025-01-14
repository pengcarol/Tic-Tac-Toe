class tictactoe:

  def __init__(self):
    self.board = {'1' : ' ', '2' : ' ', '3' : ' ', '4' : ' ', 
                  '5' : ' ', '6' : ' ', '7' : ' ', '8' : ' ', '9' : ' '}
    self.current = 'X'
    self.count = 0

  # switchTurn(self) keeps track of who's turn it is  
  def switchTurn(self):
    if self.current == 'X':
      self.current = 'O'
    else:
      self.current = 'X'
  
  # printBoard(self) prints the game board
  def printBoard(self):
    print(self.board['1'] + '|' + self.board['2'] +'|' + self.board['3'])
    print('-+-+-')
    print(self.board['4'] + '|' + self.board['5'] +'|' + self.board['6'])
    print('-+-+-')
    print(self.board['7'] + '|' + self.board['8'] +'|' + self.board['9'])
  
  # won(self) checks if someone has won 
  def won(self):
    if self.count < 5:
      return 

    if self.board['1'] == self.board['2'] == self.board['3'] != ' ':
      return True
    elif self.board['4'] == self.board['5'] == self.board['6'] != ' ':
      return True
    elif self.board['7'] == self.board['8'] == self.board['9'] != ' ':
      return True
    elif self.board['1'] == self.board['4'] == self.board['7'] != ' ':
      return True
    elif self.board['2'] == self.board['5'] == self.board['8'] != ' ':
      return True
    elif self.board['3'] == self.board['6'] == self.board['9'] != ' ':
      return True
    elif self.board['1'] == self.board['5'] == self.board['9'] != ' ':
      return True
    elif self.board['3'] == self.board['5'] == self.board['7'] != ' ':
      return True
    else:
      return False
  
  # playGame(self) runs the game 
  def playGame(self):

    while self.count < 9:
      self.printBoard()
      print(f"Player {self.current}'s turn:")
      position = input("Select your position: ")

      # Making sure the position is valid 
      if position not in self.board:
        print('Invalid input. Please try again.') 
        continue
      elif self.board[position] != ' ':
        print('Invalid input. Please try again.') 
        continue

      # Updating the board 
      self.board[position] = self.current
      self.count += 1 

      # Checking to see if someone has won
      if self.won():
        self.printBoard()
        print(f"Player {self.current} has won!")
        return
      else:
        self.switchTurn()
    
    # Let players know game is over
    self.printBoard()
    print("Draw.")
      
if __name__ == "__main__":
    game = tictactoe()
    game.playGame()    

