import streamlit as st
import requests
import pandas as pd

# GANTI DENGAN PUNYAMU DARI STRAVA SETTINGS
CLIENT_ID = '198781'
CLIENT_SECRET = 'b1c82f5d0e9d964496766a89c98292b5a2ae5a91'
REDIRECT_URI = 'http://localhost:8501/'

st.set_page_config(page_title="PokeRun Analyzer", page_icon="⚡")

# --- CSS Estetik Gen Z ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { border-radius: 50px; background: linear-gradient(45deg, #FF4B4B, #FF9068); color: white; border: none; padding: 10px 24px; font-weight: bold; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    .card { padding: 30px; border-radius: 25px; background: white; border: 4px solid #000; box-shadow: 12px 12px 0px #000; margin: 20px 0; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏃‍♂️ PokeRun")
st.write("### Connect your Strava, find your inner Pokemon!")

# --- AUTH LOGIC ---
query_params = st.query_params

if "code" not in query_params:
    # Tombol Login
    auth_url = f"https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&approval_prompt=auto&scope=activity:read_all"
    st.markdown(f'<a href="{auth_url}" target="_self"><button style="width:100%; cursor:pointer; padding:15px; border-radius:15px; background-color:#FC4C02; color:white; border:none; font-weight:bold;">🔥 LOGIN WITH STRAVA</button></a>', unsafe_allow_html=True)
else:
    # Ambil Data Setelah Login Berhasil
    code = query_params["code"]
    
    # Tukar Code dengan Access Token
    token_response = requests.post("https://www.strava.com/oauth/token", data={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code'
    }).json()

    access_token = token_response.get('access_token')

    if access_token:
        # Ambil Aktivitas Lari Terakhir
        activities = requests.get(
            "https://www.strava.com/api/v3/athlete/activities",
            headers={'Authorization': f'Bearer {access_token}'},
            params={'per_page': 5}
        ).json()

        if activities:
            # Ambil rata-rata pace dari lari terakhir (m/s ke min/km)
            last_run = activities[0]
            avg_speed = last_run['average_speed'] # m/s
            pace_min_km = (1000 / avg_speed) / 60 if avg_speed > 0 else 0
            
            # --- Klasifikasi ---
            if pace_min_km < 5.0:
                pkmn, color, emoji = "Rapidash", "#FF4B4B", "🔥"
                desc = "Lari kamu kenceng banget! Kayak Rapidash yang kakinya api semua. Aura kompetitif kamu kerasa sampe sini, no cap!"
            elif pace_min_km < 7.5:
                pkmn, color, emoji = "Pikachu", "#FDE047", "⚡"
                desc = "Energik parah! Kamu lari dengan penuh keceriaan. Konsisten dan selalu jadi penyemangat buat pelari lain!"
            else:
                pkmn, color, emoji = "Slowpoke", "#FDA4AF", "🌸"
                desc = "Chill abis. Kamu lari buat nikmatin vibes, bukan buat dikejar target. Yang penting gerak dan tetep slay!"

           # ... kode sebelumnya ...
            st.markdown(f"""
                <div class="card">
                    <h2 style='color:{color};'>You are {pkmn}! {emoji}</h2>
                    <hr>
                    <p style='font-size:1.1em;'><b>Recent Pace:</b> {pace_min_km:.2f} min/km</p>
                    <p style='font-style: italic;'>"{desc}"</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.balloons() # <--- Ganti ini dari st.confetti()
        else:
            st.warning("Belum ada data lari di akun Strava kamu nih. Yuk lari dulu!")
