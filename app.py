import streamlit as st

# --- CONFIGURARE ---
st.set_page_config(page_title="George-Bac Premium", page_icon="📚", layout="wide")

if 'score' not in st.session_state: st.session_state.score = 0
if 'subscribed' not in st.session_state: st.session_state.subscribed = False
if 'page' not in st.session_state: st.session_state.page = "🏠 Acasă"

# --- DESIGN ---
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
    .citat { font-style: italic; color: #555; background: #fff5f2; padding: 10px; border-left: 3px solid #FF512F; display: block; margin: 15px 0; }
    .titlu-sectiune { color: #1a1a1a; font-family: 'Georgia', serif; border-bottom: 1px solid #eee; padding-bottom: 10px; margin-top: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac")
    st.metric("Puncte Acumulate ⭐", st.session_state.score)
    menu = st.radio("Navigare", ["🏠 Acasă", "📚 Biblioteca", "💎 Upgrade PRO"])
    if st.session_state.page not in ["Ion"]: st.session_state.page = menu
    st.write("---")
    cod = st.text_input("🔓 Cod Admin", type="password")
    if cod == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL activat!")

# --- PAGINA ION ---
if st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion de Liviu Rebreanu – Analiză Completă")
    
    t1, t2 = st.tabs(["📄 Eseu Detaliat (Subiectul III)", "🎮 Jocuri & Teste"])

    with t1:
        st.markdown('<div class="eseu-text">', unsafe_allow_html=True)
        
        st.markdown('<h2 class="titlu-sectiune">I. Introducere și Încadrare</h2>', unsafe_allow_html=True)
        st.write("""
        Publicat în **1920**, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu reprezintă un pilon fundamental al literaturii române interbelice, fiind considerat primul roman realist-obiectiv de amploare. 
        Opera este o monografie a satului ardelean de la începutul secolului al XX-lea, construită pe principiile realismului critic. 
        Naratorul este **omniprezent și omniscient**, relatând evenimentele la persoana a III-a dintr-o perspectivă detașată, neutră, ce conferă textului o autoritate aproape istorică. 
        Structura este una circulară, simetria fiind oferită de imaginea drumului care „vine” și „pleacă” din satul Pripas, sugerând că viața comunității își continuă cursul imperturbabil, indiferent de tragediile individuale.
        """)

        st.markdown('<h2 class="titlu-sectiune">II. Tema și Viziunea despre Lume</h2>', unsafe_allow_html=True)
        st.write("""
        Tema centrală este **lupta pentru pământ** într-o societate rurală în care posesia averii condiționează statutul social și demnitatea umană. 
        Eugen Lovinescu îl definea pe Ion drept o „brută ingenioasă”, a cărei existență este sfâșiată între două forțe opuse, simbolizate prin titlurile celor două volume: **„Glasul pământului”** și **„Glasul iubirii”**. 
        Viziunea despre lume a autorului este una aspră, marcată de determinism: personajul nu este doar o victimă a societății bântuite de lăcomie, ci și a propriilor instincte primare care îl dezumanizează treptat.
        """)

        # --- SECTIUNE BLOCATA ---
        if not st.session_state.subscribed:
            st.warning("⚠️ Restul eseului (încă 400 de cuvinte) și analiza scenelor cheie sunt disponibile doar pentru membrii PRO.")
        else:
            st.markdown('<h2 class="titlu-sectiune">III. Secvențe Reprezentative</h2>', unsafe_allow_html=True)
            st.write("""
            Un prim episod fundamental este cel al **horei de duminică**. Această scenă de început nu este doar un eveniment social, ci o „hartă” a ierarhiilor din Pripas. 
            Aici, Ion o alege la joc pe Ana, fata bogătașului Vasile Baciu, deși o iubește pe Florica. Această decizie marchează debutul conflictului: Ion sacrifică sentimentul pur pentru dorința de ascensiune socială. 
            Vasile Baciu îl numește „sărăntoc”, moment în care Ion înțelege că fără pământ nu este nimic în ochii satului.
            <br><br>
            A doua secvență esențială, punctul culminant al „Glasului pământului”, este **sărutarea pământului**. După ce Ion obține prin vicleșug averile lui Vasile Baciu, acesta merge la câmp într-o zi de primăvară. 
            Gestul său depășește sfera economică, devenind un act cvasi-mistic. 
            <span class="citat">„Îl sărută cu patimă, ca pe o amantă. Şi abia acum pământul i se păru frumos...”</span> 
            Această imagine este simbolul dezumanizării: Ion a înlocuit iubirea pentru o femeie (Florica/Ana) cu o obsesie materială personificată. Pământul nu mai este o resursă, ci o stăpână care îi devorează sufletul.
            """)
            
            

            st.markdown('<h2 class="titlu-sectiune">IV. Elemente de Structură și Conflict</h2>', unsafe_allow_html=True)
            st.write("""
            Romanul este organizat în **13 capitole** cu titluri sugestive (Blestemul, Ștreangul, Iubirea etc.), grupate în două părți simetrice. 
            Conflictul exterior este triplu: **social** (lupta pentru pământ între Ion și Vasile Baciu), **național** (problema românilor din Transilvania sub stăpânire austro-ungară) și **erotic** (rivalitatea dintre Ion și George Bulbuc). 
            Însă cel mai puternic rămâne **conflictul interior**, dat de imposibilitatea lui Ion de a împăca cele două „glasuri”. 
            După ce obține pământul, „Glasul iubirii” revine cu o forță distructivă, împingându-l spre Florica și, implicit, spre finalul său tragic sub loviturile de sapă ale lui George.
            """)

            st.markdown('<h2 class="titlu-sectiune">V. Concluzie</h2>', unsafe_allow_html=True)
            st.write("""
            În concluzie, <span class="highlight">"Ion"</span> rămâne o capodoperă a realismului critic prin profunzimea analizei psihologice și prin rigoarea construcției. 
            Destinul protagonistului este o lecție despre limitele lăcomiei și despre modul în care instinctele necontrolate pot duce la prăbușirea morală și biologică a individului.
            """)
        
        st.markdown('</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed:
            st.error("🔒 Secțiunea de jocuri este blocată.")
        else:
            st.subheader("🎮 Antrenament pentru Subiectul III")
            # JOCUL DE CITATE
            st.write("Cine este personajul care reprezintă 'Glasul Iubirii'?")
            q1 = st.selectbox("Alege varianta:", ["Ana", "Florica", "Savista"], index=None)
            if st.button("Verifică"):
                if q1 == "Florica":
                    st.success("Corect! +20 puncte"); st.session_state.score += 20
                else: st.error("Incorect!")
