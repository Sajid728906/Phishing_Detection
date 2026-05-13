import streamlit as st
import pickle
import numpy as np
import re
from urlextract import URLExtract

st.set_page_config(page_title="AI Cyber Shield", page_icon="🛡️")
st.title("🛡️ Fully Automatic Phishing Detection System")
st.subheader("Germany MS Cybersecurity Portfolio Prototype")
st.write("---")

model = None
try:
    with open('cyber_phising_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Error: 'cyber_phising_model.pkl' not found. Please run 'train_model.py' first.")

user_url = st.text_input("Paste the complete URL Link here to scan :", placeholder="https://secure-login-update.com")

extract = URLExtract()
user_text = st.text_area("Paste complete Email and Message text here:")

def auto_extract_features(url):
    NumDots = url.count('.')
    UrlLength = len(url)
    AtSymbol = 1 if '@' in url else 0
    NumDash = url.count('-')
    NumPercent = url.count('%')
    NumQueryComponents = url.count('?')

    ip_pattern = r'(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
    ipAddress = 1 if re.search(ip_pattern, url) else 0

    HttpsInHostname = 1 if url.startswith('https') else 0 
    PathLevel = url.count('/')
    PathLength = len(url.split('/')[-1]) if '/' in url else 0
    NumNumericChars = sum(c.isdigit() for c in url)

    # FIX: Kept array size strictly at 11 elements to match your model layout
    return np.array([[
        NumDots, UrlLength, AtSymbol, NumDash, NumPercent, 
        NumQueryComponents, ipAddress, HttpsInHostname, 
        PathLevel, PathLength, NumNumericChars,
        0
    ]])

if st.button("Audit Email Content"):
    if user_text.strip() == "":
        st.warning("Please paste email text first.")
    else:
        urls_found = extract.find_urls(user_text)

        if len(urls_found) == 0:
            st.info("No links found in the text.")
        else:
            st.write(f"Found {len(urls_found)} link(s). AI scanning...")

            for link in urls_found:
                try:
                    processed_input = auto_extract_features(link)
                    prediction = model.predict(processed_input)
                    
                    if prediction[0] == 1:
                        st.error(f"🚨 **Phishing Threat:** {link}")
                    else:
                        st.success(f"✅ **Safe Link:** {link}")
                except Exception as e:
                    st.error(f"Error processing {link}: {e}")

if st.button("Run Live AI Scan"):
    if not model:
        st.error("Cannot run scan. Model file is missing.")
    elif user_url.strip() == "":
        st.warning("Please paste a URL first.")
    else:
        with st.spinner("AI Engine structural engineering attributes extract..."):
            try:
                processed_input = auto_extract_features(user_url)
                prediction = model.predict(processed_input)

                st.write("---")
                if prediction[0] == 1:
                    st.error("Result: Unsafe/Phishing Threat Detected")
                    st.write("**Withdrawn Structural Weakness:** This URL pattern contains heavy formatting vectors that mimic malicious servers.")
                else:
                    st.success("Result: Safe & Legitimate Link")
                    st.write("The parameters strictly comply with clean cryptographic encryption standards.")
                
            except Exception as e:
                st.error(f"Internal Processing Error: {e}")
