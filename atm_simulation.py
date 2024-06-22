name  = input("Plz enter your name : ")
print("Helllo ",name)

message = """
How may i help you sir .

Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL.
"""
print(message)
task = int(input("Plz insert your option : "))
available_amount = 5000

if task >=1 and task <=3:  # in btwn 1 - 3 
    print("Welcome to you in virtual bank!")

    #check balance
    if task == 1:
        print("Your available balance is : ",available_amount)
    
    # deposit amount
    elif task == 2:
        deposit_amount = int(input("plz enter deposit amout : "))

        if deposit_amount >=500:
            # available_amount =  available_amount + deposit_amount
            available_amount += deposit_amount 
            print("you have successfully deposited amount : ",deposit_amount)
            print("Your available balance is : ",available_amount)

        else:
            print("Plz enter more than 500 rupees!")

    
    # withdrawl amount 
    else:
        withdrawl_amount = int(input('Plz enter withdrawl amount : '))
        if withdrawl_amount <= available_amount:
            available_amount -= withdrawl_amount
            print("You have successfully withrdrawl your amount : ",withdrawl_amount)
            print("Your available balance is : ",available_amount)

        else:
            print('you have no sufficient balance in your account!')
else:
    print("Plz choose correct input in between 1 to 3 !")


