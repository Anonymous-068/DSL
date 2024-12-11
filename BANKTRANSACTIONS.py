'''
Madhur Jaripatke
Roll No. 56
SE A Computer
RMDSSOE, Warje, Pune
'''
'''
Write a Python program that computes the net amount of a bank account based on a 
transaction log from console input. The transaction log format is shown as following: D 
100 W 200 (Withdrawal is not allowed if balance is going negative. Write functions for 
withdraw and deposit) D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300, D 300 , W 200, D 100 Then, the output should be: 500
'''
def deposit(num):
    global total
    total+=num
def withdraw(num):
    global total
    if total>num:
        total-=num
    else:
        print('Insufficient balance')
list1=[]
total=0
str1=input('Enter transaction log ')
list1.append(str1.split())
a=int(input('Enter number of transactions '))
for var in list1:
    for i in range(0,2*a):
        if var[i]=='D':
            deposit(int(var[i+1]))
        elif var[i]=='W':
            withdraw(int(var[i+1]))
print('Balance is', total)
