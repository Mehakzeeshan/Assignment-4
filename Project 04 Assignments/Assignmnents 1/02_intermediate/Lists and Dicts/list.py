def main():
    fruit_list: list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print(len(fruit_list))
    fruit_list.append('mango')
    print(fruit_list)
    for fruit in fruit_list:
        print(fruit)

if __name__ == '__main__':
    main()
    