class ArithmeticOperation:
     def __init__(self,num_1,num_2):
          self.num_1 = num_1
          self.num_2 = num_2

     def addition(self):
          result = self.num_1 + self.num_2
          print("Result:",result)

num_1 = float(input("Enter the first number:"))
num_2 = float(input("Enter the second number:"))
result1 = ArithmeticOperation(num_1,num_2)
result1.addition()

        
          
          