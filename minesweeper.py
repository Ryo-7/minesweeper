import numpy as np

bomb = 5

board = [[0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]]
board = np.array(board)
display_board = [['x','x','x','x','x'],
                ['x','x','x','x','x'],
                ['x','x','x','x','x'],
                ['x','x','x','x','x'],
                ['x','x','x','x','x']]
display_board = np.array(display_board)



def bomb_check(x,y,board_max):
    bomb_around = 0
    if board[y,x] == 1:
        print("game over!")
        print(board)
        print("bombs place")
        exit()
    elif x == 0 and y == 0:
        bomb_around = bomb_around + 1 if board[y+1,x] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y,x+1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y+1,x+1] == 1 else bomb_around
    elif x == board_max and y == board_max:
        bomb_around = bomb_around + 1 if board[y-1,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y-1,x] == 1 else bomb_around
    elif x == 0:
        if y != board_max:
            bomb_around = bomb_around + 1 if board[y+1,x] == 1 else bomb_around
            bomb_around = bomb_around + 1 if board[y+1,x+1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y-1,x] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y-1,x+1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y,x+1] == 1 else bomb_around
        
    elif y == 0:
        if x != board_max:
            bomb_around = bomb_around + 1 if board[y,x+1] == 1 else bomb_around
            bomb_around = bomb_around + 1 if board[y+1,x+1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y+1,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y+1,x] == 1 else bomb_around

    elif x == board_max:
        bomb_around = bomb_around + 1 if board[y-1,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y+1,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y-1,x] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y+1,x] == 1 else bomb_around
    elif y == board_max:
        bomb_around = bomb_around + 1 if board[y-1,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y-1,x] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y-1,x+1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y,x+1] == 1 else bomb_around
                
    else:
        bomb_around = bomb_around + 1 if board[y-1,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y+1,x-1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y-1,x] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y+1,x] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y-1,x+1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y,x+1] == 1 else bomb_around
        bomb_around = bomb_around + 1 if board[y+1,x+1] == 1 else bomb_around
    display_board[y,x] = bomb_around

board_max = len(board) - 1
panel = len(board)**2


print(display_board)
a = input("xyの順でスペースで分割して入力").split()
x = int(a[0])
y = int(a[1])

panel -= 1

for i in range(bomb):
    while(1):
        tmpX = np.random.randint(0,len(board))
        tmpY = np.random.randint(0,len(board))
        if board[tmpY,tmpX] != 1 and tmpX != x and tmpY != y:
            board[tmpY,tmpX] = 1
            break
bomb_check(x,y,board_max)

while(1):
    print(display_board)
    a = input("xyの順でスペースで分割して入力").split()
    x = int(a[0])
    y = int(a[1])
    #print(board.shape)
    print(panel)
    if display_board[y,x] == 'x':
        bomb_check(x,y,board_max)
        panel -= 1
        if panel == bomb:
            print("game clear!")
            exit()


        