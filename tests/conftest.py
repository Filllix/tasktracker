import os
from pathlib import Path


def _set_database_url():
    if os.getenv("DATABASE_URL"):
        return  # sudah diberikan dari luar (misalnya CI), jangan ditimpa

    env_file = Path(__file__).resolve().parent.parent / ".env"
    if not env_file.exists():
        return

    values = {}
    for line in env_file.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip()

    user = values.get("POSTGRES_USER", "app")
    password = values.get("POSTGRES_PASSWORD", "")
    db = values.get("POSTGRES_DB", "appdb")
    os.environ["DATABASE_URL"] = (
        f"postgresql://{user}:{password}@127.0.0.1:5432/{db}?connect_timeout=5"
    )


_set_database_url()