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
    
    def moves_left(self):
        left = False
        
        if '-' in self.board:
            left = True
        
        return left
    
    def win_player(self, player):
        if player == 1:
            sign = 'X'
        elif player == 2:
            sign = 'O'
        
        win = False
        
        # Row line 
        for row in range(0, 7, 3):
            line = 0
            for col in range(row, 3 + row):
                if self.board[col] == sign:
                    line += 1
                if line == 3:
                    win = True
                    break
        
        #Col line
        if not win:
            for col in range(3):
                line = 0
                for row in range(col, 9, col + 3):
                    if self.board[row] == sign:
                        line += 1
                    if line == 3:
                        win = True
                        break
        
        #Downward diagonal
        if not win:
            line = 0
            for dgl in range(0, 9, 4):
                if self.board[dgl] == sign:
                    line += 1
                if line == 3:
                    win = True
                    break
        
        #Upward diagonal
        if not win:
            line = 0
            for dgl in range(2, 7, 4):
                if self.board[dgl] == sign:
                    line += 1
                if line == 3:
                    win = True
                    break
                
        return win
            
    def tie(self):
        tie = False
        
        if not self.win_player(1) & self.win_player(2) & self.moves_left():
            tie = True
        
        return tie
    
def play_game():
        b = Board()
        
        print('-- Tic tac toe --')
        
        player1 = input('\nEn player 1 name: ')
        player2 = input('\nEn player 2 name: ')
        
        print('\n-- Starts the game --')
        
        while not b.win_player(1) & b.win_player(2) & b.tie():    
            b.display_board()
            b.player1_turn(input('\n' + player1 + ' moves:'))
            
            
            
            
            
                
play_game()