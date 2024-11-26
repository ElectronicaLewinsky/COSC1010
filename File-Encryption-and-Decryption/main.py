#      .
#   .
#   . .
#    ...
#  \~~~~~/
#   \   /
#    \ /
#     V
#     | 
#     |
#   -----     
# Alice J Black 
# 2024NOV25
# File Encryption and Decryption Programming Project
# COSC 1010 NT
#
def encryption():
    # Assign "codes" to each letter of the alpabet and numbers for decryption
    codes_encrypt = {'!': 'A', '@': 'B', '#': 'C', '$': 'D', '%': 'E', '^': 'F', '&': 'G', '*': 'H', '(': 'I',
                     ')': 'J', '-': 'K', '_': 'L', '+': 'M', '=': 'N', '`': 'O', '~': 'P', '{': 'Q', '[': 'R',
                     '}': 'S', ']': 'T', ':': 'U', ';': 'V', '"': 'W', '<': 'X', '>': 'Y', '0': 'Z', '1': 'a',
                     '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', 'a': 'j',
                     'b': 'k', 'c': 'l', 'd': 'm', 'e': 'n', 'f': 'o', 'g': 'p', 'h': 'q', 'i': 'r', 'j': 's',
                     'k': 't', 'l': 'u', 'm': 'v', 'n': 'w', 'o': 'x', 'p': 'y', 'q': 'z', '/': '0', 'v': '1',
                     'z': '2', 'N': '3', 's': '4', 'G': '5', 'Q': '6', 'P': '7', '|': '8', 'Y': '9'}

# opens the file
    orig_file = open('/Users/main/Documents/COSC1010/COSC1010-main/File-Encryption-and-Decryption/text.txt', 'r')
    file_read = orig_file.read()  # reads the file
    orig_file.close()  # closes the encrypted file
# creates the encrypted file in write mode
    encrypt_file = open('/Users/main/Documents/COSC1010/COSC1010-main/File-Encryption-and-Decryption/encrypted.txt', 'w')

    for ch in file_read:  # characters in encrypted file
        if ch in codes_encrypt:
            encrypt_file.write(codes_encrypt[ch])
        else:
            encrypt_file.write(ch)

    encrypt_file.close()
    encrypt_file = open('/Users/main/Documents/COSC1010/COSC1010-main/File-Encryption-and-Decryption/encrypted.txt', 'r')
    file_read = encrypt_file.read()
    encrypt_file.close()
    codes_items = codes_encrypt.items()

    for ch in file_read:
        if not ch in codes_encrypt.values() or ch == '.' or ch == ',' or ch == '!':
            print(ch)
        else:
            for k, v in codes_items:
                if ch == v and ch != '.':
                    print(k, end='')


encryption()
