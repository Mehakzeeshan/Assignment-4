def num_in_stock(fruit):

    if fruit == "banana":
        return 5
    
    if fruit == "apple":
        return 30
    
    if fruit == "lychee":
        return 50
    
    if fruit == "guava":
        return 20
    
    if fruit == "mango":
        return 40
    
    else:
        return 0
    
def main():
    fruit_name: str = input("Enter the name of the fruit: ")
    stock = num_in_stock(fruit_name)

    if stock == 0:
        print(f"Sorry, we do not have {fruit_name} in stock.")
    else:
        print(f"We have {stock} {fruit_name}s in stock.")

if __name__ == "__main__":
    main()