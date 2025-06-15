# Imports
import sys
import os
import streamlit as st  
 
# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
# Import the function from the Main 
from main import Frontend_Email_Tone_Converter

# Main Page Layout
st.set_page_config(page_title="Email Tone Convertor", page_icon="🔁", layout="wide")
st.title("📧 Email Tone Converter 🎭")
user_input = st.text_area("Paste your email here:", height=200)
tone_Select = st.selectbox("Select the tone you want to convert to:", ["Formal", "Informal", "Casual", "Professional", "Friendly"])

if st.button("Tone Convert"):
    user_input = Frontend_Email_Tone_Converter(user_input,tone_Select)
    st.markdown("✅ Converted Email Response")
    st.write(user_input["response"])

    st.markdown("💡 Tone Suggestion Feedback")
    st.write(user_input["suggestion"])