import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

last_prompt = "" #Aca se guarda la ultima consulta

while True:
    try:
        if last_prompt:
            prompt = input(f"Edita la última consulta ('{last_prompt}'): ")
        else:
            prompt = input("Introduce una consulta (o presiona Ctrl+C para salir): ")

        if prompt.strip():
            last_prompt=prompt
    except KeyboardInterrupt: #Ctrl + c
        print('\nSaliendo del programa')
        break
    except Exception as e:
        print('Error al leer la entrada: ', e)
        continue

    try:
        completion = client.completions.create(
            model="gpt-3.5-turbo",
            prompt=last_prompt,
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



