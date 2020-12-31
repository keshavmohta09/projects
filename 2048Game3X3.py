from random import randint
l = [0]*10
l1 = [' ']*10
temp = [0]*10
temp2 = []
numbers = [2,4]
print('************Welcome to 2048 Game************')
print("----------Press (u or ') for slide up or (d or ;) for slide down or (r or /) for slide right or (l or .) for slide left. For undo press 1----------")

def printformat():
    for i in range(1,10):
        if l[i]!=0:
            q = str(l[i])
            for j in range(4-len(q)):
                q+=' '
            l1[i] = q
        else:
            l1[i] = '    '
    print(f'[{l1[1]}|{l1[2]}|{l1[3]}]')
    print(f'[{l1[4]}|{l1[5]}|{l1[6]}]')
    print(f'[{l1[7]}|{l1[8]}|{l1[9]}]\n')

def fillnumber():
    while True:
        place = randint(1,9)
        if l[place] == 0:
            l[place] = numbers[randint(0,1)]
            break

def slideup():
    for i in range(1,7):
        if l[i]==l[i+3]:
            l[i] = l[i]+l[i+3]
            l[i+3] = 0
    for i in range(1,7):
        try:
            if l[i] == l[i+6] and l[i+3]==0:
                l[i] = l[i]+l[i+6]
                l[i+6] = 0
        except:
            pass
    for i in range(1,7):
        try:
            if l[i+3]==l[i+6]:
                l[i+3] = l[i+3]+l[i+6]
                l[i+6] = 0
        except:
            pass
    for i in range(1,10):
        try:
            if l[i]==0:
                l[i] = l[i+3]
                l[i+3] = 0
        except:
            pass
    for i in range(1,10):
        try:
            if l[i]==0:
                l[i] = l[i+3]
                l[i+3] = 0
        except:
            pass

def slidedown():
    temp[1] = l[7]
    temp[2] = l[8]
    temp[3] = l[9]
    temp[4] = l[4]
    temp[5] = l[5]
    temp[6] = l[6]
    temp[7] = l[1]
    temp[8] = l[2]
    temp[9] = l[3]  

def slideright():
    temp[1] = l[9]
    temp[2] = l[6]
    temp[3] = l[3]
    temp[4] = l[8]
    temp[5] = l[5]
    temp[6] = l[2]
    temp[7] = l[7]
    temp[8] = l[4]
    temp[9] = l[1]

def slideleft():
    temp[1] = l[1]
    temp[2] = l[4]
    temp[3] = l[7]
    temp[4] = l[2]
    temp[5] = l[5]
    temp[6] = l[8]
    temp[7] = l[3]
    temp[8] = l[6]
    temp[9] = l[9]


def checkwin():
    if 2048 in l:
        printformat()
        print('----------You Win----------')
        exit()

place = randint(1,9)
l[place] = numbers[randint(0,1)]
while True:
    if 0 not in l[1:]:
        print('Game Over')
        exit()
    fn = randint(1,50)
    if fn not in (11,25,46,50):
        fillnumber()
    temp2.append(l)
    printformat()
    while True:
        opt = input('Enter slide : ')
        if opt in ('u',"'"):   
            slideup()
            temp2.append(l)
            break
        elif opt in ('r','/'):  
            slideright()  
            l = list(temp)
            slideup()
            slideright()
            l = list(temp)
            temp2.append(l)
            break
        elif opt in ('l','.'): 
            slideleft()
            l = list(temp)
            slideup()
            slideleft()
            l = list(temp)
            temp2.append(l)
            break
        elif opt in ('d',';'):
            slidedown()
            l = list(temp)
            slideup()
            slidedown()
            l = list(temp)
            temp2.append(l)
            break
        elif opt=='1':
            try:
                l = temp2[-3]
                temp2.remove(l)
            except:
                pass
            printformat()
        else:
            printformat()
    checkwin()