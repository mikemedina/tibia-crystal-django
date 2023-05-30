# Tibia Utility Django Back-end

![Tibia Utility Logo](logo.png)

This Django back-end serves as the core component of the Tibia Utility website, designed to provide helpful calculations and features for Tibia players. The utility includes functionalities such as spell damage calculation, party hunt loot distribution, and more.

## Getting Started

To get started with the Tibia Utility Django back-end, follow the instructions below.

### Prerequisites

- Docker

### Starting the PostgreSQL Container

1. Ensure Docker is installed on your system.

2. Clone this repository to your local machine.

3. Navigate to the project's root directory.

4. In the terminal, go to the `docker/postgres` directory:

   ```bash
   cd docker/postgres
   ```

5. Build the PostgreSQL image and start the container:

   ```bash
   docker build -t tibia-postgres .
   docker run -d 
     --name tibia-postgres 
     -p 5432:5432 
     -v "${pwd}/init.sql:/docker-entrypoint-initdb.d/init.sql" 
     -e POSTGRES_USER=tibia 
     -e POSTGRES_PASSWORD=clicky 
     -e POSTGRES_DB=crystal 
     tibia-postgres:latest
   ```
   
This command will build the PostgreSQL image and start the container, initializing the database with the init.sql script.

### Starting the Django Backend

1. Make sure the PostgreSQL container is running.

2. In the terminal, go to the project's root directory.

3. Build the Django backend image and start the container:

   ```bash
   docker-compose up
   ```
   
This command will build the Django backend image and start the container, linking it to the PostgreSQL container.


4. Once the Django container is up and running, you can access the application at http://localhost:8000.


### Utilities
Use this command to connect to and query the postgres container:

   ```bash
   docker exec -it tibia-postgres psql -U tibia -d crystal 
   ```
