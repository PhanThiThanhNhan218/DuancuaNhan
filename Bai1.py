def caesar_encrypt(plaintext, k):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha(): 
            shift = 65 if char.isupper() else 97  
            ciphertext += chr((ord(char) - shift + k) % 26 + shift)
        else:
            ciphertext += char  
    return ciphertext

# =============================
# Chạy chương trình
# =============================
if __name__ == "__main__":
    plaintext = input("Nhập tên (không dấu, không khoảng trắng): ")
    k = int(input("Nhập số STT của bạn: "))
    
    ciphertext = caesar_encrypt(plaintext, k)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)