# String Function

print("hello")

print("\nlen()")
txt = "hello"
print(txt)
print(len(txt))

print("\nuppercase()")
txt1 = "hello world"
print(txt1.upper())


print("\nstrip()")
txt2 = "  hello     "
print(txt2.strip())

print("\nreplace()")
txt3 = "hello all"

print(txt3)
print(txt3.replace("all","world"))

print("\nsplit()")
txt4 = "hello,all"

print(txt4)

print(txt4.split(","))

print("\njoin()")
txt5 = "hello","world","!"

print(txt5)

print(" ".join(txt5))

print("\nfind()")
txt6 = "Hi all!, this is python training"

print(txt6)

print(txt6.find("python"))

print("\ncount()")
print(txt6)

print(txt6.count("t"))


print("\nisalpha(), isdigit(), isalnum()")
txt7 = "hello world"
txt8 = "456"
txt9 = "name12345"

print(txt7 + "\n" + txt8 + "\n" + txt9)

print(txt7.isalpha())
print(txt8.isdigit())
print(txt9.isalnum())

print("\ncapitaize(), title()")
txt10 = "python training"
txt11 = "hello all"

print(txt10 + "\n" + txt11)

print(txt10.capitalize())
print(txt11.title())