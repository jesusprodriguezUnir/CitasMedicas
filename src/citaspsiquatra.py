import requests
import re

def obtener_citas(id_centros):
    url = 'https://citahos.sanidadmadrid.org/webae/MostrarCitasDisponibleAction.do?1748705253879'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://citahos.sanidadmadrid.org',
        'Referer': 'https://citahos.sanidadmadrid.org/webae/BuscarCentroAction.do?1748705246705',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }
    cookies = {
        'AlteonP': 'BC84QiRMHaz1XT13N1QVCw$$',
        '_pk_id.100.f94c': 'd2f479315072abc7.1748543534.1.1748543553.1748543534.',
        '_pk_ref..f94c': '%5B%22%22%2C%22%22%2C1748618904%2C%22https%3A%2F%2Fwww.comunidad.madrid%2F%22%5D',
        '_pk_id..f94c': '7dfcc3445ed37b3b.1748237895.5.1748618904.1748546444.',
        '_pk_ref.undefined.f94c': '%5B%22%22%2C%22%22%2C1748618904%2C%22https%3A%2F%2Fwww.comunidad.madrid%2F%22%5D',
        '_pk_id.undefined.f94c': '7dfcc3445ed37b3b.1748237895.5.1748618904.1748546444.',
        'JSESSIONID': 'NN4m85R-93rJAlh9KeLpvgwG82l2q8-tfhbNLlML4T1HNcybhBAN!-1403265650'
    }
    
    resultados = []
    for id_centro in id_centros:
        data = {'ID_CENTRO': id_centro}
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        if response.status_code == 200:
            resultados.append(response.text)
        else:
            print(f"Error al obtener citas para el centro {id_centro}: {response.status_code}")
    
    return resultados

def filtrar_citas(texto):
    citas = re.findall(
        r'\b(lunes|martes|miércoles|jueves|viernes|sábado|domingo),\s*(\d{1,2}\s\w+\s\d{4})\s(\d{2}:\d{2})\s.*?-.*?(?=\n|$)',
        texto, re.IGNORECASE
    )
    return citas

centros = {
    2552: "HOSPITAL FUNDACION JIMENEZ DIAZ",
    2553: "C.E.P. PONTONES FJD (HOSPITAL FUNDACION JIMENEZ DIAZ)",
    2546: "HOSPITAL CLINICO SAN CARLOS",
    2560: "HOSPITAL DE EL ESCORIAL",
    2550: "HOSPITAL GENERAL UNIVERSITARIO GREGORIO MARAÑON",
    2557: "HOSPITAL UNIVERSITARIO 12 DE OCTUBRE",
    2555: "HOSPITAL UNIVERSITARIO DE FUENLABRADA",
    2558: "HOSPITAL UNIVERSITARIO DE GETAFE",
    2548: "HOSPITAL UNIVERSITARIO DE LA PRINCESA",
    2828: "HOSPITAL UNIVERSITARIO DE TORREJON",
    2661: "HOSPITAL UNIVERSITARIO DEL HENARES",
    2663: "HOSPITAL UNIVERSITARIO DEL SURESTE",
    2665: "HOSPITAL UNIVERSITARIO DEL TAJO",
    3026: "HOSPITAL UNIVERSITARIO GENERAL DE VILLALBA",
    2659: "HOSPITAL UNIVERSITARIO INFANTA ELENA",
    2662: "HOSPITAL UNIVERSITARIO INFANTA LEONOR",
    2539: "HOSPITAL UNIVERSITARIO LA PAZ",
    2556: "HOSPITAL UNIVERSITARIO PRINCIPE DE ASTURIAS",
    2712: "HOSPITAL UNIVERSITARIO PUERTA DE HIERRO MAJADAHONDA",
    2559: "HOSPITAL UNIVERSITARIO RAMON Y CAJAL",
    2829: "HOSPITAL UNIVERSITARIO REY JUAN CARLOS"
}

id_centros = [
    2552, 2553, 2546, 2560, 2550, 2557, 2555, 2558, 2548, 2828, 2661, 2663, 
    2665, 3026, 2659, 2662, 2539, 2556, 2712, 2559, 2829
]

citas = obtener_citas(id_centros)

print("Cita para: Psiquiatría")
for id_centro in id_centros:
    print(centros[id_centro])
print("Las primeras citas disponibles para su solicitud de Psiquiatría")
print("En los centros elegidos\n")

for idx, cita in enumerate(citas):
    citas_filtradas = filtrar_citas(cita)
    if citas_filtradas:
        for dia, fecha, hora in citas_filtradas:
            print(f"{dia.capitalize()}, {fecha} {hora} horas - {centros[id_centros[idx]]}")
        print()