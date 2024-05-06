# Inventory Flask CRUD Project with Dockerfile, MySQL, SQLAlchemy and Docker Compose

This repository contains a CRUD (Create, Read, Update, Delete) project built with Python Flask, MySQL, SQLAlchemy, and Docker Compose. The project is containerized using Docker, with separate services for the Flask application and MySQL database.

## Quick start (With Docker)
```bash
$ docker compose up
```

## Prerequisites

Before you begin, ensure you have Docker and Docker Compose installed on your system.

- [Docker Installation Guide](https://docs.docker.com/get-docker/)
- [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)
- Have Docker installed and set up on your system.
- Understand the basics of SQL and relational databases.
- Understand Docker

## Getting Started

1. Clone this repository to your local machine:

    ```bash
    git clone 
    ```

2. Navigate to the project directory:

    ```bash
    cd hootsi_project
    ```

3. Ensure Docker is running on your machine.

4. Run the following command to start the application and database services using Docker Compose:

    ```bash
    docker-compose up flask_app
    ```

5. Once the services are up and running, you can access the Flask application at `http://localhost:4000`.

## Project Structure

The project structure is as follows:

Hootsi_project/
│
│
├── templates/             # HTML templates
│   ├── create.html
│   ├── delete.html
│   ├── header.html
│   ├── index.html
│   ├── master.html
│   └── update.html
├── app.py                # Flask app with routes & SQLAlchemy model
├── docker-compose.yml    # Docker Compose configuration file
├── Dockerfile            # Dockerfile for Flask application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


## Configuration

- The `docker-compose.yml` file defines the services for the Flask application and MySQL database, along with their configurations.
- The Flask application uses environment variables defined in the `flask_app` service to connect to the MySQL database.
- MySQL database configuration is specified in the `mysql_db` service, including the database name, user credentials, and health check settings.

## Usage

- The Flask application provides endpoints for CRUD operations on the MySQL database.
- You can customize the application routes and functionality by modifying the files in the `app/` directory.
- Ensure that you have the necessary Python dependencies installed. You can install them using:

    ```bash
    pip install -r requirements.txt
    ```

- To stop the services, use `Ctrl + C`, and then run:

    ```bash
    docker-compose down
    ```

---

With these instructions, you should be able to set up and run the Flask CRUD project with MySQL using Docker Compose easily.
