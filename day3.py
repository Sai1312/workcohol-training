print("\nif()")

age = int(input("Enter Age : "))

# if age >= 18:
#     print("Voting Accepted")
# else:
#     print("Voting declained")

result = "Voting Accepted" if age >=18 else "Voting Decalined"
print(result)


print("\nfor()")

for i in range(3, 10, 3):
    print(i)
