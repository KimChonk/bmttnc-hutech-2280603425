def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def mds_hash(message):
    # Khởi tạo các biến ban đầu
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    # Liên kết xử lý từng block
    original_length = len(message)
    message += b'\x80'
    while len(message) % 64 != 56:
        message += b'\x00'

    message += original_length.to_bytes(8, 'little')

    # Chia thành các block 512-bit
    for i in range(0, len(message), 64):
        block = message[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]

        # Vòng lặp chính của thuật toán MD5
        aa, bb, cc, dd = a, b, c, d

        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5*j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3*j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7*j) % 16

            temp = b + left_rotate((a + f + 0x5A827999 + words[g]) & 0xFFFFFFFF, 3)
            a, b, c, d = d, temp & 0xFFFFFFFF, b, c

        a = (a + aa) & 0xFFFFFFFF
        b = (b + bb) & 0xFFFFFFFF
        c = (c + cc) & 0xFFFFFFFF
        d = (d + dd) & 0xFFFFFFFF

    return format(a, '08x') + format(b, '08x') + format(c, '08x') + format(d, '08x')

# Test the implementation
input_string = "Hello, World!"
print(mds_hash(input_string.encode()))
