file = "rich"
parts =file.split(".")
print(parts)
if len(parts) > 1:
    print("extension include")
else:
    file += ".txt"
print(file)

print(type(int("8")))

print([x**3 for x in range(10)])


import re

zip_code = input("Please enter your 5 digit zip code: ")

correct = re.search("[0-9]{5}", zip_code)

if correct:
    print("It works")

else:
    print("No dice")