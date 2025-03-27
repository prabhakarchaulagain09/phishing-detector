import urllib.parse
import re
import socket
import ssl
import whois
from datetime import datetime
import requests
from urllib.parse import urlparse
import ipaddress
import numpy as np
import pandas as pd
import joblib
import warnings

# Feature extractor
class URLFeatureExtractor:
    def __init__(self, url):
        self.url = url
        self.parsed_url = urlparse(url)
        
    def _get_domain_info(self):
        try:
            domain = self.parsed_url.netloc
            
            # Check if domain is an IP address
            try:
                ipaddress.ip_address(domain)
                is_ip = 1
            except ValueError:
                is_ip = 0
            
            # Domain registration length
            try:
                domain_info = whois.whois(domain)
                creation_date = domain_info.creation_date
                if isinstance(creation_date, list):
                    creation_date = creation_date[0]
                
                if creation_date and isinstance(creation_date, datetime):
                    domain_age = max(0, (datetime.now() - creation_date).days)
                else:
                    domain_age = 0
            except Exception:
                domain_age = 0
            
            return is_ip, domain_age
        except Exception:
            return 0, 0

    def extract_features(self):
        features = {}
        
        feature_names = [
            'having_IP_Address', 'URL_Length', 'Shortining_Service',
            'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix',
            'having_Sub_Domain', 'SSLfinal_State', 'Domain_registeration_length',
            'Favicon', 'port', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor',
            'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL',
            'Redirect', 'on_mouseover', 'RightClick', 'popUpWidnow', 'Iframe',
            'age_of_domain', 'DNSRecord', 'web_traffic', 'Page_Rank',
            'Google_Index', 'Links_pointing_to_page', 'Statistical_report'
        ]
        
        for feature in feature_names:
            features[feature] = 0
        
        # 1. URL Length
        features['URL_Length'] = len(self.url)
        
        # 2. Having IP Address
        features['having_IP_Address'], features['age_of_domain'] = self._get_domain_info()
        features['Domain_registeration_length'] = features['age_of_domain']
        
        # 3. Shortening Service
        shortening_services = [
            'bit.ly', 'goo.gl', 't.co', 'tinyurl', 'ow.ly', 
            'tiny.cc', 'bc.vc', 'rb.gy', 'is.gd', 'cutt.ly'
        ]
        features['Shortining_Service'] = int(any(
            service in self.url.lower() for service in shortening_services
        ))
        
        # 4. Having @ Symbol
        features['having_At_Symbol'] = int('@' in self.url)
        
        # 5. Double Slash Redirecting
        features['double_slash_redirecting'] = int(self.url.count('//') > 1)
        
        # 6. Prefix/Suffix
        def has_prefix_suffix(domain):
            return int(bool(re.search(r'[-_]', domain)))
        
        features['Prefix_Suffix'] = has_prefix_suffix(self.parsed_url.netloc)
        
        # 7. Subdomain
        subdomain_count = len(self.parsed_url.netloc.split('.')) - 2
        features['having_Sub_Domain'] = int(subdomain_count > 1)
        
        # 8. SSL Final State
        try:
            hostname = self.parsed_url.netloc
            context = ssl.create_default_context()
            with socket.create_connection((hostname, 443), timeout=3) as sock:
                with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
                    secure_sock.getpeercert()
                    features['SSLfinal_State'] = 1
        except Exception:
            features['SSLfinal_State'] = 0
        
        # 9. HTTPS Token
        features['HTTPS_token'] = int('https' in self.url.lower())
        
        # 10. Web Traffic (basic check)
        try:
            response = requests.get(f"https://www.alexa.com/siteinfo/{self.parsed_url.netloc}", timeout=3)
            features['web_traffic'] = int(response.status_code == 200)
        except:
            features['web_traffic'] = 0
        
        # 11. Google Indexing
        try:
            google_search = f"https://www.google.com/search?q=site:{self.parsed_url.netloc}"
            response = requests.get(google_search, timeout=3)
            features['Google_Index'] = int("did not match any documents" not in response.text)
        except:
            features['Google_Index'] = 0
        
        # Create DataFrame with predefined column order
        features_df = pd.DataFrame([features])
        features_df = features_df.reindex(columns=feature_names)
        
        return features_df

def check_url_phishing(url, model, feature_names=None):
    try:
        # Suppress specific warnings
        warnings.filterwarnings('ignore', category=UserWarning)
        
        # Extract features
        extractor = URLFeatureExtractor(url)
        features = extractor.extract_features()
        
        # Make predictions
        prediction = model.predict(features)
        prediction_proba = model.predict_proba(features)
        
        return {
            'is_phishing': bool(prediction[0]),
            'phishing_probability': prediction_proba[0][1],
            'legitimate_probability': prediction_proba[0][0]
        }
    except Exception as e:
        print(f"Error analyzing URL: {e}")
        return None

if __name__ == "__main__":
    # Example usage for testing
    model = joblib.load('phishing_model.pkl')
    
    test_urls = [
        'http://suspicious-site.com',
        'https://www.legitimate-bank.com',
        'http://bit.ly/suspicious-link'
    ]
    
    for url in test_urls:
        result = check_url_phishing(url, model)
        if result:
            print(f"\nURL: {url}")
            print(f"Phishing: {result['is_phishing']}")
            print(f"Phishing Probability: {result['phishing_probability']:.2%}")
        else:
            print(f"\nURL: {url} - Analysis failed")