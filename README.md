# Cat Track API - GCP Cloud Run deployment version
## My Nucamp Back-end, SQL and DevOps with Python boot camp portfolio project.
----
### Cat Track API (ctapi) is a back-end Django REST API application to track cats, vets, fosters, and medications for a small cat rescue. 

#### This is my first attempt at Django REST API in Python with a Postgresql DB as the back end deployed on GCP Cloud Run. The is API built on [Django Rest Framework](https://www.django-rest-framework.org/)
----
#### [Insomnia](https://insomnia.rest/download) configuration included in project root. Import 'Insomnia_config.json' to [Insomnia](https://insomnia.rest/download) to test CRUD operations via GET , POST, PUT and DELETE POST 
----
*** Get current URL from Cloud Run ***
#### Last assigned URL: https://ctapi-z2o35wwlva-uc.a.run.app
----
## PIP Prerequisites:
Required Python packages are in requirements.txt file in the project root folder. Create a virtual python environment and install required packages:
```python
python3 -m venv env
pip install -r requirements.txt
```
----
### Follow this guide for deployment to GCP Cloud Run:

[Django on Google Cloud Run | by Rahul Sharma | Medium](https://medium.com/@rahulxsharma/django-on-google-cloud-run-3f2f93ae0917)
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
