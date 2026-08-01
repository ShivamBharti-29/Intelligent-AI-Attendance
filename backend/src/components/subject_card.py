import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:white; border-left: 8px solid #EB459E; padding:22px 25px; border-radius: 20px;
                    box-shadow: 0 8px 20px rgba(35,39,96,0.10); margin-bottom:20px;">
        <h3 style="margin:0; color: #232760; font-size: 1.4rem; font-family:'Outfit', sans-serif; font-weight:700;">{name}</h3>
        <p style="color:#64748b; margin:10px 0; font-family:'Outfit', sans-serif;">
            Code : <span style="background:#E0E3FF; color:#5865F2; padding:2px 10px; border-radius:8px; font-weight:600;">{code}</span>
            &nbsp;|&nbsp; Section : <b>{section}</b>
        </p>

        """

    if stats:
        html += """
        <div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:6px;">
        """
        for icon, label, value in stats:
            html += f'''<div style="background:#5865F212; color:#232760; padding:6px 14px; border-radius:12px;
                        font-size:0.9rem; font-family:'Outfit', sans-serif;">{icon} <b>{value}</b> {label}</div>'''

        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()