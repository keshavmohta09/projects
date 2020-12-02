import time
count = 0
acrt = 0
wrong = []
line1 = "Most of us wonder if there is a God and if He really is the God of the Bible. In"
line2 = "the Bible God says 'I will make your name great' and today the name of Abraham/Abram"
line3 = "is known worldwide. This promise has come true. The earliest copy of Genesis found"
line4 = "in the Dead Sea Scrolls is dated 200-100 B.C. which means the promise has been in"
line5 = "writing since at least that time. At that time the name of Abraham was not well-known"
line6 = "so the promise came true only after it was written down, not before."
line = {1:line1,2:line2,3:line3,4:line4,5:line5,6:line6}

print("\n**********Welcome to typing test**********\n")

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)

enter = input("\nPlease Enter to continue.....")
if enter=='':
    print("Type...........")
    t1 = time.time()
    for j in range(1,7):
        type_t = input()
        if type_t == '':
            break
        fline = line[j].split()
        ty_sp = type_t.split()
        if len(ty_sp)>len(fline):
            extra = len(ty_sp)-len(fline)
            for ex in range(extra):
                ty_sp.pop()

        for i in range(len(ty_sp)):
            if  ty_sp[i] == fline[i]:
                acrt+=1
            else:
                word = ty_sp[i] + '-(line' + str(j) + ')  '
                wrong.append(word)
            count+=1
    t2 = time.time()
    t = (t2-t1)/60
    acrtt = acrt
    countt = count
    if count == 0:    count = 1
    acrt = acrt*100/count
    if count==1:    count = 0
    print("\nYour typing speed is",count//t,"words per minute")
    print("Your accuracy is {0:.2f}%".format(acrt))
    print("Your correct words", acrtt, "in", countt)
    for item in wrong:
        print(item,end=' ')