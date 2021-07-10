alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type shift alphabet number:\n"))

def encrypt(text, shift):
    # проверяем, выходит ли сдвиг за рамки списка.
    if shift > len(alphabet) - 1:
        # делим на размер списка, чтобы получить сдвиг в пределах списка
        shift = shift % len(alphabet)
    en_message = ""
    for letter in text:
        index = alphabet.index(letter)+shift
        # проверяем, выходит ли индекс за рамки списка
        if index > len(alphabet) - 1:
            # делим на размер списка, чтобы получить индекс в пределах списка
            index = index % len(alphabet)
        en_message += alphabet[index]
    return en_message

def decrypt(text, shift):
    # проверяем, выходит ли сдвиг за рамки списка.
    if shift > len(alphabet) - 1:
        # делим на размер списка, чтобы получить сдвиг в пределах списка
        shift = shift % len(alphabet)
    de_message = ""
    for letter in text:
        index = alphabet.index(letter)-shift
        # НЕОБЯЗАТЕЛЬНЫЙ код, который делает индекс в пределах списка, если он упал ниже 0, после вычисления индекса
        #if index < 0:
        #   index = index + len(alphabet)
        # Python отрицательные значения индекса считает с конца списка, так что тут манипуляции не нужны
        de_message += alphabet[index]
    return de_message

if direction == "encode":
    en = encrypt(text, shift)
    print(en)
elif direction == "decode":
    de = decrypt(text, shift)
    print(de)
else:
    print("I don't understand it...")