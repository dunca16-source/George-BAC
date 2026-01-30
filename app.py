import streamlit as st

# --- CONFIGURARE PAGINĂ ---
st.set_page_config(page_title="George-Bac TOTAL", page_icon="📚", layout="wide")

if 'page' not in st.session_state: st.session_state.page = "🏠 Acasă"
if 'subscribed' not in st.session_state: st.session_state.subscribed = False

def nav_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- DESIGN ---
st.markdown("""
    <style>
    .highlight { color: #FF512F; font-weight: bold; }
    .citat { font-style: italic; color: #444; background: #fff5f2; padding: 20px; border-left: 5px solid #FF512F; border-radius: 8px; margin: 20px 0; border-right: 5px solid #FF512F; }
    .titlu-sectiune { color: #1a1a1a; font-family: 'serif'; border-bottom: 2px solid #FF512F; padding-bottom: 8px; margin-top: 35px; font-weight: bold; font-size: 1.6em; }
    .text-eseu { font-size: 1.15em; line-height: 1.8; text-align: justify; color: #2c3e50; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac PRO")
    if st.button("🏠 Acasă", use_container_width=True): nav_to("🏠 Acasă")
    if st.button("📚 Biblioteca", use_container_width=True): nav_to("📚 Biblioteca")
    st.write("---")
    admin_cod = st.text_input("🔓 Cod Admin", type="password")
    if admin_cod == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL Deblocat!")

# --- PAGINA: ACASĂ ---
if st.session_state.page == "🏠 Acasă":
    st.title("George-Bac: Platforma Completă ⚡")
    st.write("Această versiune conține eseurile integrale și maratonul de 50 de grile.")
    if st.button("Deschide Biblioteca 🚀"): nav_to("📚 Biblioteca")

# --- PAGINA: BIBLIOTECA ---
elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Alege Opera")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📖 Ion (Eseu Complet + 20 Grile)"): nav_to("Ion")
    with c2:
        if st.button("📖 Enigma Otiliei (Eseu Complet + 30 Grile)"): nav_to("Enigma Otiliei")

# --- PAGINA: ION ---
elif st.session_state.page == "Ion":
    st.title("📖 Ion - Liviu Rebreanu (Analiză Integrală)")
    t1, t2 = st.tabs(["📄 Eseu Complet", "🎮 Maraton 20 Grile"])
    
    with t1:
        st.markdown('<div class="titlu-sectiune">I. Introducere și Încadrare Contextuală</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1920</b>, romanul "Ion" de Liviu Rebreanu reprezintă un punct de cotitură în literatura română, fiind considerat primul roman realist-obiectiv de valoare europeană. Acesta aparține perioadei interbelice și ilustrează perfect trăsăturile realismului: obiectivitatea naratorului omniscient, tehnica detaliului semnificativ și caracterul verosimil. Universul ficțional creat de Rebreanu oferă o veritabilă <b>monografie</b> a satului ardelean de la începutul secolului al XX-lea. Scena horei, redarea obiceiurilor de nuntă și înmormântare, precum și stratificarea socială riguroasă, îi conferă textului o profunzime documentară remarcabilă.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea despre Lume</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală este <b>patima pentru pământ</b> a țăranului român, privită ca sursă de demnitate și identitate socială. Viziunea autorului este marcată de un determinism biologic și social: personajul este produsul mediului său. Eugen Lovinescu definea protagonistul drept o „brută ingenioasă”, a cărei existență se desfășoară între două impulsuri irezistibile, sugerate de titlurile celor două volume: <b>„Glasul pământului”</b> (instinctul de stăpân) și <b>„Glasul iubirii”</b> (chemarea sufletului).</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Introdu codul admin pentru restul eseului și jocuri!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative și Simboluri</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">O secvență fundamentală este cea a <b>horei</b>, unde se manifestă conflictul social dintre „sărăntoci” și bogații satului (precum Vasile Baciu). Însă, cea mai puternică imagine rămâne <b>sărutarea pământului</b>:</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud. Şi în sărutarea aceasta pătimaşă simţi un fior rece, ameţitor... Îl sărută cu patimă, ca pe o <b>ibovnică</b>.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Acest gest ritualic marchează momentul posesiei totale, dar și începutul dezumanizării. Ion nu mai vede pământul ca pe un mijloc de existență, ci ca pe o divinitate pătimașă.</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="titlu-sectiune">IV. Structura și Particularități Compoziționale</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Romanul are o <b>structură circulară</b>, oferind simetrie prin descrierea drumului care „vine la Pripas” în incipit și drumul care „pleacă” în final, lăsând satul neschimbat, indiferent la dramele individuale. Această tehnică subliniază ideea că viața merge mai departe, iar destinul lui Ion este doar un accident într-un mecanism social implacabil.</div>', unsafe_allow_html=True)

    with t2:
        if not st.session_state.subscribed: st.error("Deblochează Premium!")
        else:
            # MARATON 20 GRILE ION
            questions = [
                ("1. Anul apariției?", ["1910", "1920", "1930"], "1920"),
                ("2. Specia literară?", ["Nuvelă", "Roman", "Basm"], "Roman"),
                ("3. Curentul literar?", ["Simbolism", "Realism", "Romantism"], "Realism"),
                ("4. Tipul naratorului?", ["Subiectiv", "Omniscient și Obiectiv", "Martor"], "Omniscient și Obiectiv"),
                ("5. Satul în care se petrece acțiunea?", ["Pripas", "Lumina", "Măgura"], "Pripas"),
                ("6. Cele două glasuri sunt:", ["Pământul și Iubirea", "Banii și Familia", "Credința și Neamul"], "Pământul și Iubirea"),
                ("7. Cum e numit Ion de Lovinescu?", ["Erou tragic", "Brută ingenioasă", "Om de prisos"], "Brută ingenioasă"),
                ("8. Ion sărută pământul ca pe o...", ["Mamă", "Sfântă", "Ibovnică"], "Ibovnică"),
                ("9. Cine este rivalul lui Ion la iubire?", ["Vasile Baciu", "George Bulbuc", "Herdelea"], "George Bulbuc"),
                ("10. Ce reprezintă scena horei?", ["Un dans simplu", "O monografie socială", "O sărbătoare religioasă"], "O monografie socială"),
                ("11. Prima victimă a lui Ion este:", ["Florica", "Ana", "Vasile"], "Ana"),
                ("12. Structura romanului este:", ["Liniară", "Circulară", "Fragmentată"], "Circulară"),
                ("13. Conflictul exterior principal?", ["Ion și George", "Ion și Vasile Baciu", "Ion și Preotul"], "Ion și Vasile Baciu"),
                ("14. Finalul prezintă drumul care:", ["Se închide", "Părăsește satul", "Se bifurcă"], "Părăsește satul"),
                ("15. Statutul social al lui Ion la început?", ["Bogat", "Sărăntoc", "Mijlăcaș"], "Sărăntoc"),
                ("16. Glasul pământului reprezintă instinctul de:", ["Supraviețuire", "Posesie", "Libertate"], "Posesie"),
                ("17. Ana se sinucide prin:", ["Otrăvire", "Spânzurare", "Înecare"], "Spânzurare"),
                ("18. Cine reprezintă intelectualitatea satului?", ["Vasile Baciu", "Familia Herdelea", "George"], "Familia Herdelea"),
                ("19. Obiectivitatea narativă presupune:", ["Detașare", "Implicare emoțională", "Opinie"], "Detașare"),
                ("20. Ion moare lovit cu:", ["O sapă", "Un cuțit", "O piatră"], "O sapă")
            ]
            for q, opts, ans in questions:
                user_ans = st.radio(q, ["Selectează..."] + opts, key=f"ion_{q}")
                if user_ans == ans: st.success("Corect!")

# --- PAGINA: ENIGMA OTILIEI ---
elif st.session_state.page == "Enigma Otiliei":
    st.title("📖 Enigma Otiliei - G. Călinescu (Analiză Integrală)")
    t_e1, t_e2 = st.tabs(["📄 Eseu Complet", "🎮 Maraton 30 Grile"])

    with t_e1:
        st.markdown('<div class="titlu-sectiune">I. Realismul Balzacian și Tehnica Detaliului</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1938</b>, romanul este o operă programatică prin care G. Călinescu demonstrează viabilitatea modelului balzacian în perioada interbelică. Trăsăturile balzaciene sunt evidente încă din <b>incipit</b>: fixarea precisă a timpului (iulie 1909) și a spațiului (București, strada Antim). <b>Tehnica detaliului</b> arhitectural este utilizată pentru a caracteriza indirect personajele; degradarea casei lui Costache Giurgiuveanu, amestecul de stiluri și zidăria veche anticipează <b>avarția</b> și declinul moral al locatarilor.</div>', unsafe_allow_html=True)
        
        

        st.markdown('<div class="titlu-sectiune">II. Titlul și Modernismul: Enigma și Pluriperspectivismul</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Titlul inițial, <i>"Părinții Otiliei"</i>, viza tema balzaciană a <b>paternității</b> (reflectată prin Costache, protectorul avar, și Pascalopol, protectorul rafinat). Titlul final, <i>"Enigma Otiliei"</i>, mută accentul pe o perspectivă modernistă. Enigma eroinei nu este un secret de fapt, ci rezultă din <b>pluriperspectivism</b> (tehnica oglinzilor paralele). Otilia este reflectată diferit în conștiința celorlalte personaje: pentru Felix, ea este idealul feminin; pentru Pascalopol, este amestecul de candoare și maturitate; pentru Aglae, este o „dezmățată” care vânează averea fratelui său.</div>', unsafe_allow_html=True)

        if not st.session_state.subscribed:
            st.warning("🔒 Deblochează analiza tipologiilor și jocurile cu codul Premium!")
        else:
            st.markdown('<div class="titlu-sectiune">III. Tipologii și Caractere Balzaciene</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Călinescu construiește personaje-tip: <br>1. <b>Costache Giurgiuveanu</b> reprezintă tipul <b>avarului</b>, dar un avar umanizat de afecțiunea pentru „feetița” lui.<br>2. <b>Stănică Rațiu</b> este tipul <b>arivistului</b>, demagogul fără scrupule care fură banii de sub perna muribundului.<br>3. <b>Aglae Tulea</b> este „baba absolută”, simbolul răutății gratuite și al invidiei.<br>4. <b>Felix Sima</b> reprezintă tânărul aflat pe drumul formării (element de <b>bildungsroman</b>).</div>', unsafe_allow_html=True)
            
            

            st.markdown('<div class="titlu-sectiune">IV. Conflictul și Semnificația Finalului</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Conflictul principal este cel pentru <b>moștenirea</b> lui Costache, o luptă acerbă între clanul Tulea și „orfanii” Felix și Otilia. Finalul este marcat de celebrul citat: <i>„Aici nu stă nimeni”</i>, sugerând că timpul a șters misterul și frumusețea de altădată, lăsând în urmă doar o realitate banală.</div>', unsafe_allow_html=True)

    with t_e2:
        if not st.session_state.subscribed: st.error("Deblochează Premium!")
        else:
            # MARATON 30 GRILE ENIGMA
            questions_e = [
                ("1. Anul apariției?", ["1920", "1938", "1944"], "1938"),
                ("2. Autorul?", ["Rebreanu", "Călinescu", "Camil Petrescu"], "Călinescu"),
                ("3. Modelul literar urmat?", ["Proustian", "Balzacian", "Stendhalian"], "Balzacian"),
                ("4. Strada unde locuiește Costache?", ["Lipscani", "Antim", "Victoriei"], "Antim"),
                ("5. Titlul inițial?", ["Felix și Otilia", "Părinții Otiliei", "Averea"], "Părinții Otiliei"),
                ("6. Cine este 'baba absolută'?", ["Otilia", "Aglae", "Aurica"], "Aglae"),
                ("7. Tipologia lui Stănică Rațiu?", ["Avarul", "Arivistul", "Inocentul"], "Arivistul"),
                ("8. Ce tehnică definește 'Enigma'?", ["Fluxul conștiinței", "Oglinzile paralele", "Monologul"], "Oglinzile paralele"),
                ("9. Felix studiază pentru a fi:", ["Avocat", "Medic", "Arhitect"], "Medic"),
                ("10. Pascalopol o vede pe Otilia ca pe:", ["O rivală", "O floare rară", "O fiică/iubită"], "O fiică/iubită"),
                ("11. Tema principală este:", ["Iubirea", "Moștenirea", "Războiul"], "Moștenirea"),
                ("12. Cine fură banii lui Costache?", ["Aglae", "Stănică Rațiu", "Felix"], "Stănică Rațiu"),
                ("13. Otilia îl părăsește pe Felix pentru a-i lăsa:", ["Banii", "Libertatea carierei", "Casa"], "Libertatea carierei"),
                ("14. Specia literară?", ["Nuvelă", "Roman", "Povestire"], "Roman"),
                ("15. Perspectiva narativă?", ["Obiectivă (dindărăt)", "Subiectivă", "Martor"], "Obiectivă (dindărăt)"),
                ("16. Ce este Aurica?", ["O orfană fericită", "Fata bătrână", "O mamă grijulie"], "Fata bătrână"),
                ("17. Titi Tulea este tipul:", ["Geniului", "Debilului mintal", "Arivistului"], "Debilului mintal"),
                ("18. Motivul central balzacian?", ["Pământul", "Moștenirea/Banii", "Codrul"], "Moștenirea/Banii"),
                ("19. Ce trăsătură are casa lui Costache?", ["Modernitate", "Degradare și hibridism", "Minimalism"], "Degradare și hibridism"),
                ("20. Cum este definit Felix?", ["Un ratat", "Un ambițios", "Un leneș"], "Un ambițios"),
                ("21. Otilia are comportament:", ["Modernist/Imprevizibil", "Rigid", "Previzibil"], "Modernist/Imprevizibil"),
                ("22. Finalul romanului este:", ["Închis", "Deschis/Melancolic", "Violent"], "Deschis/Melancolic"),
                ("23. Ce reprezintă descrierea camerei Otiliei?", ["Dezordine", "Caracterizarea feminității", "Sărăcie"], "Caracterizarea feminității"),
                ("24. Cine moare în roman?", ["Felix", "Costache", "Aglae"], "Costache"),
                ("25. Stănică Rațiu este maestru în:", ["Chirurgie", "Demagogie/Vorbit", "Pictură"], "Demagogie/Vorbit"),
                ("26. Relația Felix-Otilia este un:", ["Eșec asumat", "Succes total", "Conflict armat"], "Eșec asumat"),
                ("27. Ce element este modern?", ["Descrierea casei", "Ambiguitatea personajului", "Fixarea timpului"], "Ambiguitatea personajului"),
                ("28. Costache o strigă pe Otilia:", ["Draga mea", "Feetița", "Nepoata"], "Feetița"),
                ("29. Romanul este și un:", ["Basm", "Bildungsroman", "Eseu"], "Bildungsroman"),
                ("30. Citatul final: 'Aici...'", ["trăiește Otilia", "nu stă nimeni", "e fericirea"], "nu stă nimeni")
            ]
            for q, opts, ans in questions_e:
                user_ans = st.radio(q, ["Selectează..."] + opts, key=f"en_{q}")
                if user_ans == ans: st.success("Corect!")
