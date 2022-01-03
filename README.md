# Cat Track API - GCP CLoud Run version
## My Nucamp Coding Bootcamp portfolio  project.
#### Cat Track (ctapi) is a Django REST API App to track cats, vets, fosters, and medications for a small cat rescue. This is my first attempt at Django REST API in Python with a Postgresql DB as the back end deployed on GCP Cloud Run. It's a Django REST API built on Django Rest Framework. https://www.django-rest-framework.org/

----
*** Get current URL from Cloud Run ***
Last assigned URL: https://ctapi-z2o35wwlva-uc.a.run.app

----
## PIP Prerequisites:
Required Python packages are in requirements.txt file in the project root folder. Create a virtual python environment and install required packages:
```sh
python3 -m venv env
pip install -r requirements.txt
```
----
### Follow this guide for deployment to GCP Cloud Run:

[Django on Google Cloud Run. In this tutorial, we will create a… | by Rahul Sharma | Medium](https://medium.com/@rahulxsharma/django-on-google-cloud-run-3f2f93ae0917)
----
### Useful commands:
Migrations/Collect Static Files and create Admin site superuser account:
```bash
# for dev environment with GCP cloud SQL proxy connected to cloud db instance.
docker-compose up -d
docker-compose run --rm app sh -c "django-admin startproject app ." 
docker-compose run --rm app sh -c "python3 manage.py startapp <APP_NAME>"
----
Migrations/Collect Static Files and create Admin site superuser account:

*** ONLY RUN FOR INITIAL DB MIGRATION ***
docker-compose run --rm app sh -c "python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py collectstatic --no-input"
docker compose run --rm app sh -c "python manage.py createsuperuser --username=<DESIRED_USERNAME> --email=<YOUR EMAIL>"

*** ONLY RUN AFTER ADDING A NEW APP ***
docker-compose run --rm app sh -c "python manage.py makemigrations <APP_NAME>"

*** RUN after modifying Django models or other files: ***

docker-compose run --rm app sh -c "python manage.py makemigrations" )
docker-compose run --rm app sh -c "python manage.py migrate"
```
-----
## GCP and GIT specific notes:

#### To trigger a build/deploy on GPC:

Run from project root:
```bash
. build.sh 
```
----
#### When ready for deployment user docker-compose up -d to test migrations, etc.

#### Dev environment is connecting to the production GCP Cloud SQL instance.

----

The 'cloudbuild.yaml' file will run 'makemigrations', 'migrate, and 'collectstatic' commands during deployment to Cloud Run.

API is deployed on Cloud Run using GIT pushes from local repository to trigger GPC Cloud Build after code updates. 

Any updates to local repository will trigger rebuild once pushed to Github.

----

GS_BUCKET_NAME=django_dev_bucket

SQL connection for SQL_AUTH_PROXY: sodium-petal-335020:us-central1:django-dev-db

Get current URL from Cloud Run. Last known: https://ctapi-z2o35wwlva-uc.a.run.app
