from flask import Flask, jsonify, request

app = Flask(__name__)

# Route to return student number in JSON format
@app.route('/')
def get_student_number():
    student_number = "200501406" 
    response_data = {
        'student_number': student_number
    }
    return jsonify(response_data)

# Route for Dialogflow webhook
@app.route('/webhook', methods=['POST'])
def dialogflow_webhook():
    data = request.get_json()

    # Extract parameters from the request
    intent = data.get('queryResult', {}).get('intent', {}).get('displayName', '')
    parameters = data.get('queryResult', {}).get('parameters', {})

    # Perform fulfillment logic
    # For simplicity, let's just echo back the parameters
    response_text = f'You said: {intent}. Parameters: {parameters}'

    response_data = {
        'fulfillmentText': response_text,
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
