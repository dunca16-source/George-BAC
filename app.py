import streamlit as st

# --- 1. CONFIGURARE ---
st.set_page_config(page_title="George-Bac Premium", page_icon="📚", layout="wide")

if 'score' not in st.session_state: st.session_state.score = 0
if 'subscribed' not in st.session_state: st.session_state.subscribed = False
if 'page' not in st.session_state: st.session_state.page = "🏠 Acasă"

# --- 2. DESIGN ---
st.markdown("""
    <style>
    .stApp { background: #fdfdfd; }
    .eseu-text { 
        font-size: 1.2em; 
        line-height: 1.8; 
        color: #2c3e50; 
        background: white; 
        padding: 40px; 
        border-radius: 20px; 
        box-shadow: 0px 10px 30px rgba(0,0,0,0.08); 
        text-align: justify;
        border-left: 5px solid #FF512F;
    }
    .highlight { color: #FF512F; font-weight: bold; }
    .citat { font-style: italic; color: #555; background: #fff5f2; padding: 15px; border-left: 3px solid #FF512F; display: block; margin: 15px 0; border-radius: 5px; }
    .titlu-sectiune { color: #1a1a1a; font-family: 'Georgia', serif; border-bottom: 2px solid #eee; padding-bottom: 5px; margin-top: 30px; font-weight: bold; font-size: 1.5em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac")
    st.metric("Puncte ⭐", st.session_state.score)
    menu = st.radio("Navigare", ["🏠 Acasă", "📚 Biblioteca", "💎 Upgrade PRO"])
    if st.session_state.page not in ["Ion"]: st.session_state.page = menu
    st.write("---")
    cod_admin = st.text_input("🔓 Cod Admin", type="password")
    if cod_admin == "george123":
        st.session_state.subscribed = True
        st.success("Admin ACTIV")

# --- 4. PAGINA ION ---
if st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

    st.title("📖 Ion de Liviu Rebreanu – Analiză Completă")
    
    t1, t2 = st.tabs(["📄 Eseu Detaliat", "🎮 Jocuri"])

    with t1:
        # Construim eseul în memorie înainte de afișare
        partea_1 = """
        <div class="eseu-text">
            <div class="titlu-sectiune">I. Introducere și Încadrare</div>
            Publicat în <b>1920</b>, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu reprezintă un pilon fundamental al literaturii române interbelice, fiind considerat primul roman realist-obiectiv de amploare. 
            Opera este o monografie a satului ardelean de la începutul secolului al XX-lea, construită pe principiile realismului critic. 
            Naratorul este <b>omniprezent și omniscient</b>, relatând evenimentele la persoana a III-a dintr-o perspectivă detașată, neutră.
            <br><br>
            Structura este una circulară, simetria fiind oferită de imaginea drumului care „vine” și „pleacă” din satul Pripas, sugerând că viața comunității își continuă cursul imperturbabil, indiferent de tragediile individuale.

            <div class="titlu-sectiune">II. Tema și Viziunea despre Lume</div>
            Tema centrală este <b>lupta pentru pământ</b> într-o societate rurală în care posesia averii condiționează statutul social. 
            Eugen Lovinescu îl definea pe Ion drept o „brută ingenioasă”, a cărei existență este sfâșiată între două forțe opuse: 
            <span class="highlight">„Glasul pământului”</span> și <span class="highlight">„Glasul iubirii”</span>. 
            Viziunea despre lume este marcată de determinism: personajul este o victimă a propriilor instincte primare.
        """

        partea_2 = """
            <div class="titlu-sectiune">III. Secvențe Reprezentative</div>
            Un prim episod fundamental este cel al <b>horei de duminică</b>. Această scenă de început prezintă „harta” ierarhiilor din Pripas. 
            Ion o alege la joc pe Ana, fata bogătașului Vasile Baciu, deși o iubește pe Florica. Ion sacrifică sentimentul pur pentru dorința de ascensiune socială. 
            <br><br>
            A doua secvență esențială este <b>sărutarea pământului</b>. După ce Ion obține averile lui Vasile Baciu, acesta merge la câmp și, într-un gest ritualic:
            <span class="citat">„Îl sărută cu patimă, ca pe o amantă. Şi abia acum pământul i se păru frumos...”</span> 
            Această imagine este simbolul dezumanizării: Ion a înlocuit iubirea umană cu o obsesie materială personificată.

            <div class="titlu-sectiune">IV. Elemente de Structură și Conflict</div>
            Romanul este organizat în <b>13 capitole</b> cu titluri sugestive. Conflictul exterior este triplu: social, național și erotic. 
            Însă cel mai puternic rămâne <b>conflictul interior</b>, dat de impsibilitatea lui Ion de a împăca cele două „glasuri”. 
            După ce obține pământul, „Glasul iubirii” revine distructiv, împingându-l spre Florica și spre finalul tragic.

            <div class="titlu-sectiune">V. Concluzie</div>
            În concluzie, <span class="highlight">"Ion"</span> rămâne o capodoperă a realismului prin profunzimea analizei psihologice. 
            Destinul protagonistului este o lecție despre limitele lăcomiei și despre modul în care instinctele necontrolate duc la prăbușirea morală.
        </div>
        """
        
        # AFIȘARE FINALĂ (Repară eroarea de cod vizibil)
        if st.session_state.subscribed:
            st.markdown(partea_1 + partea_2, unsafe_allow_html=True)
        else:
            st.markdown(partea_1 + "</div>", unsafe_allow_html=True)
            st.warning("🔒 Secțiunile III, IV și V sunt blocate. Introdu codul Admin în stânga.")

    with t2:
        if st.session_state.subscribed:
            st.subheader("🎮 Quiz rapid")
            # Adăugăm un quiz simplu care funcționează
            check = st.radio("Cine îl omoară pe Ion?", ["Vasile Baciu", "George Bulbuc", "Ana"])
            if st.button("Verifică"):
                if check == "George Bulbuc":
                    st.success("Corect! +20 puncte")
                    st.session_state.score += 20
                else: st.error("Incorect!")
        else:
            st.info("Jocurile sunt disponibile pentru PRO.")

# --- RESTUL PAGINILOR ---
elif st.session_state.page == "🏠 Acasă":
    st.title("George-Bac ⚡")
    st.write("Pregătire completă pentru examen.")
    if st.button("Vezi Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

elif st.session_state.page == "📚 Biblioteca":
    st.title("Bibliotecă")
    if st.button("Ion - Liviu Rebreanu"):
        st.session_state.page = "Ion"
        st.rerun()
