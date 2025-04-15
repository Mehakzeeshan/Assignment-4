def get_last_element(last):

    print(last[-1])

def get_last():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    last: list = []
    elements: str = input("Please enter an element of the list or press enter to stop. ")
    while elements != "":
        last.append(elements)
        elements: str = input("Please enter an element of the list or press enter to stop. ")
    return last
    
def main():
    last =get_last()
    get_last_element(last)

if __name__ == '__main__':
    main()