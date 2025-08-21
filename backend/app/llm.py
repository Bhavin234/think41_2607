# import os
# import openai
# from dotenv import load_dotenv

# load_dotenv()
# openai.api_key = os.getenv("GROQ_API_KEY")
# openai.api_base = "https://api.groq.com/openai/v1"

# def get_llm_response(messages):
#     response = openai.ChatCompletion.create(
#         model="mixtral-8x7b-32768",
#         messages=messages,
#         temperature=0.4,
#     )
#     return response.choices[0].message["content"]

import httpx
import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

async def generate_response(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant for an e-commerce clothing site."},
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=payload
        )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
