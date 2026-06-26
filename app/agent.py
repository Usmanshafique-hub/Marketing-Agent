from groq import Groq
from app.config import get_groq_api_key

# Create client safely
client = Groq(
    api_key=get_groq_api_key()
)


def generate_marketing_content(
    business_name,
    audience,
    goal,
    platform,
    tool
):

    if tool == "Facebook Ad":
        prompt = f"""
Create 3 high-converting Facebook Ads.

Business Name: {business_name}
Audience: {audience}
Goal: {goal}

Include:
- Primary Text
- Headline
- Description
- CTA
"""

    elif tool == "Instagram Post":
        prompt = f"""
Create an Instagram marketing post.

Business Name: {business_name}
Audience: {audience}
Goal: {goal}

Include:
- Caption
- CTA
- 15 Hashtags
"""

    elif tool == "Google Ad":
        prompt = f"""
Create Google Search Ads.

Business Name: {business_name}
Audience: {audience}
Goal: {goal}

Include:
- 5 Headlines
- 5 Descriptions
"""

    elif tool == "Email Marketing":
        prompt = f"""
Create a marketing email.

Business Name: {business_name}
Audience: {audience}
Goal: {goal}
"""

    elif tool == "SEO Keywords":
        prompt = f"""
Generate SEO keywords.

Business Name: {business_name}
Audience: {audience}
Goal: {goal}
"""

    else:
        prompt = f"""
You are a senior digital marketing strategist.

Business Name: {business_name}
Audience: {audience}
Goal: {goal}
Platform: {platform}

Generate:

1. Marketing Strategy
2. Audience Analysis
3. CTA
4. Social Media Caption
5. 15 Hashtags
6. Competitor Suggestions
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content