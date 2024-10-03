## API Endpoints

### /

- **Method:** GET
- **Description:** Retrieves the homepage or landing page of the application.
- **Response:** Redirects the client to the HTML page located at the specified path.

### /document

- **Method:** POST
- **Description:** Generates updated documentation based on changes in a GitHub repository.
- **Request Body Parameters:**
 - `repo_owner` (String): The GitHub username of the repository owner.
 - `repo` (String): The name of the GitHub repository.
 - `files_changed` (Array of Strings): A list of filenames that have been modified in the repository.
- **Example Request Body:**
```json
{
 "repo_owner": "my-user",
 "repo": "my-repo",
 "files_changed": ["file1.py", "folder/file2.js"]
}
```
- **Responses:**
 - **Success:**
 - `updated_doc` (String): Contains the generated documentation in Markdown format, including the changes from the specified files.
 - **Example Success Response:**
 ```json
 {
 "updated_doc": "# Documentation for my-repo\n\n## Changes in this update:\n- file1.py: Added new function for data processing.\n- folder/file2.js: Refactored code for improved readability."
 }
 ```
 - **Error:**
 - `error` (String): Provides an error message describing the failure.
 - **Example Error Response:**
 ```json
 {
 "error": "Invalid repository credentials."
 }
 ```
