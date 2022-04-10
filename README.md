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


# Frontend instruction

```bash

cd frontend/musicalworks

npm install

npm run dev 
```