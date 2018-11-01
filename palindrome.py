user_input = input('Input what you want to check for palindromic properties: ')

def clean_text(text):
    # given a text, return the text with no punctuation.
    new_text = ""
    for character in text.lower():
        if character.isalpha():
            new_text = new_text + character
    return new_text

user_input = list(clean_text(user_input))

def is_palindrome(test):
    print(test)
    if test[0] != test[-1]:
        return False
    elif len(test) == 0:
        return True
    elif len(test) > 1:
        is_palindrome(test[0:-1])
        return True

if is_palindrome(user_input) == True:
    print('is a palindrome')
else:
    print("is not a palindrome")
