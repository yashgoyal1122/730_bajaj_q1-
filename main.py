from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        return jsonify({"operation_code": 1})

    if request.method == 'POST':
        data = request.json.get('data', [])
        file_b64 = request.json.get('file_b64', None)

        # Parse data array into numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

        # Process file if provided
        file_valid, file_mime_type, file_size_kb = False, None, None
        if file_b64:
            try:
                decoded_file = base64.b64decode(file_b64)
                file_size_kb = len(decoded_file) / 1024
                # Example for MIME type validation
                if b'%PDF' in decoded_file[:4]:
                    file_mime_type = 'application/pdf'
                elif b'\x89PNG' in decoded_file[:4]:
                    file_mime_type = 'image/png'
                file_valid = True
            except:
                pass

        response = {
            "is_success": True,
            "user_id": "yash_goyal_11052004",  # Replace with dynamic logic for user_id
            "email": "yg9532@srmist.edu.in",
            "roll_number": "RA2111003011730",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else [],
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }

        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
