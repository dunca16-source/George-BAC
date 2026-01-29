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
    .citat { font-style: italic; color: #444; background: #fff5f2; padding: 20px; border-left: 5px solid #FF512F; display: block; margin: 20px 0; border-radius: 8px; }
    .titlu-sectiune { color: #1a1a1a; border-bottom: 2px solid #FF512F; padding-bottom: 8px; margin-top: 35px; font-weight: bold; font-size: 1.6em; }
    .text-eseu { font-size: 1.15em; line-height: 1.8; text-align: justify; color: #2c3e50; }
    .quiz-container { background: #f8f9fa; padding: 20px; border-radius: 15px; border: 1px solid #eee; margin-bottom: 20px; }
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

# --- 4. LOGICA PAGINI ---
if st.session_state.page == "🏠 Acasă":
    st.title("George-Bac: Platforma Ta de Nota 10 🚀")
    st.write("Învață literatura prin logică și jocuri, nu prin memorare.")
    if st.button("Deschide Biblioteca"):
        st.session_state.page = "📚 Biblioteca"
        st.rerun()

elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Biblioteca de Opere")
    if st.button("📖 Ion - Liviu Rebreanu"):
        st.session_state.page = "Ion"
        st.rerun()

elif st.session_state.page == "Ion":
    if st.button("⬅️ Înapoi"):
        st.session_state.page = "📚 Biblioteca"; st.rerun()

    st.title("📖 Ion - Liviu Rebreanu (Eseu & 10 Jocuri)")
    
    t1, t2 = st.tabs(["📄 Eseu Complet", "🎮 Maratonul de Jocuri (10)"])

    with t1:
        st.markdown('<div class="titlu-sectiune">I. Introducere și Context</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Apărut în anul <b>1920</b>, romanul <span class="highlight">"Ion"</span> reprezintă prima mare capodoperă a lui Liviu Rebreanu și fundamentul romanului realist-obiectiv. Opera oferă o imagine panoramică asupra satului ardelean, unde pământul reprezintă condiția demnității umane.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="titlu-sectiune">II. Tema și Viziunea</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Tema centrală este <b>lupta pentru pământ</b>, dublată de tema destinului. Viziunea este marcată de un determinism social: personajele sunt marionete ale propriilor instincte. Perspectiva narativă este <b>obiectivă</b>, naratorul fiind un „mic demiurg” omniscient.</div>', unsafe_allow_html=True)

        if st.session_state.subscribed:
            st.markdown('<div class="titlu-sectiune">III. Secvențe Reprezentative</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Scena <b>horei</b> prezintă ierarhia satului, în timp ce <b>sărutarea pământului</b> simbolizează posesia totală și dezumanizarea.</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Îl sărută cu patimă, ca pe o amantă. Şi abia acum pământul i se păru frumos...”</span>', unsafe_allow_html=True)
            
            st.markdown('<div class="titlu-sectiune">IV. Structură</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Romanul are o <b>structură circulară</b> (drumul de la început și final) și este împărțit în: <b>„Glasul pământului”</b> și <b>„Glasul iubirii”</b>.</div>', unsafe_allow_html=True)
        else:
            st.warning("🔒 Introdu codul Admin pentru eseul complet.")

    with t2:
        if not st.session_state.subscribed:
            st.error("🔒 Introdu codul ADMIN pentru a juca cele 10 jocuri!")
        else:
            st.header("🎮 Maraton de Pregătire (10 Nivele)")

            # JOC 1: Baza Teoretică
            with st.expander("1. Test Fulger: Teorie (An & Curent)", expanded=True):
                c1, c2 = st.columns(2)
                an = c1.selectbox("În ce an a apărut romanul?", ["1910", "1920", "1933"])
                curent = c2.selectbox("Din ce curent face parte?", ["Romantism", "Realism", "Simbolism"])
                if st.button("Verifică Nivel 1"):
                    if an == "1920" and curent == "Realism": st.success("Corect! +10 pct"); st.session_state.score += 10
                    else: st.error("Mai citește introducerea!")

            # JOC 2: Tema
            with st.expander("2. Identifică Tema"):
                tema = st.radio("Care este tema principală?", ["Iubirea neîmplinită", "Lupta pentru pământ", "Războiul"])
                if st.button("Verifică Nivel 2"):
                    if tema == "Lupta pentru pământ": st.success("Bravo! +10 pct"); st.session_state.score += 10

            # JOC 3: Elementul Realist
            with st.expander("3. Elemente Realiste"):
                el = st.multiselect("Alege elementele realiste:", ["Perspectiva obiectivă", "Finalul fericit", "Tehnica detaliului", "Personaje fantastice"])
                if st.button("Verifică Nivel 3"):
                    if set(el) == {"Perspectiva obiectivă", "Tehnica detaliului"}: st.success("Corect! +20 pct"); st.session_state.score += 20

            # JOC 4: Structura
            with st.expander("4. Arhitectura Romanului"):
                struct = st.selectbox("Ce formă are structura romanului?", ["Liniară", "Circulară", "În spirală"])
                if st.button("Verifică Nivel 4"):
                    if struct == "Circulară": st.success("Perfect! +10 pct"); st.session_state.score += 10

            # JOC 5: Simboluri
            with st.expander("5. Traducătorul de Simboluri"):
                simbol = st.radio("Ce reprezintă drumul din debutul operei?", ["O simplă cale de acces", "Metafora intrării în universul ficțiunii", "O eroare de descriere"])
                if st.button("Verifică Nivel 5"):
                    if "universul ficțiunii" in simbol: st.success("Așa este! +15 pct"); st.session_state.score += 15

            # JOC 6: Personaje (Cine cu cine?)
            with st.expander("6. Potrivește Cuplurile"):
                p1 = st.selectbox("Ion se căsătorește cu:", ["Florica", "Ana", "Savista"])
                if st.button("Verifică Nivel 6"):
                    if p1 == "Ana": st.success("Corect (din interes)! +10 pct"); st.session_state.score += 10

            # JOC 7: Conflicte
            with st.expander("7. Conflictul Interior"):
                conf = st.radio("Între ce forțe se dă conflictul interior al lui Ion?", ["Vasile și George", "Glasul pământului și Glasul iubirii", "Preot și Învățător"])
                if st.button("Verifică Nivel 7"):
                    if "Glasul" in conf: st.success("Esențial pentru eseu! +20 pct"); st.session_state.score += 20

            # JOC 8: Citate
            with st.expander("8. Completează Citatul"):
                st.write("'Îl sărută cu patimă, ca pe o ...'")
                cit = st.text_input("Cuvântul lipsă (fără spații):")
                if st.button("Verifică Nivel 8"):
                    if cit.lower() == "amantă": st.success("Excelent! +25 pct"); st.session_state.score += 25

            # JOC 9: Scene cheie
            with st.expander("9. Ordinea Cronologică"):
                st.write("Care scenă este la începutul romanului?")
                scena = st.radio("Alege:", ["Moartea lui Ion", "Sărutarea pământului", "Hora în sat"])
                if st.button("Verifică Nivel 9"):
                    if scena == "Hora în sat": st.success("Corect! +10 pct"); st.session_state.score += 10

            # JOC 10: Finalul
            with st.expander("10. Concluzia Tragediei"):
                fin = st.radio("Cum moare Ion?", ["De bătrânețe", "Ucis de George cu sapa", "Se sinucide"])
                if st.button("Verifică Nivel 10"):
                    if "George" in fin: 
                        st.balloons()
                        st.success("FELICITĂRI! Ai terminat maratonul Ion! +30 pct")
                        st.session_state.score += 30
