class Board:
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    
    def __init__(self):
        pass
        
    def display_board(self):
        print(self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('---------')
        print(self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('---------')
        print(self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
        
    def player1_turn(self, position):
        position = self.style_position(position)
        
        if self.valid_move(position):
            self.board[position-1] = 'X'
        
    def player2_turn(self, position):
        position = self.style_position(position)
        
        if self.valid_move(position):
            self.board[position-1] = 'O'
    
    @staticmethod
    def style_position(position):
        if position in [1, 2, 3]:
            position += 6
        
        if position in [7, 8, 9]:
            position -= 6
            
        return position
    
    @staticmethod
    def valid_move(position):
        valid = True
        
        position = Board.style_position(position) - 1
        
        if Board.board[position] in ['X', 'O']:
            valid = False
            print('Not valid move')
        
        return valid
    
def play_game():
        b = Board()
        
        b.display_board()
        b.player1_turn(7)
        b.display_board()
        b.player2_turn(5)
        b.display_board()
        b.player1_turn(5)
        b.display_board()
        
play_game()