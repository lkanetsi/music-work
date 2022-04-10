# musical-work instructions

## Getting Started

First create vitruial env, setup django server and install dependencies:

```bash
cd backend/

python3 -m venv musicEnv

cd musicwork

pip install -r requirements.txt

```
Second setup a postgres database with following credentials:
- username: musicuser
- database: musicdb
- password: musicp@55
- run migrations/makemigrations

Third run django command to populate database with csv data:  
```bash

./manage.py load_csv works_metadata

./manage.py runserver

```

Open [http://localhost:8000/apiv1/](http://localhost:8000/apiv1) with your browser to see the rest api point for listing and filtering.


# Frontend instructions

```bash

cd frontend/musicalworks

npm install

npm run dev 
```

# Questions
## Part 1
1. I have chosen use  pandas library to load csv file as it provides the easier way of manipulating data, analysing and cleaning( removing duplicates with missing values and merging column data ) and iterated through rows to commit them to database using bulk_create method.

2. We can schedule django command for reconciling and commiting data to database using tools like celery / crons to trigger  when there is new data.


## Part 2 

1. I have already integrated django rest framework pagination to avoid large payloads which will impact response time 