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
    try:
        prompt = input("Introduce una pregunta: ")
    except KeyboardInterrupt:
        print('\Saliendo del programa')
        break
    except Exception as e:
        print('Error al leer la entrada: ', e)
        continue

    try:
        completion = client.completions.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=2048
    )
    except Exception as e:
        print('Error al obtener la respuesta: ', e)
        continue

    try:
        print('You: ', prompt)
        print('ChatGPT: ', completion.choices[0].text)
    except Exception as e:
        print('Error al imprimir la respuesta: ', e)

