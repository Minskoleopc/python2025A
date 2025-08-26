# # try except else finally
# try:
#     numA = input("please enter a number")
#     numB =input("please enter a numbe12r")
#     print(int(numA)/int(numB))
#     a = [11,22,33]
#     print(a[4])
# except TypeError:
#     print("type error")
# except ZeroDivisionError:
#     print("print zero division error")
# except IndexError:
#     print("exception raised index error")
# except:
#     print("exception raises")
# finally:
#     print("i will alaways execute")


# A single try block can be followed by several except block - true
# mutilple except blocks can be used to handle multiple exceptions -true
# we cannot write except block without try block - true
# we can write  a try block without except block -true
# else and finally blocks are not compulsory - true
# When ther is no exception else block is executed after try block - true
# Finally block is always executed  - true


# try:
#     print(10/5)
# finally:
#     print("i will always except")


# program 3

# try:
#     numA  = input("enter a number")
#     numB = input("enter a number")
#     print(int(numA)/int(numB))
# except ArithmeticError:
#     print("cannot divide by zero")
# else:
#     print("division occured")
# finally:
#     print("i will always execute...")

# Type of exception in python - inbuilt exception
# user defined exception

# try:
#     x = int(input("Enter the number between 5 to 10"))
#     assert x >= 5 and x <=10
# except AssertionError:
#     print("The condition is failed..")


# try:
#     x = int(input("Enter the number between 5 to 10"))
#     assert x >= 5 and x <=10,"input number is incorrect..."
# except AssertionError as obj:
#     print(obj)

# user Defined Exception
# AssertError , ZeroDivision , indexErr

info = {
    "fullaName":"amol rao",
    "balance":1000
}

class MyException(Exception):
    def __init__(self,args):
        self.msg = args


def check(dicts):
    for key in dicts.keys():
        if key == "balance":
            return "pass"
    raise MyException("balance key is not present")


def checkBal(dicts):
    for key,val in dicts.items():
        if key == "balance" and val> 2000:
            return "pass"
    raise MyException("balance is low")

# user define exception
# try:
#     check(info)
# except MyException as obj:
#     print(obj)


try:
    checkBal(info)
except MyException as obj:
    print(obj)



# numpy and pandas seaborne matlablib
# sql (mySQL) (MondoDB) and excel 
# reporting powerBI

# oct 29 
# prompt engineering 
# agentic AI
# git copilot cursor AI
# DSA
# e


# Pragati , Varadraj- MOR 
# list , dict , tuple , set , function ,str
# 8 sept