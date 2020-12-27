# Azure Active Directory Web App using Django and Python

This sample demonstrates how to authenticate a Django web app using Azure Active Directory Authentication.

# Running the App

## App registration

1. Register an Azure AD application with web application authentication and a reply URL of `https://127.0.0.1:8000/complete/aad`, and generate a client secret.
2. Rename `.env.example` to `.env` and populate it with the AAD_CLIENT_ID, AAD_TENANT_ID, AAD_CLIENT_SECRET

## Running the application

1. Have a Python environment, you can use miniconda, venv, whatever you prefer, as long as you are running Python 3.x
2. Install the needed dependencies with `pip install -r requirements.txt`
3. Run `python manage.py migrate` to migrate the database schema
4. Run `python manage.py runsslserver 8000` to run the server, or open in VSCode and hit F5

Open the browser, and visit `https://127.0.0.1` and sign in.

# Running the App with Docker

To run the sample with `docker`:

1. Rename the `.env.example` file to `.env`, change the environment variables, and register the URLs above.
2. Run `sh exec.sh` to build and run the docker image in Linux or run `.\exec.ps1` to build and run the docker image on Windows.
3. Use either nginx or ngrok or deploy to Azure App Service to expose the site on https, and modify the app registration reply URL accordingly. Azure AD requires your app to run on https unless it is localhost.