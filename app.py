elif current_page == "Ion":
    # Buton de navigare înapoi
    if st.button("⬅️ Înapoi la Bibliotecă"):
        st.session_state.page = "📚 Biblioteca de Opere"
        st.rerun()
        
    st.title("📖 Ion – Liviu Rebreanu")
    st.markdown("### *Primul roman realist-obiectiv din literatura română (1920)*")

    # Layout pe coloane: Stânga (Eseu), Dreapta (Interactivitate)
    col_eseu, col_interactiv = st.columns([2, 1])

    with col_eseu:
        # --- SECȚIUNEA 1: ÎNCADRARE (GRATUITĂ) ---
        with st.expander("📌 1. Încadrarea în curent și context", expanded=True):
            st.write("""
            **Context:** Publicat în **1920**, romanul deschide drumul modernizării literaturii române prin obiectivitate.
            
            **Trăsături Realiste:**
            * **Obiectivitatea naratorului:** Narator omniscient, omniprezent, care relatează detașat, „dindărăt” (viziune focalizată zero).
            * **Verosimilitatea:** Acțiunea este plasată în satul Pripas, o imagine fidelă a societății ardelene de la începutul secolului XX.
            * **Personajul tipic:** Ion este țăranul sărac a cărui demnitate depinde de posesia pământului.
            """)

        # --- VERIFICARE ABONAMENT PENTRU SECȚIUNILE 2 ȘI 3 ---
        if st.session_state.get('subscribed', False):
            # --- SECȚIUNEA 2: TEMA ȘI EPISOADELE ---
            with st.expander("🎭 2. Tema și două episoade reprezentative", expanded=True):
                st.markdown("#### **Tema: Lupta pentru pământ și iubirea neîmplinită.**")
                
                st.info("**Episodul 1: Hora de duminică.**")
                st.write("""
                Scena de început a romanului fixează ierarhia socială. Ion o alege la joc pe Ana, fata bogătașului Vasile Baciu, 
                deși o iubește pe Florica. Acest moment reprezintă declanșarea conflictului interior dintre 'glasul pământului' 
                și 'glasul iubirii'.
                """)
                
                st.info("**Episodul 2: Sărutarea pământului.**")
                st.write("""
                După obținerea pământurilor prin căsătoria cu Ana, Ion îngenunchează la câmp într-un gest de posesiune cvasi-religios. 
                *„Îl sărută cu patimă, ca pe o amantă”*. Această scenă subliniază obsesia sa și victoria (temporară) asupra condiției sociale.
                """)

            # --- SECȚIUNEA 3: ELEMENTE DE STRUCTURĂ ---
            with st.expander("🏗️ 3. Elemente de structură și limbaj", expanded=True):
                st.write("""
                * **Structura circulară:** Romanul începe și se termină cu imaginea drumului care intră și iese din satul Pripas.
                * **Compoziția:** Două părți simetrice: **'Glasul pământului'** și **'Glasul iubirii'**, urmărind decăderea morală a lui Ion.
                * **Conflictele:** - *Exterior:* Ion vs. Vasile Baciu (avere) și Ion vs. George Bulbuc (rivalitate erotică).
                    - *Interior:* Lupta între dorința de ascensiune socială și fericirea sufletească.
                """)
        else:
            # PAYWALL PENTRU UTILIZATORII NEPLĂTITORI
            st.markdown("""
                <div style="background-color: white; padding: 20px; border-radius: 10px; border: 2px dashed #FF512F; text-align: center;">
                    <h4>🔒 Conținut Blocat</h4>
                    <p>Pentru a vedea eseu complet (Tema, Episoadele și Structura), activează abonamentul <b>PRO</b> sau introdu codul de Admin.</p>
                </div>
            """, unsafe_allow_html=True)

    with col_interactiv:
        st.markdown("### 🏆 Antrenament")
        st.write("Câștigă puncte pentru scorul tău!")
        
        # QUIZ 1
        q1 = st.radio("Cine este personajul care îl ucide pe Ion?", ["Vasile Baciu", "George Bulbuc", "Preotul Belciug"], index=None)
        if st.button("Verifică Răspuns"):
            if q1 == "George Bulbuc":
                st.success("Corect! +20 Puncte")
                st.session_state.score += 20
                st.balloons()
            else:
                st.error("Incorect! -5 Puncte")
                st.session_state.score -= 5

        st.markdown("---")
        # SCHEMA VIZUALA A RELAȚIILOR
        st.write("🔍 **Relații Personaje:**")
        st.markdown("""
        - **Ion ↔ Ana:** Căsătorie din interes (Pământ).
        - **Ion ↔ Florica:** Iubire pătimașă (Regret).
        - **Ion ↔ Vasile Baciu:** Conflict social brutal.
        """)
