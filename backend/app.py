from flask import Flask, request, jsonify
from model import AIModel
import logging
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To handle CORS if the frontend is hosted elsewhere

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize the AI model
model_name = "facebook/bart-large-mnli"
ai_model = AIModel(model_name)

@app.route('/predict', methods=['POST'])
def predict():
    text = request.json.get('text')
    
    if not text:
        logging.error("No text provided")
        return jsonify({"error": "No text provided"}), 400
    
    logging.info(f"Received query: {text}")
    
    # Get prediction from the model
    prediction = ai_model.predict(text)
    
    if isinstance(prediction, dict) and 'intent' in prediction:
        logging.info(f"Prediction: {prediction}")
        return jsonify({
            "intent": prediction['intent'],
            "confidence": prediction.get('confidence', 0.0)
        })
    else:
        logging.error(f"Prediction failed or format not expected: {prediction}")
        return jsonify({"error": "Prediction failed or is not in expected format"}), 500

if __name__ == "__main__":
    app.run(debug=True)
