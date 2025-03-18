import hashlib

def blake2b(message):
    blake2b_hash = hashlib.blake2b(digest_size=64)
    blake2b_hash.update(message)
    return blake2b_hash.digest()

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed_text = blake2b(text)
    
    print("chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("mã băm BLAKE2b:", hashed_text.hex())

if __name__ == "__main__":
    main()