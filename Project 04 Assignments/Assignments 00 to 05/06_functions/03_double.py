def double_the_num(num: int) -> int:
    

    return num * 2

def main():
    num = int(input("Enter a number: "))
    double_num = double_the_num(num)
    print(f"The double of {num} is {double_num}")

if __name__ == "__main__":
    main()