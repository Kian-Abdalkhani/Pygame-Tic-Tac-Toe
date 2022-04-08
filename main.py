'''
What this Tic-Tac-Toe game entails:
    -X goes first always
    -closes game after every finished round
'''

import pygame

pygame.init()
pygame.font.init()

pygame.display.set_caption("Tic-Tac-Toe")

pygame.mouse.set_visible(True)

FPS = 60
clock = pygame.time.Clock()

WIDTH,HEIGHT = 500,600
BORDER_THICKNESS = 10

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

#delcare the fonts of the characters
GAME_FONT = pygame.font.SysFont("comicsans",100)
#font of word box
WORD_FONT = pygame.font.SysFont("comicsans",30)

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

def display_window(squares,marks,turn,game_going,tie_game):
    WIN.fill(WHITE)
    starting_pos = WIDTH // 3
    for l in range(2):  #draws the board
        vert = pygame.Rect((starting_pos - BORDER_THICKNESS//2,0),(BORDER_THICKNESS,HEIGHT))
        hrzn = pygame.Rect((0,starting_pos - BORDER_THICKNESS//2),(WIDTH,BORDER_THICKNESS))
        starting_pos = starting_pos * 2 + BORDER_THICKNESS//2
        pygame.draw.rect(WIN,BLACK,vert)
        pygame.draw.rect(WIN,BLACK,hrzn)
    #draws black background for text box
    more_border = pygame.Rect((0,WIDTH),(WIDTH,HEIGHT - WIDTH))
    pygame.draw.rect(WIN,BLACK,more_border)
    #draws actual text box
    text_box = pygame.Rect((0+BORDER_THICKNESS,WIDTH+BORDER_THICKNESS),(WIDTH-BORDER_THICKNESS*2,HEIGHT - WIDTH))
    pygame.draw.rect(WIN,WHITE,text_box)
    #display game squares
    for s in squares:
        pygame.draw.rect(WIN,WHITE,s)
    #prints the marks of x's and o's
    xplayer = GAME_FONT.render("X",1,BLACK)
    oplayer = GAME_FONT.render("O",1,BLACK)
    for index,mark in enumerate(marks):
        if mark == 'X':
            WIN.blit(xplayer,(squares[index].x + 35,squares[index].y + 5))
        elif mark == 'O':
            WIN.blit(oplayer,(squares[index].x + 35,squares[index].y + 5))
        else:
            pass
    words_position_x = BORDER_THICKNESS * 2
    words_position_y = WIDTH + BORDER_THICKNESS * 2
    if game_going == True:
        if turn % 2 == 1:   #x's turn
            xplayer_turn = WORD_FONT.render("X's Turn",1,BLACK)
            WIN.blit(xplayer_turn,(words_position_x,words_position_y))
        elif turn % 2 == 0: #o's turn
            oplayer_turn = WORD_FONT.render("O's Turn",1,BLACK)
            WIN.blit(oplayer_turn,(words_position_x,words_position_y))

    elif game_going == False:
        if turn % 2 == 0 and tie_game == False:   #x's win
            x_wins = WORD_FONT.render("X WINS",1,GREEN)
            WIN.blit(x_wins,(words_position_x,words_position_y))
        elif turn % 2 == 1 and tie_game == False: #o's turn
            o_wins = WORD_FONT.render("O WINS",1,GREEN)
            WIN.blit(o_wins,(words_position_x,words_position_y))
        else:
            tie_game = WORD_FONT.render("TIE",1,RED)
            WIN.blit(tie_game,(words_position_x,words_position_y))


    pygame.display.update()

def word_box(turn,game_going): #states whos turn it is
    words_position_x = BORDER_THICKNESS * 2
    words_position_y = WIDTH + BORDER_THICKNESS * 2
    if game_going == True:
        if turn % 2 == 1:   #x's turn
            xplayer_turn = WORD_FONT.render("X's Turn",1,BLACK)
            WIN.blit(xplayer_turn,(words_position_x,words_position_y))
        elif turn % 2 == 0: #o's turn
            oplayer_turn = WORD_FONT.render("O's Turn",1,BLACK)
            WIN.blit(oplayer_turn,(words_position_x,words_position_y))

    elif game_going == False:
        if turn % 2 == 0:   #x's win
            x_wins = WORD_FONT.render("X WINS",1,GREEN)
            WIN.blit(x_wins,(words_position_x,words_position_y))
        elif turn % 2 == 1: #o's turn
            o_wins = WORD_FONT.render("O WINS",1,GREEN)
            WIN.blit(o_wins,(words_position_x,words_position_y))
        else:
            tie = WORD_FONT.render("TIE",1,RED)
            WIN.blit(tie,(words_position_x,words_position_y))

    pygame.display.update()

def check_win(marks,game_going):
    if(marks[:3] == ['X','X','X'] or marks[3:6] == ['X','X','X'] or marks[6:] == ['X','X','X'] or
     marks[::3] == ['X','X','X'] or marks[1::3] == ['X','X','X'] or marks[2::3] == ['X','X','X'] or
     marks[0::4] == ['X','X','X'] or marks[2:7:2] == ['X','X','X']):    #X's Win
        return False,False
    elif(marks[:3] == ['O','O','O'] or marks[3:6] == ['O','O','O'] or marks[6:] == ['O','O','O'] or
     marks[::3] == ['O','O','O'] or marks[1::3] == ['O','O','O'] or marks[2::3] == ['O','O','O'] or
     marks[0::4] == ['O','O','O'] or marks[2:7:2] == ['O','O','O']):    #O's Win
        return False,False
    elif('' not in marks):  #TIE
        return False,True
    else:
        return True,False
    
    

def main():
    turn = 1
    x, y = 0,0
    squares = []
    for c in range(3):
        for r in range(3):
            squares.append(pygame.Rect((x,y),(WIDTH//3-BORDER_THICKNESS//2,WIDTH//3-BORDER_THICKNESS//2)))
            x += WIDTH//3 - BORDER_THICKNESS//2 + BORDER_THICKNESS
        x = 0
        y += WIDTH//3 - BORDER_THICKNESS//2 + BORDER_THICKNESS
    
    marks = ['','','','','','','','','']
            
        
    
    game_going = True
    while game_going:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_going = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   #checks the left button
                    for s in squares:
                        if s.collidepoint(pygame.mouse.get_pos()):
                            if turn % 2 == 1 and marks[squares.index(s)] == '':
                                marks[squares.index(s)] = 'X'
                                turn += 1
                            elif turn % 2 == 0 and marks[squares.index(s)] == '':
                                marks[squares.index(s)] = 'O'
                                turn += 1
                            else:
                                pass

        mouse_presses = pygame.mouse.get_pressed()
        game_going,tie_game = check_win(marks,game_going)
        display_window(squares,marks,turn,game_going,tie_game)
    
    pygame.time.delay(3000)


if __name__ == '__main__':
    main()