<h1 align="center"> 
🍲  FastAPI Boilerplate
</h1>

<h2 align="center">
  The simplest production ready Django like FastAPI boilerplate 🐍
</h2>

<img src="https://github.com/rawheel/fastapi-boilerplate/blob/main/media/fastapi%20boilerplate%20cover.png" alt="fastapi boilerplate">

---

# 💎 Features

✅ Production ready with one docker-compose command. \
✅ Similar to Django Code Structure. \
✅ Local dockerized db.\
✅ Dockerized PgAdmin to check the db records.\
✅ Migrations, Serializers and ORM configured.\
✅ CRUD APIs (Sneaker App).\
✅ Token Authentication.\
✅ Logging Mechanism.\
✅ Testcases TDD with Pytest. \
✅ Seperate Database(Sqlite) and mock session configured for test cases.\
✅ Poetry dependency management and packaging made easy. (Better than pip)


# ⚒️ Techologies Used

- Alembic: For Database Migrations.
- SQLAlchemy: For ORM.
- Pydantic: For Typing or Serialization.
- Pytests: For TDD or Unit Testing.
- Poetry: Python dependency management and packaging made easy. (Better than pip)
- Docker & docker-compose : For Virtualization.
- postgresSQL: Database.
- PgAdmin: To interact with the Postgres database sessions.
- Loguru: Easiest logging ever done.

# 🚀 Up and run in 5 mins 🕙
Make sure you have docker and docker-compose installed [docker installation guide](https://docs.docker.com/compose/install/)
## Step 1
create **.env** file in root folder fastapi-boilerplate/.env
```
DATABASE_URL=postgresql+psycopg://postgres:password@db:5432/boiler_plate_db
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=boiler_plate_db 
PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin
X_TOKEN=12345678910
```

## Step 2
```
docker-compose up
```

# 🎉 Your Production Ready FastAPI CRUD backend app is up and running on `localhost:8000`

- Swagger docs on `localhost:8000/docs`
<img src="https://github.com/rawheel/fastapi-boilerplate/blob/main/media/swagger%20docs.png" alt="fastapi boilerplate">

- GET request example

<img src="https://github.com/rawheel/fastapi-boilerplate/blob/main/media/swagger%20get%20docs.png" alt="fastapi boilerplate">


- PgAdmin on `localhost:5050`

<img src="https://github.com/rawheel/fastapi-boilerplate/blob/main/media/pgadmin.png" alt="fastapi boilerplate">
