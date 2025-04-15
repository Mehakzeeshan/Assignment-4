def greetings(name: str) -> str:

    return f"Greetings! {name}"

def main():
    name = str(input("Enter your name: "))
    print(greetings(name))

if __name__ == "__main__":
    main()