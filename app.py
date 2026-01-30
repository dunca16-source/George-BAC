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
    .citat { font-style: italic; color: #444; background: #fff5f2; padding: 20px; border-left: 5px solid #FF512F; border-radius: 8px; margin: 20px 0; }
    .titlu-sectiune { color: #1a1a1a; font-family: 'serif'; border-bottom: 2px solid #FF512F; padding-bottom: 8px; margin-top: 35px; font-weight: bold; font-size: 1.6em; }
    .text-eseu { font-size: 1.15em; line-height: 1.8; text-align: justify; color: #2c3e50; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac PRO")
    st.metric("Puncte ⭐", st.session_state.score)
    
    if st.button("🏠 Acasă"): 
        st.session_state.page = "🏠 Acasă"
        st.rerun()
    if st.button("📚 Biblioteca"): 
        st.session_state.page = "📚 Biblioteca"
        st.rerun()
    
    st.write("---")
    cod = st.text_input("🔓 Cod Admin", type="password")
    if cod == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL deblocat!")

# --- 4. LOGICA PAGINILOR ---

if st.session_state.page == "🏠 Acasă":
    st.title("George-Bac ⚡")
    st.subheader("Platforma ta completă pentru nota 10")
    if st.button("Începe Studiul 🚀"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

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

elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion de Liviu Rebreanu")
    t1, t2 = st.tabs(["📄 Eseul Complet", "🎮 Maraton 20 Grile"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Introducere și Realismul Obiectiv</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1920</b>, romanul <b>"Ion"</b> marchează nașterea romanului românesc modern. Este o operă realist-obiectivă, unde naratorul omniscient controlează destinele personajelor fără a interveni afectiv. Caracterul <b>monografic</b> este dat de descrierea detaliată a tradițiilor: hora, nunta, înmormântarea și ierarhia socială a satului Pripas.</div>', unsafe_allow_html=True)
        
        if not st.session_state.subscribed:
            st.warning("🔒 Eseul complet este blocat. Introdu codul!")
        else:
            st.markdown('<div class="titlu-sectiune">II. Tema și Simbolistica</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Tema centrală este <b>posesia pământului</b>, văzută ca sursă a demnității umane. Ion este sfâșiat între „Glasul pământului” (instinctul de stăpân) și „Glasul iubirii” (pasiunea pentru Florica). Celebra scenă a sărutării pământului subliniază caracterul ritualic al legăturii omului cu glia:</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud... Îl sărută cu patimă, ca pe o <b>ibovnică</b>.”</span>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("Deblochează din sidebar!")
        else:
            q_i1 = st.radio("1. Tipul naratorului în Ion?", ["...", "Subiectiv", "Omniscient și Obiectiv"], key="qi1")
            if q_i1 == "Omniscient și Obiectiv": st.success("Corect! +10")

elif st.session_state.page == "Enigma Otiliei":
    if st.button("⬅️ Înapoi"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Enigma Otiliei - George Călinescu")
    t1, t2 = st.tabs(["📄 Eseul Detaliat", "🎮 Maraton 30 Grile"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Realism Balzacian și Tehnica Detaliului</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1938</b>, romanul este o operă de factură balzaciană. G. Călinescu adoptă metoda lui Honoré de Balzac prin fixarea precisă a cadrului (iulie 1909, strada Antim) și prin <b>tehnica detaliului semnificativ</b>. Descrierea minuțioasă a casei lui Costache Giurgiuveanu (fațada bizară, crăpăturile, zidăria veche) anticipează direct degradarea morală a locatarilor.</div>', unsafe_allow_html=True)
        
        

        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile despre Modernism și Tipologii sunt blocate!")
        else:
            st.markdown('<div class="titlu-sectiune">II. Semnificația Titlului și Modernismul</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Titlul inițial, <i>"Părinții Otiliei"</i>, evidenția tema paternității (Moș Costache și Pascalopol ca figuri paterne). Schimbarea în <i>"Enigma Otiliei"</i> introduce elementul <b>modernist</b>: enigma nu este una polițistă, ci una psihologică. Ea provine din <b>pluriperspectivism</b> – Otilia este văzută diferit de fiecare personaj masculin: Felix o vede ca pe un ideal, Pascalopol ca pe o femeie matură, iar Aglae ca pe o rivală vicleană.</div>', unsafe_allow_html=True)

            st.markdown('<div class="titlu-sectiune">III. Tipologii de Personaje</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Romanul este o galerie de tipuri umane balzaciene:<br>1. <b>Costache Giurgiuveanu</b> reprezintă <b>Avarul</b> (tipologia omului stăpânit de lăcomie, dar care păstrează o urmă de afecțiune pentru Otilia).<br>2. <b>Stănică Rațiu</b> reprezintă <b>Arivistul</b> (tipul demagogului care calcă pe cadavre pentru a parveni social).<br>3. <b>Aglae Tulea</b> este <b>Baba Absolută</b> (simbolul răutății și al invidiei feminine).</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("Deblochează din sidebar!")
        else:
            st.subheader("Grile de Verificare Teoretică")
            
            e1 = st.radio("1. Ce trăsătură a casei lui Costache indică degradarea?", ["Modernismul", "Arhitectura hibridă și starea de ruină", "Luxul"], key="e1")
            if e1 == "Arhitectura hibridă și starea de ruină": st.success("Corect! +10")

            e2 = st.radio("2. Care este tipologia lui Stănică Rațiu?", ["Eroul tragic", "Arivistul", "Inocenta"], key="e2")
            if e2 == "Arivistul": st.success("Corect! +10")

            e3 = st.radio("3. Ce tehnică modernistă definește caracterizarea Otiliei?", ["Fluxul conștiinței", "Pluriperspectivismul (tehnica oglinzilor)", "Monologul interior"], key="e3")
            if e3 == "Pluriperspectivismul (tehnica oglinzilor)": st.success("Bravo! +10")

            e4 = st.radio("4. De ce îl părăsește Otilia pe Felix?", ["Pentru că nu îl iubește", "Pentru a-i lăsa libertatea de a-și construi cariera", "Din dorința de avere"], key="e4")
            if e4 == "Para a-i lăsa libertatea de a-și construi cariera": st.success("Corect! +10")

            e5 = st.radio("5. Ce reprezintă Aglae Tulea?", ["Idealul feminin", "Baba absolută", "Maternitatea"], key="e5")
            if e5 == "Baba absolută": st.success("Corect! +10")

st.write("---")
st.caption("George-Bac 2026 - Versiunea Premium Robustă")
