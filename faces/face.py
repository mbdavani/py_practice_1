def main():
    x = input("Type an emoticon based on how you are feeling!")
    if x == ":)":
        print("🙂")
    elif x== ":(":
        print("🙁")

## Better code, more generalized. note to self: stop overusing Regular Expressions (RE)
def main2():
    x = input("How are you? ")
    return x.replace(":)", "🙂").replace(":(","🙁")
xx = main2()
print(xx)