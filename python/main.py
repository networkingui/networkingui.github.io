#states variable user and asks for selection
import os 
import user 
os. environ['USER'] = 'New User'
def Selection_function(one, two, three):   # input function
    print("you have selected input " + one )
    print("you have selected input " + two)
    print("you have selected input " + three)
y = str("one", "two", "three")   #choice for selection
print("please select a one of the following for an  input on second window .")
print(y)
#execute first input, asks for users name input and prints  user input str 
name = input("please enter your username:")
    print("hello, " + name + "!")
password = input("Please input your password for the session:")
    print("your password is " + password)
print("data =  " name + password)
#user string input, user makes selection and prints choice + your selection for confirmation
x = input("User input selection:")
    print( "selection = " + x )

if x = one:
    Selection_function()







