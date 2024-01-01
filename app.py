"""
Flask app for key generation, encryption, and decryption.
"""

from flask import Flask, render_template, request, jsonify
from cryptography.fernet import InvalidToken
from core import generate_key, encrypt_message, decrypt_message

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index page.
    """
    return render_template('index.html')

@app.route('/generate_key', methods=['GET'])
def gen_key():
    """
    Generate a key and return it.
    """
    try:
        key = generate_key()
        return key.decode()
    except ValueError as error:
        return jsonify({'error': str(error)}), 500

@app.route('/encrypt', methods=['POST'])
def encrypt():
    """
    Encrypt the provided text using the key.
    """
    try:
        data = request.get_json()
        text = data['text']
        key = data['key']
        encrypted_text = encrypt_message(text, key.encode())
        return encrypted_text.decode()
    except ValueError as error:
        return jsonify({'error': str(error)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    """
    Decrypt the provided text using the key.
    """
    try:
        data = request.get_json()
        text = data['text']
        key = data['key']
        decrypted_text = decrypt_message(text.encode(), key.encode())
        return decrypted_text
    except ValueError as error:
        return jsonify({'error': str(error)}), 500
    except InvalidToken as error:
        return jsonify({'error': f'Invalid encoded string {str(error)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
