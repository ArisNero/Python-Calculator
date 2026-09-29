CalculatorOn=True
def add(a,b):
        return a + b
def substraction(a,b):
        return a-b
def multiply(a,b):
       return a*b
def trueDivison(a,b):
       return a/b
def modulo(a,b):
       return a%b
while CalculatorOn:
        print("Please give the first number x=")
        number1=float(input())
        print("Please give the second number y=")
        number2=float(input())
        print("Please select the operation (+,-,*,/,%)")
        operation=input()
        if operation=="+":
            print("the result is:",add(number1,number2))
            
        else:
               if operation=="-":
                    print("the result is:",substraction(number1,number2))
               else:
                      if operation=="*":
                             print("the result is:",multiply(number1,number2))
                      else:
                             if operation=="/":
                                    print("the result is:",trueDivison(number1,number2))
                             else: 
                                    if operation=="%":
                                        print("the result is:", modulo(number1,number2))
                        