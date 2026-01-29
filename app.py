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
    .titlu-sectiune { color: #1a1a1a; font-family: 'Georgia', serif; border-bottom: 1px solid #eee; padding-bottom: 10px; margin-top: 30px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
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

# --- 4. LOGICA PAGINI ---
if st.session_state.page == "🏠 Acasă":
    st.title("Pregătit de BAC? 🚀")
    st.write("Eseuri complete de 500+ cuvinte și jocuri interactive.")
    if st.button("Mergi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Biblioteca George-Bac")
    col_ion, col_baltag = st.columns(2)
    with col_ion:
        st.subheader("Ion")
        st.caption("Liviu Rebreanu")
        if st.button("DESCHIDE ION"):
            st.session_state.page = "Ion"
            st.rerun()

elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion de Liviu Rebreanu – Analiză Completă")
    
    t1, t2 = st.tabs(["📄 Eseu Detaliat (Subiectul III)", "🎮 Jocuri & Teste"])

    with t1:
        # Folosim o singură variabilă mare pentru eseu ca să nu avem erori
        eseu_html = f"""
        <div class="eseu-text">
            <h2 class="titlu-sectiune">I. Introducere și Încadrare</h2>
            Publicat în <b>1920</b>, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu reprezintă un pilon fundamental al literaturii române interbelice, fiind considerat primul roman realist-obiectiv de amploare. 
            Opera este o monografie a satului ardelean de la începutul secolului al XX-lea, construită pe principiile realismului critic. 
            Naratorul este <b>omniprezent și omniscient</b>, relatând evenimentele la persoana a III-a dintr-o perspectivă detașată, neutră.
            <br><br>
            Structura este una circulară, simetria fiind oferită de imaginea drumului care „vine” și „pleacă” din satul Pripas, sugerând că viața comunității își continuă cursul imperturbabil, indiferent de tragediile individuale.

            <h2 class="titlu-sectiune">II. Tema și Viziunea despre Lume</h2>
            Tema centrală este <b>lupta pentru pământ</b> într-o societate rurală în care posesia averii condiționează statutul social. 
            Eugen Lovinescu îl definea pe Ion drept o „brută ingenioasă”, a cărei existență este sfâșiată între două forțe opuse: 
            <span class="highlight">„Glasul pământului”</span> și <span class="highlight">„Glasul iubirii”</span>. 
            Viziunea despre lume este marcată de determinism: personajul este o victimă a propriilor instincte primare.
        """

        if not st.session_state.subscribed:
            st.markdown(eseu_html + "</div>", unsafe_allow_html=True)
            st.warning("⚠️ Restul eseului este disponibil pentru membrii PRO / Admin.")
        else:
            eseu_pro = f"""
            <h2 class="titlu-sectiune">III. Secvențe Reprezentative</h2>
            Un prim episod fundamental este cel al <b>horei de duminică</b>. Această scenă de început prezintă „harta” ierarhiilor din Pripas. 
            Ion o alege la joc pe Ana, fata bogătașului Vasile Baciu, deși o iubește pe Florica. Ion sacrifică sentimentul pur pentru dorința de ascensiune socială. 
            <br><br>
            A doua secvență esențială este <b>sărutarea pământului</b>. După ce Ion obține averile lui Vasile Baciu, acesta merge la câmp și, într-un gest ritualic:
            <span class="citat">„Îl sărută cu patimă, ca pe o amantă. Şi abia acum pământul i se păru frumos...”</span> 
            Această imagine este simbolul dezumanizării: Ion a înlocuit iubirea umană cu o obsesie materială personificată.

            <h2 class="titlu-sectiune">IV. Elemente de Structură și Conflict</h2>
            Romanul este organizat în <b>13 capitole</b> cu titluri sugestive. Conflictul exterior este triplu: social, național și erotic. 
            Însă cel mai puternic rămâne <b>conflictul interior</b>, dat de imposibilitatea lui Ion de a împăca cele două „glasuri”. 
            După ce obține pământul, „Glasul iubirii” revine distructiv, împingându-l spre Florica și spre finalul tragic.

            <h2 class="titlu-sectiune">V. Concluzie</h2>
            În concluzie, <span class="highlight">"Ion"</span> rămâne o capodoperă a realismului prin profunzimea analizei psihologice. 
            Destinul protagonistului este o lecție despre limitele lăcomiei și despre modul în care instinctele necontrolate duc la prăbușirea morală.
        </div>
            """
            st.markdown(eseu_html + eseu_pro, unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed:
            st.error("🔒 Jocuri blocate.")
        else:
            st.subheader("🎮 Testează-ți cunoștințele")
            q1 = st.radio("Câte volume are romanul?", ["1", "2", "3"])
            if st.button("Verifică"):
                if q1 == "2": st.success("Corect! Glasul Pământului și Glasul Iubirii."); st.session_state.score += 20
                else: st.error("Incorect!")

elif st.session_state.page == "💎 Upgrade PRO":
    st.title("Devino PRO")
    if st.button("Deblochează totul"):
        st.session_state.subscribed = True
        st.rerun()
