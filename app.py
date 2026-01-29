import streamlit as st

# Configurare stil pagină
st.set_page_config(page_title="BacLogos - Ion", page_icon="📚")

# --- CSS Personalizat pentru aspect Premium ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    .highlight { background-color: #fff3cd; padding: 10px; border-left: 5px solid #ffc107; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Meniul de navigare) ---
st.sidebar.title("🚀 BacLogos v1.0")
st.sidebar.info("Pregătire Premium pentru Bacalaureat")

menu = st.sidebar.radio("Navigare", ["🏠 Acasă", "📖 Ion - L. Rebreanu", "💎 Abonament Pro"])

# --- PAGINA ACASĂ ---
if menu == "🏠 Acasă":
    st.title("Salut, viitorule student! 👋")
    st.write("Aceasta este platforma ta interactivă pentru eseuri de nota 10.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Liviu_Rebreanu_1.jpg/800px-Liviu_Rebreanu_1.jpg", width=200)
    st.warning("⚠️ În varianta gratuită ai acces doar la introducerea operelor.")

# --- PAGINA ION ---
elif menu == "📖 Ion - L. Rebreanu":
    st.title("Ion de Liviu Rebreanu")
    st.subheader("Roman Realist-Obiectiv")

    # Secțiunea 1: Gratuită
    with st.expander("1. Încadrarea în curent și context", expanded=True):
        st.write("""
        Romanul **'Ion'**, publicat în **1920**, reprezintă un prag de modernitate în literatura română.
        Este un roman **realist-obiectiv** de tip doric.
        
        **Trăsături cheie:**
        * Obiectivitatea naratorului (omniprezent și omniscient).
        * Verosimilitatea (satul Pripas).
        * Personajul tipic (țăranul a cărui valoare e dată de pământ).
        """)

    # Secțiunile 2 și 3: Blocate (Simulare Paywall)
    st.markdown("---")
    st.markdown("### 🔒 Conținut Premium")
    
    paywall = st.container()
    if 'subscribed' not in st.session_state:
        st.session_state.subscribed = False

    if not st.session_state.subscribed:
        st.error("Restul eseului (Tema, Episoadele și Structura) este disponibil doar pentru membrii Pro.")
        if st.button("Deblochează tot conținutul - 49 RON"):
            st.session_state.subscribed = True
            st.rerun()
    else:
        st.success("✅ Ai acces la varianta completă!")
        
        with st.expander("2. Tema și două episoade reprezentative"):
            st.markdown("<div class='highlight'><b>Sfat:</b> Reține citatul despre pământ pentru punctaj maxim!</div>", unsafe_allow_html=True)
            st.write("""
            **Tema:** Lupta pentru pământ într-o societate rurală stratificată.
            
            **Episodul 1: Hora de duminică.** Prefigurează conflictele și stratificarea socială.
            **Episodul 2: Sărutarea pământului.** *"Îl sărută cu patimă, ca pe o amantă"*. Gestul simbolizează posesiunea și legătura organică.
            """)

        with st.expander("3. Elemente de structură"):
            st.write("""
            * **Structură circulară:** Drumul spre Pripas apare la început și la sfârșit.
            * **Conflicte:** Exterior (Ion vs Vasile Baciu) și Interior (Glasul pământului vs Glasul iubirii).
            """)

        # --- PARTE INTERACTIVĂ ---
        st.markdown("### 🧠 Quiz Interactiv")
        raspuns = st.radio("Ce tip de roman este 'Ion'?", ["Romantic", "Realist-Obiectiv", "Modernist-Subiectiv"])
        if st.button("Verifică răspunsul"):
            if raspuns == "Realist-Obiectiv":
                st.balloons()
                st.success("Corect! Ai învățat trăsătura principală.")
            else:
                st.error("Mai citește o dată secțiunea 1!")

# --- PAGINA ABONAMENT ---
elif menu == "💎 Abonament Pro":
    st.title("Devino membru Premium")
    st.write("Obține acces la toate cele 17 eseuri structurate + Audio + Quiz-uri.")
    st.markdown("### Beneficii:")
    st.write("- ✅ Eseuri detaliate (500+ cuvinte)")
    st.write("- ✅ Scheme logice pentru memorare rapidă")
    st.write("- ✅ Suport AI 24/7 pentru întrebări")
    st.button("Plătește prin Stripe")