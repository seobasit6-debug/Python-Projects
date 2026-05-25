def get_ascii_art():
    print("""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"      "" ""     `Y8 a8P_____88 I8[      "" ""     `Y8 88P'   "Y8 
8b          ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88         
"8a,    ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88         
 `"Ybbd8"'  `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88         

 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,  ,adPPYba, 8b,dPPYba,  
a8"      "" 88 88P'    "8a 88P'   "Y8 a8P_____88 88P'   "Y8 
8b          88 88       d8 88         8PP""""""" 88         
"8a,    ,aa 88 88b,   ,a8" 88         "8b,   ,aa 88         
 `"Ybbd8"'  88 88`YbbdP"'  88          `"Ybbd8"' 88         
               88                                             
               88                                             
""")


def caesar_encode(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def caesar_decode(message, shift):
    return caesar_encode(message, -shift)


def main():
    get_ascii_art()

    while True:
        action = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").strip().lower()

        if action not in ('encode', 'decode'):
            print("Invalid option. Please type 'encode' or 'decode'.")
            continue

        message = input("Type your message: ")

        try:
            shift = int(input("Type the shift number: "))
        except ValueError:
            print("Invalid shift number. Please enter an integer.")
            continue

        if action == 'encode':
            result = caesar_encode(message, shift)
            print(f"Here's the encoded result: {result}")
        else:
            result = caesar_decode(message, shift)
            print(f"Here's the decoded result: {result}")

        again = input("Type 'yes' if you want to go again. Otherwise type 'no': ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()