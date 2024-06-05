from flask import Flask, jsonify, request
from controller import retrieve
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, Flask! Welcome to Docubot!'

@app.route('/document', methods=['POST'])
def document():
    if request.is_json:
        data = request.get_json()
        repo_owner = data.get('repo_owner')
        repo = data.get('repo')
        files_changed = data.get('files_changed')

        if not repo_owner or not repo:
            return jsonify(error="Missing data: 'repo' and 'repo_owner' required."), 400
        if not files_changed:
            return jsonify(message="No files changed."), 200
        
        try:
            # print(repo_owner, repo, files_changed)
            updated_doc = retrieve(repo_owner, repo, files_changed)
            
            if updated_doc == "No previous documentation found":
                return jsonify({'error': "No previous documentation found"})

            return jsonify({'updated_doc': updated_doc})
        except Exception as e:
            print(f"Exception: {e}")
            return jsonify(error="Failed to fetch files"), 400
    else:
        return jsonify(message="Request was not JSON"), 400

if __name__ == '__main__':
    app.run(debug=True)
