from PIL import Image

def extract_lsb(image_path):
    """Trích xuất các bit thấp nhất từ ảnh (RGB)"""
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata())
    
    # Lấy bit cuối của từng kênh màu
    lsb_values = [(r & 1, g & 1, b & 1) for r, g, b in pixels]
    return lsb_values

def compare_images(original_path, stego_path):
    """So sánh ảnh gốc và ảnh nghi ngờ có giấu tin hay không"""
    lsb_original = extract_lsb(original_path)
    lsb_stego = extract_lsb(stego_path)
    
    # Đếm số pixel có sự thay đổi ở bit thấp nhất
    diff_count = sum(1 for o, s in zip(lsb_original, lsb_stego) if o != s)
    
    print(f"Số pixel có bit LSB thay đổi: {diff_count}")
    if diff_count > 0:
        print("🔍 Phát hiện sự khác biệt! Ảnh có thể đã bị giấu tin nhắn.")
    else:
        print("✅ Không phát hiện sự khác biệt rõ ràng. Ảnh có thể là nguyên bản.")

# 🔥 Chạy chương trình với ảnh mẫu
original_image = "C:/CODING/BMTT_NANG_CAO/bmttnc-hutech-2280603425/lab05/img-hidden/image.jpg"  # Thay bằng đường dẫn ảnh gốc
stego_image = "C:/CODING/BMTT_NANG_CAO/bmttnc-hutech-2280603425/lab05/img-hidden/encoded_image.png"  # Thay bằng đường dẫn ảnh nghi ngờ
compare_images(original_image, stego_image)
