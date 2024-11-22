import streamlit as st
from supabase import create_client, Client
import time

# Supabase configuration
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_description_by_id(record_id):
    """
    Fetches the description column from the llmResult table by ID.
    """
    try:
        response = supabase.table("llmResult").select("description").eq("resultId", record_id).execute()
        if response.data:
            return response.data[0]["description"]
        else:
            return None
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

def stream_text(text):
    """
    Streams text character by character.
    """
    streamed_text = st.empty()  # Create a placeholder for dynamic text updates
    current_text = ""
    for char in text:
        current_text += char
        streamed_text.markdown(f"**{current_text}**")  # Update text dynamically
        time.sleep(0.05)  # Add delay for streaming effect

st.title("Route Sense")

query_params = st.query_params
record_id = query_params.get("id", "")
description = fetch_description_by_id(record_id)
st.markdown(description)
