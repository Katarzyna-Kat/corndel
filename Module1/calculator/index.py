# number_1 = int(input("Please type in your first number: "))
# number_2 = int(input("Please type in your second number: "))

# operator = input("Please input your operator from '+', '-', '*', '/': ")

with open("step_2.txt", 'r') as f:
    text_string = f.read()

list_of_string = text_string.splitlines()

for i in list_of_string:
    item_split = i.split()
    operator = item_split[1]
    number_1 = int(item_split[2])
    number_2 = int(item_split[3])


def calculator(number_1, number_2, operator):
    if operator == "+":
        print(number_1 + number_2)
    elif operator == "-":
        print(number_1 - number_2)
    elif operator == "x":
        print(number_1 * number_2)
    elif operator == "/":
        print(number_1 / number_2)
    else:
        print("You did not chose a vaild option.")
        
calculator(number_1, number_2, operator)
