import streamlit as st

# --- CONFIGURARE PAGINĂ ---
st.set_page_config(page_title="George-Bac PREMIUM", page_icon="📚", layout="wide")

if 'page' not in st.session_state: st.session_state.page = "🏠 Acasă"
if 'subscribed' not in st.session_state: st.session_state.subscribed = False

def nav_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- STILURI VIZUALE ---
st.markdown("""
    <style>
    .highlight { color: #FF512F; font-weight: bold; }
    .citat { font-style: italic; color: #444; background: #fffdfa; padding: 25px; border-left: 6px solid #FF512F; border-radius: 4px; margin: 25px 0; line-height: 1.6; box-shadow: 2px 2px 10px rgba(0,0,0,0.05); }
    .titlu-sectiune { color: #1a1a1a; font-family: 'serif'; border-bottom: 3px solid #FF512F; padding-bottom: 10px; margin-top: 45px; font-weight: bold; font-size: 1.8em; text-transform: uppercase; letter-spacing: 1px; }
    .text-eseu { font-size: 1.2em; line-height: 1.9; text-align: justify; color: #1e293b; margin-bottom: 20px; }
    .intro-box { background-color: #f1f5f9; padding: 20px; border-radius: 10px; border: 1px solid #cbd5e1; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGARE SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac PRO")
    if st.button("🏠 Acasă", use_container_width=True): nav_to("🏠 Acasă")
    if st.button("📚 Biblioteca", use_container_width=True): nav_to("📚 Biblioteca")
    st.write("---")
    admin_cod = st.text_input("🔓 Cod Admin", type="password")
    if admin_cod == "george123":
        st.session_state.subscribed = True
        st.success("Acces PREMIUM Deblocat!")

# --- PAGINA: ACASĂ ---
if st.session_state.page == "🏠 Acasă":
    st.title("George-Bac: Manualul Complet Interactiv ⚡")
    st.markdown("### Bine ai venit în cea mai detaliată aplicație pentru Subiectul III.")
    st.write("Aici găsești eseurile dictate la clasă, extinse cu analiză critică și maraton de grile.")
    if st.button("Deschide Biblioteca 🚀"): nav_to("📚 Biblioteca")

# --- PAGINA: BIBLIOTECA ---
elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Selectează Opera pentru Studiu Aprofundat")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📖 ION - Liviu Rebreanu (Eseu Extins + 20 Grile)"): nav_to("Ion")
    with c2:
        if st.button("📖 ENIGMA OTILIEI - G. Călinescu (Eseu Extins + 30 Grile)"): nav_to("Enigma Otiliei")

# --- PAGINA: ION ---
elif st.session_state.page == "Ion":
    st.title("📖 Ion de Liviu Rebreanu")
    t1, t2 = st.tabs(["📄 Eseu Detaliat (Subiectul III)", "🎮 Maraton 20 Grile"])
    
    with t1:
        st.markdown('<div class="intro-box"><b>Curent:</b> Realism Obiectiv | <b>An:</b> 1920 | <b>Perspectivă:</b> Omniscientă</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="titlu-sectiune">I. Introducere și Încadrare</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1920</b>, romanul „Ion” de Liviu Rebreanu reprezintă primul roman <b>realist-obiectiv</b> din literatura română, marcând începutul modernității romanului prin detașarea naratorului și rigoarea construcției. Opera aparține curentului realist prin obiectivitate, verosimilitate, tehnica detaliului semnificativ și caracterul <b>monografic</b> al satului Pripas. Naratorul este omniscient și omniprezent, adoptând o perspectivă „dindărăt”, fără să intervină în destinele personajelor prin comentarii moralizatoare.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea despre Lume</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală este <b>patima pentru pământ</b> a țăranului român la începutul secolului al XX-lea, pentru care posesia gliei reprezintă singura cale de a-și asigura respectul comunității. Viziunea despre lume este una aspră, dominată de un <b>determinism biologic și social</b>. Personajele sunt sclavele propriilor instincte și ale contextului social. Această dualitate este sugerată de titlurile celor două volume: <b>„Glasul pământului”</b>, care simbolizează instinctul de posesiune și lăcomia, și <b>„Glasul iubirii”</b>, reprezentând chemarea sufletului și a pasiunii pentru Florica.</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Introdu codul 'george123' în sidebar pentru a vedea analiza secvențelor, structura și jocurile!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Analiza Secvențelor Reprezentative</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Un prim moment definitoriu este <b>scena horei</b> din incipit. Aceasta nu este doar un eveniment social, ci o „punere în scenă” a ierarhiei satului Pripas. Așezarea oamenilor reflectă stratificarea economică: bogații precum Vasile Baciu stau separat de „sărăntocii” precum Alexandru Glanetașu. Alegerea Anei la joc de către Ion, deși inima lui îi aparține Floricăi, marchează declanșarea intrigii.</div>', unsafe_allow_html=True)
            
            
            
            st.markdown('<div class="text-eseu">Cea mai celebră secvență este <b>sărutarea pământului</b>. După ce obține pământurile lui Vasile Baciu prin forțarea Anei la sinucidere simbolică, Ion merge pe câmp. Gestul său este descris în termeni erotici și ritualici:</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud. Şi în sărutarea aceasta pătimaşă simţi un fior rece, ameţitor... Îl sărută cu patimă, ca pe o <b>ibovnică</b>. Şi abia acum pământul i se păru frumos, cu iarbă moale, proaspătă.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Această scenă subliniază <b>dezumanizarea</b> protagonistului; pământul devine o obsesie care înlocuiește orice urmă de umanitate.</div>', unsafe_allow_html=True)

            st.markdown('<div class="titlu-sectiune">IV. Elemente de Structură și Compoziție</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Romanul este construit pe principiul <b>simetriei</b> și al <b>circularității</b>. Metafora drumului deschide și închide romanul, sugerând indiferența cosmică față de suferința umană. La început, drumul „vine” la Pripas, introducând cititorul în viața satului; la final, drumul „trece peste sat”, lăsând în urmă o comunitate neschimbată de moartea violentă a lui Ion. Compoziția este bazată pe planuri narative paralele: viața țărănimii și viața intelectualității (familia Herdelea).</div>', unsafe_allow_html=True)

            st.markdown('<div class="titlu-sectiune">V. Concluzie</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">În concluzie, „Ion” rămâne o capodoperă a literaturii române prin forța cu care portretizează un destin tragic determinat de lăcomie. Ion nu este nici erou, nici ticălos, ci un produs al societății sale, a cărui singură vină este dorința de a fi „cineva” într-o lume care nu iartă sărăcia.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("Deblochează Premium!")
        else:
            questions = [
                ("1. Anul apariției?", ["1920", "1938", "1900"], "1920"),
                ("2. Tipul naratorului?", ["Subiectiv", "Omniscient și Obiectiv", "Personaj"], "Omniscient și Obiectiv"),
                ("3. Curent literar?", ["Modernism", "Realism", "Romantism"], "Realism"),
                ("4. Satul acțiunii?", ["Măgura", "Pripas", "Lumina"], "Pripas"),
                ("5. Titlul vol. 1?", ["Glasul iubirii", "Glasul pământului"], "Glasul pământului"),
                ("6. Ion o iubește pe:", ["Ana", "Florica"], "Florica"),
                ("7. Definirea lui Lovinescu?", ["Om superior", "Brută ingenioasă"], "Brută ingenioasă"),
                ("8. Ion sărută pământul ca pe o...", ["Sfântă", "Ibovnică"], "Ibovnică"),
                ("9. Rivalul lui Ion?", ["Vasile Baciu", "George Bulbuc"], "George Bulbuc"),
                ("10. Scena monografică?", ["Nunta", "Hora"], "Hora"),
                ("11. Ana moare prin:", ["Boală", "Spânzurare"], "Spânzurare"),
                ("12. Structura romanului?", ["Circulară", "Liniară"], "Circulară"),
                ("13. Conflict exterior principal?", ["Ion - Vasile Baciu", "Ion - Preotul"], "Ion - Vasile Baciu"),
                ("14. Imaginea finală?", ["Crucea din sat", "Drumul care pleacă"], "Drumul care pleacă"),
                ("15. Statut social Ion?", ["Bogat", "Sărăntoc"], "Sărăntoc"),
                ("16. Glasul pământului e instinctul de:", ["Supraviețuire", "Posesie"], "Posesie"),
                ("17. Prima victimă a lui Ion?", ["Ana", "Florica"], "Ana"),
                ("18. Intelectualul satului?", ["Vasile", "Învățătorul Herdelea"], "Învățătorul Herdelea"),
                ("19. Obiectivitatea înseamnă:", ["Detașare", "Implicare"], "Detașare"),
                ("20. Ion moare lovit cu:", ["Toporul", "Sapa"], "Sapa")
            ]
            for q, opts, ans in questions:
                user_ans = st.radio(q, ["..."] + opts, key=f"i_{q}")
                if user_ans == ans: st.success("Corect!")

# --- PAGINA: ENIGMA OTILIEI ---
elif st.session_state.page == "Enigma Otiliei":
    st.title("📖 Enigma Otiliei - George Călinescu")
    t_e1, t_e2 = st.tabs(["📄 Eseu Detaliat (Subiectul III)", "🎮 Maraton 30 Grile"])

    with t_e1:
        st.markdown('<div class="intro-box"><b>Curent:</b> Realism Balzacian & Modernism | <b>An:</b> 1938 | <b>Tehnică:</b> Pluriperspectivism</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="titlu-sectiune">I. Geneza și Încadrarea în Realismul Balzacian</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Apărut în <b>1938</b>, romanul reprezintă o pledoarie pentru romanul de tip clasic, realist, de factură <b>balzaciană</b>. G. Călinescu respinge subiectivismul proustian și optează pentru metoda lui Honoré de Balzac: fixarea precisă a timpului (iulie 1909) și a spațiului (București, strada Antim). Trăsătura fundamentală a realismului balzacian prezentă aici este <b>tehnica detaliului semnificativ</b>. Descrierea minuțioasă a arhitecturii casei lui Costache Giurgiuveanu (hibridismul stilurilor, zidăria în paragină) nu este doar decor, ci o modalitate de <b>caracterizare indirectă</b>, anticipând amestecul de avariție și nehotărâre al locatarilor.</div>', unsafe_allow_html=True)
        
        

        st.markdown('<div class="titlu-sectiune">II. Tema și Semnificația Titlului</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală este viața burgheziei bucureștene de la începutul secolului al XX-lea, construită pe motivul <b>moștenirii</b> și al <b>paternității</b>. Inițial, autorul a dorit să numească romanul „Părinții Otiliei”, titlu ce sublinia ideea balzaciană a orfanului protejat de figuri paterne contrastante (Costache – tatăl biologic avar, Pascalopol – tatăl spiritual rafinat). Schimbarea în <b>„Enigma Otiliei”</b> aduce o notă de <b>modernism</b>, mutând accentul spre psihologia feminină insesizabilă. Enigma nu este un secret, ci provine din <b>pluriperspectivism</b>: Otilia este reflectată diferit în conștiința personajelor masculine, fiecare având „dreptatea” sa.</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Introdu codul 'george123' pentru a citi analiza tipologiilor și a finaliza maratonul de 30 de grile!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Tipologii Umane și Caracterizarea Personajelor</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">G. Călinescu creează o galerie de tipuri umane, fiecare fiind definit de o trăsătură dominantă:<br>1. <b>Costache Giurgiuveanu</b> reprezintă <b>Avarul</b>, dar unul atipic, umanizat de dragostea pentru „feetița” lui.<br>2. <b>Stănică Rațiu</b> este tipul <b>arivistului</b>, demagogul care își urmărește interesul financiar cu o vitalitate feroce.<br>3. <b>Aglae Tulea</b> este definită drept „baba absolută”, reprezentând răutatea și invidia care distruge totul în jur.<br>4. <b>Otilia Mărculescu</b> este personajul modern, caracterizat prin <b>comportamentism</b> (i se cunosc doar faptele și gesturile, nu și gândurile) și prin farmecul „eternei feminități”.</div>', unsafe_allow_html=True)
            
            

            st.markdown('<div class="titlu-sectiune">IV. Conflictul și Finalul</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Conflictul este dublu: unul de ordin <b>economic</b> (lupta clanului Tulea pentru moștenirea lui Costache) și unul de ordin <b>erotic</b> (rivalitatea dintre Felix și Pascalopol). Finalul romanului este marcat de o melancolie profundă. Reîntâlnirea lui Felix cu fotografia Otiliei de peste ani subliniază ideea că frumusețea și misterul sunt efemere: „Aici nu stă nimeni”, spune Felix în fața casei vechi, simbolizând moartea unui univers și maturizarea sa forțată.</div>', unsafe_allow_html=True)

    with t_e2:
        if not st.session_state.subscribed: st.error("Deblochează Premium!")
        else:
            eg_q = [
                ("1. Anul apariției?", ["1920", "1938", "1944"], "1938"),
                ("2. Modelul literar?", ["Proustian", "Balzacian", "Fantastic"], "Balzacian"),
                ("3. Strada unde locuiește Costache?", ["Lipscani", "Antim", "Victoriei"], "Antim"),
                ("4. Titlul inițial?", ["Părinții Otiliei", "Averea", "Moștenirea"], "Părinții Otiliei"),
                ("5. Tipologia lui Costache?", ["Arivistul", "Avarul", "Eroul"], "Avarul"),
                ("6. Cine este 'baba absolută'?", ["Otilia", "Aglae", "Aurica"], "Aglae"),
                ("7. Tipologia lui Stănică Rațiu?", ["Avarul", "Arivistul", "Victima"], "Arivistul"),
                ("8. Tehnica modernă folosită pentru Otilia?", ["Monolog", "Pluriperspectivism", "Jurnal"], "Pluriperspectivism"),
                ("9. Meseria lui Felix la final?", ["Avocat", "Medic", "Arhitect"], "Medic"),
                ("10. Pascalopol reprezintă:", ["Răutatea", "Rafinamentul", "Avariția"], "Rafinamentul"),
                ("11. Tema principală?", ["Războiul", "Moștenirea", "Natura"], "Moștenirea"),
                ("12. Cine fură banii?", ["Aglae", "Stănică Rațiu", "Titi"], "Stănică Rațiu"),
                ("13. Otilia îl părăsește pe Felix pentru:", ["Bani", "Libertatea lui", "Pascalopol"], "Libertatea lui"),
                ("14. Specia literară?", ["Nuvelă", "Roman", "Povestire"], "Roman"),
                ("15. Perspectiva narativă?", ["Obiectivă", "Subiectivă", "Martor"], "Obiectivă"),
                ("16. Cine e Aurica?", ["O orfană", "Fata bătrână", "Servitoarea"], "Fata bătrână"),
                ("17. Titi Tulea este tipul:", ["Geniului", "Debilului mintal", "Avarului"], "Debilului mintal"),
                ("18. Motivul central?", ["Pământul", "Banii", "Codrul"], "Banii"),
                ("19. Casa lui Costache arată:", ["Lux", "Degradare", "Modernitate"], "Degradare"),
                ("20. Felix este caracterizat ca:", ["Un leneș", "Un ambițios", "Un ratat"], "Un ambițios"),
                ("21. Caracterizarea Otiliei e:", ["Directă", "Comportamentistă", "Lirică"], "Comportamentistă"),
                ("22. Finalul este:", ["Fericire totală", "Melancolic", "Violent"], "Melancolic"),
                ("23. Camera Otiliei arată:", ["Sărăcie", "Personalitatea ei", "Murdărie"], "Personalitatea ei"),
                ("24. Cine moare de atac cerebral?", ["Felix", "Costache", "Pascalopol"], "Costache"),
                ("25. Stănică excelează în:", ["Chirurgie", "Demagogie", "Pictură"], "Demagogie"),
                ("26. Relația Felix-Otilia?", ["Idilă reușită", "Eșec asumat", "Căsnicie"], "Eșec asumat"),
                ("27. Element modernist?", ["Descrierea străzii", "Ambiguitatea", "Timpul fix"], "Ambiguitatea"),
                ("28. Costache o strigă pe Otilia:", ["Nepoata", "Feetița", "Otiliuța"], "Feetița"),
                ("29. Romanul este și un:", ["Basm", "Bildungsroman", "Manual"], "Bildungsroman"),
                ("30. Citatul final: 'Aici...'", ["e viața", "nu stă nimeni", "stă Otilia"], "nu stă nimeni")
            ]
            for q, opts, ans in eg_q:
                user_ans = st.radio(q, ["..."] + opts, key=f"e_{q}")
                if user_ans == ans: st.success("Corect!")
