import streamlit as st

# --- 1. CONFIGURARE ---
st.set_page_config(page_title="George-Bac PREMIUM", page_icon="⚡", layout="wide")

# Inițializare stare sesiune
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
    .stRadio > label { font-weight: bold; color: #1e293b; background: #f8fafc; padding: 10px; border-radius: 5px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (NAVIGARE FIXĂ) ---
with st.sidebar:
    st.title("⚡ George-Bac PRO")
    st.metric("Puntos ⭐", st.session_state.score)
    st.write("---")
    if st.button("🏠 Acasă", use_container_width=True):
        st.session_state.page = "🏠 Acasă"
        st.rerun()
    if st.button("📚 Biblioteca", use_container_width=True):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()
    st.write("---")
    cod = st.text_input("🔓 Cod Admin", type="password")
    if cod == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL Deblocat!")

# --- 4. PAGINI ---

# --- PAGINA: ACASĂ ---
if st.session_state.page == "🏠 Acasă":
    st.title("George-Bac: Excelență în Literatură ⚡")
    st.subheader("Pregătire completă pentru examenul de Bacalaureat")
    if st.button("Deschide Biblioteca de Opere 🚀"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

# --- PAGINA: BIBLIOTECA ---
elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Biblioteca George-Bac")
    c1, c2 = st.columns(2)
    with c1:
        st.info("REALISM OBIECTIV")
        if st.button("📖 Ion - Liviu Rebreanu", use_container_width=True):
            st.session_state.page = "Ion"; st.rerun()
    with c2:
        st.info("REALISM BALZACIAN / MODERNISM")
        if st.button("📖 Enigma Otiliei - G. Călinescu", use_container_width=True):
            st.session_state.page = "Enigma Otiliei"; st.rerun()

# --- PAGINA: ION (ESEUL TĂU COMPLET) ---
elif st.session_state.page == "Ion":
    st.title("📖 Ion de Liviu Rebreanu - Analiză Completă")
    t1, t2 = st.tabs(["📄 Eseul de Nota 10", "🎮 Maraton 20 Grile"])
    
    with t1:
        st.markdown('<div class="titlu-sectiune">I. Introducere și Context</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1920</b>, romanul reprezintă primul text realist-obiectiv de valoare europeană din literatura română. Aparține perioadei interbelice și respectă trăsăturile realismului: naratorul omniscient și omniprezent, tehnica detaliului semnificativ și verosimilitatea. Scena horei și descrierea satului Pripas conferă operei un caracter <b>monografic</b>.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală este <b>destinul țăranului român</b> și patima pentru pământ. Viziunea este marcată de determinismul social. Eugen Lovinescu definește personajul drept o „brută ingenioasă”, oscilând între cele două volume: <b>„Glasul pământului”</b> (instinctul de stăpân) și <b>„Glasul iubirii”</b> (pasiunea pentru Florica).</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile III, IV și V sunt blocate. Introdu codul george123!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud... Îl sărută cu patimă, ca pe o <b>ibovnică</b>.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Această secvență a sărutării pământului este definitorie pentru personaj, simbolizând victoria instinctului de posesie. Un alt moment cheie este <b>Hora</b>, unde se observă ierarhia socială (bogații vs. sărăntocii).</div>', unsafe_allow_html=True)
            st.markdown('<div class="titlu-sectiune">IV. Structura Circulară</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Romanul are o structură circulară, bazată pe simetrie. Drumul care intră în sat la început și drumul care părăsește satul în final sugerează indiferența lumii față de dramele umane individuale.</div>', unsafe_allow_html=True)
            st.markdown('<div class="titlu-sectiune">V. Concluzie</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Ion este un personaj eponim care eșuează sub povara propriei lăcomii, opera rămânând pilonul realismului românesc.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("Deblochează Premium!")
        else:
            st.subheader("Maraton Ion - Alege răspunsul corect:")
            q1 = st.radio("1. Anul apariției?", ["...", "1920", "1938", "1900"], key="i1")
            q2 = st.radio("2. Statutul moral al lui Ion?", ["...", "Ascensiune spirituală", "Dezumanizare progresivă"], key="i2")
            q3 = st.radio("3. Rivalul lui Ion pentru pământ?", ["...", "George Bulbuc", "Vasile Baciu"], key="i3")
            if q1=="1920" and q2=="Dezumanizare progresivă" and q3=="Vasile Baciu": st.balloons()

# --- PAGINA: ENIGMA OTILIEI (COMPLET) ---
elif st.session_state.page == "Enigma Otiliei":
    st.title("📖 Enigma Otiliei de George Călinescu")
    t1, t2 = st.tabs(["📄 Eseul Critic Complet", "🎮 Maraton 30 Grile"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Realism Balzacian și Metoda Detaliului</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1938</b>, romanul este o operă realistă de factură balzaciană. G. Călinescu adoptă modelul balzacian prin fixarea exactă a timpului și spațiului (iulie 1909, București, strada Antim) și prin <b>tehnica detaliului semnificativ</b>. Descrierea minuțioasă a casei lui Costache Giurgiuveanu anticipează direct degradarea morală a locatarilor.</div>', unsafe_allow_html=True)
        
        

        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile despre Titlu, Modernism și Tipologii sunt blocate!")
        else:
            st.markdown('<div class="titlu-sectiune">II. Titlul și Modernismul (Pluriperspectivismul)</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Titlul inițial, „Părinții Otiliei”, viza tema paternității. Titlul final, „Enigma Otiliei”, introduce elementul <b>modernist</b>. Enigma provine din <b>pluriperspectivism</b> (tehnica oglinzilor paralele): Otilia este văzută diferit de fiecare personaj (Felix o idealizează, Pascalopol o admiră, Aglae o urăște). Acest lucru îi conferă personajului o aură de mister feminin.</div>', unsafe_allow_html=True)

            st.markdown('<div class="titlu-sectiune">III. Tipologii Umane Balzaciene</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">1. <b>Costache Giurgiuveanu</b> reprezintă <b>Avarul</b>.<br>2. <b>Stănică Rațiu</b> reprezintă <b>Arivistul</b> (parvenitul fără scrupule).<br>3. <b>Aglae Tulea</b> reprezintă <b>Baba Absolută</b> (simbolul răutății).</div>', unsafe_allow_html=True)
            
            

            st.markdown('<div class="titlu-sectiune">IV. Conflictul și Finalul</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Conflictul principal este cel pentru <b>moștenirea</b> lui Costache. Finalul este marcat de melancolie: Felix devine un medic de succes, dar o pierde pe Otilia, care alege siguranța lângă Pascalopol.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("Deblochează Premium!")
        else:
            st.subheader("Grile Teoretice (Alege varianta corectă):")
            e1 = st.radio("1. Care este strada unde se află casa lui Costache?", ["...", "Antim", "Lipscani", "Victoriei"], key="e1")
            e2 = st.radio("2. Cine este arivistul romanului?", ["...", "Felix", "Stănică Rațiu"], key="e2")
            e3 = st.radio("3. Tehnica prin care Otilia e văzută de toți?", ["...", "Oglinzile paralele", "Fluxul conștiinței"], key="e3")
            e4 = st.radio("4. Tipologia Aglaei?", ["...", "Baba absolută", "Eroina tragică"], key="e4")
            e5 = st.radio("5. Meseria lui Felix la final?", ["...", "Avocat", "Medic"], key="e5")
            if e1=="Antim" and e2=="Stănică Rațiu" and e3=="Oglinzile paralele": st.success("Ai trecut primele niveluri!")
