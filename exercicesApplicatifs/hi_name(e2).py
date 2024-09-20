def input_name():
    name = input("Entrer votre prénom: ")
    return name

def greeting(name):
    print(f"Bonjour {name} !")

def select_function(name):
    while name != "Alfredo":
        input_name()
    print("Bye Alfredo")

def main():
    usr_name = input_name()
    greeting(usr_name)

if __name__ == '__main__':
    main()