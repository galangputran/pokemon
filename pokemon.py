import streamlit as st
import requests

# --- CONFIG & STYLING ---
st.set_page_config(page_title="PokeRun", page_icon="⚡", layout="centered")

# CSS untuk estetika Modern & Minimalist
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #ffffff;
    }

    /* Card container */
    .hero-card {
        padding: 40px;
        border-radius: 24px;
        background: #fdfdfd;
        border: 1px solid #eee;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
        margin-top: 50px;
    }

    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: -webkit-linear-gradient(#FF4B4B, #FF9068);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    .sub-title {
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }

    /* Button Styling */
    .strava-btn {
        display: inline-block;
        background-color: #FC4C02;
        color: white !important;
        padding: 14px 32px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 700;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    
    .strava-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(252, 76, 2, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC ---
CLIENT_ID = 'ISI_ID_KAMU'
CLIENT_SECRET = 'ISI_SECRET_KAMU'
REDIRECT_URI = 'http://localhost:8501/'

# Mengambil parameter 'code' dari URL
query_params = st.query_params

# --- UI DISPLAY ---
if "code" not in query_params:
    # TAMPILAN AWAL (ELEGAN & SIMPLE)
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown(f"""
            <div class="hero-card">
                <p style="font-size: 3rem;">🏃‍♂️</p>
                <h1 class="main-title">PokeRun</h1>
                <p class="sub-title">Discover your inner Pokemon based on your Strava performance.</p>
                <div style="margin: 40px 0;">
                    <a href="https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&api_scope=activity:read_all&response_type=code&redirect_uri={REDIRECT_URI}&approval_prompt=auto&scope=activity:read_all" 
                       class="strava-btn">
                        Connect Strava Account
                    </a>
                </div>
                <p style="color: #999; font-size: 0.8rem;">Safe & Secure with Strava API</p>
            </div>
        """, unsafe_allow_html=True)

else:
    # TAMPILAN HASIL (SETELAH LOGIN)
    code = query_params["code"]
    
    # (Logika tukar token & ambil data sama seperti sebelumnya...)
    # Disini kamu bisa pasang hasil karakter Pokemon-nya
    st.success("Connected! Analyzing your runs...")
    st.balloons()
