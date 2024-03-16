from flask import Flask, request, jsonify
from google.cloud import vision
import io
import os
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/ubuntu/github/BabEwha-ai/visionapitest-417306-78020a95f35a.json"
client = vision.ImageAnnotatorClient()

app = Flask(__name__)

@app.route('/cart', methods=['POST'])
def detect_menu_price():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    content = file.read()

    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)

    if response.error.message:
        return jsonify({"error": response.error.message}), 500

    texts = response.text_annotations

    menu = []
    price = []

    if texts:
        lines = texts[0].description.split('\n')
        for i, line in enumerate(lines):
            if '가격 :' in line or '가격:' in line:
                menu_name = lines[i-1].strip()
                menu.append(menu_name)
            if '옵션변경' in line:
                price_info = lines[i-1].split(':')[1].strip()
                price_digits = ''.join(re.findall(r'[\d.]+', price_info))
                price.append(int(price_digits))
    else:
        return jsonify({"message": "No Texts Found"}), 404

    return jsonify({"menu": menu, "price": price})

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false') == 'true'
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
