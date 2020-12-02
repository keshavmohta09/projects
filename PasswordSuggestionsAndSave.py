import random,string
x=1                             #for run again same command using loop
while x==1:
    digit = input("Enter the numbers of digits of password: ")
    try:                        #if digit can be change in int else print invalid number and run again
        digit = int(digit)
        if digit<1:
            print("Invalid number")
        elif digit<4:
            print("Password is too short")
        elif digit>50:
            print("Password is too long")
        else:
            x+=1
    except:
        print("invalid number")
x-=1
temp_l = []                    #This is a empty list to save password suggestion
for j in range(5):
    password = list()
    i=0
    while i<=digit:
        i+=1
        if i<=digit: password.append(random.choice(string.ascii_lowercase))
        i+=1
        if i<=digit: password.append(random.choice(string.punctuation))
        i+=1
        if i<=digit: password.append(random.randint(0,9))
        i+=1
        if i<=digit: password.append(random.choice(string.ascii_uppercase))
    random.shuffle(password)
    print("Suggestion",j+1,": ",end='')
    for i in range(len(password)):
        print(password[i],end='')
    temp_l.append(password)    #storing password in temp_l list
    print()
while x==1:
    ask_save = input("Do you want to save the password[Y/n]: ")
    if ask_save == 'Y' or ask_save == 'y':
        while x==1:
            pass_save = input("Which password you want to save: ")
            try:
                pass_save = int(pass_save)
                if pass_save>5 or pass_save<1:
                    print("This suggestion does not exist")
                    continue
                else: x+=1
            except: print("Enter a valid suggestion")
        massage_save = input("Which account is this password: ")
        file = open("password.txt","a")                         #to save password in this file
        listToStr = ''.join(map(str, temp_l[pass_save-1]))      #to convert list to string
        listToStr = listToStr + "    (" + massage_save + ")\n"
        file.write(listToStr)
        file.close()
        print("Your password save in 'password.txt' file")
    elif ask_save == 'N' or ask_save == 'n':
        exit()
    else: print("Enter the correct command")