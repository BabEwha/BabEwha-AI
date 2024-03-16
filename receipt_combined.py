from flask import Flask, request, jsonify
from google.cloud import vision
import io
import os
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/ubuntu/github/BabEwha-ai/visionapitest-417306-78020a95f35a.json"
client = vision.ImageAnnotatorClient()

app = Flask(__name__)

@app.route('/receipt', methods=['POST'])
def detect_fee_discount():
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

    delivery = 0
    discount = 0
    fee = 0
    coupon = 0

    if texts:
        lines = texts[0].description.split('\n')

        for i, line in enumerate(lines):
            if '배달팁' in line:
                delivery_fee = lines[i+1].strip()
                if delivery_fee == '무료':
                    devliery = 0
                else:
                    delivery = int(''.join(filter(str.isdigit, delivery_fee)))
                if lines[i+2] != '총 결제금액':
                    if '%' in lines[i+2]:
                        match = re.search(r'(\d+)%', lines[i+2])
                        discount = (int(match.group(1)))
                    else:
                        discount = 0
                        coupon_discount = lines[i+3].strip()
                        coupon = int(''.join(filter(str.isdigit, coupon_discount)))
                        fee = delivery - coupon
                if lines[i+4] != '총 결제금액':
                    if '%' in lines[i+4]:
                        match = re.search(r'(\d+)%', lines[i+4])
                        discount = (int(match.group(1)))
                    else:
                        coupon_discount = lines[i+5].strip()
                        coupon = int(''.join(filter(str.isdigit, coupon_discount)))
                        fee = fee - coupon
    else:
        return jsonify({"message": "No Texts Found"}), 404

    return jsonify({"fee": fee, "discount": discount})

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false') == 'true'
    app.run(host="0.0.0.0", port=5001, debug=debug_mode)
