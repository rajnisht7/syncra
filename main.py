# linux_sync_server.py

from flask import Flask, request, jsonify
import os
import pyperclip
import notify2

app = Flask(__name__)

UPLOAD_FOLDER = os.path.expanduser("~/Downloads/from_android")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
notify2.init("AndroidSync")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if file:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        notify2.Notification("File Received", f"{file.filename} saved").show()
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "no file"}), 400

@app.route("/clipboard", methods=["POST"])
def receive_clipboard():
    data = request.json
    content = data.get("text", "")
    pyperclip.copy(content)
    notify2.Notification("Clipboard Synced", content).show()
    return jsonify({"status": "clipboard updated"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1732)
