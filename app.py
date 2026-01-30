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
    
    # Navigare automată din sidebar
    if menu == "🏠 Acasă": st.session_state.page = "🏠 Acasă"
    if menu == "📚 Biblioteca": st.session_state.page = "📚 Biblioteca"
    
    st.write("---")
    if st.text_input("🔓 Cod Admin", type="password") == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL deblocat!")

# --- 4. LOGICA PAGINILOR ---

# --- ACASĂ ---
if st.session_state.page == "🏠 Acasă":
    st.title("George-Bac ⚡")
    st.subheader("Platforma ta interactivă pentru nota 10 la Română")
    if st.button("Deschide Biblioteca"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

# --- BIBLIOTECA ---
elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Biblioteca de Opere")
    col1, col2 = st.columns(2)
    with col1:
        st.info("Realism Obiectiv")
        if st.button("📖 Ion - Liviu Rebreanu"):
            st.session_state.page = "Ion"
            st.rerun()
    with col2:
        st.info("Realism Balzacian / Modernism")
        if st.button("📖 Enigma Otiliei - G. Călinescu"):
            st.session_state.page = "Enigma Otiliei"
            st.rerun()

# --- PAGINA ION ---
elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion - Analiză & Maraton 20 Jocuri")
    t1, t2 = st.tabs(["📄 Eseu Detaliat", "🎮 Maraton 20 Niveluri"])
    
    with t1:
        st.markdown('<div class="titlu-sectiune">I. Introducere</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în anul <b>1920</b>, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu reprezintă un moment de cotitură... Tehnica detaliului semnificativ și caracterul verosimil... Scena horei îi conferă textului un caracter monografic.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală este <b>destinul țăranului român</b>... "Glasul pământului" și "Glasul iubirii".</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile III-V sunt blocate. Introdu codul Admin!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud... Îl sărută cu patimă, ca pe o <b>ibovnică</b>.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="titlu-sectiune">IV. Structura</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Structură <b>circulară</b>, bazată pe simetrie.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("🔒 Cod ADMIN necesar!")
        else:
            st.header("🎮 Maraton Ion (20 Nivele)")
            c1, c2 = st.columns(2)
            with c1:
                with st.expander("1-10: Acțiune"):
                    if st.selectbox("An?", ["1920", "1930"], key="i1") == "1920": st.success("+10")
                    if st.text_input("Citat (Nivel 8): Ca pe o...", key="i8").lower().strip() in ["ibovnică", "ibovnica"]: st.success("+25")
            with c2:
                with st.expander("11-20: Teorie & Personaj"):
                    if st.radio("Statut social Ion?", ["Bogat", "Sărăntoc"], key="i11") == "Sărăntoc": st.success("+10")
                    if st.selectbox("Statut Moral?", ["Degradare", "Ascensiune"], key="i12") == "Degradare": st.success("+10")

# --- PAGINA ENIGMA OTILIEI ---
elif st.session_state.page == "Enigma Otiliei":
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Enigma Otiliei - Analiză & Maraton 30 Jocuri")
    t1, t2 = st.tabs(["📄 Eseu Critic", "🎮 Maraton 30 Niveluri"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Realism Balzacian</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1938</b>, romanul ilustrează viața burgheziei bucureștene... Tehnica detaliului în descrierea străzii Antim.</div>', unsafe_allow_html=True)
        
        if not st.session_state.subscribed:
            st.warning("🔒 Restul analizei este blocat!")
        else:
            st.markdown('<div class="titlu-sectiune">II. Tema și Titlul</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Tema moștenirii și a paternității. Titlul inițial: "Părinții Otiliei".</div>', unsafe_allow_html=True)
            st.markdown('<div class="titlu-sectiune">III. Caracterizarea Otiliei</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Otilia reprezintă <b>"eternul feminin"</b>. Este caracterizată prin pluriperspectivism.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("🔒 Cod ADMIN necesar!")
        else:
            st.header("🏆 Maraton Enigma (30 Niveluri)")
            c1, c2, c3 = st.columns(3)
            with c1:
                with st.expander("1-10: Bazele Balzaciene"):
                    if st.selectbox("An apariție?", ["1938", "1920"], key="e1") == "1938": st.success("+5")
                    if "Antim" in st.text_input("Strada?", key="e6"): st.success("+10")
            with c2:
                with st.expander("11-20: Modernism & Conflicte"):
                    if st.checkbox("Pluriperspectivism", key="e12"): st.success("+10")
                    if "Stănică" in st.text_input("Cine fură banii?", key="e18"): st.success("+15")
            with c3:
                with st.expander("21-30: Otilia & Final"):
                    if "Orfană" in st.radio("Statut Otilia?", ["Bogată", "Orfană"], key="e21"): st.success("+5")
                    if st.button("Finalizează Maratonul"): st.balloons()

# --- UPGRADE PRO ---
elif st.session_state.page == "💎 Upgrade PRO":
    st.title("💎 Upgrade la Premium")
    st.write("Introdu codul primit de la profesor pentru a debloca tot conținutul.")
