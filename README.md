# Documentation
# API Endpoints
## / - Homepage
### GET
- Returns a message confirming that the API is running.

## /document - Update Document
### POST
- Request Body: 
 - `repo_owner`: String (required)
 - `repo`: String (required)
 - `files_changed`: Array of Strings (required)
- Response: 
 - `updated_doc`: Updated document content
 - Status Code: 200 OK
 - Error Messages:
 + `error`: Missing data: 'repo' and 'repo_owner' required.
 + `message`: No files changed.
 + `error`: Failed to fetch files.
