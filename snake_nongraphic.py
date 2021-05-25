def clear_bord():

    game_bord=[]                                            #create a list for rows

    for number in range(10):                                 #create rows in a loop
        row=[".",".",".",".",".",".",".",".",".","."]
        game_bord.append(row)
    return game_bord

clear_bord()                                                    #append rows to created list


def print_gamebord(rows):
    for row in rows:
        print(''.join (row))

#print_gamebord(game_bord)

movement=[(0,0),(1,0),(2,0)]          #tuppels in a list, x & y
apple_list=[(2,5),(7,3),(9,9)]

def change_map(draw_map, apple_list):
    updated_bord=clear_bord()
    for i in draw_map:
        y= i[0]                                         #y=row
        x= i[1]                                         #x=position in list
        updated_bord[x][y]="X"
    for i in apple_list:
        y=i[0]
        x=i[1]
        updated_bord[x][y]="o"

    print_gamebord(updated_bord)                           #call printfunction

change_map(movement, apple_list)                         #call change_mapfunction with draw_maplist



#user_input=input("Give me a direction: n,s,w or e: ")
                                       #initiating startposition x,y for row and position

def movement_snake(movement,user_input):

    y= movement[-1][0]                                   #[position in list] [position in tupple]
    x= movement[-1][1]

    if user_input=="s"and x<9:
        movement.append((y,x+1))
        movement.pop(0)
    elif user_input=="n" and x>0:
        movement.append((y,x-1))
        movement.pop(0)
    elif user_input=="w" and y>0:
        movement.append((y-1,x))
        movement.pop(0)
    elif user_input=="e" and y<9:
        movement.append((y+1,x))
        movement.pop(0)

    else:
        input("Wrong direction or not possible, please typ n,s,w or e: ")



while True:
    user_input=input("Give me a direction: n,s,w or e: ")
    movement_snake(movement,user_input)
    change_map (movement, apple_list)
