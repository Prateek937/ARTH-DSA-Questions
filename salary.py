'''
Coding question 1:💻

Ramesh's basic salary is input through the keyboard. 
His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. 
Write a program to calculate his gross salary.
'''

basic_salary = float(input("Enter Ramemsh's the basic salary: "))
dearness_allowance = (basic_salary*40)/100
rent_allowance = (basic_salary*20)/100
gross_salary = basic_salary + dearness_allowance + rent_allowance

print("Gross salary of Ramesh: gross_salary", gross_salary)