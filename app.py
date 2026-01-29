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
    .eseu-text { font-size: 1.15em; line-height: 1.7; color: #1a1a1a; background: white; padding: 30px; border-radius: 15px; box-shadow: 5px 5px 20px rgba(0,0,0,0.05); text-align: justify; }
    .highlight { color: #FF512F; font-weight: bold; font-style: italic; }
    .titlu-sectiune { color: #2c3e50; border-bottom: 2px solid #FF512F; padding-bottom: 5px; margin-top: 20px; }
    div.stButton > button { width: 100%; border-radius: 20px; font-weight: bold; background: linear-gradient(90deg, #FF512F, #DD2476); color: white; border: none; }
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
    st.title("Pregătit de BAC? 🚀")
    st.write("Aici găsești eseurile complete de 500+ cuvinte și jocurile care te ajută să reții structura operei.")
    if st.button("Mergi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Opere Disponibile")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Ion")
        st.caption("Liviu Rebreanu")
        if st.button("DESCHIDE ION - ESEU COMPLET"):
            st.session_state.page = "Ion"
            st.rerun()

elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

    st.title("📖 Ion - Liviu Rebreanu (Eseu Varianta Lungă)")
    
    t1, t2 = st.tabs(["📄 Eseu Detaliat (500+ cuvinte)", "🎮 Jocuri Interactive"])

    with t1:
        st.markdown('<div class="eseu-text">', unsafe_allow_html=True)
        
        st.markdown('<h3 class="titlu-sectiune">1. Încadrarea în context și curent</h3>', unsafe_allow_html=True)
        st.write("""
        Publicat în anul **1920**, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu constituie un moment de cotitură în literatura română, fiind primul roman realist-obiectiv de valoare europeană. Acesta aparține perioadei interbelice și ilustrează perfect trăsăturile realismului: perspectiva narativă obiectivă, tehnica detaliului semnificativ și caracterul verosimil al acțiunii. 
        
        Naratorul este **omniscient și omniprezent**, adoptând o viziune "dindărăt", ceea ce conferă textului un caracter impersonal. Această detașare narativă îi permite cititorului să observe mecanismele sociale și psihologice care duc la degradarea morală a personajelor, fără ca autorul să intervină cu judecăți de valoare.
        """)

        st.markdown('<h3 class="titlu-sectiune">2. Tema și viziunea despre lume</h3>', unsafe_allow_html=True)
        st.write("""
        Tema centrală a operei este **destinul țăranului român** din Ardeal la începutul secolului al XX-lea, pentru care posesia pământului reprezintă singura cale de a obține demnitatea socială. Viziunea despre lume este una aspră, dominată de determinism social și biologic: într-o lume în care "pământul e totul", instinctele primare de supraviețuire și de mărire devin mai puternice decât legile morale.
        
        Un prim episod reprezentativ este cel al **horei**, scena de început a romanului. Aici este prezentată, în miniatură, întreaga structură socială a satului Pripas. Stratificarea este evidentă: bogații satului (fruntașii) stau separat de sărăntoci, iar preotul Belciug și învățătorul Herdelea reprezintă intelectualitatea satului. Ion, un tânăr harnic, dar sărac, o alege la joc pe Ana, fata bogătașului Vasile Baciu. Această alegere nu este întâmplătoare, ci reprezintă primul pas dintr-un plan bine calculat de a obține pământ, deși Ion este atras fizic și sufletește de Florica, o fată frumoasă, dar lipsită de zestre.
        """)

        if not st.session_state.subscribed:
            st.warning("Restul eseului (Sărutarea pământului, Analiza personajului, Structura și Finalul) este blocat. Folosește codul Admin!")
        else:
            st.write("""
            Un al doilea episod fundamental este cel al **sărutării pământului**. După ce Ion reușește să-l forțeze pe Vasile Baciu să-i cedeze toate pământurile, protagonistul merge la câmp într-o dimineață de primăvară. Gestul său de a îngenunchea și de a săruta glia este descris într-un limbaj ritualic: <span class="highlight">"Îl sărută cu patimă, ca pe o amantă"</span>. Pământul încetează să mai fie un obiect de producție, devenind o forță cosmică, o divinitate în fața căreia Ion se simte acum "mare și puternic". Totuși, acest moment marchează și dezumanizarea sa totală: pentru pământ, Ion a sacrificat viața Anei și propriul echilibru interior.
            """)

            st.markdown('<h3 class="titlu-sectiune">3. Elemente de structură și compoziție</h3>', unsafe_allow_html=True)
            st.write("""
            Romanul se remarcă printr-o **structură circulară**, bazată pe simetrie. Imaginea drumului care intră în satul Pripas la începutul cărții și drumul care părăsește satul în final, trecând pe lângă crucea strâmbă de la marginea localității, sugerează indiferența lumii față de dramele individuale. Totul trece, viața merge înainte, iar moartea lui Ion nu schimbă cu nimic rânduiala satului.
            
            Compozițional, textul este împărțit în două volume cu titluri metaforice: **"Glasul pământului"** (dorința de avere) și **"Glasul iubirii"** (regretul pentru Florica). Cele două voci luptă continuu în sufletul protagonistului. Conflictul exterior este dat de lupta dintre Ion și Vasile Baciu, doi bărbați la fel de încăpățânați, în timp ce conflictul interior este drama omului care nu poate împăca instinctul de posesiune cu nevoia de fericire.
            """)

            st.markdown('<h3 class="titlu-sectiune">4. Concluzie</h3>', unsafe_allow_html=True)
            st.write("""
            În concluzie, prin <span class="highlight">"Ion"</span>, Liviu Rebreanu creează un personaj monumental, o "brută ingenioasă" (E. Lovinescu), care eșuează din cauza propriei lăcomii. Opera rămâne o capodoperă a realismului prin rigoarea construcției și prin profunzimea analizei sociale, fiind un reper obligatoriu în literatura română.
            """)
        
        st.markdown('</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed:
            st.warning("Jocurile sunt disponibile doar pentru membrii PRO / Admin!")
        else:
            st.header("🕹️ Centrul de Antrenament")
            st.subheader("1. Quiz de logică - Subiectul III")
            # Adăugăm jocuri care verifică exact ce s-a scris mai sus
            q_structura = st.radio("Ce tip de structură are romanul Ion?", ["Liniară", "Circulară", "Fragmentară"])
            if st.button("Verifică Structura"):
                if q_structura == "Circulară":
                    st.success("Corect! Simetria este dată de imaginea drumului."); st.session_state.score += 20
                else: st.error("Incorect! Recitește secțiunea 3.")
            
            st.write("---")
            st.subheader("2. Esența personajului")
            atribute = st.multiselect("Alege trăsăturile lui Ion:", ["Harnic", "Lacom", "Romantic", "Violent", "Generos"])
            if st.button("Verifică Trăsături"):
                if set(atribute) == {"Harnic", "Lacom", "Violent"}:
                    st.success("Excelent! Acestea sunt trăsăturile realiste."); st.session_state.score += 30
                else: st.warning("Ion nu este nici romantic, nici generos.")
