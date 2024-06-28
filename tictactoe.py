def create():
    num=0
    for i in range(rows):
        one_row=[]
        for j in range(columns):
            one_row.append(num)
            num+=1
        board.append(one_row)
def display():
    for i in board:
        for j in i:
            print(f"{j}\t",end="")
        print()
def win():
    for i in range(rows):
        winner=True
        for j in range(columns-1):
            if(board[i][j]!=board[i][j+1]):
                winner=False
        if(winner==True):
            return winner
    for i in range(columns):
        winner=True
        for j in range(rows-1):
            if(board[j][i]!=board[j+1][i]):
                winner=False
        if(winner==True):
            return winner
    if(rows==columns):
        winner=True
        for i in range(rows-1):
            if board[i][i]!=board[i+1][i+1]:
                winner=False
        if(winner==True):
            return winner
        col_no=0
        winner=True
        for i in range(columns-1,0,-1):
            if board[i][col_no]!=board[i-1][col_no+1]:
                winner=False
            col_no+=1
    return winner   
rows=6
columns=6
board=[]
player_1=input("Player 1 plz enter your name:")
player_2=input("Player 2 plz enter your name:")
print("____________________________")
print(f"{player_1} vs {player_2}")
print("____________________________")
player=player_1
moves=win_check=0
create()
display()
entries=[]
while(True):
    check=0
    while(True): 
        box=eval(input(f"{player}!Enter box number (0-{rows*columns-1}):"))
        if(box not in entries and 0<=box<=rows*columns-1):
            entries.append(box)
            moves+=1
            check=1
        else:
            print()
            print(f"Hey {player}! Box {box} is already occupied or does not exist")
            print()
        if(check==1):
            break
    board[int(box/columns)][box%columns]=player
    print()
    display()
    win_check=win()
    if(win_check==1):
        print(f"Winner :{player}")
        break
    if(player==player_1):
        player=player_2
    else:
        player=player_1
    if(moves==rows*columns):
        print("Drawn")
        break