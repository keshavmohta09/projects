print("\n**********Welcome to Tic Tac Toe Game**********\n\n")
player1 = input("Enter the name of player 1: ")
player2 = input("Enter the name of player 2: ")
place = [' ']*10                                  #to print pattern
check_choice = [0]*10                             #to check already exist input
temp_count = 1                                    #for all 9 choices

print()
print("  1  |  2  |  3 ")
print("-----+-----+-----")
print("  4  |  5  |  6 ")
print("-----+-----+-----")
print("  7  |  8  |  9 ")
print("\n\nPress any number for each place\n%s's choice is X\n%s's choice is O\n"%(player1,player2))

def check_all_conditions(player,choice,Xor0):
    '''The work of this function is to check conditions that is number input again, win player and print pattern.'''
    for i in range(1, 10):
        if check_choice[i] == choice:
            print("This number is already used")
            return False

    place[choice] = Xor0
    print(f"  {place[1]}  |  {place[2]}  |  {place[3]} ")
    print("-----+-----+-----")
    print(f"  {place[4]}  |  {place[5]}  |  {place[6]} ")
    print("-----+-----+-----")
    print(f"  {place[7]}  |  {place[8]}  |  {place[9]} ")
    print()

    if (place[1] == place[2] == place[3] == Xor0) or \
        (place[4] == place[5] == place[6] == Xor0) or \
        (place[7] == place[8] == place[9] == Xor0) or \
        (place[1] == place[4] == place[7] == Xor0) or \
        (place[2] == place[5] == place[8] == Xor0) or \
        (place[3] == place[6] == place[9] == Xor0) or \
        (place[1] == place[5] == place[9] == Xor0) or \
        (place[3] == place[5] == place[7] == Xor0):
        print('\n👏👏👏👏',player,'win 👏👏👏👏\n')
        exit()
    return True

while temp_count<10:
    if temp_count%2!=0: player, Xor0 = player1, 'X'
    else:   player, Xor0 = player2, 'O'
    while True:
        choice = input("%s's choice: "%(player))
        if choice in ('1','2','3','4','5','6','7','8','9'):
            choice = int(choice)
            exitloop = check_all_conditions(player,choice,Xor0)
            if exitloop:  break
        else:
            print("Enter the correct choice")
    check_choice[temp_count] = choice
    if check_choice[9]!=0:
        print("\n🤝🤝🤝🤝 Draw 🤝🤝🤝🤝\n")
        exit()
    temp_count+=1