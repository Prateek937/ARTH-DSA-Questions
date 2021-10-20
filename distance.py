'''
Coding question 2:💻

The distance between two cities (in km) is input through keyboard. 
Write a program to convert and print the distance in meters, feet, inches and centimetres.
'''

kilometers = float(input("Distance in km: "))

meters = kilometers*1000
feet = kilometers*3280.84
inches = kilometers*39370.1
centimeters = kilometers*100000   

print(f'''
Distance in :-
Meters: {meters}
Feet: {feet}
Inch: {inches}
Centimeters: {centimeters}
''')