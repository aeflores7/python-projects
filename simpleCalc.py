#Angelo Flores 11.19.24
#Simple Calculator

#init
#Functions
#Adds num1 + num2 and prints results
def add(num1, num2):

        result=num1+num2
        print("The result is: " +str(result))
def sub(num1,num2):
    answer= num1-num2
    print("The answer is: " +str(answer))
def mul(num1,num2):
    product=num1*num2
    print("The product is: "+str(product))
def div(num1, num2):
    quotient=num1/num2
    print("The quotient is: "+str(quotient))
def calc():
        print("Welcome Preschoolers to Simple Calculator")
        while True:
            print("Please choose an operation: ")
            print("""
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Quit""")
            operation=int(input("(1-5) :"))

            if operation==1:
                add1=int(input("Enter first number: "))
                add2 = int(input("Enter second number: "))
                add(add1,add2)
            elif operation==2:
                sub1=int(input("Enter first number: "))
                sub2=int(input("Enter second number: "))
                sub(sub1,sub2)
            elif operation==3:
                mul1=int(input("Enter first number: "))
                mul2=int(input("Enter second number: "))
                mul(mul1,mul2)
            elif operation==4:
                div1=int(input("Enter first number: "))
                div2=int(input("Enter second number: "))
                div(div1,div2)
            elif operation==5:
                print("Goodbye!")
                break






#Main2
calc()
