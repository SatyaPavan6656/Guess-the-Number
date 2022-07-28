import random
count=1
score=0
while True:
    a=int(input("Enter Your Starting Number:"))
    b=int(input("Enter Your Ending Number:"))
    c=int(input("Please Choose a number in between your Range:"))
    d=random.randrange(a,b+1,1)
    print("User's Choice:",c)
    print("Computer's Choice:",d)
    if(c<a and c>b):
        print("Out Of Range!!!")
    elif(d==c):
        score+=5
        print("Score:",score)
        print("You Won!!!")
        break
    elif(d>c):
        score+=3
        print("Score:",score)
        print("You Lose")
        count+=1
    else:
        score+=1
        print("Score:",score)
        print("You Lose")
        count+=1
print("No of Trails You Played:",count)
print("Total Score:",score)
