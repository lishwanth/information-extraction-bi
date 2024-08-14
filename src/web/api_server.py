from flask import Flask, request, jsonify
from src.model.pipeline import DataPipeline

app = Flask(__name__)
pipeline = DataPipeline()

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    file_path = f'./data/{file.filename}'
    file.save(file_path)
    predictions = pipeline.run_pipeline(file_path)
    return jsonify(predictions)

def start_server():
    app.run(host='0.0.0.0', port=5000)
