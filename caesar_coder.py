def caesar(text, shift):
    if shift < 1 or shift > 25:
        return("Shift must be between 1 and 25")

    alphabet ='abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet , shifted_alphabet)
    return text.translate(translation_table)
 


def non_caesar(code,shift):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    deshiftred_alphabet=alphabet[shift:]+alphabet[:shift]
    solution_table=str.maketrans(deshiftred_alphabet,alphabet)
    return code.translate(solution_table)

message=input("Enter the message you want to encrypt: ")
coded=caesar(message,4)
print('your coded message is: ', coded)
decoded=non_caesar(coded,4)
print('your decoded message is: ', decoded)
