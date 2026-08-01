import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:20px">
            <div style="background:rgba(255,255,255,0.12); border-radius:50%; padding:18px; box-shadow:0 10px 30px rgba(0,0,0,0.25);">
                <img src='{logo_url}' style='height:80px; display:block;' />
            </div>
            <h1 style='text-align:center; color:#E0E3FF; margin-top:14px; text-shadow:0 4px 18px rgba(0,0,0,0.25);'>SNAP<br/>CLASS</h1>
        </div>

                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:flex-start; gap:14px;">
            <div style="background:#E0E3FF; border-radius:16px; padding:10px; display:flex; align-items:center; justify-content:center;">
                <img src='{logo_url}' style='height:48px; display:block;' />
            </div>
            <h2 style='text-align:left; color:#5865F2; margin:0;'>SNAP<br/>CLASS</h2>
        </div>

                """, unsafe_allow_html=True)