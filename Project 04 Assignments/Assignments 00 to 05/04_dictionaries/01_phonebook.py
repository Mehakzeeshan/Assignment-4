def phonenumber_library():

    phonebook = {}
    while True:
        name = input("Enter your name:")
        if name == "":
            break
        number = input("Enter you phone number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    for name in phonebook:
        print(f"{name}: {phonebook[name]}")

def read_phonebook(phonebook):
    while True:
        name = input("Enter a name to read from phonebook: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"{phonebook[name]}")

def main():
    phonebook = phonenumber_library()
    print_phonebook(phonebook)
    read_phonebook(phonebook)

if __name__ == '__main__':
    main()