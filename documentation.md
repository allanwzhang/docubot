## API Endpoints

### /document

- **Method:** POST

- **Request Body Parameters:**

 - `repo_owner`: String. The owner of the GitHub repository.
 - `repo`: String. The name of the GitHub repository.
 - `files_changed`: Array of Strings. A list of filenames that have changed in the repository.

- **Example Request Body:**

 ```json
 {
 "repo_owner": "allanwzhang",
 "repo": "docubot",
 "files_changed": ["README.md", "src/main.py"]
 }
 ```

- **Response:**

 - `updated_doc`: String. The updated documentation in Markdown format, containing the changes reflected in the specified files.

- **Response Example:**

 ```json
 {
 "updated_doc": "# Docubot\n\n[...]\n\n## New Changes\n\n- Updated README.md with latest features.\n- Refactored code in src/main.py for improved performance."
 }
 ```
