import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_api_key"))

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "system", "content": "Jesteś koderem w pythonie"},
        {"role": "user", "content": "Napisz mi funkcje unitest" }
    ],
    temperature=0.5,
    max_tokens=500,
    top_p=0.9,
    frequency_penalty=0.1
)
print(response.choices[0].message.content)
print("Ilość tokenów", response.usage)