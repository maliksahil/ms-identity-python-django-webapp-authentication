docker build -t aad-django .
docker run --env-file .env -p 8000:8000 -it aad-django
