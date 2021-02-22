alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l" ,"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l" ,"m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("암호화를 원하면 'encode', 복호화를 원하면 'decode'를 입력하세요: \n").lower()
text = input("원하는 텍스트를 입력하세요: \n")
# caesar_cipher.py

shift = int(input("원하는 이동량을 입력하세요: \n"))

def encode(plain_text, shift_amount):
    """암호화"""
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    return cipher_text

def decode(cipher_text, shift_amount):
    """복호화"""
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            cipher_text += alphabet[new_position]
        else:
            plain_text += letter
    return plain_text

def cipher(start_text, shift_amount, shift_direction):
    """카이사르 암호"""
    shift_amount = shift_amount % 26

    if shift_direction == "encode":
        result = encode(start_text, shift_amount)
    elif shift_direction == "decode":
        result = decode(start_text, shift_amount)

    print("결과:", result)



cipher(text, shift, direction)
