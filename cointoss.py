import random
def cointoss():
    number=False
    #define looping condition
    while not number:
        a=int(input("number of flips: "))
        #ask user to input number of flips and convert to an integer
        if a <0:
            print("Please enter a positive integer")
            number=False
            #test if a is negative
            #if test fails, start while-loop again
        else:
            recordlist=[]
            #record of results starts from null
            heads=0
            tails=0
            for amount in range(int(a)):
            #for-loop to simulate tossing for a times
                flip=random.randint(0,1)
                #randomly generate 0 or 1 and assign value to flip to define heads and tails
                if (flip==0):
                    recordlist.append("heads")
                    #define 0 as heads
                else:
                    recordlist.append("tails")
                    #define 1 as tails
                    #add new result to the recordlist
            print(str(recordlist))
            print("you got "+str(recordlist.count("heads"))+" heads and "+str(recordlist.count("tails"))+" tails")
            #display summary result of the cointoss
        break
        #break the loop to finish the program
