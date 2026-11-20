# DevOps Practical

A minimal Flask application that serves a versioned greeting.

`GET /` returns `Hello, DevOps World! V1`. The server listens on `0.0.0.0` and uses the `PORT` environment variable, defaulting to `5000`.

## Run the application

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Run the tests

```bash
pytest
```
