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
        
        self.board[position] = 'X'
        
    def player2_turn(self, position):
        position = self.style_position(position)
        
        self.board[position] = 'O'
    
    @staticmethod
    def style_position(position):
        if position in [1, 2, 3]:
            position += 6
        elif position in [7, 8, 9]:
            position -= 6
            
        return position - 1
   
    #* Changed to normal method from static but generate problems with position
    def valid_move(self, position):
        valid = True
        
        position = self.style_position(position)
        
        if self.board[position] in ['X', 'O']:
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
        
        if (self.win_player(1) == False & self.win_player(2) == False) & self.moves_left() == False:
            tie = True
        
        return tie

def play_game():
        b = Board()
        
        print('\n-- Tic tac toe --')
        
        player1 = input('\nEnter player 1 name: ')
        player2 = input('\nEnter player 2 name: ')
        
        print('\n-- Starts the game --\n')
        b.display_board()
        
        while not (b.win_player(1) | b.win_player(2) | b.tie()):    
            position1 = int(input('\n' + player1 + ' moves: '))
            
            while not b.valid_move(position1):
                position1 = int(input('\n' + player1 + ' moves: '))
                
            b.player1_turn(position1)
            print()
            b.display_board()
            
            if b.win_player(1):
                print('\nEnd of the game: ' + player1 + ' won!')
            elif b.tie():
                print('\nEnd of the game: tie!')
            else:
                position2 = int(input('\n' + player2 + ' moves: '))
                
                while not b.valid_move(position2):
                    position2 = int(input('\n' + player2 + ' moves: '))
                
                b.player2_turn(position2)    
                print()
                b.display_board()
                
                if b.win_player(2):
                    print('\nEnd of the game: ' + player2 + ' won!')
                elif b.tie():
                    print('\nEnd of the game: tie!')

play_game()