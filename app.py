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
    .citat { font-style: italic; color: #444; background: #fff5f2; padding: 20px; border-left: 5px solid #FF512F; display: block; margin: 20px 0; border-radius: 8px; line-height: 1.6; }
    .titlu-sectiune { color: #1a1a1a; font-family: 'serif'; border-bottom: 2px solid #FF512F; padding-bottom: 8px; margin-top: 35px; font-weight: bold; font-size: 1.6em; }
    .text-eseu { font-size: 1.15em; line-height: 1.8; text-align: justify; color: #2c3e50; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac")
    st.metric("Puncte George ⭐", st.session_state.score)
    menu = st.radio("Meniu", ["🏠 Acasă", "📚 Biblioteca", "💎 Upgrade PRO"])
    if st.session_state.page not in ["Ion"]: st.session_state.page = menu
    st.write("---")
    if st.text_input("🔓 Cod Admin", type="password") == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL deblocat!")

# --- 4. PAGINA ION ---
if st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion - Liviu Rebreanu (Analiză Completă & Maraton 10 Jocuri)")
    
    t1, t2 = st.tabs(["📄 Eseu Detaliat (500+ cuvinte)", "🎮 Maratonul de Jocuri (10 Niveluri)"])

    with t1:
        # --- ESEUL COMPLET ȘI NESCHIMBAT (doar cuvântul corectat) ---
        st.markdown('<div class="titlu-sectiune">I. Introducere și Încadrare în Context</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în anul <b>1920</b>, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu reprezintă un moment de cotitură în literatura română, fiind considerat primul roman realist-obiectiv de valoare europeană. Acesta aparține perioadei interbelice și ilustrează perfect trăsăturile realismului. Perspectiva narativă obiectivă, heterodiegetică, tehnica detaliului semnificativ și caracterul verosimil al acțiunii sunt elemente  care incadreaza acest roman in realism. El onstruieste un univers ficțional care reușește să creeze iluzia vieții. Este descris cu fidelitate satul ardelean. Situațiile de viață relatate dau impresia implicării într-o lume vie și cunoscută. Scena horei, în care se detaliază jocul tradițional, respectiv redarea obiceiurilor de nuntă și înmormântare, îi conferă textului un caracter monografic. Naratorul este <b>omniscient și omniprezent</b>, adoptând o viziune „dindărăt”, ceea ce conferă textului un caracter impersonal. Această detașare narativă îi permite cititorului să observe mecanismele sociale și psihologice care duc la degradarea morală a personajelor, fără ca autorul să intervină cu judecăți de valoare.</div>', unsafe_allow_html=True)

        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea despre Lume</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală a operei este <b>destinul țăranului român</b> din Ardeal la începutul secolului al XX-lea, pentru care posesia pământului reprezintă singura cale de a obține demnitatea socială. Viziunea despre lume este una aspră, dominată de determinism social și biologic: într-o lume în care „pământul e totul”, instinctele primare de supraviețuire și de mărire devin mai puternice decât legile morale. Eugen Lovinescu îl definea pe Ion drept o „brută ingenioasă”, a cărei existență este sfâșiată între două forțe opuse, simbolizate prin titlurile celor două volume: <b>„Glasul pământului”</b> și <b>„Glasul iubirii”</b>.</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile III, IV și V sunt blocate. Introdu codul Admin!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative – Analiză Aprofundată</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Un prim episod reprezentativ este cel al <b>horei</b>, scena de început a romanului. Aici este prezentată, în miniatură, întreaga structură socială a satului Pripas. Stratificarea este evidentă: bogații satului stau separat de „sărăntoci”, iar preotul Belciug și învățătorul Herdelea reprezintă intelectualitatea. Ion o alege la joc pe Ana, fata bogătașului Vasile Baciu, reprezentând primul pas dintr-un plan calculat de a obține pământ, deși inima îi aparține Floricăi.</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="text-eseu">Un al doilea episod fundamental este cel al <b>sărutării pământului</b>. După ce Ion reușește să-l forțeze pe Vasile Baciu să-i cedeze pământurile, protagonistul merge la câmp într-o dimineață de primăvară. Gestul său de a îngenunchea și de a săruta glia este descris într-un limbaj ritualic:</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud. Şi în sărutarea aceasta pătimaşă simţi un fior rece, ameţitor... Îl sărută cu patimă, ca pe o <b>ibovnică</b>. Şi abia acum pământul i se păru frumos, cu iarbă moale, proaspătă.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Această imagine este simbolul dezumanizării: Ion a înlocuit iubirea umană cu o obsesie materială personificată. Pământul încetează să mai fie un obiect, devenind o divinitate în fața căreia Ion se simte „mare și puternic”.</div>', unsafe_allow_html=True)

            st.markdown('<div class="titlu-sectiune">IV. Elemente de Structură și Compoziție</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Romanul se remarcă printr-o <b>structură circulară</b>, bazată pe simetrie. Imaginea drumului care intră în satul Pripas la începutul cărții și drumul care părăsește satul în final, trecând pe lângă crucea strâmbă, sugerează indiferența lumii față de dramele individuale. Compozițional, textul este împărțit în cele două volume menționate anterior, care reflectă conflictul interior dintre dorința de avere și nevoia de fericire. Conflictul exterior este dat de lupta dintre Ion și Vasile Baciu, în timp ce finalul tragic, uciderea lui Ion de către George Bulbuc, închide destinul personajului sub semnul fatalității.</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="titlu-sectiune">V. Concluzie</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">În concluzie, prin <span class="highlight">"Ion"</span>, Liviu Rebreanu creează un personaj monumental care eșuează din cauza propriei lăcomii. Opera rămâne o capodoperă a realismului prin rigoarea construcției și prin profunzimea analizei sociale, fiind un reper obligatoriu în literatura română care demonstrează că ignorarea laturii spirituale duce inevitabil la prăbușire.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed:
            st.error("🔒 Maratonul de 10 jocuri este blocat. Introdu codul ADMIN!")
        else:
            st.header("🎮 Maratonul de Pregătire Ion (10 Nivele)")
            
            with st.expander("1. Anul Apariției și Curentul Literar"):
                an = st.selectbox("În ce an a apărut Ion?", ["1900", "1920", "1945"])
                curent = st.selectbox("În ce curent literar se încadrează?", ["Realism", "Romantism", "Modernism"])
                if st.button("Verifică Nivel 1"):
                    if an == "1920" and curent == "Realism": st.success("Correct! +10 pct"); st.session_state.score += 10
            
            with st.expander("2. Identificarea Temei"):
                tema = st.radio("Care este tema principală a operei?", ["Războiul", "Lupta pentru pământ", "Condiția intelectualului"])
                if st.button("Verifică Nivel 2"):
                    if tema == "Lupta pentru pământ": st.success("Correct! +10 pct"); st.session_state.score += 10

            with st.expander("3. Caracteristici Realiste"):
                er = st.multiselect("Alege elementele realiste prezente:", ["Perspectivă obiectivă", "Final fericit", "Tehnica detaliului", "Personaje fantastice"])
                if st.button("Verifică Nivel 3"):
                    if set(er) == {"Perspectivă obiectivă", "Tehnica detaliului"}: st.success("Correct! +20 pct"); st.session_state.score += 20

            with st.expander("4. Arhitectura Romanului"):
                structura = st.selectbox("Cum este structura romanului?", ["Circulară", "Liniară", "Hachurată"])
                if st.button("Verifică Nivel 4"):
                    if structura == "Circulară": st.success("Correct! +10 pct"); st.session_state.score += 10

            with st.expander("5. Cele două volume"):
                vol = st.multiselect("Care sunt titlurile celor două volume?", ["Glasul iubirii", "Glasul sângelui", "Glasul pământului", "Glasul datoriei"])
                if st.button("Verifică Nivel 5"):
                    if set(vol) == {"Glasul iubirii", "Glasul pământului"}: st.success("Correct! +20 pct"); st.session_state.score += 20

            with st.expander("6. Simbolul Drumului"):
                drum = st.radio("Ce sugerează descrierea drumului de la început?", ["O eroare geografică", "Intrarea în universul ficțiunii", "Graba naratorului"])
                if st.button("Verifică Nivel 6"):
                    if "ficțiunii" in drum: st.success("Correct! +15 pct"); st.session_state.score += 15

            with st.expander("7. Conflictul principal"):
                rival = st.selectbox("Cine este rivalul principal al lui Ion pentru Florica?", ["Vasile Baciu", "George Bulbuc", "Titu Herdelea"])
                if st.button("Verifică Nivel 7"):
                    if rival == "George Bulbuc": st.success("Correct! +10 pct"); st.session_state.score += 10

            # --- NIVEL 8 REPARAT CU IBOVNICĂ ---
            with st.expander("8. Analiză de text (Citat)", expanded=True):
                st.write("'Îl sărută cu patimă, ca pe o ...'")
                r8 = st.text_input("Scrie cuvântul lipsă aici:", key="q8_input")
                if st.button("Verifică Nivel 8"):
                    if r8.lower().strip() in ["ibovnică", "ibovnica"]:
                        st.success("BRAVO! Ai reținut termenul exact al lui Rebreanu. +25 pct")
                        st.session_state.score += 25
                    else:
                        st.error("Incorect. Gândește-te la termenul regional/arhaic folosit în text.")

            with st.expander("9. Destinul Anei"):
                ana = st.radio("Ce se întâmplă cu Ana în final?", ["Pleacă la oraș", "Se sinucide", "Se recăsătorește"])
                if st.button("Verifică Nivel 9"):
                    if ana == "Se sinucide": st.success("Correct! +15 pct"); st.session_state.score += 15

            with st.expander("10. Deznodământul"):
                final = st.radio("Cum moare protagonistul?", ["Bătrân și bogat", "Ucis de George cu sapa", "Accident"])
                if st.button("Verifică Nivel 10"):
                    if "George" in final:
                        st.balloons()
                        st.success("FELICITĂRI! Maraton Ion completat! +30 pct")
                        st.session_state.score += 30

elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Biblioteca")
    if st.button("📖 Ion - Liviu Rebreanu"):
        st.session_state.page = "Ion"; st.rerun()

elif st.session_state.page == "🏠 Acasă":
    st.title("George-Bac ⚡")
    if st.button("Deschide Biblioteca"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()



