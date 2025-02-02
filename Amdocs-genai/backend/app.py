from flask import Flask, request, jsonify
from flask_cors import CORS
from routes.link_analysis import analyze_link
from routes.image_analysis import analyze_image
from routes.text_analysis import analyze_text

# Initialize Flask app
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for frontend communication
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the ClarifAI API Backend!"})

# --------------------
# Route for Link Analysis
# --------------------
@app.route('/analyze/link', methods=['POST'])
def link_endpoint():
    try:
        url = request.json.get('url')
        if not url:
            return jsonify({"error": "URL is required"}), 400

        result = analyze_link(url)
        return jsonify({"trust_score": result['trust_score'], "details": result['details']})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --------------------
# Route for Image Analysis
# --------------------
@app.route('/analyze/image', methods=['POST'])
def image_endpoint():
    try:
        image_file = request.files.get('file')
        if not image_file:
            return jsonify({"error": "Image file is required"}), 400

        result = analyze_image(image_file)
        return jsonify({"trust_score": result['trust_score'], "details": result['details']})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --------------------
# Route for Text Analysis
# --------------------
@app.route('/analyze/text', methods=['POST'])
def text_endpoint():
    try:
        text_data = request.json.get('text')
        if not text_data:
            return jsonify({"error": "Text data is required"}), 400

        result = analyze_text(text_data)
        return jsonify({"trust_score": result['trust_score'], "details": result['details']})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --------------------
# Combined Analysis Route
# --------------------
@app.route('/analyze/combined', methods=['POST'])
def combined_endpoint():
    """
    Handles the combined analysis for links, images, and text together.
    """
    try:
        url = request.json.get('url')
        text_data = request.json.get('text')
        image_file = request.files.get('file')

        result = {
            "link_score": analyze_link(url) if url else {"trust_score": 0, "details": "No link provided"},
            "text_score": analyze_text(text_data) if text_data else {"trust_score": 0, "details": "No text provided"},
            "image_score": analyze_image(image_file) if image_file else {"trust_score": 0, "details": "No image provided"}
        }

        # Calculate average trust score
        total_score = sum([result[key]['trust_score'] for key in result]) // 3

        return jsonify({"trust_score": total_score, "analysis_details": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
