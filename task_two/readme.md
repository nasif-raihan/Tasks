# Simple CRUD App

This Django-based CRUD (Create, Read, Update, Delete) app provides basic functionalities for managing data entities. Users can perform operations such as adding, deleting, retrieving, and updating data through a simple web interface.

## Features

- **Add:** Add new data entities to the system.
- **Delete:** Remove existing data entities from the system.
- **Retrieve:** View a list of all existing data entities and access their details.
- **Update:** Modify the information of existing data entities.

## Code Structure

### 1. **`home` View:**

- **URL:** `/home`
- **Description:** Renders the base HTML template with the title "home."

### 2. **`add_data` View:**

- **URL:** `/add_data`
- **Description:** Allows users to add new user data.
- **Form:** Uses the `UserForm` from `task_two.forms`.
- **HTTP Methods:** Handles both GET and POST requests.
  - **GET:** Renders the `add.html` template with the title "Add User" and an empty form.
  - **POST:** Validates and saves the form data. If successful, redirects to the `retrieve_data` view to display all user data.

### 3. **`retrieve_data` View:**

- **URL:** `/retrieve_data`
- **Description:** Retrieves and displays all user data.
- **HTTP Method:** Handles only GET requests.
  - **GET:** Renders the `retrieve.html` template with the title "User Data" and a list of all user data.

### 4. **`update_data` View:**

- **URL:** `/update_data/<uid>`
- **Description:** Allows users to update existing user data.
- **Form:** Uses the `UserForm` from `task_two.forms`.
- **HTTP Methods:** Handles both GET and POST requests.
  - **GET:** Renders the `update.html` template with the title "Update User" and a form pre-filled with the current user data.
  - **POST:** Validates and saves the form data. If successful, redirects to the `retrieve_data` view to display all updated user data.

### 5. **`delete_data` View:**

- **URL:** `/delete_data/<uid>`
- **Description:** Allows users to delete existing user data.
- **HTTP Method:** Handles only GET requests.
  - **GET:** Deletes the user with the specified UID and redirects to the `retrieve_data` view to display the remaining user data.

## Important Notes

- The app uses the `User` model from `.models` to store user information.

- The `UserForm` is employed for user data input and updating.

- Templates are used for rendering HTML pages (`add.html`, `retrieve.html`, `update.html`).

- Error handling includes checking for the existence of a user before attempting deletion.

- URLs and views are organized to follow RESTful conventions.

Feel free to customize, extend, or integrate this app into your Django project as needed. If you encounter any issues or have suggestions for improvement, please feel free to contribute or open an issue.

## Usage

1. **Add:**
   - Click on the "Add" button to add new data entities.

2. **Delete:**
   - On the data entities list page, click on the "Delete" button next to the entity you want to remove.

3. **Retrieve:**
   - View a list of all data entities on the homepage.

4. **Update:**
   - Click on the "Edit" button next to the entity you want to update, make changes, and save.

## Docker Considerations

- Ensure Docker is installed on your machine before building and running the Docker image.

- The Dockerfile assumes a simple setup. Adjustments may be needed based on your project structure and requirements.

Feel free to customize, extend, or integrate this app into your Django project as needed. If you encounter any issues or have suggestions for improvement, please feel free to contribute or open an issue.