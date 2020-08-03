import random

print("H A N G M A N")
    
def hangman():   
    
    lst = ['python', 'java', 'kotlin', 'javascript']
    l = random.choice(lst)

    a = "-"*len(l)
    x = 0
    lst1 = []

    while x < 8:
        print("")
        print(a)
        if a == l:
            print("You guessed the word!")
            break

        w = input("Input a letter: ")

        if len(w) != 1:
            print("You should input a single letter")

        elif w.islower():
            if w not in lst1:
                lst1.append(w)

                if w in l:             
                    for i in range(len(l)):
                        if l[i] == w:
                            a = a[:i] + w + a[i+1:]

                else:
                    print("No such letter in the word")
                    x += 1 

            else:
                print("You already typed this letter")
        else:
            print("It is not an ASCII lowercase letter")


    if a == l:
        print("You survived!")
    else:
        print("You are hanged!")
        
        
        
        
        
a = input("""Type "play" to play the game, "exit" to quit: """)        
while a != "exit":
    if a != "play":
        a = input("""Type "play" to play the game, "exit" to quit: """)
    else:
        hangman()
        a = input("""Type "play" to play the game, "exit" to quit: """)
    
        