from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv('AWANLLM_API_KEY')

def askllm(code):
    url = "https://api.awanllm.com/v1/chat/completions"

    payload = json.dumps({
    "model": "Awanllm-Llama-3-8B-Dolfin",
    "messages": [
        {
        "role": "user",
        "content": f"Can you create documentation for the api endpoints created by this code?\n{code}"
        }
    ]
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {api_key}"
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    llm_response = response.json()['choices'][0]['message']['content']

    return llm_response