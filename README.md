# Testing Alembic

## Getting setup

1. install requirements
2. create .env file with DB connection e.g. `DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/alembic`
3. Run `alembic upgrade head` to install the latest changes
4. Make a change to a model in `main.py`
5. Run `alembic revision --autogenerate -m "upgrade description here"`
6. Run `alembic upgrade head` to install that revision.

## TODO

- Add CI pipeline to run alembic
- Add CI pipeline to check for Model changes that have no version file
