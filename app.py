from flask import Flask, request, jsonify
import os


app = Flask(__name__)

@app.route('/fulfillment', methods=['POST'])
def fulfillment():
    data = request.get_json()

    # Extract parameters from the request
    intent = data.get('queryResult', {}).get('intent', {}).get('displayName', '')
    parameters = data.get('queryResult', {}).get('parameters', {})

    # Perform fulfillment logic
    # For simplicity, let's just echo back the parameters
    response = {
        'fulfillmentText': f'You said: {intent}. Parameters: {parameters}',
    }

    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
