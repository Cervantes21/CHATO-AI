import os
import argparse
import requests
from dotenv import load_dotenv

load_dotenv()

url = "https://api.openai.com/v1/engines/davinci-codex/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
}

def generate_text(prompt, temperature=0.5, max_tokens=100):
    data = {
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['text']

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Genera texto utilizando la API de OpenAI')
    parser.add_argument('prompt', type=str, help='La frase de inicio para la generación de texto')
    parser.add_argument('--temperature', type=float, default=0.5, help='La temperatura para la generación de texto')
    parser.add_argument('--max-tokens', type=int, default=100, help='La cantidad máxima de tokens para la generación de texto')
    args = parser.parse_args()

    prompt = args.prompt.strip()
    temperature = args.temperature
    max_tokens = args.max_tokens

    if not prompt:
        print('La frase de inicio no puede estar vacía')
    else:
        response = generate_text(prompt, temperature=temperature, max_tokens=max_tokens)
        print("ChatGPT: " + response)

