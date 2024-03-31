import os
import sys
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY']
)

conversation_buffer = [] #almacen de consultas y respuestas

if "--convers" in sys.argv:
    convers_mode = True
else:
    convers_mode = False

def add_to_buffer(query, response):
    conversation_buffer.append((query, response)) #almacena la consulta y respuesta en el buffer

def get_last_query(query, response):
    if conversation_buffer:
        return conversation_buffer[-1][0]
    else:
        return ""
    
def get_full_query():
    return " ".join(query for query, _ in conversation_buffer) #Obtiene toda la conversacion

last_prompt = "" #Aca se guarda la ultima consulta

while True:
    try:
        if convers_mode:
            prompt = input("Introduce una pregunta (o presiona Ctrl+C para salir): ")
        else:
            prompt = input("Introduce una pregunta: ")

        if prompt.strip():
            last_query= get_last_query() if convers_mode else ""
            full_query = get_full_query() if convers_mode else ""
            prompt = f"{last_query} {prompt} {full_query}" if convers_mode else prompt

        completion = client.completions.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=2048
    )
        print('You: ', prompt)
        print('ChatGPT: ', completion.choices[0].text)

        response = completion.choices[0].text

        if convers_mode:
            add_to_buffer(prompt, response)

    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        break
    except Exception as e:
        print("Error:", e)
