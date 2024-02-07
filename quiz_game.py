print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
     quit()
     
print("Okay! Let's play :)")
score = 0

answer = input("What country is Nufan from? ")
if answer.lower() == "Sri Lanka ":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again")
    
answer = input("How tall is Nufan? ")
if answer.lower() == "5 foot 10":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again ")
    
answer = input("What does Nufan prefer, Mercedes or BMW? ")
if answer.lower() == "Mercedes":
    print("Correct!")
    score += 1
else:
    print("Incorrect! Try again")
    
answer = input("Would Nufan prefer a Golf MK6 as a first car or a Fiat 500? ")
if answer.lower() == "Golf MK6":
    score += 1
    print("Correct!")
else:
    print("Incorrect! Try again")
    
    print("You got " + str(score) + " correct! ")
    print("You got " + str((score / 4)) + "%. ")