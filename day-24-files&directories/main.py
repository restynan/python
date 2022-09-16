# with key word manages the file for us as soon as it notices we are done using  it closes it
with open("my_file.txt") as file:
    content = file.read()
    print(content)

# a-append w-write deletes the existing info, if file doesnot exist it creates a new one
with open("my_file5.txt", mode="w") as file:
    file.write("\n ************")

with open("data.txt") as data:
    content = data.read()
   #data_list = content

print(content)
"""
file = open("my_file.txt")
content = file.read()
print(content)
file.close()  # frees up resources
"""
