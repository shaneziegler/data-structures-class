# Write your code here

# HINT: create a dictionary from flowers.txt
flowers = {}
with open('flowers.txt', 'r') as f:
    for str in f:
        key = str[0]
        value = str[3:len(str)-1]
        flowers[key] = value
        print(key)
        print(value)
       
# HINT: create a function to ask for user's first and last name
def get_user():
    return input("Enter your First [space] Last name only: ")

# print the desired output

name = get_user()
print("Unique flower name with the first letter: " + flowers[name[0].upper()])
