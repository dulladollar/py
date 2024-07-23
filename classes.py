# where objects might store information (store some data inside them) and also support ability to perform types of operation.
# some sort of actions or methods, or fuction as we might call them.
# clase is as a template for a type of object( template means a preset format for a document or file) 
 
class Point():
     
# we use __init__ everytimes that we want try to create a new point
# all fuction that operate on objects themself( otherwise known as methods)are going to take the first argument called sef ( # self.)
     def __init__(self, input1, input2):
          self.x = input1
          self.y = input2
     
# if you want to create a new           
p = Point(2, 8)
print(p.x)
print(p.y)