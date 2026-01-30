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

    st.title("📖 Ion - Liviu Rebreanu (Analiză Completă & Maraton 20 Jocuri)")
    
    t1, t2 = st.tabs(["📄 Eseu Detaliat (500+ cuvinte)", "🎮 Maratonul de Jocuri (20 Niveluri)"])

    with t1:
        # I. Introducere
        st.markdown('<div class="titlu-sectiune">I. Introducere și Încadrare în Context</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în anul <b>1920</b>, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu reprezintă un moment de cotitură în literatura română, fiind considerat primul roman realist-obiectiv de valoare europeană. Acesta aparține perioadei interbelice și ilustrează perfect trăsăturile realismului. Tehnica detaliului semnificativ și caracterul verosimil al acțiunii sunt elemente care incadreaza acest roman in realism. Acest univers ficțional reușește să creeze iluzia vieții. Este descris cu fidelitate satul ardelean. Situațiile de viață relatate dau impresia implicării într-o lume vie și cunoscută. Scena horei, în care se detaliază jocul tradițional, respectiv redarea obiceiurilor de nuntă și înmormântare, îi conferă textului un caracter monografic.</div>', unsafe_allow_html=True)
        
        # II. Tema
        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea despre Lume</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală a operei este <b>destinul țăranului român</b> din Ardeal la începutul secolului al XX-lea, pentru care posesia pământului reprezintă singura cale de a obține demnitatea socială. Viziunea despre lume este una aspră, dominată de determinism social și biologic: într-o lume în care „pământul e totul”, instinctele primare de supraviețuire și de mărire devin mai puternice decât legile morale. Eugen Lovinescu îl definea pe Ion drept o „brută ingenioasă”, a cărei existență este sfâșiată între două forțe opuse, simbolizate prin titlurile celor două volume: <b>„Glasul pământului”</b> și <b>„Glasul iubirii”</b>.</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile III, IV și V sunt blocate. Introdu codul Admin!")
        else:
            # III. Secvente
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative – Analiză Aprofundată</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Un prim episod reprezentativ este cel al <b>horei</b>, scena de început a romanului. Aici este prezentată, în miniatură, întreaga structură socială a satului Pripas. Stratificarea este evidentă: bogații satului stau separat de „sărăntoci”, iar preotul Belciug și învățătorul Herdelea reprezintă intelectualitatea. Ion o alege la joc pe Ana, fata bogătașului Vasile Baciu, reprezentând primul pas dintr-un plan calculat de a obține pământ, deși inima îi aparține Floricăi.</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="text-eseu">Un al doilea episod fundamental este cel al <b>sărutării pământului</b>. După ce Ion reușește să-l forțeze pe Vasile Baciu să-i cedeze pământurile, protagonistul merge la câmp într-o dimineață de primăvară. Gestul său de a îngenunchea și de a săruta glia este descris într-un limbaj ritualic:</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud. Şi în sărutarea aceasta pătimaşă simţi un fior rece, ameţitor... Îl sărută cu patimă, ca pe o <b>ibovnică</b>. Şi abia acum pământul i se păru frumos, cu iarbă moale, proaspătă.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Această imagine este simbolul dezumanizării: Ion a înlocuit iubirea umană cu o obsesie materială personificată. Pământul încetează să mai fie un obiect, devenind o divinitate în fața căreia Ion se simte „mare și puternic”.</div>', unsafe_allow_html=True)

            # IV. Structura
            st.markdown('<div class="titlu-sectiune">IV. Elemente de Structură și Compoziție</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Perspectiva narativă obiectivă, naratorul este <b>omniscient și omniprezent</b>, adoptând o viziune „dindărăt”. Romanul se remarcă printr-o <b>structură circulară</b>, bazată pe simetrie. Imaginea drumului care intră în satul Pripas la începutul cărții și drumul care părăsește satul în final, trecând pe lângă crucea strâmbă, sugerează indiferența lumii față de dramele individuale. Compozițional, textul este împărțit în cele două volume menționate anterior, care reflectă conflictul interior dintre dorința de avere și nevoia de fericire. Conflictul exterior este dat de lupta dintre Ion și Vasile Baciu, în timp ce finalul tragic, uciderea lui Ion de către George Bulbuc, închide destinul personajului sub semnul fatalității.</div>', unsafe_allow_html=True)
            
            # V. Concluzie
            st.markdown('<div class="titlu-sectiune">V. Concluzie</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">În concluzie, prin <span class="highlight">"Ion"</span>, Liviu Rebreanu creează un personaj monumental care eșuează din cauza propriei lăcomii. Opera rămâne o capodoperă a realismului prin rigoarea construcției și prin profunzimea analizei sociale, fiind un reper obligatoriu în literatura română care demonstrează că ignorarea laturii spirituale duce inevitabil la prăbușire.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed:
            st.error("🔒 Maratonul de jocuri este blocat. Introdu codul ADMIN!")
        else:
            st.header("🎮 Maratonul Teoretic Ion (20 Niveluri)")
            
            # --- JOCURILE 1-10 (Existente) ---
            c1, c2 = st.columns(2)
            with c1:
                with st.expander("1. Anul și Curentul"):
                    if st.selectbox("Anul apariției?", ["1900", "1920", "1933"]) == "1920": st.success("+10 pct")
                with st.expander("2. Tema"):
                    if st.radio("Tema principală?", ["Iubirea", "Pământul", "Familia"]) == "Pământul": st.success("+10 pct")
                with st.expander("3. Caracteristici Realiste"):
                    if "Tehnica detaliului" in st.multiselect("Alege:", ["Fantastic", "Tehnica detaliului"]): st.success("+10 pct")
                with st.expander("4. Structura"):
                    if st.selectbox("Forma romanului?", ["Circulară", "Liniară"]) == "Circulară": st.success("+10 pct")
                with st.expander("5. Volumele"):
                    if len(st.multiselect("Titlurile?", ["Glasul Pământului", "Glasul Iubirii", "Glasul Cerului"])) == 2: st.success("+10 pct")

            with c2:
                with st.expander("6. Simbolul Drumului"):
                    if "universul ficțiunii" in st.radio("Semnificație?", ["Simplu drum", "Intrarea în universul ficțiunii"]): st.success("+10 pct")
                with st.expander("7. Conflictul Ion-George"):
                    if st.selectbox("Miza conflictului?", ["Florica", "Banii", "Oile"]) == "Florica": st.success("+10 pct")
                with st.expander("8. Citatul Cheie (Ibovnică)"):
                    if st.text_input("Sărută pământul ca pe o...", key="q8").lower().strip() in ["ibovnică", "ibovnica"]: st.success("+25 pct")
                with st.expander("9. Ana"):
                    if st.radio("Finalul Anei?", ["Sinucidere", "Nuntă"]) == "Sinucidere": st.success("+10 pct")
                with st.expander("10. Moartea lui Ion"):
                    if "sapa" in st.radio("Cum moare?", ["Sapa lui George", "Bătaia preotului"]): st.success("+10 pct")

            st.markdown("---")
            st.subheader("🔥 Niveluri Noi: Teoria Personajului și Conflicte")

            # --- JOCURILE 11-20 (Noi) ---
            colA, colB = st.columns(2)
            with colA:
                with st.expander("11. Statutul Social"):
                    statut = st.radio("La început, Ion este un:", ["Țăran bogat", "Țăran sărac (sărăntoc)", "Intelectual"])
                    if statut == "Țăran sărac (sărăntoc)": st.success("Corect! +10 pct")

                with st.expander("12. Statutul Moral"):
                    moral = st.selectbox("Evoluția morală a lui Ion este:", ["O ascensiune spirituală", "O degradare (dezumanizare)", "Rămâne neschimbat"])
                    if "degradare" in moral: st.success("Corect! Sacrifică tot pentru pământ. +10 pct")

                with st.expander("13. Statutul Psihologic"):
                    psih = st.radio("Ion este un personaj:", ["Simplist", "Complex, stăpânit de instincte", "Idealizat"])
                    if "Complex" in psih: st.success("Corect! Sfâșiat de 'glasuri'. +10 pct")

                with st.expander("14. Caracterizarea Directă"):
                    direct = st.multiselect("Cine îl caracterizează direct pe Ion?", ["Naratorul", "Alte personaje", "El însuși (autocaracterizare)", "Dumnezeu"])
                    if set(direct) == {"Naratorul", "Alte personaje", "El însuși (autocaracterizare)"}: st.success("Bravo! +20 pct")

                with st.expander("15. Trăsături Realiste (Obiectivitate)"):
                    obj = st.radio("Cum este vocea naratorului?", ["Implicată emoțional", "Detașată, obiectivă", "Subiectivă"])
                    if "obiectivă" in obj: st.success("Specific realismului! +10 pct")

            with colB:
                with st.expander("16. Semnificația Horei"):
                    hora = st.selectbox("Ce rol are scena horei?", ["Simpla distracție", "Prezentarea ierarhiei sociale", "Decor de nuntă"])
                    if "ierarhiei" in hora: st.success("Corect! Monografia satului. +15 pct")

                with st.expander("17. Conflictul Exterior Principal"):
                    conf_ext = st.radio("Conflictul pentru pământ se dă între:", ["Ion și George", "Ion și Vasile Baciu", "Ion și Preotul Belciug"])
                    if "Vasile Baciu" in conf_ext: st.success("Corect! Socrul vs Ginerele. +10 pct")

                with st.expander("18. Titlul Romanului"):
                    titlu = st.selectbox("Titlul 'Ion' sugerează:", ["Un nume rar", "Caracterul reprezentativ (exponent al clasei sale)", "O poreclă"])
                    if "reprezentativ" in titlu: st.success("Erou eponim! +10 pct")

                with st.expander("19. Semnificația Sărutării"):
                    sarut = st.radio("Sărutarea pământului reprezintă:", ["Respectul pentru natură", "Instinctul de posesie și contopirea cu lutul", "O glumă"])
                    if "posesie" in sarut: st.success("Perfect pentru eseu! +20 pct")

                with st.expander("20. Trăsătura Dominantă a lui Ion"):
                    dom = st.selectbox("Care este trăsătura care îl definește?", ["Lenea", "Pasiunea devorantă (pentru pământ)", "Bunătatea"])
                    if "Pasiunea" in dom: 
                        st.balloons()
                        st.success("EXCELENT! Ai terminat toate cele 20 de niveluri!")
                        st.session_state.score += 50

# Pagini Restante
elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Biblioteca")
    if st.button("📖 Ion - Liviu Rebreanu"): st.session_state.page = "Ion"; st.rerun()
elif st.session_state.page == "🏠 Acasă":
    st.title("George-Bac ⚡")
    if st.button("Start"): st.session_state.page = "📚 Biblioteca"; st.rerun()
