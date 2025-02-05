import streamlit as st
import utils.functions as func


def mostra():
    with st.sidebar:
        st.title("menu laterale")


        if st.button("login"):
            st.session_state.chi_loggato = "-2"
            st.session_state.pagina = "login"
            st.rerun()
    # st.session_state.errore = ""

    st.header("OrderAI")

    # CSS personalizzato
    st.markdown("""
    <style>
        .main {background-color: #f8f9fa;}
        h1 {color: #2d3436;}
        .feature-card {padding: 20px; border-radius: 10px; background: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1); min-height: 16rem; margin: 10px;}
        .pricing-card {border: 1px solid #e0e0e0; padding: 25px; border-radius: 15px; text-align: center; margin: 10px;}
        .highlight {border: 2px solid #6c5ce7; transform: scale(1.05);}
        .stButton>button {width: 100%; background: #6c5ce7; color: white;}
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("🚀 Rivoluziona la Gestione degli Ordini con l'AI")
        st.markdown(
            "**Trasforma ordini cartacei, email, PDF in dati ERP pronti all'uso**")
        st.button("Inizia la Prova Gratis →")

    with col2:
        st.image("https://via.placeholder.com/400x250?text=Demo+Interfaccia+AI",
                 use_container_width=True)

    st.divider()

    # Features Section
    st.header("✨ Perché Scegliere OrdiniElaborati.ai?")
    cols = st.columns(4)
    features = [
        ("📸", "Scatta o carica", "Qualsiasi formato ordine"),
        ("⚡", "Elaborazione immediata", "Tempo reale con AI"),
        ("🔧", "JSON personalizzato", "Integrazione ERP facile"),
        ("🛡️", "Sicurezza GDPR", "Dati protetti in UE")
    ]

    for col, (emoji, title, text) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <h2>{emoji}</h2>
                <h4>{title}</h4>
                <p>{text}</p>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # How It Works
    st.header("📲 Come Funziona?")
    steps = [
        ("1️⃣", "Carica documento", "Foto/PDF/Email"),
        ("2️⃣", "Elaborazione AI", "Riconoscimento dati"),
        ("3️⃣", "JSON strutturato", "Formato personalizzato"),
        ("4️⃣", "Integrazione ERP", "Automatica o manuale")
    ]

    cols = st.columns([0.1, 2, 2, 2, 2, 0.1])
    for i in range(1, 5):
        with cols[i]:
            emoji, title, text = steps[i-1]
            st.markdown(f"""
            <div style="text-align: center; padding: 15px">
                <div style="font-size: 40px">{emoji}</div>
                <h4>{title}</h4>
                <small>{text}</small>
            </div>
            """, unsafe_allow_html=True)

    # Demo Uploader
    with st.expander("🚀 Prova Subito - Carica un Ordine di Prova"):
        uploaded_file = st.file_uploader(
            "Carica un'immagine o PDF", type=["jpg", "png", "pdf"])
        if uploaded_file:
            st.success("✅ File caricato con successo! Elaborazione in corso...")
            # Qui andrebbe l'integrazione con il modello AI
            st.json({"ordine_id": "12345",
                    "cliente": "Esempio Srl", "articoli": [...]})

    # Pricing
    st.header("💼 Piani Tariffari")
    cols = st.columns(3)
    plans = [
        ("Starter", "29€", "500 ordini/mese", "Supporto base"),
        ("Pro", "99€", "Ordini illimitati", "Priority API", True),
        ("Enterprise", "Personalizzato", "Soluzioni su misura", "Supporto dedicato")
    ]

    for col, plan in zip(cols, plans):
        with col:
            border = "highlight" if len(plan) > 4 and plan[4] else ""
            st.markdown(f"""
            <div class="pricing-card {border}">
                <h3>{plan[0]}</h3>
                <h2>{plan[1]}</h2>
                <p>{plan[2]}</p>
                <p>{plan[3]}</p>
                <br>
                <button class="stButton">Scegli {plan[0]}</button>
            </div>
            """, unsafe_allow_html=True)

    # Footer
    st.divider()
    st.markdown("""
    <div style="text-align: center; padding: 20px">
        <small>🔒 Dati protetti con crittografia end-to-end | GDPR compliant | Supporto 24/7</small>
        <br><br>
        <p>© 2024 OrdiniElaborati.ai - P.IVA 12345678901</p>
    </div>
    """, unsafe_allow_html=True)
