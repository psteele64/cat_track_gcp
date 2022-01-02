# Cat Track API - GCP CLoud Run version
## My Nucamp Coding Bootcamp portfolio  project.
### Cat Track (ctapi) is a Django REST API App to rtrack cats, vets, fosters, and medications for a small cat rescue. This is my first attempt at Django REST API in Python with a Postgresql DB as the back end deployed on GCP Cloud Run. It's a Django REST API built on Django Rest Framework.

https://www.django-rest-framework.org/

## PIP Prerequisites:
Required Python packages are in requirements.txt file in the project root folder. Create a virtual python environment and install required packages:
```sh
python3 -m venv env
pip install -r requirements.txt
```
### Follow this guide for deployment to GCP Cloud Run:

[Django on Google Cloud Run. In this tutorial, we will create a… | by Rahul Sharma | Medium](https://medium.com/@rahulxsharma/django-on-google-cloud-run-3f2f93ae0917)

### Useful commands:
Migrations/Collect Static Files and create Admin site superuser account:
```bash
docker-compose run --rm app sh -c "python manage.py migrate" (FIRST TIME CREATES TABLES FOR DRFADMIN SITE)
docker-compose run --rm app sh -c "python manage.py makemigrations ctapi" (ONLY RUN FIRST TIME: to create migrations for ctapi app)
docker-compose run --rm app sh -c "python manage.py makemigrations" (after updating Django models)
docker-compose run --rm app sh -c "python manage.py migrate" (after updating models and "makemigrations"
docker-compose run --rm app sh -c "python manage.py collectstatic --no-input"
docker compose run --rm app sh -c "python manage.py createsuperuser --username=<DESIRED_USERNAME> --email=<YOUR EMAIL>"
```
### GCP and GIT specific info:
API is deployed on Cloud Run using GIT pushes from local repository to trigger builds after code updates. 
Local git repository folder name: 'django-gcp-cloudrun'
GS_BUCKET_NAME=django_dev_bucket
SQL connection for SQL_AUTH_PROXY: sodium-petal-335020:us-central1:django-dev-db
Get current URL from Cloud Run. Last known: https://ctapi-z2o35wwlva-uc.a.run.app


