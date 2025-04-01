from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    text = input("Nhập chuỗi văn bản ").encode('utf-8')
    hashed_text = sha3(text)
    
    print("chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("mã băm SHA3-256:", hashed_text.hex())

if __name__ == "__main__":
    main()