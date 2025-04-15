def ones_digit(num):

    return num % 10

def main():
    num = int(input("Enter a number: "))
    ones_digit_num = ones_digit(num)
    print(f"The ones digit of {num} is {ones_digit_num}")

if __name__ == "__main__":
    main()