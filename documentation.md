# API Documentation

## Introduction

This documentation outlines the available API endpoints and their functionalities for interacting with the application. 

Base URL: `https://docubot-two.vercel.app/`

## Endpoints

### /document

**Method:** POST

**Request Body:**

- `repo_owner`: String. The owner of the repository.
- `repo`: String. The name of the repository.
- `files_changed`: Array of Strings. A list of filenames that have changed.

**Response:**

- `updated_doc`: String. The updated documentation in Markdown format.

--- 

This comprehensive documentation provides a clear outline of the API endpoints, including the request parameters and the expected responses. It serves as a reference for developers looking to interact with the application's API.
