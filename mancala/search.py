import Node
import mancala
from mancala import *
import random
from math import inf
import copy
import pygame

boardInit = {'A':4,'B':4,'C':4,'D':4,'E':4,'F':4,'1':0,
               'G':4,'H':4,'I':4,'J':4,'K':4,'L':4,'2':0
              }


depth=12

class Play:
   
    def MinMaxAlphaBetaPruning (game, MinMax, player, depth, alpha, beta):
      if game.gameOver()==True or depth == 1:
        bestValue = game.evaluate()
        bestPit = None
        return bestValue, bestPit
        
      if MinMax == 1:
        bestValue =-inf
        for pit in game.state.possibleMoves(player):
            child_game = copy.deepcopy(game)
            
            x, _ = child_game.state.doMove(pit,player)
            
            if x==0:
                value,_ = Play.MinMaxAlphaBetaPruning(child_game ,-MinMax, player,depth-1,alpha, beta)
            else:
                value,_ = Play.MinMaxAlphaBetaPruning(child_game ,MinMax, player,depth-1,alpha, beta)
                
            if value > bestValue:
                bestValue = value
                bestPit =pit
            alpha = max(alpha, bestValue)
            if beta <= alpha:
                break
                
        return bestValue,bestPit
        
      else:
        bestValue =inf
        for pit in game.state.possibleMoves(player):
            child_game =copy.deepcopy(game) 
     
            x, _ = child_game.state.doMove(pit,player)
       
            if x==0:
                value,_ = Play.MinMaxAlphaBetaPruning(child_game ,-MinMax, player,depth-1,alpha, beta)
            else:
                value,_ = Play.MinMaxAlphaBetaPruning(child_game ,MinMax, player,depth-1,alpha, beta)
            if value < bestValue:
                bestValue = value
                bestPit =pit
            beta = min(beta, bestValue)
            if beta <= alpha:
                break
        return bestValue,bestPit




    @staticmethod
    def humanTurn(game):
        print('human')

        if  not game.gameOver():
            if game.player_side['1']==-1:
                player=1
            else:
                player=2
             

            print("Your possible moves are: ", game.state.possibleMoves(player))            
            pit = input("Which pit would you like to select? ")            
            while pit not in game.state.possibleMoves(player):                
                pit = input("Invalid move. Please select a valid pit: ")                

            
            next_player, BD = game.state.doMove(pit,player)
            game.state.display_mancala(BD)

            if next_player!=0:
                Play.humanTurn(game)
            else:
                Play.computerTurn(game)

        else:
            print("End of Game ")
            score=game.findWinner()
            print(f"Le score est de {score}")

        
    
    @staticmethod
    def computerTurn(game):
        global depth
        global boardInit
        
        print("\ncomputer\n")
        
        if  not game.gameOver() :
            if game.player_side['1'] == 1:
                player=1
            else:
                player=2
            
            if game.state.board == boardInit:
                if game.player_side['1']==1:

                    _, BD = game.state.doMove('C',1) #1er meilleur mouvement
                    game.state.display_mancala(BD)
                    next_player, BD =game.state.doMove('F',1) #2eme meilleur mouvement
                    game.state.display_mancala(BD)

                else:                   
                    
                    _, BD = game.state.doMove('I',2)  #1er meilleur mouvement
                    game.state.display_mancala(BD)
                    
                    depth = depth-1
  
                    next_player, BD =game.state.doMove('G',2)  #2eme meilleur mouvement
                    game.state.display_mancala(BD)

    
            else:                  
                _,best_pit = Play.MinMaxAlphaBetaPruning(game ,1, player ,depth-1, -inf, inf)              
                next_player, BD =game.state.doMove(str(best_pit),player)
                game.state.display_mancala(BD)


            if next_player != 0:  
                Play.computerTurn(game)
            else:        
                Play.humanTurn(game)
        
        else:
            print("End of Game ")
            score=game.findWinner()
            print(f"Le score est de {score}")

            


import pygame_menu
from pygame_menu import themes


choice_Player = 1     #le choix par defaut dans le menu = Player1
choice_Start = 1      #le choix par defaut dans le menu = OUI

pygame.init()
surface = pygame.display.set_mode((745, 430))
menu = pygame_menu.Menu('Welcome', 745, 430, theme=pygame_menu.themes.THEME_GREEN)


def set_Player(value, choice) :   
    global choice_Player
    
    if (choice == 1): choice_Player = 1
    else: choice_Player = 2

def set_Start(value, choice):
    global choice_Start
    choice_Start = choice
    
    

def start_the_game():
    global choice_Player
    global choice_Start
    global boardInit
    global menu
    
    menu.disable()
    menu.full_reset()
    pygame.display.update()
     
    player = choice_Player 
    start = choice_Start

    while True:
        
        if player==1:
            player_side = {'1':-1, '2':1}
            
        if player==2:
            player_side = {'1':1, '2':-1}
           

        etatInit=mancala.MancalaBoard()
        game=Node.Game(etatInit,player_side)
       
        etatInit.display_mancala(boardInit)

        if start == 1:
            Play.humanTurn(game)
            break
        else:
            Play.computerTurn(game)
            break

    
        #retour vers le menu :                
        menu.enable()
        menu.update(events)
        pygame.display.update()
        
        
        
    
#--------- Menue to choose --------#
        
menu.add.selector('Do you want to start the game ? :', [('Yes', 1), ('No', 2)], onchange=set_Start)
menu.add.selector('Player :', [('1', 1), ('2', 2)], onchange=set_Player)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
 
    if not (menu.is_enabled()):
        self.menu.enable()
        
    menu.update(events)
    menu.draw(surface)
        
    # Flip surface
    pygame.display.flip()
    pygame.display.update()
    
    
