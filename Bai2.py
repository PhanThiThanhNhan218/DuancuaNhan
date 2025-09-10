def ceasar_encrypt(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            c = (ord(char) - base + k) % 26
            ciphertext += chr(c + base)
        else:
            ciphertext += char
    return ciphertext

# chạy
p = "PhanNhan"
k = 23  # STT của bạn

c = ceasar_encrypt(p, k)
print("Plaintext:", p)
print("Ciphertext:", c)