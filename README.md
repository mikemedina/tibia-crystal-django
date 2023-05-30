# Tibia Utility Django Back-end

![Tibia Utility Logo](logo.png)

This Django back-end serves as the core component of the Tibia Utility website, designed to provide helpful calculations and features for Tibia players. The utility includes functionalities such as spell damage calculation, party hunt loot distribution, and more.

## Getting Started

To get started with the Tibia Utility Django back-end, follow the instructions below.

### Prerequisites

- Git, Docker Desktop, and Docker Compose

### Build the PostgreSQL Container

1. Ensure Docker is installed on your system.

2. Clone this repository to your local machine.

3. In the terminal, go to the project's root directory.

4. Use docker-compose to provision the database and launch the app

   ```bash
   docker-compose up
   ```
   
This command will provision the database container, build the Django backend, and start the backend container, linking it to the PostgreSQL container.

5. Once the Django container is up and running, you can access the application at http://localhost:8000/spells
   or the admin page at http://localhost:8000/admin. The default admin credentials are tibia/clicky


### Utilities
Use this command to connect to and query the postgres container:

   ```bash
   docker exec -it tibia-postgres psql -U tibia -d crystal 
   ```
