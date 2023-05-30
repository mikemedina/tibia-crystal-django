FROM postgres:13.11-bullseye

# Set environment variables for the PostgreSQL user and database
ENV POSTGRES_USER tibia
ENV POSTGRES_PASSWORD clicky
ENV POSTGRES_DB crystal

# Copy the initialization script to the Docker image
COPY init.sql /docker-entrypoint-initdb.d/

# Start the PostgreSQL server
CMD ["postgres"]
