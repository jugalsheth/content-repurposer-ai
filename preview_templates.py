import streamlit as st
import html

def render_preview(platform, content):
    content = html.escape(content)

    if platform == "LinkedIn":
        st.markdown(f"""
            <div style="max-width:375px; margin:auto; font-family: 'Segoe UI', sans-serif; font-size:15px; background:#fff; color:#171717; border:1px solid #dcdcdc; border-radius:12px; box-shadow:0 2px 8px rgba(0,0,0,0.05);">
            <!-- Header -->
            <div style="display:flex; padding:10px 16px; align-items:center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="36" height="36" style="border-radius:50%;">
                <div style="margin-left:10px;">
                <div style="font-weight:600; font-size:14px;">Jugal Sheth</div>
                <div style="font-size:12px; color:#666;">Data Engineer · VaynerMedia</div>
                <div style="font-size:11px; color:#888;">2h · 🌐</div>
                </div>
                <div style="margin-left:auto; color:#999; font-weight:bold;">···</div>
            </div>

            <!-- Content -->
            <div style="padding:0 16px 12px 16px; line-height:1.4; white-space:pre-wrap;">
                {content}
            </div>

            <!-- Reactions -->
            <div style="padding:4px 16px; font-size:13px; color:#555; border-top:1px solid #eee; border-bottom:1px solid #eee;">
                👍 48 · 💬 12 · ↪️ 5
            </div>

            <!-- CTA Bar -->
            <div style="display:flex; justify-content:space-around; padding:8px 0; font-size:13px; color:#606770;">
                <div>👍 Like</div>
                <div>💬 Comment</div>
                <div>↪️ Share</div>
            </div>
            </div>
            """, unsafe_allow_html=True) 

    elif platform == "Twitter":
        st.markdown(f"""
<div style="
    background:#ffffff;
    color:#0f1419;
    border:1px solid #ccc;
    padding:12px;
    border-radius:10px;
    font-family:'Helvetica Neue', sans-serif;
    font-size:15px;
    line-height:1.4;
    max-width:500px;
    margin:auto;">
    <div style="color:#1da1f2; font-weight:bold;">@jugalsheth</div>
    <div style="margin-top:6px; white-space:pre-wrap;">{content}</div>
</div>
""", unsafe_allow_html=True)

    elif platform == "YouTube Description":
        st.markdown(f"""
<div style="
    background:#fff;
    border:1px solid #ccc;
    padding:15px;
    border-radius:10px;
    font-family:Arial, sans-serif;
    max-width:600px;
    margin:auto;">
    <strong style="font-size:16px;">📺 YouTube Description Preview</strong>
    <pre style="background:#f9f9f9; padding:10px; border-radius:5px; white-space:pre-wrap; font-size:14px; line-height:1.4;">{content}</pre>
</div>
""", unsafe_allow_html=True)

    elif platform == "Newsletter":
        st.markdown(f"""
<div style="
    background:#fffefc;
    border:1px solid #ccc;
    padding:16px;
    border-radius:10px;
    font-family:Georgia, serif;
    line-height:1.4;
    font-size:16px;
    max-width:600px;
    margin:auto;">
    <strong style="font-size:18px;">📰 Newsletter Preview</strong>
    <div style="margin-top:8px; white-space:pre-wrap;">{content}</div>
</div>
""", unsafe_allow_html=True)

    elif platform == "Blog Article":
        st.markdown(f"""
<div style="
    background:#ffffff;
    border-left:6px solid #007acc;
    padding:18px;
    font-family:Georgia, serif;
    font-size:16px;
    line-height:1.4;
    max-width:700px;
    margin:auto;">
    <h2 style="margin-top:0;">📝 Blog Article Preview</h2>
    <div style="white-space:pre-wrap;">{content}</div>
</div>
""", unsafe_allow_html=True)