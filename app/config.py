import os
from dotenv import load_dotenv

# Load .env only for local development
load_dotenv()

def get_groq_api_key():
    """
    Returns the GROQ API key.

    Works with:
    - Local (.env)
    - Streamlit Cloud (Secrets -> Environment Variables)
    """

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY not found. "
            "Please add it to your .env file or Streamlit Secrets."
        )

    return api_key