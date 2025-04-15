def main():

    number = int(input("Enter a number: "))

    current_number = number

    while current_number <= 100:
        print(current_number)
        current_number = current_number * 2
        
        if current_number > 100:
            break

if __name__ == "__main__":
    main()