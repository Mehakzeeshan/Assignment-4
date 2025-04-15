sentence: str = "Playing game is a fun and interesting activity. I want to develop games and make my"

def mad_libs():

    adjective: str = input("Please type an adjective and press enter: ")
    noun: str = input("Please type a noun and press enter: ")
    verb: str = input("Please type a verb and press enter: ")

    print(f"{sentence} {adjective} {noun} {verb}")

if __name__ == '__main__':
    mad_libs()