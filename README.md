# 🕵️ Phishing URL Detector

## Overview
The **Phishing URL Detector** is a web application that leverages machine learning to analyze URLs and determine their likelihood of being phishing attempts. It provides real-time analysis and detailed insights into the characteristics of URLs, helping users identify potentially malicious websites.

## 🚀 Features
- **Web Interface**: User-friendly interface for entering and analyzing URLs.
- **Machine Learning-Powered**: Uses a trained model to classify URLs as phishing or legitimate.
- **Real-Time Analysis**: Provides phishing probability and detailed breakdown of URL features.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **Detailed Feedback**: Displays probabilities and reasons for classification.

## 🛠 Technologies Used
- **Backend**: Python, Flask
- **Frontend**: HTML, Tailwind CSS
- **Machine Learning**: Scikit-learn
- **Other Libraries**: NumPy, Pandas, Python-Whois, Requests

## 📂 Project Structure
```
phishing-detector/
│
├── app.py                     # Flask web application
├── url_feature_extractor.py   # Feature extraction logic for URLs
├── phishing_model.pkl         # Pre-trained machine learning model
├── requirements.txt           # Project dependencies
├── templates/
│   └── index.html             # Web interface template
└── README.md                  # Project documentation
```

## 🔧 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/phishing-url-detector.git
cd phishing-url-detector
```

### 2. Create a Virtual Environment
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

### 4. Add the Pre-Trained Model
Ensure the `phishing_model.pkl` file is in the root directory. If you don't have the model, you can train one using a dataset of phishing and legitimate URLs.

### 5. Run the Application
```bash
python app.py
```
Open your browser and navigate to `http://127.0.0.1:5000`.

## 📊 How It Works
1. Enter a URL in the input field on the web interface.
2. Click the "Check URL" button.
3. The application analyzes the URL and provides:
   - **Phishing Status**: Whether the URL is suspicious or legitimate.
   - **Phishing Probability**: Likelihood of the URL being a phishing attempt.
   - **Legitimate Probability**: Likelihood of the URL being safe.

## 🔬 Model Training
The machine learning model is trained on a dataset of phishing and legitimate URLs. It uses features such as:
- URL length
- Presence of IP address
- SSL certificate status
- Domain registration length
- Use of shortening services
- Subdomain count
- And more...

To train your own model, create a script (e.g., `train_model.py`) to preprocess the dataset, extract features, and train a classifier (e.g., Random Forest, Logistic Regression).

## ⚠️ Limitations
- The model's accuracy depends on the quality and size of the training dataset.
- It is not 100% foolproof and should be used as an aid, not a definitive security solution.
- Requires periodic retraining to stay updated with new phishing patterns.

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a pull request.

## 🔒 Security Notes
- Always verify URLs from trusted sources.
- This tool is designed to assist in identifying phishing URLs but is not a substitute for comprehensive security measures.
- Keep the machine learning model updated with recent data to maintain accuracy.

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙌 Acknowledgments
- **Scikit-learn**: For machine learning capabilities.
- **Flask**: For the web framework.
- **Tailwind CSS**: For responsive and modern UI design.
- **Python-Whois**: For domain information extraction.

---
Feel free to reach out with any questions or suggestions!