import streamlit as st


def mostra():
    with st.sidebar:
        st.title("menu laterale")

        if st.button("demo"):
            st.session_state.pagina = "demo"
            st.rerun()
        
        if st.button("logout"):
            st.session_state.chi_loggato = "0"
            st.rerun()
    # st.session_state.errore = ""

    st.header("HOME")

    st.write(st.session_state.chi_loggato)

    # Configurazione della pagina
    # st.set_page_config(
    #     page_title="SmartDoc Analyzer",
    #     page_icon="🌐",
    #     layout="wide"
    # )

    # Hero Section
    st.markdown("""
    # 🌐 SmartDoc Analyzer  
    **Trasforma documenti cartacei in dati strutturati con un clic**  
    """)

    # Immagine di sfondo (simulata)
    st.image("public\img\steve-johnson-_0iV9LmPDn0-unsplash.jpg",
             caption="Confronto tra foto di documento cartaceo e dashboard digitale")
    st.markdown("""
    ### **Basta ore sprecate a copiare dati da fogli volanti o documenti scansionati**  
    La soluzione che legge ordini, fatture e listini come farebbe un essere umano... ma 10 volte più veloce e senza errori.
    """)

    # Perché Sceglierci?
    st.markdown("### 🔍 Perché Sceglierci?")
    st.markdown("""
    - **[Icona lampadina]** Hai ricevuto un ordine scritto a mano su un foglio di carta? → Diventa JSON pronto per l'ERP  
    - Il fornitore ti manda un listino PDF? → Struttura automatica in tabelle  
    - Fatture con dati sparsi? → Estrazione intelligente dei campi chiave  
    """)

    # Vantaggi Chiave
    st.markdown("### 🎯 Vantaggi Chiave")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("📸 **Scatta & Dimentica**")
        st.markdown("Usa la fotocamera del cellulare o carica scansioni")
        st.markdown("_Come avere un assistente che digitalizza al posto tuo_")
    with col2:
        st.markdown("🤖 **Intelligenza Ibrida**")
        st.markdown("Combina precisione OCR con la logica umana di GPT-4")
        st.markdown(
            "_Riconosce anche scritture disordinate e campi non standard_")
    with col3:
        st.markdown("🔄 **Integrazione Senza Sforzo**")
        st.markdown("Output in formato universale per qualsiasi sistema")
        st.markdown(
            "_Pronto per Excel, SAP, Zucchetti o software gestionali custom_")

    # Testimonianze Simulate
    st.markdown("### 👥 Testimonianze Simulate")
    st.markdown("""
    > "Con SmartDoc abbiamo ridotto del 70% il tempo di inserimento ordini"  
    > – Luca, Responsabile Amministrativo  

    > "Finalmente un sistema che capisce i nostri documenti ibridi cartaceo/digitali"  
    > – Giulia, Ufficio Acquisti  
    """)

    # Come Funziona
    st.markdown("### ⚙️ Come Funziona (Senza Tecnicismi)")
    st.markdown("""
    1. Carica il documento (foto, PDF, scansione)  
    2. Lascia lavorare l'AI (3-5 secondi)  
    3. Ottieni dati pronti all'uso  
    """)

    # Sicurezza
    st.markdown("### 🛡️ Perché è Sicuro")
    st.markdown("""
    - Elaborazione locale opzionale  
    - Nessuna conservazione dei dati  
    - Conforme al GDPR  
    """)

    # Call to Action Finale
    st.markdown("""
    ---
    ### 📞 Call to Action Finale  
    **Pronto a liberare il tuo team dal lavoro manuale?**  
    """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.link_button("Prova la Demo Live", "https://example.com/demo")
    with col2:
        st.link_button("Scarica Guida PDF", "https://example.com/guida")
    with col3:
        st.link_button("Contattaci su WhatsApp", "https://wa.me/123456789")

    if st.button("logout"):
        st.session_state.chi_loggato = "0"
        st.rerun()
        
    if st.button("demo"):
        st.session_state.pagina = "demo"
        st.rerun()
