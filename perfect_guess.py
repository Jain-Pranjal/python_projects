#perfect guess game 

# that generates a random number 
import random
# randint takes both the inlcuded values also 
a=random.randint(1,100)
print(a)
print("computer has generated the number and now its your turn to do the guess ................")
counter=0
while True:
    try:
        guess=int(input("Enter the guess : "))
        counter+=1
        if guess>a:
            print("lower down ")
        elif guess<a:
            print("go up ")
        else:
            break
        # i have break the loop once the number matches with the random number
    except:
        print("please enter a valid guess")
print(f"\n u have take {counter} guesses")    
print("u have guessed correctly ")


# now make a file that store the output in the file and if the guess is less than append it also 
with open ("highscore.txt","r") as f:
    highscore=int(f.read())
    print(highscore)
# string cannot be compare so we need to type cast into int 

# # counter is < as less guess means the victory
if counter<highscore:
    print("u broke the highscore as u have identify the number in less no of guesses")
    with open ("highscore.txt","w") as f:
        f.write(str(counter))
        # we cannot write the integer so converting it into the string 


# PROGRAM IS WRITTEN GOOD BUT PROBELM IS THERE IN FILE OPENING 
# invalid literal for int() with base 10: '' THIS ERROR IS SHOWING 























