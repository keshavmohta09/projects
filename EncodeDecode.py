from time import sleep
l1 = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','_','\n',\
    '0','1','2','3','4','5','6','7','8','9',',','.','|',';',':','&','%','@','!','#','(',')','{','}','[',']','+','-','*','/','=','"',"'")
l2 = ('¡','¢','£','¤','¥','¦','§','¨','©','ª','«','¬','®','¯','°','±','²','³','´','µ','¶','·','¸','¹','º','»','×',' ','Ξ','N',\
    '÷','þ','ø','ċ','ď','Ħ','ĭ','Ŋ','Œ','œ','Ŕ','ţ','Ŧ','ŭ','ƛ','Ɵ','Ơ','Ƣ','ƣ','Ʀ','Ʊ','ƾ','ȩ','ȭ','ȸ','ȹ','ȿ','Ɂ','Ɏ','ə','Δ','Θ')
while True:
    choice = input('Press e for encode and d for decode : ')
    if choice=='e':
        d = dict(zip(l1,l2))
        result = ''
        data = input("Type something you wnat to encode : \n").lower()
        for letter in data:
            if letter in d:
                result+=d[letter]
            else:
                result+=letter
        sleep(.5)
        print('\nData encoding.',end='')
        sleep(.5)
        print('.',end='')
        sleep(.5)
        print('.',end='')
        sleep(.5)
        print('.',end='')
        sleep(.5)
        print('.')
        sleep(.5)
        print(result)
        break
    elif choice=='d':
        d = dict(zip(l2,l1))
        result = ''
        data = input("Type something you wnat to decode : \n")
        for letter in data:
            if letter in d:
                result+=d[letter]
            else:
                result+=letter
        sleep(.5)
        print('\nData decoding.',end='')
        sleep(.5)
        print('.',end='')
        sleep(.5)
        print('.',end='')
        sleep(.5)
        print('.',end='')
        sleep(.5)
        print('.')
        sleep(.5)
        print(result)
        break
    else:
        print('Enter the correct command')