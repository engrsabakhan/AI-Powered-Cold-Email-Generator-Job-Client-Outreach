import requests

GROQ_API_KEY = ""  # Replace with your GroqCloud API key

def generate_email(job_title, company, skills):
    prompt = f"""Write a cold email applying for a job at {company} as a {job_title}.
Mention the following resume highlights: {skills}.
Keep it concise, confident, and professional."""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", json=payload, headers=headers)
    return response.json()["choices"][0]["message"]["content"]
