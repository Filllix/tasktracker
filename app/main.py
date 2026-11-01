import os

import psycopg
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
DB_URL = os.getenv("DATABASE_URL")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    try:
        with psycopg.connect(DB_URL, autocommit=True, connect_timeout=2) as c:
            c.execute("SELECT 1")
    except psycopg.Error:
        return JSONResponse({"status": "not ready"}, status_code=503)
    return {"status": "ready"}


@app.get("/visits")
def visits():
    with psycopg.connect(DB_URL, autocommit=True) as c:
        c.execute("CREATE TABLE IF NOT EXISTS visits (id serial PRIMARY KEY, at timestamptz DEFAULT now())")
        c.execute("INSERT INTO visits DEFAULT VALUES")
        n = c.execute("SELECT COUNT(*) FROM visits").fetchone()[0]
    return {"visits": n}