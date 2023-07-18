'''
Cyara Meza
July 18, 2023
'''
def encoder(string):
    final = ''
    for char in string:
        char = int(char)
        result = char + 3
        result = str(result)
        final += result
    return final

menu = True
def main():
    while menu:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = int(input("Please enter an option:"))
        if option == 1:
            value = input("Please enter your password to encode:")
            result = encoder(value)
            print(f"Your password has been encoded and stored!")

        elif option == 2: #Where decoding function will be used
            print(f"The encoded password is {result}, and the original password is (value from decoding function).")

        elif option == 3:
            break

if __name__ == '__main__':
    main()