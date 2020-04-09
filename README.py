# python-task-2
#collect user data: first name, last name, and email address.
import string
import random
print("Please type your details")
first_name = input("What's your first name? ")
last_name = input("Your last name? ")
email =input(" Your email? ")
user_details = [first_name, last_name, email]
for deets in [first_name, last_name, email]:
    print (deets)
print(first_name[0:2])
print(last_name[-2:])
combo=first_name[0:2]+last_name[-2:]
#generating random string of length 5, printing lower case
letters = string.ascii_lowercase
length = 5
random_password = ''.join(random.choice (letters) for i in range (length))
password = [combo + random_password]
print(password)
status = True
container = []
while status:
    #ask user to choose password themselves if password is not preferable
    Response = input(" Do you like your password? Yes or No." )
    password_loop = True
    while password_loop:
        if Response == "Yes":
           print("please confirm your details below:")
           print(user_details + password)
           password_loop = False

        else:
            prefered_password = input(str("Please enter a password longer than or equal to 7 xters "))
            #password length loop
            pass_len = True
            while pass_len:
                if len(prefered_password)>=7:
                   #add new password to user_details
                   print("please confirm your details below:")
                   #converting list(user_details) to stringH
                   user_details = ''.join(user_details)
                   print(user_details + prefered_password)
                   #breaking out of the pass_len loop
                   pass_len = False
                   #breaking out of the new_password loop
                   prefered_password = False
                else:
                    print("password is less than 7.")
                    prefered_password = input(str("enter password longer than or equal to 7 "))
#new user
new_user = input("Another user?")
if new_user == "Yes":
   status = True
   print("enter your details below:")
   #user enters details
else:
    status = False

