import streamlit as st

# --- 1. CONFIGURARE ---
st.set_page_config(page_title="George-Bac Premium", page_icon="📚", layout="wide")

if 'score' not in st.session_state: st.session_state.score = 0
if 'subscribed' not in st.session_state: st.session_state.subscribed = False
if 'page' not in st.session_state: st.session_state.page = "🏠 Acasă"

# --- 2. DESIGN ---
st.markdown("""
    <style>
    .highlight { color: #FF512F; font-weight: bold; }
    .citat { font-style: italic; color: #555; background: #fff5f2; padding: 15px; border-left: 3px solid #FF512F; display: block; margin: 15px 0; border-radius: 5px; }
    .titlu-sectiune { color: #1a1a1a; font-family: 'serif'; border-bottom: 2px solid #FF512F; padding-bottom: 5px; margin-top: 30px; font-weight: bold; font-size: 1.5em; }
    .container { background: white; padding: 30px; border-radius: 15px; box-shadow: 0px 4px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac")
    st.metric("Puncte ⭐", st.session_state.score)
    menu = st.radio("Meniu", ["🏠 Acasă", "📚 Biblioteca", "💎 Upgrade PRO"])
    if st.session_state.page not in ["Ion"]: st.session_state.page = menu
    st.write("---")
    if st.text_input("🔓 Cod Admin", type="password") == "george123":
        st.session_state.subscribed = True
        st.success("Admin ACTIV")

# --- 4. LOGICA PAGINI ---
if st.session_state.page == "🏠 Acasă":
    st.title("Pregătit de BAC? 🚀")
    if st.button("Vezi Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

elif st.session_state.page == "📚 Biblioteca":
    st.title("Bibliotecă")
    if st.button("Ion - Liviu Rebreanu"):
        st.session_state.page = "Ion"
        st.rerun()

elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion de Liviu Rebreanu – Analiză Completă")
    
    t1, t2 = st.tabs(["📄 Eseu Detaliat", "🎮 Jocuri"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Introducere și Încadrare</div>', unsafe_allow_html=True)
        st.markdown('Publicat în **1920**, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu reprezintă un pilon fundamental al literaturii române interbelice. Este primul roman realist-obiectiv de amploare, construit ca o monografie a satului ardelean.', unsafe_allow_html=True)
        st.markdown('Naratorul este **omniprezent și omniscient**, oferind o perspectivă detașată. Structura este circulară, simetria fiind oferită de imaginea drumului care „vine” și „pleacă” din satul Pripas.', unsafe_allow_html=True)

        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea despre Lume</div>', unsafe_allow_html=True)
        st.markdown('Tema centrală este **lupta pentru pământ** într-o societate rurală unde averea dictează respectul. Ion este sfâșiat între <span class="highlight">„Glasul pământului”</span> și <span class="highlight">„Glasul iubirii”</span>.', unsafe_allow_html=True)

        if st.session_state.subscribed:
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative</div>', unsafe_allow_html=True)
            st.markdown('**Scena horei:** Reprezintă harta ierarhiilor din sat. Ion o alege pe Ana pentru avere, sacrificând iubirea pentru Florica.', unsafe_allow_html=True)
            st.markdown('**Sărutarea pământului:** Este momentul posesiei totale. Ion îngenunchează și sărută pământul ca pe o amantă.', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Îl sărută cu patimă, ca pe o amantă. Şi abia acum pământul i se păru frumos...”</span>', unsafe_allow_html=True)

            st.markdown('<div class="titlu-sectiune">IV. Elemente de Structură și Conflict</div>', unsafe_allow_html=True)
            st.markdown('Conflictul este triplu: **social** (Ion vs Vasile Baciu), **erotic** (Ion vs George) și **interior** (cele două glasuri). Finalul este tragic, Ion fiind ucis de George cu o sapă.', unsafe_allow_html=True)

            st.markdown('<div class="titlu-sectiune">V. Concluzie</div>', unsafe_allow_html=True)
            st.markdown('În concluzie, romanul este o lecție despre limitele lăcomiei și despre modul în care instinctele distrug umanitatea.', unsafe_allow_html=True)
        else:
            st.warning("🔒 Introdu codul Admin pentru a vedea continuarea (III, IV, V).")

    with t2:
        if st.session_state.subscribed:
            st.subheader("🎮 Quiz")
            check = st.radio("Cine îl omoară pe Ion?", ["Vasile", "George", "Ana"], index=None)
            if st.button("Verifică"):
                if check == "George": st.success("Corect! +20 puncte"); st.session_state.score += 20
                else: st.error("Incorect!")
        else:
            st.info("Deblochează PRO pentru jocuri.")
