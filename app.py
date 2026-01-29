import streamlit as st

# --- 1. CONFIGURARE PAGINĂ ---
st.set_page_config(page_title="George-Bac", page_icon="⚡", layout="wide")

# --- 2. INITIALIZARE VARIABILE (SESSION STATE) ---
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'subscribed' not in st.session_state:
    st.session_state.subscribed = False
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Acasă"

# --- 3. DESIGN PREMIUM (CSS) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    .stExpander { background-color: white !important; border-radius: 15px !important; box-shadow: 0px 4px 15px rgba(0,0,0,0.05); border: none !important; margin-bottom: 10px; }
    div.stButton > button { 
        background: linear-gradient(90deg, #FF512F 0%, #DD2476 100%); 
        color: white; border-radius: 50px; font-weight: bold; border: none; transition: 0.3s;
    }
    div.stButton > button:hover { transform: scale(1.02); box-shadow: 0px 4px 15px rgba(221, 36, 118, 0.3); }
    .score-card { background: white; padding: 20px; border-radius: 20px; text-align: center; border-bottom: 5px solid #FF512F; box-shadow: 0px 10px 20px rgba(0,0,0,0.05); }
    .main-title { font-size: 3em; font-weight: 800; color: #333; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR (NAVIGARE & ADMIN) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>⚡ George-Bac</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="score-card">
            <span style="color: #666;">Puncte George</span><br>
            <span style="font-size: 2.5em; font-weight: bold; color: #FF512F;">{st.session_state.score}</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    # Navigare principală
    choice = st.radio("Meniu principal", ["🏠 Acasă", "📚 Biblioteca de Opere", "🏆 Clasament", "💎 Upgrade PRO"])
    
    # Sincronizare navigare
    if st.session_state.page not in ["Ion"]: # Paginile speciale rămân dacă sunt selectate
        st.session_state.page = choice

    st.markdown("---")
    cod_secret = st.text_input("🔓 Cod Admin", type="password")
    if cod
