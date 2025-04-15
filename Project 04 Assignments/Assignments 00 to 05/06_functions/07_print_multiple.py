def print_multiple(message, repeat):

    for i in range(repeat):
        print(message)

def main():
    message = input("Enter a message: ")
    repeat = int(input("Enter a number of times you to repeat the message: "))

    print_multiple(message, repeat)

if __name__ == "__main__":
    main()