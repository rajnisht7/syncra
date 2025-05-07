from flask import Flask, request, jsonify
import pyperclip

app = Flask(__name__)

@app.route('/clipboard', methods=['POST'])
def receive_clipboard():
    data = request.get_json()
    content = data.get('content', '')

    if content:
        pyperclip.copy(content)
        return jsonify({'status': 'clipboard updated'}), 200
    return jsonify({'error': 'No content provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1717)
