# Imports
import streamlit as st  
import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Import the function from Main
from main import Frontend_Email_Language_Detector

# Main Page Layout
st.set_page_config(page_title="Email Language Detector", page_icon="🈳", layout="wide")
st.title("📧 Email Language Detector 🔤")
user_input = st.text_area("Paste your email here:", height=300)

if st.button("Detect Language"):
    user_input = Frontend_Email_Language_Detector(user_input)
    st.subheader(user_input)

