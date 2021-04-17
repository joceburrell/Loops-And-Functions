#register
# - first name, last name, password, email
# - generate user account


#login
# - accountnumber, password

# bank operations

#Initializing the system

import random

database = {} #dictionary

def init():

    isValidOptionSelected = False
    print('Welcome to Jocelyns bank')

    while isValidOptionSelected == False:
        haveAccount = int(input('Do you have an account with us? 1 (yes) 2 (no) \n'))
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print('You have selected an invalid option')


def login():
    print('************ Login **************')

    isLoginSuccessful = False

    while isLoginSuccessful == False:
        accountNumberFromUser = int(input('What is your account number \n'))
        password = input('What is your password \n')

        for accountNumber,userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    isLoginSuccessful = True

        print('Invalid account or password')
    bankOperation(userDetails)

def register():
    print('********* Register ********* \n')
    email = input('What is your email? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create a password \n')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print('Your account has been created')
    print('== === ====== ===== ===')
    print('Your account number is %d' % accountNumber)
    print('Make sure you keep it safe')
    print('== ==== ====== ===== == =')

    login()



def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawl (3) Logout (4) Exit \n"))

    if selectedOption == 1:

        depositOperation()
    elif selectedOption == 2:

        withdrawlOperation()
    elif selectedOption == 3:

        logout()
    elif selectedOption == 4:

        exit()
    else:

        print("Invalid option selected")
        bankOperation(user)

def withdrawlOperation():
        print('You selected withdrawl')
        withdrawl = int(input('How much would you like to withdraw?'))
        print('Please take your %s dollars \n' % withdrawl)
        bankOperation()

def depositOperation():
        print('You selected deposit')
        deposit = int(input('How much would you like to deposit?'))
        print('Thank you for your deposit. Your balance is %s dollars \n' % deposit)
        bankOperation()

def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

def logout():
    login()


### ACTUAL BANKING SYSTEM ###

init()

