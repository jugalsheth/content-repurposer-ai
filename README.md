# 🪄 Content Repurposer AI

An open-source GenAI-powered app that transforms your blog drafts, ideas, and notes into engaging content tailored for **LinkedIn**, **Twitter**, **Newsletters**, **Blog Posts**, and more. Built to help creators, marketers, and thought leaders **maximize the reach of a single idea** across platforms in seconds.

---

## 🚀 Journey & Motivation

It started with a creator's dilemma:

> "I wrote this great blog post, but how do I turn this into a thread, a LinkedIn post, or a YouTube description without sounding repetitive?"

The idea was simple: Let AI intelligently **repurpose** your content, maintain your voice, match platform expectations, and go beyond just "summarizing".

Version 1 brings:

- ✍️ Multi-platform post generation  
- 🧠 Advanced AI insights (hook grading, engagement prediction, hashtag suggestions)  
- 📱 Realistic platform previews  
- 🧬 Style transfer (write like Naval, GaryVee, MrBeast...)  
- ⚡ Sprint mode (generate for all platforms in one go!)

---

## ✅ Functional Requirements

- Allow users to input free-form content (blog, draft, idea)
- Choose target platform (LinkedIn, Twitter, YouTube, etc.)
- Set tone presets (Witty, Professional, Inspiring, etc.)
- Output 3 AI-generated post versions
- Visual preview block for each platform style
- Insight layer: score hooks, generate hashtags, predict engagement
- Download + copy post options

---

## 📦 Non-Functional Requirements

- 🔒 Secure API key handling using `.env`
- ⚡ Responsive and mobile-friendly preview interface
- 🧠 Fast response time using GPT-3.5-turbo
- ♻️ Stateless design with `st.session_state` for history tracking
- 🪶 Lightweight: No DB needed, works fully client-side (except OpenAI API calls)
- 🎯 Customizable prompts to extend edge case handling

---

## 🧠 System Design Highlights

### Architecture

Streamlit UI <---> generate_content.py (OpenAI Prompt Logic)
|__ repurpose_text()
|__ predict_engagement_score()
|__ grade_hook()
|__ generate_hashtags()
|__ style_transfer()
|__ sprint_repurpose()
|__ check_redundancy_across_versions()


### Key Modules

- **Frontend/UI**: Built with Streamlit  
- **Backend Logic**: Modular functions in `generate_content.py`  
- **AI Models**: OpenAI GPT-3.5-Turbo for all content generation tasks  
- **Session Management**: Using `st.session_state` to store outputs and history  
- **Rendering**: HTML + CSS injected into Streamlit for post-style previews

---

## 🔍 Sneak Peek

### 🔄 Generate  
Turn one blog into 3 platform-ready posts with 1 click.

### 📈 Insights & Scoring  
Each version is scored for hook strength, engagement, hashtags.

### 📱 Platform Previews  
Live visual previews for LinkedIn, Twitter, YouTube, Newsletters.

<img width="757" alt="Screenshot 2025-05-31 at 11 08 41 PM" src="https://github.com/user-attachments/assets/78edfdc1-7dba-4205-9ae2-98ff864e6e8f" />

---

## 🛠 Tech Stack

- Python 3.9+
- Streamlit
- OpenAI API (GPT-3.5-Turbo)
- `python-dotenv`

---

## 📁 Setup Instructions


git clone https://github.com/yourusername/content-repurposer-ai.git
cd content-repurposer-ai
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

Create a .env file and add your OpenAI key:
OPENAI_API_KEY=sk-...

Run the app:

bash
Copy
Edit
streamlit run app.py
📢 Future Enhancements
🎙️ Add audio narration preview (text-to-speech)

⏰ Schedule posts via Buffer or Zapier integration

📊 Track performance across platforms (via APIs)

🔗 Collaborator sharing link

💼 Monetization toggle for ghostwriters

🤝 Contributors

Built by Jugal Sheth with 💡 and caffeine.

Feel free to fork, contribute, or feature this app in your next project!

