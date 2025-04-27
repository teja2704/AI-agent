from transformers import BartForSequenceClassification, BartTokenizer
import torch
import os
import torch.nn.functional as F

class AIModel:
    def __init__(self, model_name):
        # Model directory (ensure model is saved in this path)
        model_dir = r"C:\Users\patti\OneDrive\Desktop\AI-agent\models"

        # Ensure the model directory exists
        if not os.path.exists(model_dir):
            raise FileNotFoundError(f"Model '{model_name}' not found at {model_dir}")
        
        # Load the model and tokenizer from the directory
        self.model = BartForSequenceClassification.from_pretrained(model_dir)
        self.tokenizer = BartTokenizer.from_pretrained(model_dir)

    def predict(self, text):
        # Tokenize input text
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        
        # Make a prediction
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Softmax to get probabilities
        probabilities = F.softmax(outputs.logits, dim=1)
        
        # Get the prediction result (class with the highest probability)
        prediction = torch.argmax(probabilities, dim=1).item()
        
        # Get the confidence (probability of the predicted class)
        confidence = probabilities[0][prediction].item()
        
        return {"intent": prediction, "confidence": confidence}
