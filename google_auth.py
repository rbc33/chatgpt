from google.oauth2 import id_token
from google.auth.transport import requests

def verificar_token(token):
    CLIENT_ID = input('user')
    try:
        id_info = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
        if 'sub' in id_info:
            return id_info['sub']
    except ValueError:
        return None

# Ejemplo de uso
token = 'el_token_recibido_de_google'
usuario_id = verificar_token(token)
if usuario_id:
    # El token es válido, puedes guardar la clave API asociada con este usuario
    guardar_clave_api(usuario_id, clave_api)
else:
    # El token no es válido
    print('Error de autenticación con Google')
