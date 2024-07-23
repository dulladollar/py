# if you want to use a fuction that was defined inside of another file you have to import it 

# is by call the name of that file import that function


from function_file_1 import square

for i in range(10):
     print(f"The square of {i} is {square(i)}")

# other whay to import it is by importing the name of that file

            #ex: 2
#  import function_file_1

#    for i in range(10):
        # print(f"The square of {i} is {function.square(i)}")