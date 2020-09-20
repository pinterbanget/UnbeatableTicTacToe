#! python3

import random
import sys
import time

def printboard(B):
    #to print the playing board.
    print('')
    print(B[7] + '│' + B[8] + '│' + B[9])
    print('‒‒‒‒‒')
    print(B[4] + '│' + B[5] + '│' + B[6])
    print('‒‒‒‒‒')
    print(B[1] + '│' + B[2] + '│' + B[3])
    print('')
   
def choose():
    #to give the user a choice: crosses or naughts.
    while True:
        char = str.upper(input('Do you want to be X or O? : '))
        if char in 'XO12':
            break
        print('Please input X or O.')
        
    if char in 'X1':
        return ['X', 'O']
    else:
        return ['O', 'X']
    
def firstmove():
    #to randomize who goes first.
    if random.randint(1, 2) == 1:
        return 'The AI'
    else:
        return name

def wincond(b, c):
    #winning conditions
    return ( \
    (b[7] == c and b[8] == c and b[9] == c) or #top x-axis
    (b[4] == c and b[5] == c and b[6] == c) or #mid x-axis
    (b[1] == c and b[2] == c and b[3] == c) or #bot x-axis
    (b[7] == c and b[5] == c and b[3] == c) or #diagonal 1
    (b[9] == c and b[5] == c and b[1] == c) or #diagonal 2
    (b[7] == c and b[4] == c and b[1] == c) or #left y-axis
    (b[8] == c and b[5] == c and b[2] == c) or #mid y-axis
    (b[9] == c and b[6] == c and b[3] == c))   #right y-axis
        
def turnmove(boardd, char, move):
    #to fill the board list with the corresponding character
    boardd[move] = char

def freespace(boardd, move):
    #to check if the nth index in the board list has been filled
    return boardd[move] == ' '

def copyboardforcom(boardd):
    #duplicate board for AI calculations
    copyboard = []
    for i in boardd:
        copyboard.append(i)
        
    return copyboard

def playermove(boardd):
    #to give the player the prompt to make am move
    move = ' '   
    while True:
        try:
            move = int(input('Choose which square to go to (1-9): '))
            if move < 1 or move > 9:
              print('Please input a number (1-9).')
            elif move in '1 2 3 4 5 6 7 8 9'.split() or freespace(boardd, move):
                break
            else:
                print('The square has been filled. Please choose another square.')
        except ValueError:
            print('Please input a number (1-9).')

    return move

def randommove(boardd, movelist):
    #AI: to make a random move
    possiblemoves = []
    for i in movelist:
        if freespace(boardd, i):
            possiblemoves.append(i)
            
    if len(possiblemoves) != 0:
        return random.choice(possiblemoves)
    else:
        return None

def commove(boardd, comchar):
    #for AI
    if comchar == 'X':
        playerchar = 'O'
    else:
        playerchar = 'X'
    
    moveEdge = randommove(boardd, [2, 4, 6, 8])
    moveCorner = randommove(boardd, [1, 3, 7, 9])
    moveAll = randommove(boardd, [1, 2, 3, 4, 6, 7, 8, 9])
    
    for i in range (1, 10):
        copy = copyboardforcom(boardd)
        if freespace(copy, i):
            turnmove(copy, comchar, i)
            if wincond(copy, comchar):
                return i
            
    for i in range (1,10):
        copy = copyboardforcom(boardd)
        if freespace(copy, i):
            turnmove(copy, playerchar, i)
            if wincond(copy, playerchar):
                return i
            
    copy = copyboardforcom(boardd)
    if freespace(boardd, 5):
        return 5
    
    if board[5] == comchar:
        if setcond1a(copy, playerchar):
            return moveEdge
            
        elif freespace(boardd, 1) and freespace(boardd, 3)\
        and freespace(boardd, 7) and freespace(boardd, 9):
            return setcond2()
          
        elif 1 not in SC3:
            SC3.append(1)
            return setcond3()
        
        else:
            return moveAll
          
    elif board[5] == playerchar:
        if setcond1b(copy, playerchar):
            if freespace(boardd, 1) or freespace(boardd, 3)\
            or freespace(boardd, 7) or freespace(boardd, 9):
                return moveCorner
            else:
                return moveEdge
        
        elif freespace(boardd, 1) or freespace(boardd, 3)\
        or freespace(boardd, 7) or freespace(boardd, 9):
            return moveCorner
    
        else:
            return moveEdge
    
    else:
        return moveAll

def fullboard(boardd):
    #to check if the board is full.
    for i in range (1, 10):
        if freespace(boardd, i):
            return False
    return True

