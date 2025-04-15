def average(num1: int, num2: int) -> float:

    average_num = (num1 + num2) /2

    return average_num

def main():
    average_num = average(6, 8)
    print(f"The average of 6 and 8 is {average_num}")

if __name__ == "__main__":
    main()