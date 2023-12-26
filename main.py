class DragonCode:
    def __init__(self):
        self.encoding_key = {
            'a': '0',
            'b': '1',
            'c': '2',
            'd': '3',
            'e': '4',
            'f': '5',
            'g': '6',
            'h': '7',
            'i': '8',
            'j': '9',
            ' ': ' ',
        }

        self.decoding_key = {v: k for k, v in self.encoding_key.items()}

    def encode_message(self, message):
        encoded_message = ''.join([self.encoding_key.get(char.lower(), char) for char in message])
        return encoded_message

    def decode_message(self, encoded_message):
        decoded_message = ''.join([self.decoding_key.get(char, char) for char in encoded_message])
        return decoded_message

# Пример использования
dragon_coder = DragonCode()

# Кодирование сообщения
# original_message = "Dragon Code is fun!"
original_message = input()
encoded_message = dragon_coder.encode_message(original_message)
print("Original Message:", original_message)
print("Encoded Message:", encoded_message)

# Декодирование сообщения
decoded_message = dragon_coder.decode_message(encoded_message)
print("Decoded Message:", decoded_message)

