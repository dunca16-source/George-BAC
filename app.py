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

# --- 4. PAGINA ION (ESEUL TĂU COMPLET + 20 JOCURI) ---
if st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi la Bibliotecă"): st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion - Liviu Rebreanu (Analiză Completă & 20 Jocuri)")
    t1, t2 = st.tabs(["📄 Eseu Complet (Proză Realistă)", "🎮 Maraton 20 Niveluri Teorie"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Introducere și Încadrare în Context</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în anul <b>1920</b>, romanul <span class="highlight">"Ion"</span> de Liviu Rebreanu reprezintă un moment de cotitură în literatura română, fiind considerat primul roman realist-obiectiv de valoare europeană. Acesta aparține perioadei interbelice și ilustrează perfect trăsăturile realismului. Tehnica detaliului semnificativ și caracterul verosimil al acțiunii sunt elemente care incadreaza acest roman in realism. Acest univers ficțional reușește să creeze iluzia vieții. Este descris cu fidelitate satul ardelean. Situațiile de viață relatate dau impresia implicării într-o lume vie și cunoscută. Scena horei, în care se detaliază jocul tradițional, respectiv redarea obiceiurilor de nuntă și înmormântare, îi conferă textului un caracter monografic.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea despre Lume</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală a operei este <b>destinul țăranului român</b> din Ardeal la începutul secolului al XX-lea, pentru care posesia pământului reprezintă singura cale de a obține demnitatea socială. Viziunea despre lume este una aspră, dominată de determinism social și biologic: într-o lume în care „pământul e totul”, instinctele primare de supraviețuire și de mărire devin mai puternice decât legile morale. Eugen Lovinescu îl definea pe Ion drept o „brută ingenioasă”, a cărei existență este sfâșiată între două forțe opuse, simbolizate prin titlurile celor două volume: <b>„Glasul pământului”</b> și <b>„Glasul iubirii”</b>.</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile III, IV și V sunt blocate. Introdu codul Admin!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative – Analiză Aprofundată</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Un prim episod reprezentativ este cel al <b>horei</b>, scena de început a romanului. Aici este prezentată, în miniatură, întreaga structură socială a satului Pripas. Stratificarea este evidentă: bogații satului stau separat de „sărăntoci”, iar preotul Belciug și învățătorul Herdelea reprezintă intelectualitatea. Ion o alege la joc pe Ana, fata bogătașului Vasile Baciu, reprezentând primul pas dintr-un plan calculat de a obține pământ, deși inima îi aparține Floricăi.</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Un al doilea episod fundamental este cel al <b>sărutării pământului</b>. După ce Ion reușește să-l forțeze pe Vasile Baciu să-i cedeze pământurile, protagonistul merge la câmp într-o dimineață de primăvară. Gestul său de a îngenunchea și de a săruta glia este descris într-un limbaj ritualic:</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud. Şi în sărutarea aceasta pătimaşă simţi un fior rece, ameţitor... Îl sărută cu patimă, ca pe o <b>ibovnică</b>. Şi abia acum pământul i se păru frumos, cu iarbă moale, proaspătă.”</span>', unsafe_allow_html=True)
            
            st.markdown('<div class="titlu-sectiune">IV. Elemente de Structură și Compoziție</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Perspectiva narativă obiectivă, naratorul este <b>omniscient și omniprezent</b>. Romanul se remarcă printr-o <b>structură circulară</b>, bazată pe simetrie. Imaginea drumului care intră în satul Pripas la începutul cărții și drumul care părăsește satul în final, trecând pe lângă crucea strâmbă, sugerează indiferența lumii față de dramele individuale. Compozițional, textul este împărțit în cele două volume menționate anterior.</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="titlu-sectiune">V. Concluzie</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">În concluzie, prin "Ion", Liviu Rebreanu creează un personaj monumental care eșuează din cauza propriei lăcomii. Opera rămâne o capodoperă a realismului prin rigoarea construcției și prin profunzimea analizei sociale.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("🔒 Deblochează din Sidebar pentru a juca!")
        else:
            st.header("🎮 Maraton Ion (20 Nivele)")
            c1, c2 = st.columns(2)
            with c1:
                with st.expander("1. Anul și Curentul"):
                    if st.selectbox("Anul apariției?", ["1900", "1920", "1933"], key="i1") == "1920": st.success("+10 pct")
                with st.expander("2. Tema"):
                    if st.radio("Tema principală?", ["Iubirea", "Pământul"], key="i2") == "Pământul": st.success("+10 pct")
                with st.expander("3. Trasături Realiste"):
                    if "Tehnica detaliului" in st.multiselect("Alege:", ["Fantastic", "Tehnica detaliului"], key="i3"): st.success("+10 pct")
                with st.expander("4. Titlul"):
                    if st.selectbox("Titlul sugerează:", ["Un nume rar", "Caracterul reprezentativ"], key="i4") == "Caracterul reprezentativ": st.success("+10 pct")
                with st.expander("5. Structura"):
                    if st.selectbox("Forma romanului?", ["Circulară", "Liniară"], key="i5") == "Circulară": st.success("+10 pct")
                with st.expander("6. Conflict Interior"):
                    if "Glasul pământului vs iubirii" in st.radio("Lupta?", ["Glasul pământului vs iubirii", "Bani vs Familie"], key="i6"): st.success("+10 pct")
                with st.expander("7. Semnificația Horei"):
                    if "Ierarhia socială" in st.selectbox("Ce arată?", ["Dansul", "Ierarhia socială"], key="i7"): st.success("+10 pct")
                with st.expander("8. Citatul Cheie"):
                    if st.text_input("Sărută pământul ca pe o...", key="i8").lower().strip() in ["ibovnică", "ibovnica"]: st.success("+25 pct")
                with st.expander("9. Episoade Semnificative"):
                    if len(st.multiselect("Care sunt cele 2?", ["Hora", "Sărutarea", "Balul"], key="i9")) == 2: st.success("+10 pct")
                with st.expander("10. Moartea lui Ion"):
                    if "Sapa lui George" in st.radio("Cum moare?", ["Sapa lui George", "Bătaia"], key="i10"): st.success("+10 pct")
            with c2:
                with st.expander("11. Statut Social"):
                    if "Sărăntoc" in st.radio("Ion este:", ["Bogat", "Sărăntoc"], key="i11"): st.success("+10 pct")
                with st.expander("12. Statut Moral"):
                    if "Dezumanizare" in st.selectbox("Evoluția?", ["Dezumanizare", "Sfințenie"], key="i12"): st.success("+10 pct")
                with st.expander("13. Statut Psihologic"):
                    if "Instincte" in st.radio("E stăpânit de:", ["Rațiune", "Instincte"], key="i13"): st.success("+10 pct")
                with st.expander("14. Caracterizare Directă"):
                    if "Narator" in st.multiselect("Cine?", ["Narator", "Crucea"], key="i14"): st.success("+10 pct")
                with st.expander("15. Trasătură Ion"):
                    if "Harnic dar viclean" in st.radio("Caracter?", ["Leneș", "Harnic dar viclean"], key="i15"): st.success("+10 pct")
                with st.expander("16. Conflict Exterior"):
                    if "Ion - Vasile Baciu" in st.selectbox("Lupta pe pământ?", ["Ion - Vasile Baciu", "Preot - Învățător"], key="i16"): st.success("+10 pct")
                with st.expander("17. Simbolul Pământului"):
                    if "O divinitate" in st.radio("Pentru Ion e:", ["Un obiect", "O divinitate"], key="i17"): st.success("+10 pct")
                with st.expander("18. Ana"):
                    if "Jertfă" in st.radio("Rolul Anei?", ["Jertfă", "Parteneră"], key="i18"): st.success("+10 pct")
                with st.expander("19. Obiectivitatea"):
                    if "Dindărăt" in st.selectbox("Perspectiva?", ["Dindărăt", "Dinăuntru"], key="i19"): st.success("+10 pct")
                with st.expander("20. Finalul"):
                    if st.button("Finalizează ION"): st.balloons()

# --- 5. PAGINA ENIGMA OTILIEI (ESEU COMPLET + 30 JOCURI) ---
elif st.session_state.page == "Enigma Otiliei":
    if st.button("⬅️ Înapoi la Bibliotecă"): st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Enigma Otiliei - G. Călinescu (Analiză Completă & 30 Jocuri)")
    t1, t2 = st.tabs(["📄 Eseu Critic", "🎮 Maraton 30 Niveluri Teorie"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Realism Balzacian și Modernism</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1938</b>, romanul este unul realist-balzacian prin temă (moștenirea, paternitatea) și prin metoda de construcție a personajelor. G. Călinescu utilizează <b>tehnica detaliului</b> în descrierea arhitecturală a străzii Antim, descriere care devine o modalitate indirectă de caracterizare a personajelor. Modernismul operei constă în <b>ambiguitatea personajului Otilia</b>, în utilizarea <b>comportamentismului</b> și a <b>pluriperspectivismului</b> (tehnica oglinzilor paralele).</div>', unsafe_allow_html=True)
        
        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile Teoretice sunt blocate. Introdu codul Admin!")
        else:
            st.markdown('<div class="titlu-sectiune">II. Tema, Titlul și Conflictele</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Tema centrală este viața burgheziei bucureștene, axată pe <b>lupta pentru moștenire</b>. Titlul inițial, "Părinții Otiliei", viza tema balzaciană a paternității (Costache ca tată biologic, Pascalopol ca tată spiritual). "Enigma Otiliei" mută accentul pe psihologia feminină. <b>Conflictele</b> sunt multiple: cel succesorat (clanul Tulea vs. Otilia/Felix) și cel erotic (Felix vs. Pascalopol pentru inima Otiliei).</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="titlu-sectiune">III. Caracterizarea Otiliei și a Personajelor</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Otilia Mărculescu reprezintă <b>eternul feminin</b>. Ea este caracterizată prin contrast: candoare și maturitate. Felix Sima este personajul-martor, aflat pe drumul formării (bildungsroman). Tipologiile balzaciene sunt clare: <b>Costache Giurgiuveanu (avarul)</b>, <b>Aglae (baba absolută/răutatea)</b>, <b>Stănică Rațiu (arivistul)</b>. Finalul, în care Felix o reîntâlnește pe Otilia într-o fotografie, subliniază ideea că frumusețea și misterul sunt efemere.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("🔒 Deblochează din Sidebar!")
        else:
            st.header("🏆 Maraton Enigma (30 Niveluri)")
            c1, c2, c3 = st.columns(3)
            with c1:
                with st.expander("1. Anul"):
                    if st.selectbox("Când?", ["1933", "1938"], key="e1") == "1938": st.success("+5")
                with st.expander("2. Curent"):
                    if st.radio("Curent?", ["Realism balzacian", "Romantism"], key="e2") == "Realism balzacian": st.success("+5")
                with st.expander("3. Metoda Balzaciană"):
                    if st.checkbox("Tehnica detaliului", key="e3"): st.success("+5")
                with st.expander("4. Titlul Inițial"):
                    if "Părinții" in st.text_input("Cum se numea?", key="e4"): st.success("+10")
                with st.expander("5. Tema"):
                    if "Moștenirea" in st.radio("Tema?", ["Iubirea", "Moștenirea"], key="e5"): st.success("+5")
                with st.expander("6. Spațiul"):
                    if "Antim" in st.text_input("Strada?", key="e6"): st.success("+10")
                with st.expander("7. Arhitectura"):
                    if st.checkbox("Caracterizează personajul", key="e7"): st.success("+5")
                with st.expander("8. Tipologia: Avarul"):
                    if "Costache" in st.text_input("Cine e?", key="e8"): st.success("+10")
                with st.expander("9. Tipologia: Baba"):
                    if "Aglae" in st.text_input("Numele ei?", key="e9"): st.success("+10")
                with st.expander("10. Perspectiva"):
                    if "Obiectivă" in st.selectbox("Tip?", ["Obiectivă", "Subiectivă"], key="e10"): st.success("+5")
            with c2:
                with st.expander("11. Element Modern"):
                    if "Ambiguitatea" in st.radio("Ce e modern?", ["Ambiguitatea", "Timpul"], key="e11"): st.success("+10")
                with st.expander("12. Tehnica Oglinzilor"):
                    if st.checkbox("Pluriperspectivism", key="e12"): st.success("+10")
                with st.expander("13. Conflict Principal"):
                    if "Lupta pentru avere" in st.radio("Care e?", ["Lupta pentru avere", "Războiul"], key="e13"): st.success("+5")
                with st.expander("14. Arivistul"):
                    if "Stănică Rațiu" in st.text_input("Cine e?", key="e14"): st.success("+10")
                with st.expander("15. Personajul Martor"):
                    if "Felix" in st.selectbox("Cine?", ["Felix", "Titi"], key="e15"): st.success("+5")
                with st.expander("16. Bildungsroman"):
                    if st.checkbox("Maturizarea lui Felix", key="e16"): st.success("+10")
                with st.expander("17. Comportamentismul"):
                    if "Fapte și gesturi" in st.radio("Urmărește:", ["Fapte și gesturi", "Gânduri"], key="e17"): st.success("+10")
                with st.expander("18. Cine fură banii?"):
                    if "Stănică" in st.text_input("Nume hoț:", key="e18"): st.success("+15")
                with st.expander("19. Moartea lui Costache"):
                    if "Atac cerebral" in st.selectbox("Cauza?", ["Atac cerebral", "Otravă"], key="e19"): st.success("+5")
                with st.expander("20. Incipitul"):
                    if "Fixarea timpului" in st.checkbox("Baza balzaciană", key="e20"): st.success("+5")
            with c3:
                with st.expander("21. Statut Otilia"):
                    if "Orfană" in st.radio("Social:", ["Bogată", "Orfană"], key="e21"): st.success("+5")
                with st.expander("22. Caracterizare Otilia"):
                    if "Indirectă (mediu)" in st.checkbox("Exemple: haine, cameră", key="e22"): st.success("+10")
                with st.expander("23. Trasătura Otiliei"):
                    if "Altruism/Enigmă" in st.selectbox("Ce o definește?", ["Lăcomie", "Altruism/Enigmă"], key="e23"): st.success("+10")
                with st.expander("24. Felix - Meserie"):
                    if "Medic" in st.text_input("Ce devine?", key="e24"): st.success("+10")
                with st.expander("25. Relația Otilia-Pascalopol"):
                    if "Protector-iubit" in st.radio("Tipul:", ["Dușmănie", "Protector-iubit"], key="e25"): st.success("+10")
                with st.expander("26. Titi Tulea"):
                    if "Debil mintal" in st.radio("Tipologie:", ["Geniu", "Debil mintal"], key="e26"): st.success("+10")
                with st.expander("27. Aglae - Răutate"):
                    if "Invidia" in st.checkbox("Motivul față de Otilia", key="e27"): st.success("+10")
                with st.expander("28. Semnificația Finalului"):
                    if "Efemera frumusețe" in st.radio("Ideea?", ["Banii sunt totul", "Efemera frumusețe"], key="e28"): st.success("+10")
                with st.expander("29. Genul"):
                    if "Epic" in st.selectbox("Gen?", ["Epic", "Liric"], key="e29"): st.success("+5")
                with st.expander("30. Finalizarea"):
                    if st.button("Finalizează ENIGMA"): st.balloons()

# --- PAGINA ACASĂ & BIBLIOTECA ---
elif st.session_state.page == "🏠 Acasă":
    st.title("George-Bac ⚡")
    st.subheader("Platforma ta interactivă pentru nota 10 la Română")
    if st.button("Start Biblioteca"): st.session_state.page = "📚 Biblioteca"; st.rerun()

elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Alege Opera pentru Studiu")
    colA, colB = st.columns(2)
    with colA:
        if st.button("📖 Ion - Liviu Rebreanu"): st.session_state.page = "Ion"; st.rerun()
    with colB:
        if st.button("📖 Enigma Otiliei - G. Călinescu"): st.session_state.page = "Enigma Otiliei"; st.rerun()

elif st.session_state.page == "💎 Upgrade PRO":
    st.title("💎 Upgrade Premium")
    st.write("Introdu codul 'george123' în sidebar pentru deblocare.")
