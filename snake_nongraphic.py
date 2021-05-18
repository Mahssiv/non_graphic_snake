
game_bord=[]                                            #create a list for rows

for number in range(10):                                 #create rows in a loop
    row=[".",".",".",".",".",".",".",".",".","."]
    game_bord.append(row)
                                                    #append rows to created list


def print_gamebord(rows):
    for row in rows:
        print(''.join (row))

#print_gamebord(game_bord)

draw_map=[(0,0),(1,0),(2,0)]          #tuppels in a list, x & y

def change_map(game_bord,draw_map):
    updated_bord=game_bord.copy()
    for i in draw_map:
        y= i[0]                                         #y=row
        x= i[1]                                         #x=position in list
        updated_bord[x][y]="X"                             #exchange given position by draw_maplist

    print_gamebord(updated_bord)                           #call printfunction

change_map(game_bord, draw_map)                         #call change_mapfunction with draw_maplist

#user_input=input("Give me a direction: n,s,w or e: ")
movement=[(2,0)]                                        #initiating startposition x,y for row and position

def movement_snake(movement,user_input):

    y= movement[-1][0]                                   #[position in list] [position in tupple]
    x= movement[-1][1]

    if user_input=="s":
        movement.append((y,x+1))
        movement.pop(0)
    elif user_input=="n":
        movement.append((y,x-1))
        movement.pop(0)
    elif user_input=="w":
        movement.append((y-1,x))
        movement.pop(0)
    elif user_input=="e":
        movement.append((y+1,x))
        movement.pop(0)

    else:
        input("Wrong direction, please typ n,s,w or e: ")



while True:
    user_input=input("Give me a direction: n,s,w or e: ")
    movement_snake(movement,user_input)
    change_map(game_bord, movement)
