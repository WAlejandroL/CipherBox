# CipherBox

Aplicación básica en Python para autenticación de usuarios usando MongoDB.

## Requisitos
- Python 3.x
- pymongo
- bcrypt

## Instalación
1. Instala las dependencias:
   ```bash
   pip install pymongo bcrypt
   ```
2. Configura tu conexión a MongoDB en el archivo `main.py`.

## Uso
- Ejecuta el archivo principal:
  ```bash
  python main.py
  ```
- Se mostrarán los usuarios en la colección y podrás iniciar sesión con usuario y contraseña.

## Estructura
- `main.py`: Código principal de autenticación y conexión a MongoDB.

## Notas
- Actualmente la verificación de contraseña es en texto plano.
- Para mayor seguridad, se recomienda usar bcrypt para hashear las contraseñas.
