import requests
import base64
from llm import askllm

def retrieve(repo_owner, repo, files_changed):
    files = []
    for file_path in files_changed:
        url = f"https://api.github.com/repos/{repo_owner}/{repo}/contents/{file_path}"
        response = requests.get(url)
        if response.status_code == 200:
            json_response = response.json()
            file_content = base64.b64decode(json_response['content'])
            files.append(file_content.decode('utf-8'))
        else:
            raise Exception(f"Failed to fetch file: {response.status_code} {response.text}")
    docs = []
    for file in files:
        docs.append(askllm(file))
    return docs