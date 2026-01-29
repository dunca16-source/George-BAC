import streamlit as st

# --- 1. CONFIGURARE ---
st.set_page_config(page_title="George-Bac Premium", page_icon="📚", layout="wide")

if 'score' not in st.session_state: st.session_state.score = 0
if 'subscribed' not in st.session_state: st.session_state.subscribed = False
if 'page' not in st.session_state: st.session_state.page = "🏠 Acasă"

# --- 2. DESIGN ---
st.markdown("""
    <style>
    .stApp { background: #f8f9fa; }
    .eseu-text { font-size: 1.1em; line-height: 1.6; color: #1a1a1a; background: white; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .highlight { color: #FF512F; font-weight: bold; }
    div.stButton > button { width: 100%; border-radius: 20px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac")
    st.metric("Scorul tău ⭐", st.session_state.score)
    menu = st.radio("Navigare", ["🏠 Acasă", "📚 Biblioteca", "💎 Upgrade PRO"])
    if st.session_state.page not in ["Ion"]: st.session_state.page = menu
    
    st.write("---")
    cod = st.text_input("🔓 Cod Admin", type="password")
    if cod == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL activat!")

# --- 4. PAGINI ---
if st.session_state.page == "🏠 Acasă":
    st.title("Pregătit de BAC?")
    st.write("Alege o operă din bibliotecă pentru a vedea eseul complet și jocurile.")
    if st.button("Mergi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Opere Disponibile")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Ion")
        st.write("Liviu Rebreanu")
        if st.button("DESCHIDE ION"):
            st.session_state.page = "Ion"
            st.rerun()

elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

    st.title("📖 Ion - Liviu Rebreanu (Eseu Complet)")
    
    t1, t2 = st.tabs(["📄 Eseu Detaliat", "🎮 Jocuri Interactive"])

    with t1:
        # --- ESEUL COMPLET (500+ CUVINTE) ---
        st.markdown("""
        <div class="eseu-text">
        <h3>1. Încadrarea în context și curent</h3>
        Publicat în <b>1920</b>, romanul <i>"Ion"</i> de Liviu Rebreanu este primul roman realist-obiectiv din literatura română. 
        Este un roman de tip <b>doric</b>, ce prezintă viața satului ardelean de la începutul secolului XX într-o manieră veridică. 
        Obiectivitatea este susținută de naratorul omniscient și omniprezent, care nu intervine în destinul personajelor.
        <br><br>
        <h3>2. Tema și viziunea despre lume</h3>
        Tema centrală este <b>lupta pentru pământ</b> într-o societate rurală unde averea condiționează respectul comunității. 
        Viziunea despre lume este una dură, naturalistă, unde instinctele domină rațiunea.
        <br><br>
        <p class="highlight">Episodul cheie: Hora.</p>
        Acțiunea începe duminica, la horă, unde observăm stratificarea socială: primarul și bogații stau separat, în timp ce Ion, 
        un "sărăntoc", o alege pe Ana pentru pământ, deși inima îi aparține Floricăi.
        <br><br>
        <p class="highlight">Episodul cheie: Sărutarea pământului.</p>
        După ce intră în posesia averii lui Vasile Baciu, Ion merge la câmp și îngenunchează. Gestul său simbolic 
        reprezintă victoria instinctului de posesie. "Îl sărută cu patimă, ca pe o amantă", marcând o legătură cvasi-religioasă cu glia.
        </div>
        """, unsafe_allow_html=True)
        
        if not st.session_state.subscribed:
            st.error("Restul eseului (Caracterizarea și Structura) este blocat. Folosește codul Admin!")
        else:
            st.markdown("""
            <div class="eseu-text">
            <h3>3. Elemente de structură</h3>
            Romanul are o <b>structură circulară</b>, simetria fiind dată de imaginea drumului care intră și iese din satul Pripas. 
            Este împărțit în două volume: <i>"Glasul pământului"</i> și <i>"Glasul iubirii"</i>, titluri ce reflectă 
            conflictul interior al protagonistului. 
            <br><br>
            <b>Conflictul exterior</b> se poartă între Ion și Vasile Baciu pentru pământ, iar cel interior între dorința 
            de avere și iubirea pentru Florica. Finalul tragic, uciderea lui Ion de către George Bulbuc, 
            închide destinul personajului sub semnul fatalității.
            </div>
            """, unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed:
            st.warning("Jocurile sunt disponibile doar pentru membrii PRO / Admin!")
        else:
            st.header("🕹️ Centrul de Antrenament")
            
            # JOC 1: SORTARE LOGICĂ
            st.subheader("1. Ordinea evenimentelor")
            ordine = st.multiselect("Pune scenele în ordinea corectă:", 
                ["Moartea lui Ion", "Hora în sat", "Sărutarea pământului", "Nunta cu Ana"])
            if st.button("Verifică Ordinea"):
                if ordine == ["Hora în sat", "Nunta cu Ana", "Sărutarea pământului", "Moartea lui Ion"]:
                    st.success("Bravo! +50 puncte"); st.session_state.score += 50
                else: st.error("Mai încearcă!")

            # JOC 2: IDENTIFICĂ CITATUL
            st.write("---")
            st.subheader("2. Cine a spus?")
            citat = st.radio("'Norocul e pentru cine-l caută...'", ["Ion", "Vasile Baciu", "Titu Herdelea"])
            if st.button("Verifică Citat"):
                if citat == "Ion":
                    st.success("Corect! +20 puncte"); st.session_state.score += 20
                else: st.error("Greșit!")

            # JOC 3: ASOCIERE PERSONAJE
            st.write("---")
            st.subheader("3. Potrivește destinul")
            destin = st.selectbox("Ce se întâmplă cu Ana?", ["Se mărită cu George", "Se sinucide", "Fuge cu Ion la oraș"])
            if st.button("Verifică Destin"):
                if destin == "Se sinucide":
                    st.success("E trist, dar corect. +30 puncte"); st.session_state.score += 30
