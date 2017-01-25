# qualitative-coding-tool

# Usage

## Try the demo
This application is deployed at [here](https://shujinwu.pythonanywhere.com/admin/)

## Run Locally

+ Run `python manage.py migrate`
+ Run `python manage.py loaddata 001_009.json` to load data if needed
+ Run `python manage.py createsuperuser` to create a user for the Django admin site
+ Run `python manage.py runserver`
+ Go to `http://localhost:8000/admin`

## Docker

```bash
# Step 1: Build docker image
docker build --tag="codingtool" .

# Step 2: Bring up the container
docker run --name=codingtool --publish 8000:8000 codingtool

# Step 3: Create superuser for the Django admin site
>>> docker exec -it [container_id] bash
root@e5bc628543d8:/tool/qualitative_coding_tool# python manage.py createsuperuser

# Step 4: Access the admin site at: http://localhost:8000/admin using the username/password that you set in previous step
```
