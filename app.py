import streamlit as st

# --- 1. CONFIGURARE ---
st.set_page_config(page_title="George-Bac Premium", page_icon="⚡", layout="wide")

# Inițializare variabile de sesiune
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
    .stRadio > label { font-weight: bold; color: #FF512F; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac PRO")
    st.metric("Puncte ⭐", st.session_state.score)
    
    # Navigare fixă
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

# --- ACASĂ ---
if st.session_state.page == "🏠 Acasă":
    st.title("George-Bac ⚡")
    st.subheader("Platforma ta completă pentru succesul la Limba Română")
    st.write("Aici găsești eseurile dictate la clasă și jocuri interactive de verificare a teoriei.")
    if st.button("Începe Studiul 🚀"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

# --- BIBLIOTECA ---
elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Biblioteca de Opere")
    col1, col2 = st.columns(2)
    with col1:
        st.info("REALISM OBIECTIV")
        if st.button("📖 Ion - Liviu Rebreanu"):
            st.session_state.page = "Ion"
            st.rerun()
    with col2:
        st.info("REALISM BALZACIAN / MODERNISM")
        if st.button("📖 Enigma Otiliei - G. Călinescu"):
            st.session_state.page = "Enigma Otiliei"
            st.rerun()

# --- ION (ESEUL TĂU + 20 JOCURI) ---
elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion de Liviu Rebreanu")
    t1, t2 = st.tabs(["📄 Eseul Complet", "🎮 Maraton 20 Grile"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Introducere și Încadrare</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1920</b>, romanul reprezintă primul text realist-obiectiv din literatura română. Aparține perioadei interbelice și respectă trăsăturile realismului: obiectivitatea naratorului (omniscient și omniprezent), tehnica detaliului semnificativ și verosimilitatea. Scena horei și descrierea satului Pripas conferă operei un caracter monografic.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema principală este <b>destinul țăranului român</b> și patima pentru pământ. Viziunea este marcată de determinismul social. Eugen Lovinescu definește personajul drept o „brută ingenioasă”, oscilând între „Glasul pământului” și „Glasul iubirii”.</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile III-V sunt blocate. Introdu codul george123 în sidebar!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Secvențe Cheie</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud... Îl sărută cu patimă, ca pe o <b>ibovnică</b>.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Acest moment simbolizează dezumanizarea lui Ion și victoria instinctului de posesie asupra sentimentelor umane.</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="titlu-sectiune">IV. Structura și Conflictele</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Romanul are o structură <b>circulară</b> (simetria drumului de la început și final). Conflictul exterior este între Ion și Vasile Baciu, iar cel interior este între dorința de avere și iubirea pentru Florica.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("Deblochează conținutul din sidebar!")
        else:
            st.subheader("Alege varianta corectă:")
            q1 = st.radio("1. Anul apariției?", ["Selectează...", "1900", "1920", "1938"], key="q1")
            if q1 == "1920": st.success("Corect! +10 pct")

            q2 = st.radio("2. Statutul social inițial al lui Ion?", ["Selectează...", "Bogat", "Sărăntoc", "Mijlăcaș"], key="q2")
            if q2 == "Sărăntoc": st.success("Corect! +10 pct")

            q3 = st.radio("3. Cum moare Ion?", ["Selectează...", "Bătrânețe", "Sapa lui George Bulbuc", "Omoară-l Ana"], key="q3")
            if q3 == "Sapa lui George Bulbuc": st.success("Corect! +10 pct")

            q4 = st.radio("4. Sărută pământul ca pe o...", ["Selectează...", "Mamă", "Ibovnică", "Sfântă"], key="q4")
            if q4 == "Ibovnică": st.success("Corect! +25 pct")
            
            st.info("Completează toate cele 20 de grile din fișierul de studiu!")

# --- ENIGMA OTILIEI (ESEUL COMPLET DETALIAT + 30 JOCURI) ---
elif st.session_state.page == "Enigma Otiliei":
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Enigma Otiliei de G. Călinescu")
    t1, t2 = st.tabs(["📄 Eseul Detaliat", "🎮 Maraton 30 Grile"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Geneză și Încadrare: Realismul Balzacian</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Apărut în <b>1938</b>, romanul este o demonstrație de forță critică a lui G. Călinescu, care respinge teoria camilpetresciană a sincronizării cu modernismul de tip proustian, optând pentru modelul <b>balzacian</b>. Trăsăturile balzaciene includ: tema moștenirii, fixarea precisă a timpului și a spațiului (București, iulie 1909), tehnica detaliului arhitectural și utilizarea tipologiilor (avarul, arivistul).</div>', unsafe_allow_html=True)
        
        

        st.markdown('<div class="titlu-sectiune">II. Tema, Titlul și Structura</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu"><b>Tema</b> este viața burgheziei bucureștene de la începutul sec. XX, axată pe degradarea morală provocată de bani. <b>Titlul</b> inițial, "Părinții Otiliei", sublinia tema balzaciană a paternității. Schimbarea în "Enigma Otiliei" mută centrul de greutate spre modernism, sugerând misterul feminității și modul în care Otilia este reflectată în ochii celorlalți (tehnica oglinzilor paralele).</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Analiza detaliată a personajelor și a modernismului este blocată!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Caracterizarea Otiliei - Între Modernism și Realism</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Otilia Mărculescu este unul dintre cele mai fascinante personaje feminine. Ea este caracterizată prin <b>comportamentism</b> (nu îi știm gândurile, doar faptele) și prin <b>pluriperspectivism</b>. Pentru Felix, ea este idealul feminin; pentru Pascalopol, o femeie matură și rafinată; pentru Aglae, o „dezmățată” care vânează averea lui Costache. Enigma ei este alegerea finală: îl părăsește pe Felix pentru a-i lăsa libertatea de a deveni un mare medic, alegând protecția lui Pascalopol.</div>', unsafe_allow_html=True)
            
            

            st.markdown('<div class="titlu-sectiune">IV. Tipologii Umane</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Călinescu creează caractere memorabile: <br>1. <b>Costache Giurgiuveanu</b> – avarul care, deși își iubește „feetița”, nu-i asigură viitorul.<br>2. <b>Stănică Rațiu</b> – arivistul demagog, lipsit de scrupule.<br>3. <b>Aglae Tulea</b> – „baba absolută”, simbolul răutății gratuite.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("Cod ADMIN necesar!")
        else:
            st.subheader("Grile de Teorie Aprofundată:")
            
            eg1 = st.radio("1. Ce tip de roman este Enigma Otiliei?", ["Selectează...", "Romantic", "Realist Balzacian", "Simbolist"], key="eg1")
            if eg1 == "Realist Balzacian": st.success("Corect! +5 pct")

            eg2 = st.radio("2. Care a fost titlul inițial?", ["Selectează...", "Felix și Otilia", "Părinții Otiliei", "Averea"], key="eg2")
            if eg2 == "Părinții Otiliei": st.success("Corect! +5 pct")

            eg3 = st.radio("3. Ce personaj întruchipează tipologia arivistului?", ["Selectează...", "Felix", "Stănică Rațiu", "Pascalopol"], key="eg3")
            if eg3 == "Stănică Rațiu": st.success("Corect! +5 pct")

            eg4 = st.radio("4. Ce tehnică modernă este folosită pentru portretul Otiliei?", ["Selectează...", "Monologul", "Oglinzile paralele (Pluriperspectivismul)", "Fluxul conștiinței"], key="eg4")
            if eg4 == "
