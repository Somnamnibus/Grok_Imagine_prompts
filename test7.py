import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_api_key"))

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# Zdania
zdanie1 = "Król siedzi na tronie."
zdanie2 = "Królowa to głowa państwa."
zdanie3 = "Pizza jest smaczna."

# Embeddingi
embedding1 = get_embedding(zdanie1)
embedding2 = get_embedding(zdanie2)
embedding3 = get_embedding(zdanie3)

# Obliczanie podobieństwa
sim_1_2 = cosine_similarity(embedding1, embedding2)
sim_1_3 = cosine_similarity(embedding1, embedding3)
sim_2_3 = cosine_similarity(embedding2, embedding3)

print(f"Podobieństwo między zdaniem 1 a 2: {sim_1_2:.4f}")
print(f"Podobieństwo między zdaniem 1 a 3: {sim_1_3:.4f}")
print(f"Podobieństwo między zdaniem 2 a 3: {sim_2_3:.4f}")