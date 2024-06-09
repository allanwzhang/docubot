## API Endpoints

### /

- **Method:** GET

- **Response:** Redirects to the HTML template at templates/index.html

### /document

- **Method:** POST

- **Request Body Parameters:**
 - `repo_owner`: String. The owner of the GitHub repository.
 - `repo`: String. The name of the GitHub repository.
 - `files_changed`: Array of Strings. A list of filenames that have changed in the repository.

- **Example Request Body:**

```json
{
 "repo_owner": "your-github-username",
 "repo": "your-repository-name",
 "files_changed": ["README.md", "src/index.js"]
}
```

- **Response:**
 - Success:
 - `updated_doc`: String. The updated documentation in Markdown format, reflecting the changes made in the specified files.
 - Error:
 - `error`: String. An error message indicating the reason for the failure.

- **Response Examples:**
 - Success:
```json
{
 "updated_doc": "# Project Overview\n\n[...]\n\n## Recent Updates\n\n- Improved README.md with clearer instructions.\n- Refactored code in src/index.js for enhanced functionality."
}
```

 - Error:
```json
{
 "error": "Failed to fetch files"
}
```
