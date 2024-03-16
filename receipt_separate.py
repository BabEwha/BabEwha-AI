from flask import Flask, request, jsonify
from google.cloud import vision
import io
import os
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/ubuntu/github/BabEwha-ai/visionapitest-417306-78020a95f35a.json"
client = vision.ImageAnnotatorClient()

app = Flask(__name__)
@app.route('/receipt', methods=['POST'])
        
def detect_delivery_discount():
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
    coupon = coupon_1 = coupon_2 = 0

    lines = texts[0].description.split('\n')
    for i, line in enumerate(lines):
        if "배달팁" in line:
            delivery_line = lines[i + 1]
            if delivery_line == "무료":
                delivery = 0
            else:
                delivery = int(re.sub("[^0-9]", "", delivery_line))
            discount_line_1 = lines[i + 2]
            discount_line_2 = lines[i + 4]

            if discount_line_1 != '총 결제금액':
                if "%" in discount_line_1:
                    discount = int(re.search(r'\d+', discount_line_1).group())
                else:
                    coupon_line_1 = lines[i + 3]
                    coupon_1 = int(re.sub("[^0-9]", "", coupon_line_1))
                    coupon = - coupon_1
                        
            if discount_line_2 != '총 결제금액':                      
                if "%" in discount_line_2:
                    discount = int(re.search(r'\d+', discount_line_2).group())
                else:
                    coupon_line_2 = lines[i + 5]
                    coupon_2 = int(re.sub("[^0-9]", "", coupon_line_2))
                    coupon = coupon - coupon_2
                        
    return jsonify({"delivery": delivery, "coupon": coupon, "discount": discount})

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'false') == 'true'
    app.run(host="0.0.0.0", port=5002, debug=debug_mode)
