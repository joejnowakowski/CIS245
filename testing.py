file = "rich"
parts =file.split(".")
print(parts)
if len(parts) > 1:
    print("extension include")
else:
    file += ".txt"
print(file)