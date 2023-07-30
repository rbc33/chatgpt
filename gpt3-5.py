import os
import openai
import getpass

archivo = "chatgptAPI.txt"

if os.path.exists(archivo):
    openai.api_key_path = archivo
else:
    API_KEY = getpass.getpass("Pide una clave API y pégala: ")
    with open(archivo, "w") as ap:
        ap.write(API_KEY)


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
