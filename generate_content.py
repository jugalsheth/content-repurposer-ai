import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ------------------------------------------------
# 🧠 Repurpose Text
# ------------------------------------------------
def repurpose_text(content, platform, tone, output_format, num_versions=1):
    # Expand if input is short
    if len(content.split()) < 20:
        expansion_prompt = f"""
        You are a skilled content strategist.

        Take the following short prompt or question and expand it into a fully structured thought piece with clear value.

        Add:
        - A strong intro
        - Key arguments or insights
        - A thought-provoking close

        Keep it engaging, clear, and useful.

        Prompt:
        '''{content}'''
        """
        expansion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": expansion_prompt}],
            temperature=0.7
        )
        content = expansion.choices[0].message.content.strip()


    format_instructions = ""

    if output_format == "Thread":
        format_instructions = """
Repurpose the content into a Twitter thread.
Break it into 6–10 numbered tweets.
Use emojis where relevant.
Start with a strong hook tweet.
Make sure each tweet stands alone with value.
End with a call to action or a question.
"""
    elif output_format == "Blog Article":
        format_instructions = """
Expand the content into a full-length blog article.
Use headings (H2), bullet points, and examples where useful.
Maintain the tone and add original insights or commentary.
"""
    else:
        format_instructions = """
Write a single platform-optimized post (e.g., LinkedIn, Newsletter).
Keep it clean, value-packed, and CTA-driven.
"""

    prompt = f"""
You are an expert AI content repurposer with 20+ years of digital writing experience.

Your job:
1. If input is short, expand it intelligently without filler.
2. Preserve the voice and clarity of original content.
3. Keep all formatting (e.g., bullets, bold, links, emojis).
4. If the input is a list, keep all key points intact.
5. Follow the repurposing instructions exactly.

Tone: {tone}
Platform: {platform}
Format: {output_format}

{format_instructions}

Input content:
'''{content}'''
"""

    responses = []
    for _ in range(num_versions):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.85
        )
        responses.append(response.choices[0].message.content)

    return responses

# ------------------------------------------------
# 📈 Predict Engagement Score
# ------------------------------------------------
def predict_engagement_score(post):
    prompt = f"""
You are an expert in social media performance.

Read the following post and give it:
1. An engagement score from 1 to 10 (based on potential likes, shares, saves)
2. A 1-line reason why you gave that score.

Post:
'''{post}'''
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

# ------------------------------------------------
# 🧠 Hook Grader
# ------------------------------------------------
def grade_hook(post):
    first_line = post.strip().split("\n")[0]
    prompt = f"""
You are a viral content strategist.

Here is a hook (opening line) from a social post:
"{first_line}"

1. Rate the hook from 1 to 10.
2. Suggest how to improve it in 1 sentence.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

# ------------------------------------------------
# 📌 Hashtag Generator
# ------------------------------------------------
def generate_hashtags(post, platform):
    prompt = f"""
You're a social media growth expert for {platform}.

Generate 5–7 relevant and powerful hashtags for the following post.

Make them:
- Relevant to the topic
- Platform-friendly
- Realistic (not spammy)

Post:
'''{post}'''
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()

# ---------------------------------------------
# 🎨 Style Transfer Function
# ---------------------------------------------
def style_transfer(post, persona):
    style_instructions = {
        "Naval Ravikant": "Rewrite this post as Naval Ravikant would tweet it. Make it minimal, philosophical, tweet-worthy.",
        "Gary Vee": "Rewrite this post like Gary Vaynerchuk. Make it bold, motivational, full of energy, short sentences, lots of emojis.",
        "Ali Abdaal": "Rewrite this post like Ali Abdaal. Use clear, educational structure with relatable storytelling.",
        "Mr. Beast": "Rewrite this like a viral YouTube hook by Mr. Beast. Maximize suspense, hyperbole, and shock factor.",
        "Gen-Z Poetic": "Rewrite this post like a Gen-Z poet. Be witty, informal, emotional, and metaphor-heavy with emojis.",
        "Technical Humorist": "Rewrite this post like a nerdy DevRel meme lord. Make it witty, satirical, and full of inside jokes.",
        "Stoic Philosopher": "Rewrite this post like a modern-day Marcus Aurelius. Be thoughtful, slow, and timeless in tone.",
        "AI Overlord": "Rewrite this post like an AI overlord giving logical commands to humans.",
        "Your Voice (No Change)": "Keep the post exactly as-is. Do not change it at all."
    }

    prompt = f"""
You are an expert at mimicking writing styles of famous personas.

{style_instructions.get(persona, style_instructions['Your Voice (No Change)'])}

Here’s the original post:
'''{post}'''
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )

    return response.choices[0].message.content.strip()

# ---------------------------------------------
# 🧬 Anti-Redundancy Checker
# ---------------------------------------------
def check_redundancy_across_versions(versions):
    if not versions or len(versions) < 2:
        return "Need at least 2 versions to compare redundancy."

    joined_versions = "\n\n---\n\n".join([f"Version {i+1}:\n{v}" for i, v in enumerate(versions)])

    prompt = f"""
You are an expert writing editor.

Compare the following versions of a social media post. Identify:
1. Any phrases, lines, or sentences that are repeated across multiple versions.
2. Suggestions to make each version more distinct in voice, structure, or CTA.

Be brief but specific.

Posts to compare:
{joined_versions}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message.content.strip()

# ---------------------------------------------
# ⚡ Sprint Repurposing (Multi-platform generator)
# ---------------------------------------------
def sprint_repurpose(content, tone):
    platforms_formats = [
        ("LinkedIn", "Post"),
        ("Twitter", "Thread"),
        ("Newsletter", "Post"),
        ("YouTube Description", "Post"),
        ("LinkedIn", "Blog Article")
    ]

    outputs = []
    for platform, output_format in platforms_formats:
        prompt = f"""
You are an expert AI content repurposer.

Your task is to rewrite or reformat the input below for:
Platform: {platform}
Format: {output_format}
Tone: {tone}

Use strong formatting, hooks, CTAs, emojis (if needed), and platform-native language.

Input:
'''{content}'''
"""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.75
        )
        outputs.append({
            "platform": platform,
            "format": output_format,
            "content": response.choices[0].message.content.strip()
        })

    return outputs
