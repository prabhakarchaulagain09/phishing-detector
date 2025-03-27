from flask import Flask, render_template, request, jsonify
from url_feature_extractor import check_url_phishing
import joblib
import warnings
import traceback

# Suppress warnings
warnings.filterwarnings('ignore')

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
try:
    model = joblib.load('phishing_model.pkl')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/debug')
def debug():
    return "Flask is working correctly!"

@app.route('/check_url', methods=['POST'])
def check_url():
    # Check if model is loaded
    if model is None:
        return jsonify({
            'error': 'Machine learning model could not be loaded'
        }), 500
    
    # Get URL from request
    url = request.form.get('url')
    
    # Validate URL input
    if not url:
        return jsonify({
            'error': 'Please provide a valid URL'
        }), 400
    
    # Check URL for phishing
    try:
        result = check_url_phishing(url, model)
        
        if result is None:
            return jsonify({
                'error': 'Could not analyze the URL'
            }), 500
        
        return jsonify({
            'url': url,
            'is_phishing': result['is_phishing'],
            'phishing_probability': result['phishing_probability'],
            'legitimate_probability': result['legitimate_probability']
        })
    
    except Exception as e:
        # Print full traceback for debugging
        print(traceback.format_exc())
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True)