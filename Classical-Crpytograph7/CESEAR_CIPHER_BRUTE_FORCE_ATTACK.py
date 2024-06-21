import string


#CEASER CIPHER | SHIFT CIPHER USING PYTHON BY THE 1%

plain = string.ascii_lowercase

mapping = dict()
#whitespace_counter = 0


def assignment() -> dict:
    # Creating a Dictionary ie Alphabet:number mapping
    global mapping, plain
    counter = 0

    for letter in plain:
        mapping[letter] = "" # adding each letter to the Diction with Empty Values


    #Adding Numeric values to Each Key
    for key in mapping:
        mapping[key] = counter
        # print(mapping[key])
        if counter < 26:
            counter += 1
    return mapping

#function take a Value in range of 0-25 then return an alphabet corresponding

def Value_to_key(dict : dict, key_value) -> dict:
    for key, value in dict.items():

        if value == key_value:

            #print(key)
            return key

#Encryption Algorithm
def Encryption(plaintext, key=3) -> str.upper:
    #E(p, k) mode 26
    plaintext = plaintext.lower()
    cipher_text = ""

    #global white_space_counter;
    #white_space_counter = 0


    for char in plaintext:

        if char.isspace(): #==> Checking if if whitespace skip it
            continue

        if char.isnumeric():
            continue

        if char.isalpha(): #==> Sorting the code for only alphabets

            shift_key = (assignment()[char] + key) #==> Fetching the New shift Key

            shift_key = (shift_key % 26)


            #print(Value_to_key(assignment(), shift_key), shift_key)

            cipher_text = cipher_text+str(Value_to_key(assignment(), shift_key))

            #white_space_counter +=1
            #print("Plain_Text:", plaintext, "Cipher_Text:", cipher_text)
        else:
            print(char, "Cannot be Encrypted")



    return cipher_text.upper()


#Bruteforce Algorithms

def Bruteforce(cipher : str, key=3) -> str:
    cipher = cipher.lower()
    plain_text = ""
    for char in cipher:
        original_shift = assignment()[char] - key

        original_shift = (original_shift % 26)

        plain_text = plain_text+str(Value_to_key(assignment(), original_shift))


    return  plain_text


def main(text, key):
    #cipher_text = Encryption(text)

    plain_text = Bruteforce(text, key=key)

    #print("Plain_text:", plain_text)
    print("Trying key:", key, "Plain Text: ", plain_text)



if __name__ == "__main__":
    while True:
        """
        prompt = input("Enter Message: ")
        key = int(input("Enter Key: "))
        cipher_text = Encryption(prompt, key=key)
        print("Cipher Text: ", cipher_text)

        print("CESEAR CIPHER BRUTEFORCE ATTACK | 1%")

        cipher_text = "YPKKT"

        """
        cipher_text = input("Enter Cipher: ")
        for keys in range(26):
            main(cipher_text, key=keys)




