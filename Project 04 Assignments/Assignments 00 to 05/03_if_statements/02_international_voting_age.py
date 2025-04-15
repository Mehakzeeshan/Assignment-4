PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48


user_age: str = input("How old are you? ")
user_age = int(user_age)  # Convert the input to an integer

if user_age >= PETURKSBOUIPO_AGE:
    print("You are eligible to vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48. ")

else:
    print("You are not eligible to vote in any country. ")

if user_age >= STANLAU_AGE:
    print("You are eligible to vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48. ")

else:
    print("You are not eligible to vote in any Stanlau.")

if user_age >= MAYENGUA_AGE:
    print("You are eligible to vote in Mayengua where the voting age is 48. ")

else:
    print("You are not eligible to vote in Mayengua. ")



