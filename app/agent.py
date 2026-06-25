def generate_marketing_prompt(
    business_name: str,
    audience: str,
    goal: str,
    platform: str
):
    prompt = f"""
You are a senior digital marketing strategist.

Business Name: {business_name}
Target Audience: {audience}
Goal: {goal}

Platform:
{platform}

Generate a professional marketing report.
"""
    return prompt