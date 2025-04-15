def main():

    List :list = []
    elements: str = input("Please enter an element of the list or press enter to stop. ")
    while elements != "":
        List.append(elements)
        elements: str = input("Please enter an element of the list or press enter to stop. ")
   
    print("This is the final list ",List)  # This should print the list of elements entered by the user



if __name__ == '__main__':
    main()  