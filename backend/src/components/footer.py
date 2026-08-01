import streamlit as st


def footer_home():

    st.markdown(f"""
        <div style="margin-top:3rem; display:flex; gap:8px; justify-content:center; align-items:center; opacity:0.9;">
            <p style="font-family:'Outfit', sans-serif; font-weight:600; color:white; margin:0;">Crafted with ❤️ by Shivam</p>
        </div>

                """, unsafe_allow_html=True)


def footer_dashboard():

    st.markdown(f"""
        <div style="margin-top:3rem; padding-top:1.5rem; border-top:1px solid #C9CDF7; display:flex; gap:8px; justify-content:center; align-items:center;">
            <p style="font-family:'Outfit', sans-serif; font-weight:600; color:#3A3F72; margin:0;">Crafted with ❤️ by Shivam</p>
        </div>

                """, unsafe_allow_html=True)