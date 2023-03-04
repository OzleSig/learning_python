import copy
game_state =    [['_','_','_'], 
                ['_','_','_'],
                [' ',' ',' ']]

game_state_empty =      [['_','_','_'], 
                        ['_','_','_'],
                        [' ',' ',' ']]

def display_game_state():
    for y in game_state:
        for count, x in enumerate(y):
            if count < 2:
                print(x, end = '|')
            else:
                print(x)

def update_grid(pos,player_char):
    y = pos[0]
    x = pos[1]
    current = game_state[y][x]
    if (current=='_') or (current==' '):
        game_state[y][x]=player_char
        return True
    return False

def check_horizontals():
    for x in range(3):
        if not ((game_state[x][0]=='_') or (game_state[x][0]==' ')):
            if game_state[x][0]==game_state[x][1]==game_state[x][2]:
                return True

def check_verticles():
    for x in range(3):
        if game_state[0][x]==game_state[1][x]==game_state[2][x]:
            return True

def check_diagonal():
    if (game_state[0][0]==game_state[1][1]==game_state[2][2]) or game_state[2][0]==game_state[1][1]==game_state[0][2]:
        return True

def check_for_winner():
    if check_diagonal() or check_horizontals() or check_verticles():
        return True
    
def check_update(pos_str):
    if not len(pos_str)==3:
        print('This input is too long/too short')
        return False
    else:
        pos_str = pos_str.split(',')
        for x in pos_str:
            if not x.isnumeric():
                print('These are not coordinates')
                return False
        pos = [eval(i) for i in pos_str] 
        if pos[0]>2 or pos[1]>2 or pos[0]<0 or pos[1]<0:
            print('x, y coordinates are not in range (0-2)')
            return False
        else:
            return True
    
def player_input():
    pos_str = input('Please give a position (x,y): ')
    while not check_update(pos_str):
        pos_str = input('Try again (x,y):')
    pos_str = pos_str.split(',')
    pos = [eval(i) for i in pos_str]    
    pos[0],pos[1] = pos[1], pos[0]
    return (pos)

def x_or_o(player):
    if player%2 == 0:
        player_char = 'O'
    elif player%2 == 1:
        player_char = 'X'
    return player_char

def main():
    global game_state
    player = 0
    play_again = 'y'
    while play_again == 'y':
        while not check_for_winner():
            display_game_state()
            pos = player_input()
            player_char = x_or_o(player)
            hg = update_grid(pos,player_char)
            if not hg:
                print('Position filled, try again')
            else: 
                player +=1
        display_game_state()
        print(player_char + ' player wins!')
        play_again = input('Play again? (y/n)')
        game_state = copy.deepcopy(game_state_empty)
main()