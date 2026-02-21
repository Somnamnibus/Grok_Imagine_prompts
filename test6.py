from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_api_key"))

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

# Przykładowe zdania
zdanie1 = "Król siedzi na tronie."
zdanie2 = "Królowa to głowa państwa."
zdanie3 = "Pizza jest smaczna."

# Generowanie embeddingów
embedding1 = get_embedding(zdanie1)
embedding2 = get_embedding(zdanie2)
embedding3 = get_embedding(zdanie3)

print(f"Zdanie 1: \"{zdanie1}\"")
print(f"Wymiar wektora: {len(embedding1)}")
print(f"Fragment wektora: {embedding1[:5]}...") # Można odkomentować, by zobaczyć fragment

print(f"\nZdanie 2: \"{zdanie2}\"")
print(f"Wymiar wektora: {len(embedding2)}")

print(f"\nZdanie 3: \"{zdanie3}\"")
print(f"Wymiar wektora: {len(embedding3)}")