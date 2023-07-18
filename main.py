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


# Breanna Blackwood 18 July 2023
def decoder(password):
	decoded = []  # create empty list
    	for i in password:
        	new = int(i) - 3
        	if new < 0:
            		pos_new = new * (-1)  # will convert a neegative number into positve
            		decoded.append(str(pos_new))
        	else:
            		decoded.append(str(new))
    	dec = "". join(decoded)
    	return dec


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
# Breanna Blackwood 18 July 2023
			result = encoder(value)
			value2 = decoder(result)
			print(f"The encoded password is {result}, and the original password is {value2}.")
        	elif option == 3:
            		break

if __name__ == '__main__':
    main()
