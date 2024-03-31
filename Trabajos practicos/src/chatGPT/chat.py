import os
import sys
from openai import OpenAI #Libreria de OpenAI
from dotenv import load_dotenv #Entornos de variable
# Mi api esta limitada, asi que no pude verificar que funcionara de verdad todo
load_dotenv() #Uso de archivo .env

# openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'] #llamado de la api de openai
)

conversation_buffer = [] #almacen de consultas y respuestas

if "--convers" in sys.argv: #verifica si esta en modo convers
    CONVERS_MODE = True
else:
    CONVERS_MODE = False

def add_to_buffer(query, response):
    conversation_buffer.append((query, response)) #almacena la consulta y respuesta en el buffer

def get_last_query(query, response): #obtiene la ultima consulta
    if conversation_buffer:
        return conversation_buffer[-1][0]
    else:
        return ""

def get_full_query():
    return " ".join(query for query, _ in conversation_buffer) #Obtiene toda la conversacion

#Verificacion para la conversacion
while True:
    try:
        if CONVERS_MODE:
            prompt = input("Introduce una pregunta (o presiona Ctrl+C para salir): ")
        else: #En caso que no este en convers mode
            prompt = input("Introduce una pregunta: ")
        if prompt.strip(): # Verifica que la entrada no esté vacía
            LAST_QUERY= get_last_query() if CONVERS_MODE else "" # Guarda la ultima consulta si esta en modo convers
            FULL_QUERY = get_full_query() if CONVERS_MODE else "" # Guarda toda la conversacion si esta en modo convers
            prompt = f"{LAST_QUERY} {prompt} {FULL_QUERY}" if CONVERS_MODE else prompt
        #Uso de la api
        COMPLETION = client.completions.create(
            model="gpt-3.5-turbo",
            prompt=prompt,
            max_tokens=2048
    )
        print('You: ', prompt) #La consulta que nosotros hicimos
        print('ChatGPT: ', COMPLETION.choices[0].text) #Respuesta de ChatGPT

        response = COMPLETION.choices[0].text #darle valor a response con lo que nos aporte ChatGPT

        if CONVERS_MODE: #En caso que este en modo conversacion
            add_to_buffer(prompt, response)  # Añadimos la response al buffer

    except KeyboardInterrupt: #Ctrl + c
        print("\nSaliendo del programa...")
        break # Corta el programa
    except Exception as e: #En caso de algun error
        print("Error:", e)