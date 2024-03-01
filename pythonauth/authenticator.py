print("Loading Runtime...")
print("Welcome to the more organized version of the password data python project!")
print("What is your name?")
name = input("Please enter your full name:     ")
from getpass import getpass 
if name != "Zach H.": 
  print("Welcome " + name + " You may follow the command line to get into a space. ")
if name == "Zach H.":
  print("Welcome developer!")
  print("Please enter your su password to enter su space ")
  SU = getpass("SU Password:   ")
  if SU == "59hoodies":
    print("Authenticating...")
    print("Access granted, transfering to root")
    exit()


  else:
    print("Access denied, please try again.")
    exit()
 

Account = input("Do you have a account? y/n:      ")
Default1 = []
Default2 = []

if Account == "y":
  print("Please sign in below")
  print("")
  Username = input("Username:   ")
  Password = input("Password:   ")
 # if Username == or Password == :
  print("Authenticating...")
   
#sign up below
else:
  print("Please sign up below using your own username and passowrd: ")
  newuser = input("Username:  \n " )
  newpass = input("Password:  \n ")
  con = input("Please type confirm to create new account:    ")
  if con == "Confirm" or "confirm":
   with open('user.py', 'a') as file1:
     file1.write(newuser)
     file1.write(newpass)
   with open('user.py', 'r') as file1:
     file1.close()
     print("Account created!")
     #print(file1.read())
    
    
  
      
      
  else: 
    no = input("Continue without account y/n   ")
    if no == "y": 
      print("Redirecting")
      print("You are now in the default space")
    else:
      print("Ending proccess")
      exit()


  # Python terminal authenticator project
  # Made by Zach H. 2024
