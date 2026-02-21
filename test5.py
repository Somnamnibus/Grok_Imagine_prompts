import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_api_key"))

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "system", "content": """
        Jesteś wielkim matematykiem. Pokaż swoje obliczenia krok po kroku.
        """ },

        {"role": "user", "content": """
         W kawiarni jest 15 stolików. 5 z nich ma po 4 krzesła, a reszta ma po 2 krzesła. 
         Ile jest wszystkich krzeseł w kawiarni?
        """}
    ],
)
print(response.choices[0].message.content)
print("Ilość tokenów", response.usage)