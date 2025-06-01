import requests
from http.cookiejar import CookieJar

jar = CookieJar()
session = requests.Session()
session.cookies = jar

try:
    response = session.get("https://www.comunidad.madrid")
    response.raise_for_status()  # Verifica si la solicitud fue exitosa
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")
    exit()

cookies = {
    'AlteonP': 'BG5SICRMHawSGeZN9AA3YA$$',
    '_pk_id.100.f94c': 'd2f479315072abc7.1748543534.1.1748543553.1748543534.',
    '_pk_ref..f94c': '%5B%22%22%2C%22%22%2C1748618904%2C%22https%3A%2F%2Fwww.comunidad.madrid%2F%22%5D',
    '_pk_id..f94c': '7dfcc3445ed37b3b.1748237895.5.1748618904.1748546444.',
    '_pk_ref.undefined.f94c': '%5B%22%22%2C%22%22%2C1748618904%2C%22https%3A%2F%2Fwww.comunidad.madrid%2F%22%5D',
    '_pk_id.undefined.f94c': '7dfcc3445ed37b3b.1748237895.5.1748618904.1748546444.',
    'JSESSIONID': 'jOwndv8fDeE7DICXX_r6xFgtGlSTkt9T0dk15F8moDC4g3ChVBJY!-1403265650'
}

# Iterar sobre las cookies y mostrar su información
for name, value in cookies.items():
    # Aquí asumimos que no hay información de expiración en el diccionario
    expires = "Sin expiración"  # Puedes agregar lógica para manejar expiraciones si tienes esa información
    print(f"{name} = {value}, expires = {expires}")
