import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(160deg, #5865F2 0%, #4752C4 100%) !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    box-shadow: 0 20px 45px rgba(0,0,0,0.25) !important;
                    transition: transform 0.3s ease !important;
                    }

                .stApp div[data-testid="stColumn"]:hover{
                    transform: translateY(-6px) !important;
                    }
        </style>

                """
            ,unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(160deg, #EEF0FF 0%, #DCE0FF 100%) !important;
                }

        </style>

                """
            ,unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400..800;1,400..800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');


         /* Hide Top Bar of streamlit */

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top:1.5rem !important;
                padding-bottom: 3rem !important;
            }

            /* ---------- Typography ---------- */

            h1 {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 800 !important;
                font-style: italic !important;
                font-size: 3.5rem !important;
                line-height:1.15 !important;
                margin-bottom:0rem !important;
                color: #232760 !important;
                letter-spacing: 0.5px !important;
            }


            h2 {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 800 !important;
                font-style: italic !important;
                font-size: 2rem !important;
                line-height:1.2 !important;
                margin-bottom:0rem !important;
                color: #232760 !important;
            }

            h3, h4 {
                font-family: 'Outfit', sans-serif !important;
                color: #232760 !important;
                font-weight: 600 !important;
            }

            p, label, li {
                font-family: 'Outfit', sans-serif !important;
                color: #3A3F72 !important;
            }

            /*
              Only force our font on TEXT spans — never on icon-ligature spans.
              Streamlit renders every material icon (buttons, st.info, st.warning,
              st.error, st.success) as a <span> whose literal text content (e.g.
              "school", "arrow_outward") is turned into a glyph by the Material
              Symbols font. Overriding that font-family makes the literal word
              appear instead of the icon, which is what caused the overlap bugs.
              This selector excludes ANY span that looks like an icon span,
              across all the different data-testid names Streamlit uses for them.
            */
            span:not([data-testid*="Icon"]):not([class*="material"]):not([class*="Material"]) {
                font-family: 'Outfit', sans-serif !important;
                color: inherit;
            }

            [data-testid*="Icon"],
            .material-symbols-outlined,
            .material-symbols-rounded,
            .material-icons {
                font-family: 'Material Symbols Rounded', 'Material Symbols Outlined', 'Material Icons' !important;
            }

            /* Text sitting directly on the purple home background needs to flip to white */
            .stApp[style*="5865F2"] h1,
            .stApp[style*="5865F2"] h2 {
                color: #FFFFFF !important;
            }

            /* Subtle, single-layer shadow only — avoids the "ghosted double text" look */
            .stApp[style*="5865F2"] h1 {
                text-shadow: 0 3px 8px rgba(0,0,0,0.18) !important;
            }

            /* ---------- Buttons ---------- */

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
                box-shadow: 0 6px 14px rgba(88,101,242,0.35) !important;
                transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out !important;
                }

            /* Force every element INSIDE every button to be readable white text,
               regardless of Streamlit's own kind-specific (primary/secondary/tertiary)
               internal color variables which were winning on specificity before. */
            button, button *,
            button p, button span, button div {
                color: white !important;
                opacity: 1 !important;
            }

            /* Ensure icon + label sit side-by-side with proper spacing, never overlapping */
            button p, button div[data-testid="stMarkdownContainer"] p {
                display: inline-flex !important;
                align-items: center !important;
                gap: 6px !important;
                margin: 0 !important;
            }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                border: none !important;
                box-shadow: 0 6px 14px rgba(235,69,158,0.35) !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #111111 !important;
                border: 1px solid #2A2A2A !important;
                box-shadow: 0 6px 14px rgba(0,0,0,0.25) !important;
                }

            button:hover{
                transform: scale(1.04) translateY(-2px) !important;
                box-shadow: 0 10px 20px rgba(0,0,0,0.25) !important;
            }

            /* ---------- Inputs ---------- */

            div[data-testid="stTextInput"] input,
            div[data-testid="stTextArea"] textarea,
            div[data-baseweb="select"] > div {
                border-radius: 1rem !important;
                border: 2px solid #C9CDF7 !important;
                background-color: #FFFFFF !important;
                font-family: 'Outfit', sans-serif !important;
                color: #232760 !important;
            }

            div[data-testid="stTextInput"] input:focus {
                border-color: #5865F2 !important;
                box-shadow: 0 0 0 3px rgba(88,101,242,0.2) !important;
            }

            /* ---------- Misc containers ---------- */

            div[data-testid="stVerticalBlockBorderWrapper"] {
                border-radius: 1.75rem !important;
                background-color: #FFFFFF !important;
                box-shadow: 0 10px 25px rgba(35,39,96,0.10) !important;
                border: none !important;
            }

            hr {
                border-top: 2px solid #C9CDF7 !important;
                opacity: 0.6 !important;
            }

            div[data-testid="stAlert"] {
                border-radius: 1.25rem !important;
                font-family: 'Outfit', sans-serif !important;
            }

            div[data-testid="stDataFrame"] {
                border-radius: 1rem !important;
            }

            img {
                border-radius: 1rem !important;
            }

            /* ---------- Dialogs / Modals (st.dialog) ---------- */
            /* Streamlit renders dialogs in their own overlay using the dark theme
               by default. Multiple selectors below because Streamlit's exact DOM
               nesting for the dialog "card" varies by version — listing several
               ensures at least one reliably matches instead of silently failing
               (which is what caused dark-navy-text-on-black-background before). */

            div[data-testid="stDialog"],
            div[data-testid="stDialog"] [role="dialog"],
            [role="dialog"] {
                background-color: #FFFFFF !important;
                border-radius: 1.75rem !important;
                box-shadow: 0 25px 60px rgba(0,0,0,0.35) !important;
                border: none !important;
            }

            div[data-testid="stDialog"] h1,
            div[data-testid="stDialog"] h2,
            div[data-testid="stDialog"] h3,
            div[data-testid="stDialog"] h4 {
                color: #232760 !important;
                text-shadow: none !important;
            }

            div[data-testid="stDialog"] p,
            div[data-testid="stDialog"] label,
            div[data-testid="stDialog"] li,
            div[data-testid="stDialog"] small,
            div[data-testid="stDialog"] span:not([data-testid*="Icon"]):not([class*="material"]):not([class*="Material"]) {
                color: #3A3F72 !important;
                font-family: 'Outfit', sans-serif !important;
            }

            div[data-testid="stDialog"] div[data-testid="stTextInput"] input,
            div[data-testid="stDialog"] div[data-testid="stTextArea"] textarea,
            div[data-testid="stDialog"] div[data-baseweb="select"] > div {
                background-color: #F5F6FF !important;
                border: 2px solid #C9CDF7 !important;
                color: #232760 !important;
            }

            div[data-testid="stDialog"] div[data-testid="stTextInput"] input::placeholder {
                color: #9BA0D9 !important;
            }

            /* st.code() blocks — the copy-link / subject-code boxes */
            div[data-testid="stDialog"] div[data-testid="stCodeBlock"] {
                background-color: #F5F6FF !important;
                border-radius: 1rem !important;
                border: 2px solid #C9CDF7 !important;
            }

            div[data-testid="stDialog"] div[data-testid="stCodeBlock"] code,
            div[data-testid="stDialog"] div[data-testid="stCodeBlock"] pre,
            div[data-testid="stDialog"] div[data-testid="stCodeBlock"] span:not([data-testid*="Icon"]) {
                color: #232760 !important;
                background: transparent !important;
                font-family: 'Outfit', sans-serif !important;
            }

            div[data-testid="stDialog"] hr {
                border-top: 2px solid #E4E6FA !important;
            }

            div[data-testid="stDialog"] div[data-testid="stAlert"] {
                border-radius: 1.25rem !important;
            }

            /* Safety net — anything left uncolored inside a dialog (excluding
               icons, buttons, and code, which are already handled above) falls
               back to readable navy text instead of inheriting dark-theme white. */
            div[data-testid="stDialog"] *:not(button):not(button *):not([data-testid*="Icon"]):not([class*="material"]):not([class*="Material"]):not(code):not(pre) {
                color: #3A3F72;
            }

            /* ---------- Toasts (st.toast) ---------- */
            /* Same dark-theme-by-default issue as dialogs — "Welcome Back Ram" was
               rendering as dark navy text on a near-black background. */

            div[data-testid="stToast"] {
                background-color: #FFFFFF !important;
                border-radius: 1.25rem !important;
                box-shadow: 0 15px 35px rgba(35,39,96,0.25) !important;
                border: 1px solid #E4E6FA !important;
            }

            div[data-testid="stToast"] p,
            div[data-testid="stToast"] span:not([data-testid*="Icon"]):not([class*="material"]):not([class*="Material"]) {
                color: #232760 !important;
                font-family: 'Outfit', sans-serif !important;
                font-weight: 600 !important;
            }

        </style>

                """
            ,unsafe_allow_html=True)