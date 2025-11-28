import streamlit as st

# Set page config
st.set_page_config(page_title="AI Cold Email Generator", layout="centered")

# Custom CSS for style
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(135deg, #4169E1 0%, #00008B 100%);
        background-size: cover;
        color: white;
        font-family: 'Segoe UI', sans-serif;
        animation: fadeIn 1s ease-in;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        margin-top: -10px;
    }
    .subtitle {
        font-size: 24px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Page content
st.markdown('<div class="title">📧 Welcome to the AI Cold Email Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Craft tailored job or client outreach emails using powerful LLMs — free & automated.</div>', unsafe_allow_html=True)

st.markdown("➡️ Select **'Generate Email'** from the left sidebar to begin.")
st.markdown("💡 Tip: Upload your resume PDF and fill in job/company details for best results.")

# Optional branding image
st.image("https://cdn-icons-png.flaticon.com/512/561/561127.png", width=150)
