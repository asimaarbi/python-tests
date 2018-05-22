
def ask():
    a = input("What is Your Name ?")
    a = a.lower()

    if a == "omer":
        print("Welcome to Python")

    elif a == "asim":
        print("Welcome to Byteshaft")
    else:
        print("Wrong input")
        ask()

ask()

