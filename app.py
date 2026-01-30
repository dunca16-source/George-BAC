import streamlit as st

# --- 1. CONFIGURARE ---
st.set_page_config(page_title="George-Bac Premium", page_icon="⚡", layout="wide")

if 'score' not in st.session_state: st.session_state.score = 0
if 'subscribed' not in st.session_state: st.session_state.subscribed = False
if 'page' not in st.session_state: st.session_state.page = "🏠 Acasă"

# --- 2. DESIGN ---
st.markdown("""
    <style>
    .highlight { color: #FF512F; font-weight: bold; }
    .citat { font-style: italic; color: #444; background: #fff5f2; padding: 20px; border-left: 5px solid #FF512F; display: block; margin: 20px 0; border-radius: 8px; line-height: 1.6; }
    .titlu-sectiune { color: #1a1a1a; font-family: 'serif'; border-bottom: 2px solid #FF512F; padding-bottom: 8px; margin-top: 35px; font-weight: bold; font-size: 1.6em; }
    .text-eseu { font-size: 1.15em; line-height: 1.8; text-align: justify; color: #2c3e50; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac")
    st.metric("Puncte George ⭐", st.session_state.score)
    menu = st.radio("Meniu", ["🏠 Acasă", "📚 Biblioteca", "💎 Upgrade PRO"])
    # Navigare Sidebar
    if menu != "📚 Biblioteca" and st.session_state.page not in ["Ion", "Enigma Otiliei"]:
        st.session_state.page = menu
    
    st.write("---")
    if st.text_input("🔓 Cod Admin", type="password") == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL deblocat!")

# --- 4. LOGICA PAGINILOR ---

# --- PAGINA: ACASĂ ---
if st.session_state.page == "🏠 Acasă":
    st.title("Bun venit la George-Bac ⚡")
    st.write("Pregătire interactivă pentru examenul de Bacalaureat.")
    if st.button("Deschide Biblioteca"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

# --- PAGINA: BIBLIOTECA ---
elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Biblioteca de Opere")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📖 Ion - Liviu Rebreanu"):
            st.session_state.page = "Ion"
            st.rerun()
    with col2:
        if st.button("📖 Enigma Otiliei - G. Călinescu"):
            st.session_state.page = "Enigma Otiliei"
            st.rerun()

# --- PAGINA: ION ---
elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion - Analiză & 20 Jocuri")
    t1, t2 = st.tabs(["📄 Eseu Detaliat", "🎮 Maraton 20 Jocuri"])
    
    with t1:
        st.markdown('<div class="titlu-sectiune">I. Introducere</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1920</b>, romanul <b>"Ion"</b> de Liviu Rebreanu este primul roman realist-obiectiv...</div>', unsafe_allow_html=True)
        # ... Restul eseului tău de la Ion ...
        if st.session_state.subscribed:
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud... Îl sărută cu patimă, ca pe o <b>ibovnică</b>.”</span>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("🔒 Cod ADMIN necesar!")
        else:
            # Jocurile 1-20 de la Ion (Compactate pentru cod)
            with st.expander("Nivelele 1-10: Acțiune și Simboluri"):
                if st.text_input("Citat (Nivel 8): Ca pe o...", key="ion8").lower().strip() in ["ibovnică", "ibovnica"]: st.success("Bravo!")
            with st.expander("Nivelele 11-20: Teoria Personajului"):
                if st.radio("Statut social Ion?", ["Bogat", "Sărăntoc"]) == "Sărăntoc": st.success("+10 pct")

# --- PAGINA: ENIGMA OTILIEI ---
elif st.session_state.page == "Enigma Otiliei":
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Enigma Otiliei - Analiză & 30 Jocuri")
    t1, t2 = st.tabs(["📄 Eseu Critic", "🎮 Maraton 30 Jocuri"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Realism Balzacian</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în 1938, romanul ilustrează viața burgheziei...</div>', unsafe_allow_html=True)
        # ... Restul eseului tău de la Enigma ...

    with t2:
        if not st.session_state.subscribed: st.error("🔒 Cod ADMIN necesar!")
        else:
            c1, c2, c3 = st.columns(3)
            with c1:
                with st.expander("1-10: Bazele"):
                    if st.selectbox("An?", ["1933", "1938"], key="en1") == "1938": st.success("+5")
            with c2:
                with st.expander("11-20: Modernism"):
                    if st.checkbox("Pluriperspectivism", key="en11"): st.success("+10")
            with c3:
                with st.expander("21-30: Personaje"):
                    if st.radio("Cine e avarul?", ["Felix", "Costache"], key="en21") == "Costache": st.success("+10")
                    if st.button("Finalizează Enigma"): st.balloons()

# --- PAGINA: UPGRADE ---
elif st.session_state.page == "💎 Upgrade PRO":
    st.title("💎 George-Bac PRO")
    st.write("Introdu codul de acces pentru a debloca toate cele 50+ de jocuri și eseurile complete.")
