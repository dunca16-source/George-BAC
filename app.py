import streamlit as st

# --- 1. CONFIGURARE ---
st.set_page_config(page_title="George-Bac Premium", page_icon="📚", layout="wide")

if 'score' not in st.session_state: st.session_state.score = 0
if 'subscribed' not in st.session_state: st.session_state.subscribed = False
if 'page' not in st.session_state: st.session_state.page = "🏠 Acasă"

# --- 2. DESIGN (CSS) ---
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
    st.metric("Scor", st.session_state.score)
    menu = st.radio("Meniu", ["🏠 Acasă", "📚 Biblioteca", "💎 Upgrade PRO"])
    if st.session_state.page not in ["Ion"]: st.session_state.page = menu
    st.write("---")
    if st.text_input("🔓 Cod Admin", type="password") == "george123":
        st.session_state.subscribed = True
        st.success("Acces PRO deblocat!")

# --- 4. LOGICA PAGINI ---
if st.session_state.page == "🏠 Acasă":
    st.title("Pregătire Premium Bacalaureat 🚀")
    st.write("Eseuri dezvoltate conform baremului și exerciții interactive.")
    if st.button("Deschide Biblioteca"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Opere Studiate")
    if st.button("Ion - Liviu Rebreanu"):
        st.session_state.page = "Ion"
        st.rerun()

elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion de Liviu Rebreanu – Analiză Critică Detaliată")
    
    t1, t2 = st.tabs(["📄 Eseu Complet (Subiectul III)", "🎮 Jocuri de Fixare"])

    with t1:
        # SECȚIUNEA I
        st.markdown('<div class="titlu-sectiune">I. Introducere și Contextualizare</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Apărut în anul <b>1920</b>, romanul <span class="highlight">"Ion"</span> reprezintă prima mare capodoperă a lui Liviu Rebreanu și fundamentul romanului realist-obiectiv în literatura română. Opera este un roman de tip <b>doric</b>, ce oferă o imagine panoramică asupra satului ardelean de la începutul secolului al XX-lea. Autorul înlocuiește idilizarea specifică sămănătorismului cu o viziune crudă, naturalistă, asupra realității rurale, unde pământul nu este doar o resursă, ci o condiție a demnității umane.</div>', unsafe_allow_html=True)
        
        # SECȚIUNEA II
        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea despre Lume</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală a romanului este <b>lupta pentru pământ</b>, dublată de tema destinului și a iubirii neîmplinite. Viziunea despre lume este marcată de un determinism social și biologic: într-o lume în care „pământul e totul”, personajele sunt marionete ale propriilor instincte. Perspectiva narativă este <b>obiectivă</b>, naratorul fiind un „mic demiurg” omniscient și omniprezent, care relatează detașat, fără a interveni în evoluția personajelor, respectând principiul verosimilității specifice realismului.</div>', unsafe_allow_html=True)

        if st.session_state.subscribed:
            # SECȚIUNEA III - DEZVOLTATĂ
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative – Analiză Aprofundată</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Prima scenă definitorie este <b>„Hora în sat”</b>, care funcționează ca o „harta” sociologică a localității Pripas. Ierarhia socială este prezentată prin așezarea personajelor: bogații (fruntașii) stau separat, discutând treburi politice, în timp ce tinerii joacă sub privirile vigilente ale bătrânilor. Alegerea lui Ion de a juca cu Ana, deși o iubește pe Florica, nu este un gest spontan, ci debutul unui plan premeditat. Jignirea adusă de Vasile Baciu, care îl numește pe Ion „sărăntoc”, declanșează conflictul principal, rănind orgoliul protagonistului și împingându-l spre dezumanizare.</div>', unsafe_allow_html=True)
            
            

            st.markdown('<div class="text-eseu">Cea mai celebră secvență este cea a <b>sărutării pământului</b>. Aceasta reprezintă momentul de apogeu al „Glasului pământului”. Ion, ajuns în posesia gliei prin forțarea Anei la sinucidere morală, merge pe câmp și îndeplinește un gest ritualic de o intensitate aproape mistică.</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud. Şi în sărutarea aceasta pătimaşă simţi un fior rece, ameţitor... Îl sărută cu patimă, ca pe o amantă. Şi abia acum pământul i se păru frumos, cu iarbă moale, proaspătă.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Această scenă subliniază caracterul <b>naturalist</b> al operei: pământul este personificat, devenind o forță feminină posesivă care îl înghite pe individ. Gestul lui Ion nu este unul de recunoștință, ci unul de stăpânire brutală, care anunță însă moartea sa iminentă.</div>', unsafe_allow_html=True)

            # SECȚIUNEA IV - DEZVOLTATĂ
            st.markdown('<div class="titlu-sectiune">IV. Elemente de Structură și Compoziție</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Romanul are o <b>structură circulară</b>, simetria fiind dată de descrierea drumului de la începutul și finalul operei. La început, drumul „vine” spre Pripas, invitând cititorul în universul ficțiunii, iar la final „se pierde” în șoseaua mare, sugerând indiferența cosmică a universului față de tragismul mărunt al oamenilor. Compoziția este marcată de cele două volume, <b>„Glasul pământului”</b> și <b>„Glasul iubirii”</b>, care reflectă dualitatea sufletească a lui Ion. Conflictul interior este dat de lupta dintre dorința de ascensiune socială și nevoia de împlinire erotică, un conflict pe care Ion nu îl poate rezolva decât prin moarte.</div>', unsafe_allow_html=True)

            # SECȚIUNEA V - CONCLUZIE
            st.markdown('<div class="titlu-sectiune">V. Concluzie</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">În concluzie, prin <span class="highlight">"Ion"</span>, Liviu Rebreanu creează un personaj monumental, reprezentativ pentru o întreagă clasă socială. Este un „roman-sferă”, perfect încheiat, care demonstrează că lăcomia și ignorarea laturii spirituale duc inevitabil la prăbușire. Opera rămâne un reper estetic prin rigoarea construcției și prin forța cu care portretizează mecanismele complexe ale destinului uman.</div>', unsafe_allow_html=True)
        else:
            st.warning("🔒 Restul analizei (peste 400 de cuvinte) este vizibil doar pentru ADMIN. Introdu parola în sidebar.")

    with t2:
        if st.session_state.subscribed:
            st.subheader("🏆 Provocare de Memorie")
            q = st.selectbox("Care este simbolul circularității romanului?", ["Crucea de la drum", "Drumul care intră și iese din sat", "Nunta Anei"])
            if st.button("Verifică"):
                if "Drumul" in q: st.success("Corect! Ai punctat 50 puncte."); st.session_state.score += 50
                else: st.error("Incorect!")
        else:
            st.info("Deblochează PRO pentru a accesa testele de fixare.")
