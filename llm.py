import requests

def askllm(files, api_key, prev_doc):
    cohere_api_url = 'https://api.cohere.ai/v1/chat'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    combined_content = "Previous Documentation:\n\n" + prev_doc + "\n\nNew Files:\n\n"
    for file_path, file_content in files:
        combined_content += f"File: {file_path}\n{file_content.decode('utf-8')}\n\n"

    # Create a prompt for generating documentation
    message = f"Generate comprehensive documentation for the following files. Only generate documentation for api endpoints:\n\n{combined_content}"
    payload = {
        'message': message,
    }

    response = requests.post(cohere_api_url, headers=headers, json=payload)

    if response.status_code == 200:
        content = response.json()
        return content['text']
    else:
        raise Exception(f"Failed to get response from Cohere: {response.status_code} {response.text}")
