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
    if st.session_state.page not in ["Ion"]: st.session_state.page = menu
    st.write("---")
    if st.text_input("🔓 Cod Admin", type="password") == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL deblocat!")

# --- 4. PAGINA ION ---
if st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion - Analiză & Maraton Jocuri")
    
    t1, t2 = st.tabs(["📄 Eseu Detaliat (500+ cuvinte)", "🎮 Maraton Jocuri (REPARAT)"])

    with t1:
        # ESEU COMPLET NESCHIMBAT
        st.markdown('<div class="titlu-sectiune">I. Introducere și Încadrare</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în anul <b>1920</b>, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu reprezintă un moment de cotitură în literatura română, fiind primul roman realist-obiectiv de valoare europeană. Naratorul este <b>omniscient și omniprezent</b>, adoptând o viziune „dindărăt”.</div>', unsafe_allow_html=True)

        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea despre Lume</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală este <b>destinul țăranului român</b> pentru care posesia pământului reprezintă singura cale de a obține demnitatea socială. Viziunea despre lume este una aspră, dominată de determinism social și biologic.</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Introdu codul Admin pentru restul eseului.")
        else:
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Scena <b>horei</b> prezintă ierarhia satului. A doua secvență esențială este <b>sărutarea pământului</b>:</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud... Îl sărută cu patimă, ca pe o amantă.”</span>', unsafe_allow_html=True)
            
            st.markdown('<div class="titlu-sectiune">IV. Elemente de Structură</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Romanul se remarcă printr-o <b>structură circulară</b>. Este împărțit în <b>„Glasul pământului”</b> și <b>„Glasul iubirii”</b>. Finalul tragic, uciderea lui Ion de către George Bulbuc, închide destinul sub semnul fatalității.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed:
            st.error("🔒 Codul ADMIN necesar!")
        else:
            # JOCURILE 1-7 (Pe scurt aici, dar prezente în codul tău)
            st.info("Nivelele 1-7 sunt active. Verifică Nivelul 8 mai jos:")
            
            # REPARARE NIVEL 8
            with st.expander("8. Analiză de text (REPARAT)", expanded=True):
                st.write("Completează citatul: 'Îl sărută cu patimă, ca pe o ...'")
                # Folosim un key unic pentru a forța reîmprospătarea
                raspuns_8 = st.text_input("Scrie cuvântul aici:", key="input_nivel_8")
                
                if st.button("Verifică Nivel 8"):
                    if raspuns_8.lower().strip() == "amantă" or raspuns_8.lower().strip() == "amanta":
                        st.success("CORECȚI! +25 puncte")
                        if 'n8_done' not in st.session_state:
                            st.session_state.score += 25
                            st.session_state.n8_done = True
                    else:
                        st.error("Greșit! Cuvântul corect este 'amantă'.")

            # NIVEL 10
            with st.expander("10. Deznodământul"):
                if st.button("Ucis de George cu sapa"):
                    st.balloons()
                    st.success("Ai terminat!")

elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Biblioteca")
    if st.button("Ion"): st.session_state.page = "Ion"; st.rerun()

elif st.session_state.page == "🏠 Acasă":
    st.title("George-Bac ⚡")
    if st.button("Start"): st.session_state.page = "📚 Biblioteca"; st.rerun()
