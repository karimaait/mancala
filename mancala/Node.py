
class Game:
    def __init__(self, etat, player_side):
        
        self.state =etat
        self.player_side = player_side  #playerSide={'computer':1,
                                        #'human':-1}
                                        #-1 min 1 max

    def gameOver(self):
        if all(self.state.board[pit] == 0 for pit in self.state.player1_pits):
            for pit in self.state.player2_pits:
                self.state.board['2'] += self.state.board[pit]
                self.state.board[pit] = 0
            return True

        elif all(self.state.board[pit] == 0 for pit in self.state.player2_pits):
            for pit in self.state.player1_pits:
                self.state.board['1'] += self.state.board[pit]
                self.state.board[pit]=0
            return True
        else:        
            return False

    def findWinner(self):
        if self.state.board['1']<self.state.board['2']:
            print('Le ganiant est player 2')
            return 2,self.state.board['2']

        elif self.state.board['1']>self.state.board['2']:
            print('Le ganiant est player 1')
            return 1,self.state.board['1']
        else:
            print('Egalite')
            return 0,self.state.board['1']
            
            
    #---------------

    
    def evaluate(self):        
        if self.player_side['1'] == 1: 
            return self.state.board['1']-self.state.board['2'] 
        else:
            return self.state.board['2']-self.state.board['1'] 
               
    
    
    def evaluate2(self):        
        if self.player_side['1'] == 1:            
            return 2 * self.state.board[1] + sum(self.state.board[pit] for pit in self.state.player1_pits) - sum(self.state.board[pit] for pit in self.state.player2_pits)        
        else:            
            return 2 * self.state.board[2] + sum(self.state.board[pit] for pit in self.state.player2_pits) - sum(self.state.board[pit] for pit in self.state.player1_pits) 
        
    
    def evaluate3(self):        
        if self.player_side['1'] == 1:            
            return 2 * self.state.board[1]         
        else:            
            return 2 * self.state.board[2]