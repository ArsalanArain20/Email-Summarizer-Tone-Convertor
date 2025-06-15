# Imports
import streamlit as st   
import sys
import os

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Importing the Main Logic
from main import Frontend_Email_Intent_Detector

# Main Page Layout
st.set_page_config(page_title="Email Intent Detection", page_icon="📬", layout="wide")
st.title("📧 Intent Detection 🌐")
user_input = st.text_area("Paste your email here:", height=300)

# For Displaying Ouput Structured Way on UI
def format_output_dict(title: str, output_obj: object):
    """
    Dynamically format and display key-value pairs in Streamlit.
    Handles any number of keys.
    """
    st.markdown(f"### {title}")  # Section title

    if hasattr(output_obj, 'model_dump'):
        output_dict = output_obj.model_dump()
    elif isinstance(output_obj, dict):
        output_dict = output_obj
    else:
        raise ValueError("Unsupported object type passed to formatter")

    # Iterate and format each key-value
    for key, value in output_dict.items():
        # Handle list values nicely
        if isinstance(value, list):
            value = ", ".join(str(v) for v in value)
        st.markdown(f"**{key.capitalize()}**: {value}")

if st.button("Intent Detector"):
    user_input = Frontend_Email_Intent_Detector(user_input)
    # Access each chain’s output separately
    intent_data = user_input['intent_data']
    action_data = user_input['action_data']

    format_output_dict("INTENT RESULT", intent_data)
    format_output_dict("ACTION RESULT", action_data) 