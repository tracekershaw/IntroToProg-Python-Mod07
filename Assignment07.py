#------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Working with pickles in a class,
#              develop a program that pickles and unpickles data
#               deveop a program that uses error exception handling
#                Creating a Budget Code
# ChangeLog (Who,When,What):
#
# Tkershaw,11/20/18,Created code to complete assignment 7
# ------------------------------------------------------------------------ #

import pickle
r_list=[]
e_list=[]
g_list=[]
u_list=[]

print ("The purpose of this program is to help you think about your monthly budget")
print ("For rent:")

while True:
    try:
        r_budget=int(input("How much do you want to budget for it: "))
        r_cost=int(input("How much did you spend on it last month: "))
        r_list=[r_budget,r_cost]
        print(r_list)
        break
    except ValueError:
        print("You need to enter a numeric value, please enter a numeric value")

print ("For groceries:")

while True:
    try:
        g_budget=int(input("How much do you want to budget for it: "))
        g_cost=int(input("How much did you spend on it last month: "))
        g_list=[g_budget,g_cost]
        print(g_list)
        break
    except ValueError:
        print("You need to enter a numeric value, please enter a numeric value")

print ("For utilities:")
while True:
    try:
        u_budget=int(input("How much do you want to budget for it: "))
        u_cost=int(input("How much did you spend on it last month: "))
        u_list=[u_budget,u_cost]
        print(u_list)
        break
    except ValueError:
        print("You need to enter a numeric value, please enter a numeric value")

print ("For entertainment:")
while True:
    try:
        e_budget=int(input("How much do you want to budget for it: "))
        e_cost=int(input("How much did you spend on it last month: "))
        e_list = [e_budget, e_cost]
        print(e_list)
        break
    except:
        print ("You need to enter a numeric value")

objFile=open("budget.dat", "ab")
pickle.dump(r_list,objFile)
pickle.dump(g_list,objFile)
pickle.dump(u_list,objFile)
pickle.dump(e_list,objFile)
objFile.close()

objFile=open("budget.dat","rb")
rent=pickle.load(objFile)
groceries=pickle.load(objFile)
utilities=pickle.load(objFile)
entertainment=pickle.load(objFile)
print ("Your rent budget and monthly costs are: ", rent)
print ("Your grocery budget and monthly costs are: ", groceries)
print ("Your utilities budget and monthly costs are: ", utilities)
print ("Your grocery budget and monthly costs are: ", entertainment)
objFile.close()




