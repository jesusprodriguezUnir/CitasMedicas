import redis

# Conexión al servidor Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Probar conexión
r.set('clave', 'Hola desde Python')
valor = r.get('clave')

print(valor.decode('utf-8'))

# Listar todas las claves almacenadas en Redis
print("\nClaves almacenadas en Redis:")
for key in r.keys('*'):
    key_type = r.type(key).decode('utf-8')  # Obtener el tipo de la clave
    if key_type == 'string':  # Solo realizar GET si el tipo es string
        value = r.get(key)
        print(f"{key.decode('utf-8')} = {value.decode('utf-8')}")
    else:
        print(f"{key.decode('utf-8')} es de tipo {key_type}, no se puede usar GET.")
