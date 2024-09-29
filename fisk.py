from flask import Flask, render_template, request
from utils.api import upload_dataset, fine_tune_model  # Import functions from utils
from utils.models import get_completion  # Import completion function

app = Flask(__name__)
api_key = "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"  # Replace with your actual API token

@app.route("/")
def home():    
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file_path = "C:/Users/HP/Documents/FiskAI/Scraper.json"
    upload_response = upload_dataset(file_path, api_key)
    if "error" not in upload_response:
        dataset_id = upload_response.get("dataset_id")
        fine_tune_response = fine_tune_model(dataset_id, api_key)
        return fine_tune_response
    else:
        return upload_response

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')  
    response = get_completion(userText, api_key)  
    return response

if __name__ == "__main__":
    app.run(debug=True)
