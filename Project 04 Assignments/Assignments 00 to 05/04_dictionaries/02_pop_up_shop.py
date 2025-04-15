def main():

    fruits = {
        "apple": 20,
        "banana": 15,
        "orange": 35,
        "grape": 10,
        "kiwi": 200,
        "mango": 50,
    }

    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        quantity = int(input(f"How many {fruit_name}s would you like to buy? "))
        total_cost += price * quantity


    print(f"Your total cost is Rs.{total_cost}")

if __name__ == '__main__':
    main()