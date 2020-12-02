from random import randint
name = input("Enter your name: ")
name_point = 0
comp_point = 0

def statement():
    '''This function is only for instructions printing.'''
    print("Press 1 for Snake\nPress 2 for Water\nPress 3 for Gun")

def check_choice(name,choice):
    '''The work of this function is to print what User/Computer choose.'''
    if choice == 1: print(name,"choose Snake")
    elif choice == 2:   print(name,"choose Water")
    else:   print(name,"choose Gun")

def win_choice(name,choice,comp_choice):
    '''The work of this function is to check all conditions and give the result that User/Computer get point.'''
    if (choice==1 and comp_choice==2) or (choice==2 and comp_choice==3) or (choice==3 and comp_choice==1):
        print(name,'get 1 point')
        return True
    elif choice==comp_choice:
        print(name, 'get 1 point')
        print('Computer get 1 point')
        return None
    else:
        print('Computer get 1 point')
        return False

print("You have 5 chance")
statement()
for i in range(5):
    while True:
        choice = input('\nEnter your choice: ')
        if choice in ('1','2','3'):
            choice = int(choice)
            check_choice(name,choice)
            break
        else:  statement()
    comp_choice = randint(1,3)
    check_choice('Computer',comp_choice)
    point = win_choice(name,choice,comp_choice)
    if point==True:
        name_point+=1
    elif point==None:
        name_point += 1
        comp_point += 1
    else:
        comp_point+=1
    print("\n%s's point = %d"%(name,name_point))
    print("Computer's point =",comp_point)
print()
if name_point>comp_point:   print(name,'win')
elif name_point==comp_point:    print('Draw')
else:   print('Computer win')