def main():
    side1: float = float(input("Enter the length of the first side: "))
    side2: float = float(input("Enter the length of the second side: "))
    side3: float = float(input("Enter the length of the third side: "))

    
    print("The perimeter of the triangle is " + str(side1 + side2 + side3))

if __name__ == '__main__':
    main()