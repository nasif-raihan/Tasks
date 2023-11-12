# Tasks Django Project

This Django project, named "tasks," is a simple application that includes three different tasks. 
They are:
1. [Task one](/task_one/readme.md): MNIST Digit Recognition using Convolutional Neural Network (CNN)
2. [Task two](/task_two/readme.md): Simple CRUD App
3. [Task Three](/task_three/readme.md): Coordinate Finder App


## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/tasks.git
   cd tasks
   ```

2. **Install Poetry:**

   If you don't have Poetry installed, use the following command to install it:

   ```bash
   make venv
   ```

3. **Run Migrations:**

   ```bash
   make migrate
   ```

## Run Locally

1. **Activate Virtual Environment:**

   ```bash
   poetry shell
   ```

2. **Run Local Server:**

   ```bash
   make run-local
   ```

   The application will be accessible at [http://localhost:8000/](http://localhost:8000/).

## Run with Docker

1. **Build and Run Docker Container:**

   ```bash
   make run-docker
   ```

   The application will be accessible at [http://localhost:8000/](http://localhost:8000/).

## Usage
1. Digit Recognition Performance visualization

![performance_analysis](/images/performance_analysis.png)

2. Home Page of the project

![home_page](/images/home.png)

3. Add User

![add](/images/add.png)

4. Retrieve Data

![retrieve](/images/retrieve.png)

5. Update Data

![update](/images/update.png)

6. Get Coordinates

![get_coordinates_1](/images/get_coordinates_1.png)


![get_coordinates_2](/images/get_coordinates_2.png)

## Important Notes

- The project uses Poetry for dependency management. The virtual environment is created and activated using Poetry.

- The Dockerfile assumes a simple project structure. Adjustments may be needed based on the project structure and requirements.

- The `make` commands simplify common tasks such as migrations, running locally, and building Docker images.
