# StudentProject

This is a multi-app Django project containerized using Docker and set up for CI/CD using Jenkins.

## Run Locally

```bash
docker build -t studentproject .
docker run -p 8000:8000 studentproject
