# CHATO
Un asistente virtual vinculado con tu cuenta de OPENAI

Creación del ambiente virtual de Python
Abre una terminal en la carpeta donde se encuentra el archivo requirements.txt.

# **Información importante:**

Para continuar debes de tener tu API-KEY proporcionado por OPENAI
sí no cuentas con uno puedes generarlo [En este link](https://platform.openai.com/account/api-keys)

Una vez que tengas ese código deberas copiarlo y guardarlo.

Cuando tengas ese código. Abre un editor de texto y crea un archivo ".env" así, sin nombre, solo la pura extensión.

en el cuál crearás una variable que se llame **API-KEY**
ejemplo:

Con editor de texto vim, o nano:

```
vim .env
```

```
API_KEY=sk-y-pones-tu-clave-que-te-dieron-sin-espacios
```

Guardas el archivo y ejecutas los siguientes pasos:


# Ejecuta el siguiente comando para crear un nuevo ambiente virtual de Python:

```
python -m venv env
```

Esto creará una carpeta llamada env en tu directorio actual que contendrá todos los archivos necesarios para tu ambiente virtual.

Activa el ambiente virtual ejecutando el siguiente comando:

En Windows:
```
.\env\Scripts\activate
```

En Linux/macOS:
```
source env/bin/activate
```
Una vez activado el ambiente virtual, deberías ver (env) en el inicio de tu línea de comandos.

Instalación de las dependencias
Ejecuta el siguiente comando para instalar todas las dependencias especificadas en el archivo requirements.txt:

```
pip install -r requirements.txt
```

Esto instalará todas las dependencias necesarias para ejecutar el script.

Ejecución del script
Ejecuta el siguiente comando para iniciar el script:

```
python chato.py [--temperature TEMPERATURE] [--max-tokens MAX_TOKENS]
```
--temperature: la temperatura para la generación de texto (opcional, por defecto es 0.5).
--max-tokens: la cantidad máxima de tokens para la generación de texto (opcional, por defecto es 218).
El script te pedirá que ingreses la frase de inicio para la generación de texto.

Documentación:

generate_text(prompt, temperature=0.1, max_tokens=218)
Genera texto utilizando la API de OpenAI.

Argumentos:

prompt (str): la frase de inicio para la generación de texto.
temperature (float, opcional): la temperatura para la generación de texto (por defecto es 0.1).
max_tokens (int, opcional): la cantidad máxima de tokens para la generación de texto (por defecto es 218).
Retorna:

str: el texto generado por la API de OpenAI.
Uso
Puedes ejecutar el script utilizando el comando:

```
python chato.py [--temperature TEMPERATURE] [--max-tokens MAX_TOKENS]
```

--temperature: la temperatura para la generación de texto (opcional, por defecto es 0.5).
--max-tokens: la cantidad máxima de tokens para la generación de texto (opcional, por defecto es 218).
El script te pedirá que ingreses la frase de inicio para la generación de texto. El resultado de la generación de texto será impreso en la consola.

¡Listo! Con estos pasos ya tendrás instaladas las dependencias, podrás ejecutar el script.

