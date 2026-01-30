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
    
    if menu == "🏠 Acasă": st.session_state.page = "🏠 Acasă"
    if menu == "📚 Biblioteca" and st.session_state.page not in ["Ion", "Enigma Otiliei"]: 
        st.session_state.page = "📚 Biblioteca"
    
    st.write("---")
    if st.text_input("🔓 Cod Admin", type="password") == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL deblocat!")

# --- 4. PAGINA ION (ESEUL TĂU COMPLET) ---
if st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi"): st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion - Liviu Rebreanu (Analiză & 20 Jocuri)")
    t1, t2 = st.tabs(["📄 Eseu Complet", "🎮 Maraton 20 Niveluri"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Introducere și Încadrare în Context</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în anul <b>1920</b>, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu reprezintă un moment de cotitură în literatura română, fiind considerat primul roman realist-obiectiv de valoare europeană. Acesta aparține perioadei interbelice și ilustrează perfect trăsăturile realismului. Tehnica detaliului semnificativ și caracterul verosimil al acțiunii sunt elemente care incadreaza acest roman in realism. Acest univers ficțional reușește să creeze iluzia vieții. Este descris cu fidelitate satul ardelean. Situațiile de viață relatate dau impresia implicării într-o lume vie și cunoscută. Scena horei, în care se detaliază jocul tradițional, respectiv redarea obiceiurilor de nuntă și înmormântare, îi conferă textului un caracter monografic.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea despre Lume</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală a operei este <b>destinul țăranului român</b> din Ardeal la începutul secolului al XX-lea, pentru care posesia pământului reprezintă singura cale de a obține demnitatea socială. Viziunea despre lume este una aspră, dominată de determinism social și biologic: într-o lume în care „pământul e totul”, instinctele primare de supraviețuire și de mărire devin mai puternice decât legile morale. Eugen Lovinescu îl definea pe Ion drept o „brută ingenioasă”, a cărei existență este sfâșiată între două forțe opuse, simbolizate prin titlurile celor două volume: <b>„Glasul pământului”</b> și <b>„Glasul iubirii”</b>.</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile III-V sunt blocate. Introdu codul Admin!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Un prim episod reprezentativ este cel al <b>horei</b>. Aici este prezentată întreaga structură socială a satului Pripas. Stratificarea este evidentă: bogații satului stau separat de „sărăntoci”...</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Un al doilea episod fundamental este cel al <b>sărutării pământului</b>:</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud. Şi în sărutarea aceasta pătimaşă simţi un fior rece, ameţitor... Îl sărută cu patimă, ca pe o <b>ibovnică</b>.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="titlu-sectiune">IV. Elemente de Structură și Compoziție</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Perspectiva narativă obiectivă, naratorul este <b>omniscient și omniprezent</b>. Romanul se remarcă printr-o <b>structură circulară</b>. Imaginea drumului care intră în sat la început și drumul care părăsește satul în final sugerează indiferența lumii față de dramele individuale.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("🔒 Deblochează din Sidebar!")
        else:
            # MARATON ION - 20 NIVELURI
            st.header("🎮 Maraton Ion (20 Nivele)")
            c1, c2 = st.columns(2)
            with c1:
                with st.expander("1. Apariție/Curent"):
                    if st.selectbox("An?", ["1920", "1930"], key="i1") == "1920": st.success("+10")
                with st.expander("2. Tema"):
                    if "pământ" in st.radio("Tema?", ["Iubirea", "Lupta pentru pământ"], key="i2"): st.success("+10")
                with st.expander("8. Citatul Ibovnică"):
                    if st.text_input("Ca pe o...", key="i8").lower().strip() in ["ibovnică", "ibovnica"]: st.success("+25")
                with st.expander("11. Statut Social"):
                    if "Sărăntoc" in st.radio("Ion este un:", ["Bogat", "Sărăntoc"], key="i11"): st.success("+10")
                with st.expander("12. Statut Moral"):
                    if "degradare" in st.selectbox("Evoluția?", ["asensiune", "degradare"], key="i12"): st.success("+10")
            with c2:
                with st.expander("13. Statut Psihologic"):
                    if "instincte" in st.radio("Ion e stăpânit de:", ["rațiune", "instincte"], key="i13"): st.success("+10")
                with st.expander("17. Conflict Exterior"):
                    if "Vasile Baciu" in st.selectbox("Rival pământ?", ["Vasile Baciu", "George"], key="i17"): st.success("+10")
                with st.expander("19. Semnificația Sărutului"):
                    if "posesie" in st.radio("Ce indică?", ["respect", "posesie"], key="i19"): st.success("+10")

# --- 5. PAGINA ENIGMA OTILIEI (ESEUL COMPLET ȘI 30 JOCURI) ---
elif st.session_state.page == "Enigma Otiliei":
    if st.button("⬅️ Înapoi"): st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Enigma Otiliei - G. Călinescu (Analiză & 30 Jocuri)")
    t1, t2 = st.tabs(["📄 Eseu Detaliat", "🎮 Maraton 30 Niveluri"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Realism Balzacian și Modernism</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1938</b>, romanul este unul realist-balzacian prin temă (moștenirea, paternitatea) și prin metoda de construcție a personajelor (tipologii). Totuși, G. Călinescu inserează elemente moderne precum <b>pluriperspectivismul</b> și <b>comportamentismul</b>. Descrierea minuțioasă a străzii Antim și a casei lui Moș Costache este o trăsătură balzaciană care anticipează declinul moral al personajelor.</div>', unsafe_allow_html=True)
        
        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile Teoretice sunt blocate!")
        else:
            st.markdown('<div class="titlu-sectiune">II. Tema și Semnificația Titlului</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Tema principală este viața burgheziei bucureștene, dar lucrarea este și un <b>bildungsroman</b> (maturizarea lui Felix). Titlul inițial, <i>"Părinții Otiliei"</i>, sublinia ideea de paternitate, dar "Enigma Otiliei" evidențiază caracterul misterios al eroinei, perceput diferit de fiecare personaj: Felix o vede ca pe un ideal, Pascalopol ca pe o femeie matură, iar Aglae ca pe o rivală.</div>', unsafe_allow_html=True)
            
            

            st.markdown('<div class="titlu-sectiune">III. Caracterizarea Otiliei</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Otilia Mărculescu este personajul eponim, definit prin <b>tehnica oglinzilor paralele</b>. Ea întruchipează "eternul feminin". Este caracterizată indirect prin mediul său (camera plină de parfumuri, haine, cărți), dar și prin faptele sale: îl părăsește pe Felix nu din lipsă de iubire, ci pentru a nu-i distruge cariera, alegând siguranța oferită de Pascalopol.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("🔒 Deblochează din Sidebar!")
        else:
            st.header("🏆 Maraton Enigma (30 Niveluri)")
            c1, c2, c3 = st.columns(3)
            with c1:
                with st.expander("1-10: Teorie Balzaciană"):
                    if st.selectbox("An?", ["1933", "1938"], key="e1") == "1938": st.success("+5")
                    if "Antim" in st.text_input("Strada?", key="e6"): st.success("+10")
                    if "paternității" in st.radio("Titlu inițial?", ["paternității", "iubirii"], key="e4"): st.success("+5")
                    if st.checkbox("Tehnica detaliului", key="e7"): st.success("+5")
                    if "realism" in st.radio("Curent?", ["realism", "simbolism"], key="e2"): st.success("+5")
            with c2:
                with st.expander("11-20: Modernism & Conflicte"):
                    if st.checkbox("Pluriperspectivism", key="e11"): st.success("+10")
                    if "Aglae" in st.text_input("Baba absolută?", key="e16"): st.success("+10")
                    if "Stănică" in st.text_input("Arivistul?", key="e17"): st.success("+10")
                    if "moștenirea" in st.radio("Conflict principal?", ["moștenirea", "războiul"], key="e13"): st.success("+10")
                    if "Felix" in st.radio("Personaj martor?", ["Felix", "Otilia"], key="e15"): st.success("+5")
            with c3:
                with st.expander("21-30: Caracterizare Otilia"):
                    if "Orfană" in st.radio("Statut social?", ["Bogată", "Orfană"], key="e21"): st.success("+5")
                    if "oglinzilor" in st.selectbox("Tehnica?", ["oglinzilor", "fluxului"], key="e22"): st.success("+10")
                    if "Pascalopol" in st.text_input("O vede ca pe o floare?", key="e23"): st.success("+10")
                    if "conduită" in st.radio("Caracterizare prin:", ["conduită", "vis"], key="e26"): st.success("+5")
                    if st.button("FINISH MARATON"): st.balloons()

# --- PAGINA ACASĂ & BIBLIOTECA ---
elif st.session_state.page == "🏠 Acasă":
    st.title("George-Bac ⚡")
    if st.button("Start Biblioteca"): st.session_state.page = "📚 Biblioteca"; st.rerun()

elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Alege Lecția")
    if st.button("📖 Ion"): st.session_state.page = "Ion"; st.rerun()
    if st.button("📖 Enigma Otiliei"): st.session_state.page = "Enigma Otiliei"; st.rerun()
