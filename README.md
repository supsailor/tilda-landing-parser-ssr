### About

Tilda SSR Service - application made on Python Django for fast implementation
of self hosted landings made on [Tilda](https://tilda.cc/) and easy management with
Django admin panel

This project is unrelated with Tilda develop team

API Integration that used in this project available only on business subscription plan

Admin pannel lives at `.../admin/`

API lives at `.../api/landingService`

### How to start

Setting application, database, redis and celery variables

Change variables at `Docker-compose.yaml`

| Key                | Value                                              |
| ------------------ | -------------------------------------------------- |
|Application                                                              |
| TILDA_PUBLIC_KEY   | Your tilda public key                              |
| TILDA_SECRET_KEY   | Your tilda secret key                              |
| DB_HOST            | Database hostname for connectivity                 |
| DB_NAME            | Name of database that this application uses        |
| DB_USER            | Database username for application authentication   |
| DB_PASS            | Database password for application authentication   |
|Postgres                                                                 |
| POSTGRES_NAME      | Auto-created by database database name             |
| POSTGRES_USER      | Auto-created by database user name                 |
| POSTGRES_PASSWORD  | Auto-created by database user password             |
|Celery                                                                   | 
| DB_HOST            | Database hostname for connectivity                 |
| DB_NAME            | Name of database that this application uses        |
| DB_USER            | Your tilda secret key                              |
| DB_PASS            | Your tilda secret key                              |

When all variables are set - just use `docker-compose up -d`

Dont forget to create superuser for admin pannel usage:

`docker exec -it {application_container_id} python manage.py createsuperuser`

### TODO:
- Make more usage description at readme.md





