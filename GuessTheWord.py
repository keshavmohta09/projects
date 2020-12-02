#                                                                   Hangman                                                                     #
import random

words = ['essential','mysterious','alternative','random','arrangement','almost','entertainment','environment','generation',\
         'versatile','circle','positive','amount','argument','basketball','believe','practical','equipment','everything',\
         'circumference','scissor','reverse','decision','definition','demonstration','depression','emergency','hospital',\
         'generator','umbrella','bridge','university','experience','frequency','problem','anklet','development','enforcement',\
         'neighborhood','blanket','journey','knowledge','breakfast','introduction','confirm','confidence','dangerous','information']

comp_word_index  = random.randint(0,len(words))   #to choose a random word in list 'Words'
comp_word = list(words[comp_word_index])    #This is the choosed word by computer in list
match_word = list(words[comp_word_index])   #to match the index of '_'
temp = []           #to take the character before '_' for hints
temp_num = []       #to take the index of random generate '_' in comp_word
count_ = 0
i=0                 #for loop
while i<len(comp_word)-4:
    take = random.randint(0,len(comp_word)-1)
    if comp_word[take]=='_':
        continue
    else:
        i+=1
        temp.append(comp_word[take])
        comp_word[take] = '_'
        temp_num.append(take)
temp_num.sort()         #for sequential order to fill '_'
comp_word_str = ' '.join(comp_word)
random.shuffle(temp)
temp_str = ' '.join(temp)
print(comp_word_str,end='               ')
print("Hints: ",temp_str)
for q in range(len(comp_word)):
    print(q+1,end=' ')
print("              <--Index")
guess = 5

i=0
while i<len(temp_num)+5:
    print("You have",guess,end=' ')
    print("guess" if guess==1 else "guesses")
    for in_ in range(len(comp_word)):
        if comp_word[in_] == '_':
            a = in_
            count_+=1
    if count_>1:
        choice_index = input("\nEnter the index of input character: ")
        try:
            choice_index = int(choice_index)
            choice_index -= 1
            if choice_index > len(match_word):
                pass
            if comp_word[choice_index] != '_':
                print("\nEnter the correct index")
                i -= 1
                continue
        except:
            print("\nEnter the correct index")
            i -= 1
            continue
    if count_ == 1:
        choice_index = a

    choice = input("Enter the letter: ")
    if choice == match_word[choice_index]:
        print("\nCongrats, your guess is right\n")
        comp_word[choice_index] = choice
        comp_word_str = ' '.join(comp_word)
        print(comp_word_str)
        if count_>2:
            for q in range(len(comp_word)):
                print(q+1, end=' ')
        print()
        i+=1
        if comp_word == match_word:
            print("You Win")
            break

        if guess == 0:
            match_word_str = ''.join(match_word)
            print("Game Over\nThe correct word is",match_word_str)
            break
    else:
        while True:
            if guess == 0:
                match_word_str = ''.join(match_word)
                print("\nGame Over\nThe correct word is",match_word_str)
                exit()
            else:
                print("\nSorry, your guess is wrong\n")
                guess -= 1
                if guess==0:    continue
                break
    count_ = 0