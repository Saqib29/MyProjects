
pass_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%',
        '^', '&', '*', '+', '/' ,'-', '`', '~', '_']

def check_password(password):
    guess_password = ""
    if  password == "":
        return "Empty password!"
    for char in password:
        for letter in pass_chars:
            if char == letter:
                guess_password = guess_password + str(letter)
                break
        
    return guess_password
