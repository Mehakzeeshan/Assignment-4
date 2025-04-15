def get_data():

    name = str(input("Enter your first name: "))
    last_name = str(input("Enter your last name: "))
    email = str(input("Enter your email address: "))

    return name, last_name, email

def main():
    user_input = get_data()    
    print("Recieved the following data: " + str(user_input))

if __name__ == "__main__":
    main()