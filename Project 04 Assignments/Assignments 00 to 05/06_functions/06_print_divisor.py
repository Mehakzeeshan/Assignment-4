def get_divisors(num):
    
    print(f"The divisors of {num} are:")
    for i in range(num):
        curr_divisors = i + 1
        if num % curr_divisors == 0:
            print(curr_divisors)

def main():
    num = int(input("Enter a number: "))
    get_divisors(num)


if __name__ == "__main__":
    main()