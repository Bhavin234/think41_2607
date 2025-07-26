import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("GROQ_API_KEY")
openai.api_base = "https://api.groq.com/openai/v1"

def get_llm_response(messages):
    response = openai.ChatCompletion.create(
        model="mixtral-8x7b-32768",
        messages=messages,
        temperature=0.4,
    )
    return response.choices[0].message["content"]
