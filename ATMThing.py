from datetime import datetime
from datetime import date

now = datetime.now()
dateAndTime = now.strftime('%d/%m/%Y %H:%M:%S')
name = str(input('What is your name? \n'))
allowedUsers = ['Jeremiah', 'Bill', 'Ava']
allowedPassword = ['PasswordJeremiah', 'PasswordBill', 'PasswordAva']

if (name in allowedUsers):
        password = str(input('Your Password? \n'))
        userId =allowedUsers.index(name)
        if (password == allowedPassword[userId]):
            print('These are the available options \n')
            print('1. Withdrawl')
            print('2. Cash Deposit')
            print('3. Complaint')
            print('4. Log Out')

            selectedOption = int(input('Please select an option: '))
            if(selectedOption == 1):
                print('You selected %s' % selectedOption)
                withdrawl = int(input('How much would you like to withdraw?'))
                print('Please take your %s dollars \n' % withdrawl)
            elif(selectedOption == 2):
                print('You selected %s' % selectedOption)
                deposit = int(input('How much would you like to deposit?'))
                print('Thank you for your deposit. Your balance is %s dollars \n' % deposit)
            elif(selectedOption == 3):
                print('You selected %s' % selectedOption)
                issue = input('What is the issue you would like to report?')
                print('Thank you for contacting us! \n')
            else:
                print('Invalid option selected, please try again \n')
        else:
            print('Password incorrect, please try again \n')
else: 
    print('Name not found, please try again \n')