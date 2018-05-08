def incometax():
    income=False
    #looping condition
    while not income:
        i=float(input("what is your annual income: "))
        #ask user to input annual income
        #convert to a floating number
        if i<0:
            print("please enter a correct income figure")
            income=False
        #first condition to test if the income is positive
        else:
            #use if-loop to calculate tax for different incomes
            if i<=18200:
                tax=0
            elif (i>18200 and i<=37000):
                tax=0.19*(i-18200)
            elif (i>37000 and i<=87000):
                tax=0.325*(i-37000)+3572
            elif (i>87000 and i<=180000):
                tax=0.37*(i-87000)+19822
            else:
                tax=0.45*(i-180000)+54532
            netin=i-tax
            #calculate net income after tax
            tax=round(tax,2)
            netin=round(netin,2)
            #round to two decimal places
            print("Your tax liability is "+str(tax))
            print("Your after-tax income is "+str(netin))
            break
