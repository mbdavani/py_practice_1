## This code slows down anything a user types by adding ellipses to replace spaces

def main():
    userinput = input("What do you wish to say? ")
    return userinput.replace(" ","...")

x = main()

print(x)