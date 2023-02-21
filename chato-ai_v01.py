import requests

url = "https://api.openai.com/v1/engines/davinci-codex/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

def generate_text(prompt, temperature=0.5, max_tokens=100):
    data = {
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['text']

while True:
    prompt = input("Escribe algo para que ChatGPT responda (o escribe 'salir' para terminar): ")
    if prompt.lower() == "salir":
        break
    response = generate_text(prompt)
    print("ChatGPT: " + response)

