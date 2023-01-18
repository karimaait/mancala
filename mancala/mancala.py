
class MancalaBoard:
    def __init__(self):
        #initialisation du plateau de jeux
        self.board={'A':4,'B':4,'C':4,'D':4,'E':4,'F':4, '1':0,
                    'G':4,'H':4,'I':4,'J':4,'K':4,'L':4, '2':0  }


        #indique les fausses corespondante a chaque joueur
        self.player1_pits =('A','B','C','D','E','F')
        self.player2_pits =('G','H','I','J','K','L')

        #les fausse opposes pour chaque fosse
        self.oppose_pit ={'A':'G','B':'H','C':'I','D':'J', 'E':'K', 'F':'L',
                     'G':'A','H':'B','I':'C','J':'D','K':'E', 'L':'F'}
    
        #la fosse qui suie chaque fosse 
        self.next_pit ={'A':'B','B':'C','C':'D','D':'E', 'E':'F', 'F':'1',
                     '1':'L','L':'K','K':'J','J':'I','I':'H','H':'G', 
                     'G':'2','2':'A'}
  

    # fonction qui retourne les couper possible pour chaque player
    def possibleMoves(self, player):
        if (player==1):
            return [pit for pit in self.player1_pits if self.board[pit]>0]
        else:
            return [pit for pit in self.player2_pits if self.board[pit]>0]
        


    #unr fonction qui execute le movement et retourne le prochain joueur
    def doMove(self, pit,player):

        #recolter les graines qui se trouve dans la fosse      
        seeds=self.board[pit]

        #reinitialise la fosse a zero
        self.board[pit] = 0

        current_pit = pit

        while (seeds>0):
            current_pit = self.next_pit[current_pit]
            if player==1 :
                if current_pit !="2":
                    self.board[current_pit]+=1
                    seeds -= 1
                else:
                    current_pit = self.next_pit[current_pit]
                    self.board[current_pit]+=1
                    seeds -= 1
            
            else :
                if current_pit !="1":
                    self.board[current_pit]+=1
                    seeds -= 1
                else:
                    current_pit = self.next_pit[current_pit]
                    self.board[current_pit]+=1
                    seeds -= 1
        
      
        if player == 1 :
            if current_pit == '1':
                return 1, self.board
            
            if ((current_pit in self.player1_pits) and (self.board[current_pit])==1):
            
                opp_pit=self.oppose_pit[current_pit]
                oppSeeds = self.board[opp_pit]

                #mettre a jour les  deux fosses a zeros 
                self.board[opp_pit]=0
                self.board[current_pit]=0

                #mettre a jour le store du player1 en ajoutant les graines recolter
                self.board['1']+=oppSeeds+1

            return 0, self.board
        else:
            if current_pit == '2':
                return 2, self.board
            
            if ((current_pit in self.player2_pits) and (self.board[current_pit]))==1:
            
                opp_pit=self.oppose_pit[current_pit]
                oppSeeds = self.board[opp_pit]

                #mettre a jour les  deux fosses a zeros 
                self.board[opp_pit]=0
                self.board[current_pit]=0

                #mettre a jour le store du player2 en ajoutant les graines recolter
                self.board['2']+=oppSeeds+1

            return 0, self.board
        


        #fonction pour affiche le jeu
    def display_mancala(self, BD):

        print("\n+----+----+----+----+----+----+----+----+----+") 
        print("   G       H       I       J       K       L\n") 
        
        for pit in self.player2_pits:            
            print('  ', BD[pit], '   ', end = '')        
        print('  ')        
        print(BD['2'],'                                           ',self.board['1'])     
            
        for pit in self.player1_pits:            
            print('  ', BD[pit], '   ', end = '')                                                  
        print('  ')    
        
        print("\n   A        B       C       D       E       F")
        print("+----+----+----+----+----+----+----+----+----+\n") 
       





