import streamlit as st

# --- 1. CONFIGURARE ȘI SESIUNE ---
st.set_page_config(page_title="George-Bac PRO", page_icon="⚡", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = "🏠 Acasă"
if 'subscribed' not in st.session_state:
    st.session_state.subscribed = False

# Funcție pentru schimbarea paginii (rezolvă bug-ul de navigare)
def nav_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- 2. DESIGN ---
st.markdown("""
    <style>
    .highlight { color: #FF512F; font-weight: bold; }
    .citat { font-style: italic; color: #444; background: #fff5f2; padding: 20px; border-left: 5px solid #FF512F; border-radius: 8px; margin: 20px 0; }
    .titlu-sectiune { color: #1a1a1a; font-family: 'serif'; border-bottom: 2px solid #FF512F; padding-bottom: 8px; margin-top: 35px; font-weight: bold; font-size: 1.6em; }
    .text-eseu { font-size: 1.15em; line-height: 1.8; text-align: justify; color: #2c3e50; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("⚡ George-Bac PRO")
    if st.button("🏠 Acasă", use_container_width=True): nav_to("🏠 Acasă")
    if st.button("📚 Biblioteca", use_container_width=True): nav_to("📚 Biblioteca")
    st.write("---")
    admin_cod = st.text_input("🔓 Cod Admin", type="password")
    if admin_cod == "george123":
        st.session_state.subscribed = True
        st.success("Acces TOTAL Deblocat!")

# --- 4. LOGICA PAGINILOR ---

# --- ACASĂ ---
if st.session_state.page == "🏠 Acasă":
    st.title("George-Bac: Excelență în Literatură ⚡")
    st.write("Bine ai venit în aplicația de pregătire pentru Bacalaureat.")
    if st.button("Deschide Biblioteca 🚀"): nav_to("📚 Biblioteca")

# --- BIBLIOTECA ---
elif st.session_state.page == "📚 Biblioteca":
    st.title("📚 Biblioteca de Opere")
    c1, c2 = st.columns(2)
    with c1:
        st.info("REALISM OBIECTIV")
        if st.button("📖 Ion - Liviu Rebreanu"): nav_to("Ion")
    with c2:
        st.info("REALISM BALZACIAN / MODERNISM")
        if st.button("📖 Enigma Otiliei - G. Călinescu"): nav_to("Enigma Otiliei")

# --- ION ---
elif st.session_state.page == "Ion":
    st.title("📖 Ion - Liviu Rebreanu")
    tab1, tab2 = st.tabs(["📄 Eseu Detaliat", "🎮 Maraton 20 Grile"])
    
    with tab1:
        st.markdown('<div class="titlu-sectiune">I. Introducere și Realism</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1920</b>, romanul este pilonul realismului românesc. Naratorul este omniscient, oferind o imagine <b>monografică</b> a satului Pripas.</div>', unsafe_allow_html=True)
        
        
        
        if not st.session_state.subscribed:
            st.warning("🔒 Secțiunile următoare sunt blocate. Introdu codul george123 în sidebar!")
        else:
            st.markdown('<div class="titlu-sectiune">II. Tema și Glasurile</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Tema este destinul țăranului. Conflictul interior se dă între <b>Glasul pământului</b> și <b>Glasul iubirii</b>.</div>', unsafe_allow_html=True)
            st.markdown('<span class="citat">„Se aplecă şi-şi lipi buzele cu voluptate de pământul ud... Îl sărută cu patimă, ca pe o <b>ibovnică</b>.”</span>', unsafe_allow_html=True)
            st.markdown('<div class="titlu-sectiune">III. Structura Circulară</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Simetria este dată de drumul de la începutul și finalul romanului, sugerând indiferența destinului.</div>', unsafe_allow_html=True)

    with tab2:
        if not st.session_state.subscribed: st.error("Deblochează din sidebar!")
        else:
            st.subheader("Grile Ion")
            i1 = st.radio("1. Ce tip de roman este?", ["Selectează...", "Realist-Obiectiv", "Modern"], key="i1")
            if i1 == "Realist-Obiectiv": st.success("Corect!")
            i2 = st.radio("2. Cine o omoară pe Ana?", ["Selectează...", "Ea se sinucide", "Vasile Baciu"], key="i2")
            if i2 == "Ea se sinucide": st.success("Corect!")

# --- ENIGMA OTILIEI ---
elif st.session_state.page == "Enigma Otiliei":
    st.title("📖 Enigma Otiliei - G. Călinescu")
    tab_e1, tab_e2 = st.tabs(["📄 Eseu Detaliat", "🎮 Maraton 30 Grile"])
    
    with tab_e1:
        st.markdown('<div class="titlu-sectiune">I. Realism Balzacian</div>', unsafe_allow_html=True)
        st.markdown('<div class="text-eseu">Publicat în <b>1938</b>, romanul folosește metoda balzaciană: fixarea timpului, spațiului (strada Antim) și descrierea detaliată a mediului pentru a caracteriza personajele.</div>', unsafe_allow_html=True)
        
        
        
        if not st.session_state.subscribed:
            st.warning("🔒 Analiza complexă (Pluriperspectivism, Tipologii) este blocată!")
        else:
            st.markdown('<div class="titlu-sectiune">II. Titlul și Modernismul</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">Titlul „Enigma Otiliei” trimite la <b>pluriperspectivism</b>. Otilia este văzută diferit de fiecare personaj masculin (tehnica oglinzilor paralele).</div>', unsafe_allow_html=True)
            
            
            
            st.markdown('<div class="titlu-sectiune">III. Tipologii</div>', unsafe_allow_html=True)
            st.markdown('<div class="text-eseu">1. <b>Costache</b> - Avarul.<br>2. <b>Stănică Rațiu</b> - Arivistul.<br>3. <b>Aglae</b> - Baba absolută.</div>', unsafe_allow_html=True)

    with tab_e2:
        if not st.session_state.subscribed: st.error("Deblochează din sidebar!")
        else:
            st.subheader("Grile Enigma")
            e1 = st.radio("1. Strada principală?", ["Selectează...", "Antim", "Lipscani"], key="e1")
            if e1 == "Antim": st.success("Corect!")
            e2 = st.radio("2. Cine fură banii lui Costache?", ["Selectează...", "Stănică Rațiu", "Felix"], key="e2")
            if e2 == "Stănică Rațiu": st.success("Corect!")
