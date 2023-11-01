# Shane Allicock

def encode(pswd):
# encode function
  encode_pass = ""
  for char in pswd:
# test cases
    if int(char) == 9:
      encode_char = 2
      encode_pass += str(encode_char)

    elif int(char) == 8:
      encode_char = 1
      encode_pass += str(encode_char)

    elif int(char) == 7:
      encode_char = 0
      encode_pass += str(encode_char)

# for vals 0 through 6
    else:
      encode_char = int(char) + 3
      encode_pass += str(encode_char)

  print("Your password has been encoded and stored")
  return encode_pass

def menu():
  while True:
# menu function
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")

    option = int(input("Please enter an option: "))

    if option == 1:
    # encode option
      pswd = (input("Please enter a password to encode: "))
      encoded = encode(pswd)
    elif option == 2:
      pass
    elif option == 3:
      break


if __name__ == "__main__":
  menu()
