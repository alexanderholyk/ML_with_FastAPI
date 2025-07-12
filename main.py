# main.py
# Alex Holyk

from fastapi import FastAPI

app = FastAPI(title="My ML API", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Can now run in terminal: uvicorn main:app --reload
# This command starts the FastAPI application using Uvicorn, with auto-reload enabled.
# You can access the application at http://127.0.0.1:8000
# It will show "Hello World" in JSON format when you visit the root URL.

# In terminal, you can access endpoints at http://127.0.0.1:8000/health and http://127.0.0.1:8000/docs