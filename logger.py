name = input("What is your name? ")

with open("guest_list.txt", "a") as file:
    file.write(name + "\n")