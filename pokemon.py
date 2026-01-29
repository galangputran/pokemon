Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import streamlit as st
import pandas as pd

# Setup Page Config untuk tampilan ala Gen Z
st.set_page_config(page_title="PokeRun: What's Your Runner Type?", page_icon="🏃‍♂️", layout="centered")

# Custom CSS untuk tampilan lebih "Clean & Bold"
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    .pokemon-card {
        padding: 20px;
        border-radius: 15px;
        background: white;
        box-shadow: 10px 10px 0px #000000;
        border: 2px solid #000;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.title("⚡ PokeRun Analyzer")
st.subheader("Are you a Swift Rapidash or a Chill Slowpoke?")
st.write("Connect your Strava and let's see your inner Pokemon spirit!")

# --- Logic Klasifikasi ---
def classify_runner(avg_pace, frequency):
    # Logika sederhana: pace dalam menit/km
    if avg_pace < 5.0:
        return {
            "name": "Rapidash",
            "desc": "Gila! Kamu kenceng banget. Aspal sampe kebakar kalo kamu lewat. Definisi 'Fast & Furious' di dunia nyata!",
            "vibe": "Elite Runner Energy 🦄🔥"
        }
    elif 5.0 <= avg_pace < 7.0:
        if frequency > 3:
            return {
                "name": "Pikachu",
                "desc": "Energik dan konsisten! Kamu rajin banget lari dan selalu ceria di setiap kilometer. Main Character Energy!",
                "vibe": "Social Runner / High Spirits ⚡️"
...             }
...         else:
...             return {
...                 "name": "Bulbasaur",
...                 "desc": "Stabil dan chill. Kamu lari buat kesehatan mental dan enjoy the view. Humble tapi pasti.",
...                 "vibe": "Consistent & Balanced 🌱"
...             }
...     else:
...         return {
...             "name": "Slowpoke",
...             "desc": "Pace bukan segalanya, yang penting gerak! Kamu tipe yang lari sambil mikirin mau makan apa abis ini. Relatable banget.",
...             "vibe": "Chill & Relaxed 🌸"
...         }
... 
... # --- Mock UI untuk Demo ---
... # (Di versi asli, ini akan dihubungkan dengan OAuth Strava)
... with st.expander("🔗 Connect to Strava"):
...     st.info("Input data manual untuk preview (Fitur API sedang dalam pengembangan)")
...     pace_input = st.slider("Average Pace (min/km)", 3.0, 12.0, 6.5)
...     freq_input = st.number_input("Runs per week", 1, 7, 3)
... 
... if st.button("REVEAL MY POKEMON"):
...     result = classify_runner(pace_input, freq_input)
...     
...     st.markdown(f"""
...         <div class="pokemon-card">
...             <h1 style='color: #FF4B4B;'>You are {result['name']}!</h1>
...             <p style='font-size: 1.2em; font-weight: bold;'>{result['vibe']}</p>
...             <p>{result['desc']}</p>
...         </div>
...     """, unsafe_allow_html=True)
...     
...     st.balloons()
... 
... # --- Footer ---
... st.markdown("---")
