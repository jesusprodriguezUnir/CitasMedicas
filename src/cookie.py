import requests

def obtener_cookies():
    url_login = 'https://citahos.sanidadmadrid.org/webae/LoginAction.do'  # URL de inicio de sesión o acción inicial
    payload = {
        'username': 'tu_usuario',  # Reemplaza con tus credenciales
        'password': 'tu_contraseña'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }
    
    session = requests.Session()
    response = session.post(url_login, data=payload, headers=headers)
    
    if response.status_code == 200:
        print("Cookies obtenidas correctamente")
        return session.cookies.get_dict()
    else:
        print(f"Error al obtener cookies: {response.status_code}")
        return None

cookies = obtener_cookies()
print(cookies)