import streamlit as st

# --- CONFIGURARE PAGINĂ ---
st.set_page_config(page_title="George-Bac", page_icon="⚡", layout="wide")

# --- DESIGN PREMIUM (CSS AVANSAT) ---
st.markdown("""
    <style>
    /* Fundalul general */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Cardurile pentru Eseu */
    .stExpander {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 15px !important;
        border: none !important;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 10px;
    }
    
    /* Butoanele de acțiune */
    div.stButton > button {
        background: linear-gradient(90deg, #FF512F 0%, #DD2476 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 50px;
        font-weight: bold;
        transition: 0.3s;
        box-shadow: 0px 4px 10px rgba(221, 36, 118, 0.3);
    }
    
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 15px rgba(221, 36, 118, 0.4);
    }
    
    /* Caseta de Scor */
    .score-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        text-align: center;
        border-bottom: 5px solid #FF512F;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.05);
    }
    
    /* Titluri cu gradient */
    .main-title {
        font-family: 'Helvetica Neue', sans-serif;
        background: -webkit-linear-gradient(#333, #666);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        font-weight: 800;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGICĂ SCOR ---
if 'score' not in st.session_state:
    st.session_state.score = 0

# --- SIDEBAR DESIGN ---
with st.sidebar:
    cod_secret = st.text_input("Cod Admin", type="password")
    if cod_secret == "george123": # Poți pune orice parolă vrei
        st.session_state.subscribed = True
        st.success("Mod Admin Activat!")
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>⚡ George-Bac</h1>", unsafe_allow_html=True)
    st.markdown(f"""
        <div class="score-card">
            <span style="font-size: 0.9em; color: #666;">Puncte Acumulate</span><br>
            <span style="font-size: 2.5em; font-weight: bold; color: #FF512F;">{st.session_state.score}</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("Meniu principal", ["🏠 Acasă", "📚 Biblioteca de Opere", "🏆 Clasament", "💎 Upgrade PRO"])

# --- PAGINA ACASĂ ---
if menu == "🏠 Acasă":
    st.markdown("<h1 class='main-title'>Pregătit să iei 10?</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### De ce George-Bac?
        * **Nu tocești:** Înveți prin jocuri și scheme logice.
        * **Structură fixă:** Exact ce cer corectorii la examen.
        * **Puncte George:** Adună puncte și deblochează premii.
        """)
        if st.button("🚀 Începe cu prima operă"):
            st.info("Alege 'Biblioteca de Opere' din stânga!")
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3407/3407154.png", width=200)

# --- PAGINA BIBLIOTECĂ (Exemplu Ion) ---
elif menu == "📚 Biblioteca de Opere":
    st.title("📚 Biblioteca George-Bac")
    
    # Grid de opere
    col_ion, col_scrisoarea, col_baltagul = st.columns(3)
    
    with col_ion:
        st.subheader("Ion")
        st.caption("Liviu Rebreanu")
        if st.button("Studiază Ion"):
            st.session_state.current_page = "Ion"
            st.rerun()

    # (Aici urmează restul de opere în aceleași format)

# --- PAGINA UPGRADE ---
elif menu == "💎 Upgrade PRO":
    st.markdown("<h1 style='text-align: center;'>Deblochează tot potențialul 💎</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: white; padding: 30px; border-radius: 20px; text-align: center;">
        <h2>Abonament Full Access</h2>
        <p style="font-size: 1.5em; color: #FF512F;"><b>49 RON / lună</b></p>
        <ul style="text-align: left; display: inline-block;">
            <li>✅ Toate cele 17 eseuri detaliate</li>
            <li>✅ 50+ Jocuri interactive de memorare</li>
            <li>✅ Modele de Subiectul I și II rezolvate</li>
            <li>✅ Audio-Books pentru fiecare eseu</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.button("VREAU PRO ACUM")

