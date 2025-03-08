#test.py
from openai import OpenAI
import os


client = OpenAI(api_key=os.getenv("OPENAIKEY"))
prompt = "say Hello world"
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)

import httpx
print("httpx version:", httpx.__version__)

# import openai
# print(openai.__version__)


