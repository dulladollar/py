import sys                              #7 how to exit you have to import says
try:                                    #9 to pass str err
    x = int(input("x: "))               #1
    y = int(input("y: "))               #2
except ValueError:                      #10
    print("Error: Invalid input.")      #11
    sys.exit(1)                         # #12

try:                                    #4 to pass that err 
    result = x / y                      # #3 paform same division  if 5:10 you will get resalt but if you devide by sero you ll get err
except ZeroDivisionError:               #5
    print("Error: Cannot divide by 0.") #6

    sys.exit(1)                         # #8 and exit

print(f"{x}/{y} = {result}")     