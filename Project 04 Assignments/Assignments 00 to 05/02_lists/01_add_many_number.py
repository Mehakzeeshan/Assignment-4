def add_many_numbers(numbers) -> int:


    total_sum = 0
    for number in numbers:
        total_sum += number

    return total_sum

def main():
    list_of_numbers: list[int] = [1, 2, 3, 4, 5]
    result: int = add_many_numbers(list_of_numbers)

    print("The result of adding numbers between 1 to 5 = ", result)

if __name__ == "__main__":
    main()