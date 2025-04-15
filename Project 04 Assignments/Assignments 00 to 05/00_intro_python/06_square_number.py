def main ():
    num: int = int(input("Enter a number to get its square: "))

    formatted_num = f"\033[1;3m{num}\033[0m"
    
    print(f"{formatted_num} is squared as {num ** 2}")

    
if __name__ == "__main__":    
    main()