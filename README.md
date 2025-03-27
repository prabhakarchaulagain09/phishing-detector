# 🕵️ Phishing URL Detector

## Overview
This is a web application that uses machine learning to detect potentially malicious or phishing URLs. The application provides real-time analysis of URLs, giving users insights into the likelihood of a website being a phishing attempt.

## 🚀 Features
- Web interface for easy URL checking
- Machine learning-powered phishing detection
- Real-time probability scoring
- Responsive design
- Detailed analysis of URL characteristics

## 🛠 Technologies Used
- Python
- Flask
- Scikit-learn
- Tailwind CSS
- Machine Learning

## Prerequisites
- Python 3.7+
- pip
- Virtual environment (recommended)

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/phishing-url-detector.git
cd phishing-url-detector
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate Machine Learning Model
```bash
python train_model.py
```
This script creates a `phishing_model.pkl` file used for URL analysis.

## 🚀 Running the Application
```bash
python app.py
```
Navigate to `http://127.0.0.1:5000` in your web browser.

## 📊 How It Works
1. Enter a URL in the input field
2. Click "Check URL"
3. Receive analysis with:
   - Phishing status
   - Probability of being a phishing site
   - Probability of being legitimate

## 🔬 Model Training
The model is trained on various URL features:
- URL length
- Presence of IP address
- SSL certificate status
- Domain registration length
- Shortening service usage
- And more...

## ⚠️ Limitations
- Model accuracy depends on training data
- Not 100% foolproof
- Requires periodic retraining with new data

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 📦 Project Structure
```
phishing-url-detector/
│
├── app.py               # Flask web application
├── train_model.py       # Model training script
├── url_feature_extractor.py  # Feature extraction logic
├── phishing_model.pkl   # Trained machine learning model
├── requirements.txt     # Project dependencies
└── templates/
    └── index.html       # Web interface
```

## 🔒 Security Notes
- Always verify URLs from trusted sources
- This tool is an aid, not a definitive security solution
- Keep the model updated with recent phishing patterns

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](http://_vscodecontentref_/8) file for details.

## 🙌 Acknowledgments
- Scikit-learn for machine learning capabilities
- Flask for web framework
- Tailwind CSS for styling
```