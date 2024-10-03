## API Endpoints

### /

- **Method:** GET
- **Description:** This endpoint serves as the homepage or landing page of the application.
- **Response:** Redirects the client to the HTML template located at `templates/index.html`.

### /document

- **Method:** POST
- **Description:** This endpoint is used to generate updated documentation based on changes made in a GitHub repository.
- **Request Body Parameters:**
 - `repo_owner`: String. The GitHub username of the repository owner.
 - `repo`: String. The name of the GitHub repository.
 - `files_changed`: Array of Strings. A list of filenames that have been modified in the repository.
- **Example Request Body:**
```json
{
 "repo_owner": "octocat",
 "repo": "my-repository",
 "files_changed": ["README.md", "src/app.js"]
}
```
- **Responses:**
 - **Success:**
 - `updated_doc`: String. Contains the updated documentation in Markdown format, incorporating the changes from the specified files.
 - **Example Success Response:**
```json
{
 "updated_doc": "# My Repository Documentation\n\n## Recent Changes\n\n- Updated README with new contribution guidelines.\n- Refactored code in src/app.js for improved performance."
}
```
 - **Error:**
 - `error`: String. Provides an error message describing the reason for the failure.
 - **Example Error Response:**
```json
{
 "error": "Repository not found"
}
```
