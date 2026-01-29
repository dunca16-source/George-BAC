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
        color: white; border-radius: 50px; font-weight: bold; border: none; transition: 0.3s; width: 100%;
    }
    .score-card { background: white; padding: 20px; border-radius: 20px; text-align: center; border-bottom: 5px solid #FF512F; box-shadow: 0px 10px 20px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR (NAVIGARE & ADMIN) ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center;'>⚡ George-Bac</h1>", unsafe_allow_html=True)
    st.markdown(f"""<div class="score-card">
            <span style="color: #666;">Puncte George</span><br>
            <span style="font-size: 2.5em; font-weight: bold; color: #FF512F;">{st.session_state.score}</span>
        </div>""", unsafe_allow_html=True)
    st.markdown("---")
    
    # Navigare
    menu_selection = st.radio("Meniu principal", ["🏠 Acasă", "📚 Biblioteca de Opere", "🏆 Clasament", "💎 Upgrade PRO"])
    
    # Sincronizare automată cu meniul, mai puțin când suntem în interiorul unei opere
    if st.session_state.page not in ["Ion"]:
        st.session_state.page = menu_selection

    st.markdown("---")
    # AICI ERA EROAREA (Linia 49 fixată):
    cod_admin = st.text_input("🔓 Cod Admin", type="password")
    if cod_admin == "george123":
        st.session_state.subscribed = True
        st.success("Mod Admin: ACTIVAT")

# --- 5. LOGICA DE PAGINI ---

if st.session_state.page == "🏠 Acasă":
    st.title("Pregătit să iei 10 la Bac? 🚀")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Învață literatura prin joc și logică, nu prin memorare mecanică.")
        if st.button("Deschide Biblioteca"):
            st.session_state.page = "📚 Biblioteca de Opere"
            st.rerun()
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/3407/3407154.png", width=200)

elif st.session_state.page == "📚 Biblioteca de Opere":
    st.title("📚 Biblioteca George-Bac")
    col_ion, col_baltag, col_scrisoarea = st.columns(3)
    with col_ion:
        st.subheader("Ion")
        st.caption("Liviu Rebreanu")
        if st.button("Studiază Ion"):
            st.session_state.page = "Ion"
            st.rerun()
    with col_baltag:
        st.subheader("Baltagul")
        st.caption("Mihail Sadoveanu")
        st.button("În curând...", disabled=True)

elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca de Opere"
        st.rerun()
    
    st.title("📖 Ion – Liviu Rebreanu")
    col_eseu, col_quiz = st.columns([2, 1])

    with col_eseu:
        with st.expander("📌 1. Încadrare și Context", expanded=True):
            st.write("Roman realist-obiectiv din 1920. Narator omniscient, perspectivă 'dindărăt'.")
        
        if st.session_state.subscribed:
            with st.expander("🎭 2. Tema și Episoadele", expanded=True):
                st.write("**Tema:** Pământul și Iubirea. Episoade: Hora și Sărutarea pământului.")
            with st.expander("🏗️ 3. Structură", expanded=True):
                st.write("**Circularitate:** Drumul de la început și final încadrează satul Pripas.")
                
        else:
            st.info("🔒 Secțiunile 2 și 3 sunt blocate pentru PRO.")

    with col_quiz:
        st.subheader("🏆 Quiz")
        raspuns = st.radio("Cine e rivalul lui Ion?", ["Vasile Baciu", "George Bulbuc", "Florica"], index=None)
        if st.button("Verifică"):
            if raspuns == "George Bulbuc":
                st.success("Corect! +20 puncte"); st.session_state.score += 20
            else:
                st.error("Greșit!"); st.session_state.score = max(0, st.session_state.score - 5)

elif st.session_state.page == "🏆 Clasament":
    st.title("🏆 Clasament")
    st.table({"Elev": ["Andrei", "Elena", "Tu"], "Scor": [500, 420, st.session_state.score]})

elif st.session_state.page == "💎 Upgrade PRO":
    st.title("💎 George-Bac PRO")
    if st.button("Activează varianta completă"):
        st.session_state.subscribed = True
        st.balloons()
        st.rerun()
