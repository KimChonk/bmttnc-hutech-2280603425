from flask import Flask,request,jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
app = Flask(__name__)
caesar_cipher = CaesarCipher()
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.caesar_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})
@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.caesar_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})
vigenere_cipher = VigenereCipher()
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = str(data['key'])
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})
@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = str(data['key'])
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})
railfence_cipher = RailFenceCipher()
@app.route('/railfence/encrypt',methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    cipher_text = railfence_cipher.railfence_encrypt(plain_text,key)
    return jsonify({'cipher_text':cipher_text})
@app.route('/railfence/decrypt',methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    cipher_text = data['cipher_text']
    key = int(data['key'])
    plain_text = railfence_cipher.railfence_decrypt(cipher_text,key)
    return jsonify({'plain_text':plain_text})
#main func
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)