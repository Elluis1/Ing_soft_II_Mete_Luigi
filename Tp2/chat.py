import os
from openai import OpenAI
import openai
from dotenv import load_dotenv

load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

while True:
    prompt = input("Introduce una pregunta: ")

    completion = client.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=2048
    )
    print('You: ', prompt)
    print('ChatGPT: ', completion.choices[0].text)