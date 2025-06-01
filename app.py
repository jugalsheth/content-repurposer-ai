import streamlit as st
from generate_content import (
    repurpose_text,
    predict_engagement_score,
    grade_hook,
    generate_hashtags,
    style_transfer,
    check_redundancy_across_versions,
    sprint_repurpose
)
from preview_templates import render_preview

st.set_page_config(page_title="Content Repurposer AI", layout="centered")

st.title("🪄 Content Repurposer AI")
st.markdown("Paste your blog or draft. Get posts for Twitter, LinkedIn, etc.")

# Input: Content
content = st.text_area("✍️ Paste your blog content here:", height=200)

# Input: Platform + Tone
col1, col2 = st.columns(2)
platform = col1.selectbox("📣 Target Platform", ["LinkedIn", "Twitter", "Newsletter", "YouTube Description"])

preset_tones = {
    "Professional": "Confident and polished for B2B or tech audiences.",
    "Witty": "Casual, clever, with light humor and cultural references.",
    "Inspiring": "Motivational, big-picture, emotional tone.",
    "Educational": "Informative, detailed, focused on clarity.",
    "Custom": ""
}

selected_tone = col2.selectbox("🎭 Tone Preset", list(preset_tones.keys()))
if selected_tone == "Custom":
    tone = st.text_input("Write your custom tone (e.g., sarcastic, Gen-Z style, poetic):")
else:
    tone = preset_tones[selected_tone]

# Input: Format
output_format = st.selectbox("🧾 Repurpose As", ["Post", "Thread", "Blog Article"])
style_persona = st.selectbox("🎨 Transfer Style To", [
    "Your Voice (No Change)",
    "Naval Ravikant",
    "Gary Vee",
    "Ali Abdaal",
    "Mr. Beast",
    "Gen-Z Poetic",
    "Technical Humorist",
    "Stoic Philosopher",
    "AI Overlord"
])
sprint_mode = st.checkbox("⚡ Sprint Repurposing Mode (generate for all platforms)")


# Initialize session state
if 'result' not in st.session_state:
    st.session_state.result = []

if 'history' not in st.session_state:
    st.session_state.history = []

# Generate button
if st.button("✨ Generate Post"):
    if not content.strip():
        st.warning("Please enter some content to repurpose.")
    else:
        with st.spinner("Generating..."):

            if sprint_mode:
                outputs = sprint_repurpose(content, tone)
                st.session_state.result = outputs
            else:
                versions = repurpose_text(content, platform, tone, output_format, num_versions=3)
                st.session_state.result = versions

                if versions:
                    st.session_state.history.append({
                        "platform": platform,
                        "tone": tone,
                        "format": output_format,
                        "content": versions[0]
                    })
                else:
                    st.error("Something went wrong. Please try again.")

# Show history
if st.session_state.result:
    for i, version in enumerate(st.session_state.result, 1):
        # 🧠 Handle both sprint (dict) and normal (str) modes
        post_content = version["content"] if isinstance(version, dict) else version
        post_platform = version["platform"] if isinstance(version, dict) else platform
        post_format = version["format"] if isinstance(version, dict) else output_format

        st.markdown(f"### ✨ Version {i}: {post_platform} | {post_format}")
        st.markdown(post_content)
        st.subheader("👀 Preview")
        render_preview(post_platform, post_content)
        st.code(post_content, language="markdown")

        # 🔍 Advanced Insights Section
        with st.expander("📈 Engagement Score & Suggestions"):
            with st.spinner("🔍 Scoring..."):
                score = predict_engagement_score(post_content)
                hook = grade_hook(post_content)
                tags = generate_hashtags(post_content, post_platform)

            st.markdown(f"**📊 Engagement Score:**\n{score}")
            st.markdown(f"**🧠 Hook Grader:**\n{hook}")
            st.markdown(f"**📌 Suggested Hashtags:**\n{tags}")

        # 🎨 Style Transfer Section
        if style_persona != "Your Voice (No Change)":
            with st.expander(f"🎨 Styled as {style_persona}"):
                with st.spinner("Transforming tone..."):
                    styled_version = style_transfer(post_content, style_persona)
                    st.markdown(styled_version)
                    st.code(styled_version, language="markdown")
                    st.download_button(
                        label=f"📥 Download ({style_persona})",
                        data=styled_version,
                        file_name=f"repurposed_{style_persona.lower().replace(' ', '_')}_v{i}.txt"
                    )

        # 📥 Download original version
        st.download_button(
            label=f"📥 Download Version {i}",
            data=post_content,
            file_name=f"repurposed_v{i}.txt"
        )
