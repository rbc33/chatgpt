import requests
import getpass
import os

archivo = "chatgptAPI.txt"

if os.path.exists(archivo):
    with open(archivo, "r") as ap:
        API_KEY = ap.read()
else:
    API_KEY = getpass.getpass("Pide una clave API y pégala: ")
    with open(archivo, "w") as ap:
        ap.write(API_KEY)

API_URL = 'https://api.openai.com/v1/chat/completions'
session_token = None

def chat(prompt):
    global session_token
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'messages': [{'role': 'system', 'content': 'Nuevo usuario'}, {'role': 'user', 'content': prompt}],
        'max_tokens': 50,
        'temperature': 0.7
    }
    if session_token:
        data['messages'][0]['role'] = 'assistant'
        data['messages'][0]['content'] = session_token
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        session_token = response_data['choices'][0]['message']['content']
        return response_data['choices'][0]['message']['content']
    else:
        return 'Error al realizar la solicitud'


prompt = input("qué? \n")

while True:
    prompt = input("ya? \n")
    respuesta = chat(prompt)
    print(respuesta)
