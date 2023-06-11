# Bookstore-API

This is an open-source API for a fictional bookstore named "Geek Text". This project is for Group 2 Summer 2023 CEN4010.

## Setup

Follow the instructions below to run the API locally:

1. Clone the repository: Clone the repository from GitHub using GitHub Desktop or the terminal.

2. Setting up MySQL:
   - Install MySQL server on your preferred operating system:
     - Download MySQL server from: [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)
     - Only install the server, not the client or any other recommended software.
   - Create a database on the MySQL server:
     - Run the following command: `CREATE DATABASE geek_text;`
   - Create a user on the MySQL server:
     - Run the following commands:
       ```
       USE geek_text;
       CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
       ```
     - Note: Replace "user" and "password" with more secure values.
     - Note: "localhost" can be a local or remote IP depending on where the MySQL server is hosted.
   - Grant privileges to the user for using the database:
     - Run the following command:
       ```
       GRANT ALL PRIVILEGES ON geek_text.* TO 'user'@'localhost';
       ```

3. Configure the environment:
   - Copy the `.env-example` file and rename the copy to `.env`.
   - Fill in the variables in the `.env` file.

4. Start the server:
   - Run the following command in Bash:
     ```
     python manage.py runserver
     ```

## Making a SQL Migration

### Migration Template
To create a template for a SQL migration, run the following command:
```
python manage.py makemigrations
```
After running this command, you can write the migration.

### Running Migration
To apply all unran migrations to the database, use the following command:
```
python manage.py migrate
```
Be cautious as mistakes in the migration may require a rollback or even wiping the database.