adult_age: int = 18

def check_age(age: int):

    if age >= adult_age:
        return True
    
    return False

def main():
    age: str = int(input("Enter your age: "))

    print(check_age(age))

if __name__ == "__main__":
    main()