#AI set conditions
def setcondfree(boardd, move):
    if freespace(boardd, move):
        return move
    else:
        return randommove(board, [1, 3, 7, 9])
    
def setcond1a(b, c):
    return ( \
    (b[1] == c and b[9] == c) or \
    (b[7] == c and b[3] == c))

def setcond1b(b,c):
    return ( \
    (b[1] == c and b[5] == c) or \
    (b[7] == c and b[5] == c) or \
    (b[5] == c and b[9] == c) or \
    (b[5] == c and b[3] == c))

def setcond2():
    if board[4] == playerchar and board[2] == playerchar:
        return setcondfree(board, 1)
    elif board[6] == playerchar and board[2] == playerchar:
        return setcondfree(board, 3)
    elif board[4] == playerchar and board[8] == playerchar:
        return setcondfree(board, 7)
    elif board[6] == playerchar and board[8] == playerchar:
        return setcondfree(board, 9)
    else:
        return randommove(board, [1, 3, 7, 9])

def setcond3():
    if board[3] == playerchar and board[4] == playerchar\
    or board[7] == playerchar and board[2] == playerchar:
        return setcondfree(board, 1)
    elif board[1] == playerchar and board[6] == playerchar\
    or board[9] == playerchar and board[2] == playerchar:
        return setcondfree(board, 3)
    elif board[9] == playerchar and board[4] == playerchar\
    or board[1] == playerchar and board[8] == playerchar:
        return setcondfree(board, 7)
    elif board[3] == playerchar and board[8] == playerchar\
    or board[7] == playerchar and board[6] == playerchar:
        return setcondfree(board, 9)
    else:
        return randommove(board, [1, 3, 7, 9])
    
print('Welcome to Tic-Tac-Toe.')
print('I am TicAI, an AI specifically coded so that I will never lose.')
name = str(input('Your name: '))
while name == 'TicAI':
    print("Hey, that's me!")
    name = str(input('Please input your REAL name: '))
print('Hello, %s. Nice to meet you.' % (name))
print('For the tutorial, enter "T".')
comScore = 0
playerScore = 0
tieScore = 0
           
while True:
    SC3 = []
    board = [' '] * 10
    maingak = str.lower(input('To start the game, enter "S". To quit the game, enter "Q": '))
    
    if maingak == 's' or maingak == '1':
        playerchar, comchar = choose()
        turn = firstmove()
        print(turn + ' will go first.')
        
        while True:
            if turn == name:
                printboard(board)
                move = playermove(board)
                turnmove(board, playerchar, move)
                
                if wincond(board, playerchar):
                    printboard(board)
                    playerScore += 1
                    print('Congratulations, %s! You won. Cheating, huh?' % (name))
                    print('Score: TicAI %s - %s %s (%s draws)' % (comScore, playerScore, name, tieScore))
                    break
                
                else:
                    if fullboard(board):
                        printboard(board)
                        tieScore += 1
                        print('We got a draw!')
                        print('Score: TicAI %s - %s %s (%s draws)' % (comScore, playerScore, name, tieScore))
                        break
                        
                    else:
                        turn = 'TicAI'
            
            else:
                time.sleep(0.1)
                move = commove(board, comchar)
                turnmove(board, comchar, move)
                
                if wincond(board, comchar):
                    printboard(board)
                    comScore += 1
                    print("Haha! You can't beat me.")
                    print('Score: TicAI %s - %s %s (%s draws)' % (comScore, playerScore, name, tieScore))
                    break
                
                else:
                    if fullboard(board):
                        printboard(board)
                        tieScore +=1
                        print('We got a draw!')
                        print('Score: TicAI %s - %s %s (%s draws)' % (comScore, playerScore, name, tieScore))
                        break
                        
                    else:
                        turn = name
                    
    elif maingak == 'q' or maingak == '2':
        break
    
    elif maingak == 't':
        print('How to play Tic-Tac-Toe:')
        print('')
        print('7' + '│' + '8' + '│' + '9')
        print('‒‒‒‒‒')
        print('4' + '│' + '5' + '│' + '6')
        print('‒‒‒‒‒')
        print('1' + '│' + '2' + '│' + '3')
        print('')
        print('The board layout is shaped like pictured above, just like a numpad.')
        print('To place a piece into the square, enter the number corresponding to the square.')
        print('Example: if you want to go to the center square, enter "5".')
        print('')
    
    else:
        print('Please enter the right code..')
        
print('Thank you for playing Tic-Tac-Toe, %s. Have a nice day.' % (name))
sys.exit()
