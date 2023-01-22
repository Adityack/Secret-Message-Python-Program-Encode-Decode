#hey this is aditya
import random

def code(word):
    if len(word) >= 3:
        first_letter = word[0]
        new_word = word[1:] + first_letter
        random_chars = ''.join(random.choices(list('abcdefghijklmnopqrstuvwxyz'), k=6))
        return random_chars[:3] + new_word + random_chars[3:]
    else:
        return word[::-1]

def decode(word):
    if len(word) < 3:
        return word[::-1]
    else:
        new_word = word[3:-3]
        last_letter = new_word[-1]
        return last_letter + new_word[:-1]

# main function
def main():
    operation = input("Enter 'c' for coding or 'd' for decoding: ")
    message = input("Enter your Precious message: ")
    words = message.split()
    coded_message = ' '.join([code(word) if operation == 'c' else decode(word) for word in words])
    print("Your coded/decoded message is: " + coded_message)

# run the main function
if __name__ == '__main__':
    main()
#Follow me on https://github.com/Adityack 😘
#Subscribe for more https://youtube.com/@toi-us 😎
