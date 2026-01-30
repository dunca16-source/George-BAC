import streamlit as st

# --- 1. CONFIGURARE ---
st.set_page_config(page_title="George-Bac PRO", page_icon="⚡", layout="wide")

# Inițializare variabile de sesiune (persistente)
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
    .stRadio > label { font-size: 1.1em; font-weight: bold; color: #2c3e50; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (NAVIGARE ROBUSTĂ) ---
with st.sidebar:
    st.title("⚡ George-Bac PRO")
    st.metric("Puncte Acumulate ⭐", st.session_state.score)
    
    st.subheader("Meniu Rapid")
    if st.button("🏠 Pagina Principală", use_container_width=True):
        st.session_state.page = "🏠 Acasă"
        st.rerun()
    if st.button("📚 Biblioteca Completă", use_container_width=True):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()
    
    st.write("---")
    cod_acces = st.text_input("🔓 Cod Admin (Premium)", type="password")
    if cod_acces == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL Deblocat!")

# --- 4. PAGINĂ: ACASĂ ---
if st.session_state.page == "🏠 Acasă":
    st.title("Pregătire Premium Bacalaureat ⚡")
    st.markdown("### Bine ai venit la cea mai interactivă platformă de Română!")
    st.write("Aici nu doar citești, ci înveți prin joc și analiză critică aprofundată.")
    if st.button("Deschide Biblioteca 🚀"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

# --- 5. PAGINĂ: BIBLIOTECA ---
elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Alege Opera pentru Studiu")
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/b/b3/Liviu_Rebreanu.jpg", width=150)
        st.subheader("Ion")
        st.write("Realism Obiectiv. Destinul țăranului român.")
        if st.button("Studiază ION"):
            st.session_state.page = "Ion"
            st.rerun()
            
    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/ro/c/c5/George_C%C4%83linescu.jpg", width=150)
        st.subheader("Enigma Otiliei")
        st.write("Realism Balzacian & Modernism.")
        if st.button("Studiază ENIGMA"):
            st.session_state.page = "Enigma Otiliei"
            st.rerun()

# --- 6. PAGINĂ: ION ---
elif st.session_state.page == "Ion":
    st.title("📖 Ion - Liviu Rebreanu")
    tab1, tab2 = st.tabs(["📄 Analiza Literară Completă", "🎮 Maraton 20 Grile Teorie"])

    with tab1:
        st.markdown('<div class="titlu-sectiune">I. Context și Încadrare</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1920</b>, „Ion” este primul roman realist-obiectiv din literatura noastră. Liviu Rebreanu aduce o viziune <b>monografică</b> asupra satului ardelean (Pripas), utilizând tehnica detaliului verosimil. Naratorul este omniscient, detașat, oferind o perspectivă „dindărăt” care creează iluzia vieții complete.</div>', unsafe_allow_html=True)
        
        

        if not st.session_state.subscribed:
            st.warning("🔒 Eseul complet (Viziune, Structură, Simboluri) este blocat. Introdu codul!")
        else:
            st.markdown('<div class="titlu-sectiune">II. Tema și Glasurile</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Tema centrală este lupta pentru pământ într-o societate rurală unde averea dictează respectul. Romanul e structurat pe două planuri care converg: <b>Glasul pământului</b> (dorința de ascensiune socială) și <b>Glasul iubirii</b> (chemarea sufletului).</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud... Îl sărută cu patimă, ca pe o <b>ibovnică</b>.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="titlu-sectiune">III. Structura Circulară</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Simetria este dată de descrierea drumului care intră și iese din satul Pripas. Crucea strâmbă de la marginea satului sugerează că destinele personajelor sunt sub semnul tragicului, într-o lume indiferentă la drama individului.</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.subscribed: st.error("Deblochează Premium pentru jocuri!")
        else:
            q1 = st.radio("1. Ce tip de roman este 'Ion'?", ["Alege...", "Realist-Obiectiv", "Modern-Subiectiv", "Istoric"], key="ion1")
            if q1 == "Realist-Obiectiv": st.success("Corect! +10 pct")
            
            q2 = st.radio("2. Care este tehnica specifică descrierii satului?", ["Alege...", "Monografică", "Fantastică", "Simbolistă"], key="ion2")
            if q2 == "Monografică": st.success("Corect! +10 pct")
            
            q3 = st.radio("3. Ce personaj îl omoară pe Ion?", ["Alege...", "Vasile Baciu", "George Bulbuc", "Preotul Belciug"], key="ion3")
            if q3 == "George Bulbuc": st.success("Corect! +10 pct")

# --- 7. PAGINĂ: ENIGMA OTILIEI ---
elif st.session_state.page == "Enigma Otiliei":
    st.title("📖 Enigma Otiliei - G. Călinescu")
    tab_e1, tab_e2 = st.tabs(["📄 Analiza Critică Detaliată", "🎮 Maraton 30 Grile"])

    with tab_e1:
        st.markdown('<div class="titlu-sectiune">I. Realism Balzacian: Metoda și Cadrul</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Apărut în <b>1938</b>, romanul este o operă programatică. Călinescu utilizează <b>metoda balzaciană</b> prin fixarea exactă a timpului (iulie 1909) și a spațiului (București, strada Antim). <b>Tehnica detaliului</b> arhitectural este esențială: descrierea casei lui Costache Giurgiuveanu (fațada bizară, amestecul de stiluri, starea de paragină) anticipează direct <b>degradarea morală</b> și avariția locatarilor.</div>', unsafe_allow_html=True)
        
        

        if not st.session_state.subscribed:
            st.warning("🔒 Analiza Modernismului și a Tipologiilor este blocată!")
        else:
            st.markdown('<div class="titlu-sectiune">II. De la „Părinții Otiliei” la „Enigma Otiliei”</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Titlul inițial sublinia tema balzaciană a <b>paternității</b>. Titlul final mută accentul pe <b>modernism</b>. Enigma Otiliei nu este un secret, ci provine din <b>pluriperspectivism</b> (tehnica oglinzilor paralele). Fiecare personaj o vede diferit: Felix (idealul), Pascalopol (feminitate și candoare), Aglae (o „dezmățată”), Stănică (o cale de a obține bani).</div>', unsafe_allow_html=True)

            st.markdown('<div class="titlu-sectiune">III. Tipologii Umane (Galeria de Caractere)</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">G. Călinescu construiește tipologii clare: <br>1. <b>Costache Giurgiuveanu</b>: Avarul care manifestă o iubire paternă bizară.<br>2. <b>Stănică Rațiu</b>: Arivistul modern, demagog și fără scrupule.<br>3. <b>Aglae Tulea</b>: „Baba absolută”, personificarea răutății invidioase.</div>', unsafe_allow_html=True)
            
            

    with tab_e2:
        if not st.session_state.subscribed: st.error("Deblochează Premium!")
        else:
            e1 = st.radio("1. Ce reprezintă descrierea străzii Antim?", ["Alege...", "Un simplu decor", "O modalitate de caracterizare indirectă", "Un element romantic"], key="en1")
            if e1 == "O modalitate de caracterizare indirectă": st.success("Corect! +10 pct")
            
            e2 = st.radio("2. Ce este 'pluriperspectivismul' în acest roman?", ["Alege...", "Relatarea din mai multe orașe", "Otilia văzută diferit de celelalte personaje", "Utilizarea mai multor naratori"], key="en2")
            if e2 == "Otilia văzută diferit de celelalte personaje": st.success("Bravo! +10 pct")
            
            e3 = st.radio("3. Care este tipologia lui Costache Giurgiuveanu?", ["Alege...", "Arivistul", "Avarul", "Inocenta"], key="en3")
            if e3 == "Avarul": st.success("Corect! +10 pct")

            e4 = st.radio("4. Ce este Aglae Tulea în viziunea autorului?", ["Alege...", "Musa", "Baba absolută", "Personajul-martor"], key="en4")
            if e4 == "Baba absolută": st.success("Corect! +10 pct")

st.write("---")
st.caption("Aplicație dezvoltată pentru succesul la Bacalaureat 2026.")
