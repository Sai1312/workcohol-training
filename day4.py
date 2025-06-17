# print("function()\n")

# def welcome_txt():
#     print("Welcome User ")
#     return "Welcome!"

# # welcome_txt()
# print(welcome_txt())


# def hello_txt(name):
#     return f"Hello {name}"
    
# print(hello_txt("Millen"))
# print(hello_txt("Jack"))

# def greet(name="Guest"):
#     print("Hello, " + name)

# greet()         
# greet("Avi")  

# def celsius(c):
#     f = (c *(9/5) + 32)
#     print(f)

# celsius(32)
# celsius(int(input("Enter celsius: ")))

# print("\n using deocator")
# def my_txt(func): #decorator
#     name = input("Enter name :")
#     def wrapper(c):
#         print(f"Hello {name}!")
#         print("Your Fahrenheit is-")
#         func(c)
#         print("Thank You")
#     return wrapper
    
# @my_txt
# def celsius(c):
#     f = (c *(9/5) + 32)
#     print(f)

# # celsius(32)
# celsius(int(input("Enter celsius: ")))

print("\nexception handling") 

# num = int(input("Enter number: "))
# r = 10/num
# print(f"result is {r}")
try:
    num = int(input("Enter number: "))
    r = 10/num   
    print(f"result is {r}")
except ZeroDivisionError:
    print("Given input cannot be divided.")
except ValueError:
    print("Given input is not a number")
except Exception as e:
    print(e)
