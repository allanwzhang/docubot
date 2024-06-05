from dotenv import load_dotenv
import os
import requests
import base64
from llm import askllm

load_dotenv()
api_key = os.getenv('COHERE_API_KEY')

def retrieve(repo_owner, repo, files_changed):
    files = []
    for file_path in files_changed:
        url = f"https://api.github.com/repos/{repo_owner}/{repo}/contents/{file_path}"
        response = requests.get(url)
        if response.status_code == 200:
            json_response = response.json()
            file_content = base64.b64decode(json_response['content'])
            files.append((file_path, file_content))
        else:
            raise Exception(f"Failed to fetch file: {response.status_code} {response.text}")
        
    doc = retrieve_previous_documentation(repo_owner, repo)

    if doc == "NO DOCUMENTATION FOUND":
        return "No previous documentation found"
    
    print(doc)
    
    try:
        response = askllm(files, api_key, doc)
        print(response)
    except Exception as e:
        print(f"Exception: {e}")
        return "Failed to generate documentation"
    
    return response

def retrieve_previous_documentation(repo_owner, repo):
    file_path = "documentation.md"
    url = f"https://api.github.com/repos/{repo_owner}/{repo}/contents/{file_path}"
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        file_content = base64.b64decode(json_response['content'])
        return file_content.decode('utf-8')
    else:
        return "NO DOCUMENTATION FOUND"
