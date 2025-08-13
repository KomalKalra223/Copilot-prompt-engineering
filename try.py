import requests

# Replace with your server's IP address
OLLAMA_URL = "http://10.9.9.148:11434/api/generate"

payload = {
    "model": "llama3.1:8b",  # Change to your model name
    "prompt": "Hello, Ollama!"
}

response = requests.post(OLLAMA_URL, json=payload)
print(response.json())