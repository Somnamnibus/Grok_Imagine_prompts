import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_api_key"))

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "system", "content": "Jesteś koderem w pythonie"},
        {"role": "user", "content": "Napisz co wiesz o Pythonie w wersji 3.14" }
    ],
)
print(response.choices[0].message.content)