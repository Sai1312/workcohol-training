# Math Function

print("\nint()")
n1 = 2.8
print(n1)
print(int(n1))
print(int("9"))

print("\nfloat()")
n2 = 7.7
print(n2)
print(float(n2))    
print(float("9.2"))

print("\ncomplex()")
print(complex(6, 3))

print("\nabs()")
n3 = -9 
n4 = 3.1
print("n1 = " + str(n3) + "\n" + "n2 = " + str(n4))
print(abs(n3))
print(abs(n4))

print("\npow()")
n5 = 4
n6 = 3
print("n1 = " + str(n5) + "\n" + "n2 = " + str(n6))
print(pow(n5, n6))

print("\nround()")
n7 = 1.258
print("n1 = " + str(n7))
print(round(n7))
print(round(n7, 3))

print("\ndivmod()")
n8 = 4
n9 = 3
print("n1 = " + str(n8) + "\n" + "n2 = " + str(n9))
print(divmod(n8, n9))   

print("\nmax()")
n10 = 7
n11 = 5
n12 = 9
print("n1 = " + str(n10) + "\n" + "n2 = " + str(n11) + "\n" + "n3 = " + str(n12))
print(max(n10, n11, n12))

print("\nmin()")
n10 = 7
n11 = 5
n12 = 9
print("n1 = " + str(n10) + "\n" + "n2 = " + str(n11) + "\n" + "n3 = " + str(n12))
print(min(n10, n11, n12))

print("\ntype()")
n13 = 5
n14 = 0.9
print("n1 = " + str(n13) + "\n" + "n2 = " + str(n14))
print(type(n13))
print(type(n14))


print("\nmath() & random()")

import math

print("\nsqrt()")
num1 = 25
print("num = " + str(num1))
print(math.sqrt(num1))

print("\nceil()")
num2 = 9.2
print("num = " + str(num2))
print(math.ceil(num2))

print("\nfloor()")
print("num = " + str(num2))
print(math.floor(num2))

print("\nfactorail()")
num3 = 6
print("num = " + str(num3))
print(math.factorial(num3))

print("\nrandom()")

import random
 
print(random.random())

print("random int()")
num4 = 9
num5 = 21
print(random.randint(num4, num5))

print("random choice()")
num6 = 9
num7 = 11
num8 = 16
num9 = 22
print(random.choice([num6, num7, num8, num9]))