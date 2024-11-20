
from flask import Flask, request, jsonify
import uuid
import math
from datetime import datetime

app = Flask(__name__)

# In-memory storage for receipts
receipts = {}

def calculate_points(receipt):

    points = 0

    # Rule 1: One point for every alphanumeric character in the retailer name
    retailer_name = receipt["retailer"]
    points += sum(c.isalnum() for c in retailer_name)

    # Rule 2: 50 points if the total is a round dollar amount
    total = float(receipt["total"])
    if total.is_integer():
        points += 50

    # Rule 3: 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # Rule 4: 5 points for every two items on the receipt
    items = receipt["items"]
    points += (len(items) // 2) * 5

    # Rule 5: Points based on item descriptions
    for item in items:
        description = item["shortDescription"].strip()
        if len(description) % 3 == 0:
            price = float(item["price"])
            points += math.ceil(price * 0.2)

    # Rule 6: 6 points if the day in the purchase date is odd
    purchase_date = datetime.strptime(receipt["purchaseDate"], "%Y-%m-%d")
    if purchase_date.day % 2 != 0:
        points += 6

    # Rule 7: 10 points if the time of purchase is between 2:00pm and 4:00pm
    purchase_time = datetime.strptime(receipt["purchaseTime"], "%H:%M")
    if 14 <= purchase_time.hour < 16:
        points += 10

    return points

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    try:
        receipt = request.json
        receipt_id = str(uuid.uuid4())
        points = calculate_points(receipt)
        receipts[receipt_id] = points
        return jsonify({"id": receipt_id}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    try:
        if receipt_id not in receipts:
            return jsonify({"error": "Receipt not found"}), 404
        return jsonify({"points": receipts[receipt_id]}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
