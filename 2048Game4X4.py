from random import randint
matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print_matrix = [['','','',''],['','','',''],['','','',''],['','','','']]
num_list = [2,2,4,2,2,2,2]
def newnum():
    while True:
        row = randint(0,3)
        clm = randint(0,3)
        num = num_list[randint(0,3)]
        if matrix[row][clm]==0:
            matrix[row][clm] = num
            break

def result():
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==0:
                print_matrix[i][j] = '    '
            else:
                l = str(matrix[i][j])
                if len(l)==1:
                    print_matrix[i][j] = l+'   '
                elif len(l)==2:
                    print_matrix[i][j] = l+'  '
                elif len(l)==3:
                    print_matrix[i][j] = l+' '
                else:
                    print_matrix[i][j] = l
    print(f'[{print_matrix[0][0]}|{print_matrix[0][1]}|{print_matrix[0][2]}|{print_matrix[0][3]}]')
    print(f'[{print_matrix[1][0]}|{print_matrix[1][1]}|{print_matrix[1][2]}|{print_matrix[1][3]}]')
    print(f'[{print_matrix[2][0]}|{print_matrix[2][1]}|{print_matrix[2][2]}|{print_matrix[2][3]}]')
    print(f'[{print_matrix[3][0]}|{print_matrix[3][1]}|{print_matrix[3][2]}|{print_matrix[3][3]}]\n')

def checkwin():
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==2048:
                print('----------You Win----------')
                exit()
    return True

def notloose():
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==0:
                return True
    for i in range(4):
        for j in range(3):
            if matrix[i][j]==matrix[i][j+1]:
                return True
    for i in range(3):
        for j in range(4):
            if matrix[i][j]==matrix[i+1][j]:
                return True
    print('----------Game Over----------')
    exit()


def addindentleft():
    for i in range(4):
        for j in range(3):
            if matrix[i][j]==matrix[i][j+1] and matrix[i][j]!=0:
                matrix[i][j]*=2
                matrix[i][j+1] = 0
    for i in range(3,-1,-1):
        for j in range(3,0,-1):
            if matrix[i][j-1]==0:
                matrix[i][j-1] = matrix[i][j]
                matrix[i][j] = 0

def addindentright():
    for i in range(4):
        for j in range(3):
            if matrix[i][j+1]==matrix[i][j] and matrix[i][j+1]!=0:
                matrix[i][j+1]*=2
                matrix[i][j] = 0
    for i in range(4):
        for j in range(3):
            if matrix[i][j+1]==0:
                matrix[i][j+1] = matrix[i][j]
                matrix[i][j] = 0

def moveleft():
    addindentleft()
    addindentleft()
    addindentleft()
    addindentleft()

def moveright():
    addindentright()
    addindentright()
    addindentright()
    addindentright()

def transposeleftup():
    for i in range(4):
        for j in range(4):
            temp_matrix[i][j] = matrix[j][i]

def transposerightup():
    temp_matrix[0][0] = matrix[3][3]
    temp_matrix[0][1] = matrix[2][3]
    temp_matrix[0][2] = matrix[1][3]
    temp_matrix[0][3] = matrix[0][3]
    temp_matrix[1][0] = matrix[3][2]
    temp_matrix[1][1] = matrix[2][2]
    temp_matrix[1][2] = matrix[1][2]
    temp_matrix[1][3] = matrix[0][2]
    temp_matrix[2][0] = matrix[3][1]
    temp_matrix[2][1] = matrix[2][1]
    temp_matrix[2][2] = matrix[1][1]
    temp_matrix[2][3] = matrix[0][1]
    temp_matrix[3][0] = matrix[3][0]
    temp_matrix[3][1] = matrix[2][0]
    temp_matrix[3][2] = matrix[1][0]
    temp_matrix[3][3] = matrix[0][0]
            


print('************Welcome to 2048 Game************')
print("----------Press (u or ') for slide up or (d or ;) for slide down or (r or /) for slide right or (l or .) for slide left.----------")
newnum()
newnum()
result()
while checkwin():
    if notloose():
        choice = input('Enter move : ')
        ask = randint(1,50)
        if choice in ('u',"'"):
            temp_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            transposeleftup()
            matrix = list(temp_matrix)
            moveleft()
            temp_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            transposeleftup()
            matrix = list(temp_matrix)
            if ask not in (1,10,20,40,45,50):
                newnum()
            result()
        elif choice in ('r','/'):
            moveright()
            if ask not in (1,10,20,40,45,50):
                newnum()
            result()
        elif choice in ('l','.'):
            moveleft()
            if ask not in (1,10,20,40,45,50):
                newnum()
            result()
        elif choice in ('d',';'):
            temp_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            transposerightup()
            matrix = list(temp_matrix)
            moveleft()
            temp_matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            transposerightup()
            matrix = list(temp_matrix)
            if ask not in (1,10,20,40,45,50):
                newnum()
            result()
        else:
            result()