import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift, direction):
    # проверяем, выходит ли сдвиг за рамки списка.
    if shift > len(alphabet) - 1:
        # делим на размер списка, чтобы получить сдвиг в пределах списка
        shift = shift % len(alphabet)
    if direction == "decode":
            shift *= -1
    message = ""
    for letter in text:
        index = alphabet.index(letter)+shift
        # проверяем, выходит ли индекс за рамки списка
        if index > len(alphabet) - 1:
            # делим на размер списка, чтобы получить индекс в пределах списка
            index = index % len(alphabet)
        message += alphabet[index]
    return message

again = "yes"
print(caesar_art.logo)

while again == "yes" or again == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type shift alphabet number:\n"))
    print(caesar_cipher(text, shift, direction))
    again = input("Again?(yes/no)\n").lower()
print("Goodbye!\n")