import streamlit as st
import utils.functions as func
from streamlit.components.v1 import html


def inject_custom_css():
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;500;700&display=swap');
        
        * {{font-family: 'Inter', sans-serif !important;}}
        
        .main {{
            background: #f8fafc;
        }}
        
        .hero {{
            background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
            padding: 6rem 2rem;
            border-radius: 0 0 30px 30px;
            color: white !important;
        }}
        
        .feature-icon {{
            width: 64px;
            height: 64px;
            background: #e0e7ff;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.5rem;
        }}
        
        .pricing-card {{
            transition: all 0.3s cubic-bezier(.25,.8,.25,1);
            border: 1px solid #e2e8f0;
            border-radius: 24px;
            overflow: hidden;
        }}
        
        .pricing-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
        }}
        
        .demo-preview {{
            border-radius: 24px;
            overflow: hidden;
            border: 1px solid #e2e8f0;
            background: white;
        }}
    </style>
    """, unsafe_allow_html=True)


def mostra():
    with st.sidebar:
        st.title("menu laterale")

        if st.button("login"):
            st.session_state.chi_loggato = "-2"
            st.session_state.pagina = "login"
            st.rerun()
    # st.session_state.errore = ""

    st.header("OrderAI")

# Configurazione stile avanzata
    inject_custom_css()

    # Hero Section
    st.markdown("""
    <div class="hero">
        <div style="max-width:1200px; margin:auto">
            <div style="display: flex; flex-direction: column; gap: 2rem">
                <h1 style="font-size: 3.5rem; margin:0; color:white!important">Automazione Ordini<br>Potenziata dall'AI</h1>
                <p style="font-size: 1.4rem; color: #e0e7ff!important">Trasforma qualsiasi formato d'ordine in dati strutturati<br>con un'accuratezza del 99.9%</p>
                <div>
                    <button style="
                        background: white;
                        color: #4f46e5;
                        border: none;
                        padding: 1rem 2rem;
                        border-radius: 12px;
                        font-weight: bold;
                        cursor: pointer;
                        transition: transform 0.2s;
                    " onMouseOver="this.style.transform='scale(1.05)'" 
                    onMouseOut="this.style.transform='scale(1)'">
                        Inizia Gratis → 
                    </button>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Value Proposition
    with st.container():
        st.write("")  # Spacer
        cols = st.columns([1, 2, 1])
        with cols[1]:
            st.image(
                "https://via.placeholder.com/600x400?text=AI+Data+Processing+Demo", use_container_width=True)
        #
        st.divider()
        st.markdown("""
            <div style="padding: 2rem;">
                <h2 style="font-size: 2.5rem; color: #1e293b">Dall'ordine al sistema ERP<br>in 15 secondi</h2>
                <div style="display: flex; flex-direction: row; gap: 2rem; margin-top: 3rem;">
                    <div>
                        <div class="feature-icon">📸</div>
                        <h3 style="margin:0">Acquisizione Universale</h3>
                        <p style="color: #64748b">Supporto per immagini, PDF, email, fax e 30+ formati</p>
                    </div>
                    <div>
                        <div class="feature-icon">🧠</div>
                        <h3 style="margin:0">AI Context-Aware</h3>
                        <p style="color: #64748b">Riconosce layout complessi e dati non strutturati</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Process Visualization
    with st.container():
        st.write("")
        st.markdown("""
        <div style="max-width:1200px; margin:auto; padding:4rem 0">
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem">
                <div style="text-align: center">
                    <div style="background: #6366f1; color: white; width: 48px; height: 48px; border-radius: 12px; margin: auto; display: flex; align-items: center; justify-content: center">1</div>
                    <h4>Carica</h4>
                    <p style="color: #64748b">Documento o immagine</p>
                </div>
                <div style="text-align: center">
                    <div style="background: #818cf8; color: white; width: 48px; height: 48px; border-radius: 12px; margin: auto; display: flex; align-items: center; justify-content: center">2</div>
                    <h4>Elabora</h4>
                    <p style="color: #64748b">Riconoscimento AI avanzato</p>
                </div>
                <div style="text-align: center">
                    <div style="background: #a5b4fc; color: white; width: 48px; height: 48px; border-radius: 12px; margin: auto; display: flex; align-items: center; justify-content: center">3</div>
                    <h4>Struttura</h4>
                    <p style="color: #64748b">Generazione JSON automatica</p>
                </div>
                <div style="text-align: center">
                    <div style="background: #c7d2fe; color: white; width: 48px; height: 48px; border-radius: 12px; margin: auto; display: flex; align-items: center; justify-content: center">4</div>
                    <h4>Integra</h4>
                    <p style="color: #64748b">Invia al tuo ERP</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Interactive Demo
    with st.container():
        st.write("")
        cols = st.columns([1, 2, 1])
        with cols[1]:
            st.markdown("""
            <div class="demo-preview">
                <div style="padding: 2rem">
                    <h2 style="text-align: center; margin-bottom: 2rem">Prova l'AI in Azione</h2>
                    <div style="background: #f8fafc; padding: 2rem; border-radius: 16px">
                        <div style="border: 2px dashed #cbd5e1; padding: 2rem; text-align: center">
                            <input type="file" style="display: none" id="fileUpload">
                            <button onclick="document.getElementById('fileUpload').click()" style="
                                background: #6366f1;
                                color: white;
                                border: none;
                                padding: 1rem 2rem;
                                border-radius: 8px;
                                cursor: pointer;
                                transition: background 0.3s;
                            ">Carica un Ordine</button>
                            <p style="color: #94a3b8; margin-top: 1rem">Supports: JPG, PNG, PDF</p>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Pricing
    with st.container():
        st.write("")
        st.markdown("""
        <div style="max-width:1200px; margin:auto; padding:4rem 0">
            <h2 style="text-align: center; margin-bottom: 3rem">Piani Trasparenti</h2>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem">
                <div class="pricing-card">
                    <div style="padding: 2rem">
                        <h3>Starter</h3>
                        <div style="font-size: 2.5rem; font-weight: bold; margin: 1rem 0">€29</div>
                        <div style="color: #64748b; margin-bottom: 2rem">/mese</div>
                        <div style="text-align: left; margin-bottom: 2rem">
                            <p>✓ 500 ordini/mese</p>
                            <p>✓ Supporto base</p>
                            <p>✓ 1 utente</p>
                        </div>
                        <button style="
                            background: #6366f1;
                            color: white;
                            border: none;
                            padding: 1rem;
                            border-radius: 8px;
                            width: 100%;
                            cursor: pointer;
                        ">Inizia Gratis</button>
                    </div>
                </div>
                <div class="pricing-card" style="border: 2px solid #6366f1">
                    <div style="padding: 2rem">
                        <h3>Pro</h3>
                        <div style="font-size: 2.5rem; font-weight: bold; margin: 1rem 0">€99</div>
                        <div style="color: #64748b; margin-bottom: 2rem">/mese</div>
                        <div style="text-align: left; margin-bottom: 2rem">
                            <p>✓ Ordini illimitati</p>
                            <p>✓ Priority Support</p>
                            <p>✓ Team dashboard</p>
                        </div>
                        <button style="
                            background: #4f46e5;
                            color: white;
                            border: none;
                            padding: 1rem;
                            border-radius: 8px;
                            width: 100%;
                            cursor: pointer;
                        ">Scelta Popolare</button>
                    </div>
                </div>
                <div class="pricing-card">
                    <div style="padding: 2rem">
                        <h3>Enterprise</h3>
                        <div style="font-size: 2.5rem; font-weight: bold; margin: 1rem 0">Custom</div>
                        <div style="color: #64748b; margin-bottom: 2rem">&nbsp;</div>
                        <div style="text-align: left; margin-bottom: 2rem">
                            <p>✓ Volume discount</p>
                            <p>✓ SLA 24/7</p>
                            <p>✓ On-premise</p>
                        </div>
                        <button style="
                            background: #6366f1;
                            color: white;
                            border: none;
                            padding: 1rem;
                            border-radius: 8px;
                            width: 100%;
                            cursor: pointer;
                        ">Contattaci</button>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div style="background: #1e293b; color: white; padding: 4rem 0; margin-top: 6rem">
        <div style="max-width:1200px; margin:auto; display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem">
            <div>
                <h4>OrdiniElaborati.ai</h4>
                <p style="color: #94a3b8">Automazione intelligente per la gestione ordini</p>
            </div>
            <div>
                <h4>Legal</h4>
                <p style="color: #94a3b8">Privacy Policy</p>
                <p style="color: #94a3b8">Termini di Servizio</p>
            </div>
            <div>
                <h4>Risorse</h4>
                <p style="color: #94a3b8">Documentazione</p>
                <p style="color: #94a3b8">API Reference</p>
            </div>
            <div>
                <h4>Contatti</h4>
                <p style="color: #94a3b8">support@ordini.ai</p>
                <p style="color: #94a3b8">+39 02 1234567</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
