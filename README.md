
# CipherBox

Aplicación básica en Python para autenticación de usuarios y registro de acciones usando MongoDB.

## Requisitos
- Python 3.x
- pymongo
- bcrypt

## Instalación
1. Instala las dependencias:
   ```powershell
   pip install pymongo bcrypt
   ```
2. Configura tu conexión a MongoDB en el archivo `DB.py`.

## Uso
- Ejecuta el archivo principal:
  ```powershell
  python main.py
  ```
- Podrás registrar usuarios, iniciar sesión y todas las acciones importantes quedarán registradas en la colección `logs` de MongoDB.

## Estructura
- `main.py`: Código principal de autenticación y conexión a MongoDB.
- `DB.py`: Funciones para registro de usuarios, login y registro de logs.

## Seguridad
- Las contraseñas se almacenan usando bcrypt (hash seguro).
- El login verifica la contraseña usando bcrypt y registra cada intento (exitoso o fallido) en la base de datos.

## Registro de acciones (logs)
Cada acción relevante (login, login_fail, cifrar, decifrar, etc.) se guarda en la colección `logs` con los siguientes campos:
- `id`: Identificador único
- `usuario`: Usuario que realiza la acción
- `accion`: Tipo de acción (login, logout, cifrar, decifrar, etc.)
- `archivo`: Nombre del archivo (opcional, para futuras funciones)
- `fecha`: Fecha de la acción
- `hora`: Hora de la acción

## Notas
- Para mayor seguridad, nunca almacenes contraseñas en texto plano.
- Puedes extender el sistema de logs para registrar más acciones según lo requiera tu aplicación.
