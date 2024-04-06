from flask import Flask, request, jsonify
from datetime import datetime
app = Flask(__name__)

def analyze_transaction(transaction_data):
    # Implement fraud detection logic here
    rule_violated = []  # Placeholder for violated rules
    # Example logic:

    transaction_amount = float(transaction_data["transactionAmount"])
    card_balance = float(transaction_data["cardBalance"])
    locations = transaction_data["latitude"]

    if transaction_amount >= 300000 and card_balance * 0.7 <= transaction_amount:
        rule_violated.append("RULE-001")

   
    if len(locations) > 5 and transaction_amount >= 100000:
        rule_violated.append("RULE-002")
    # Add more rules here...
    return rule_violated

@app.route('/detect-fraud', methods=['POST'])
def detect_fraud():
    transaction_data = request.json
    rule_violated = analyze_transaction(transaction_data)
    if rule_violated:
        response = {
            "status": "ALERT",
            "ruleViolated": rule_violated,
            "timestamp": datetime.now().timestamp() # Replace with actual timestamp
        }
    else:
        response = {
            "status": "OK",
            "ruleViolated": [],
            "timestamp": datetime.now().timestamp()  #Replace with actual timestamp
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
