## README.md

### by Alex Holyk

### Description:

This project serves as a brief use of ML for sentiment analysis, as a template or tutorial for applying ML in the FastAPI interface via a Docker container.

### Prerequisites
Docker and Python must be installed on the user's computer. Further libraries are listed in requirements.txt, but by following How to Run, these will be added loaded automatically. Postman is recommended for accessing the API, though not required.

### API Endpoints

- /health 
    method: `GET`
    A simple endpoint to confirm that the API is running.

- /predict
    method: `POST`
    Takes a text input and returns the predicted sentiment.

- /predict_proba
    method: `POST`
    Takes a text input and returns the predicted sentiment along with its confidence score.

- /example
    method: `GET`
    Returns a random review from the original IMDB training dataset. This is useful for testing the prediction endpoints.

### How to clone and run in Docker

- On command line, run: `git clone https://github.com/alexanderholyk/ML_with_FastAPI`

- Switch into the folder: `cd ML_with_FastAPI` or similar

- On command line, run: `make build` to build the image in Docker

- On command line, run: `make run` to run a container. This will show a Local URL; you can copy and paste this into the browser to load the API. Alternatively, after calling `make run` you can open Postman, choose your method and endpoint (e.g. http://127.0.0.1:8000/health), and test it that way. For endpoints with `GET` method, you can just click Send. For endpoints with `POST` method, click the Body tab, select raw, and enter a JSON (like {"text": "This movie was a masterpiece!"}) before clicking Send. At this point, you can also access the auto-generated FastAPI documentation at http://127.0.0.1:8000/docs.

- To terminate the program, on command line press `ctrl + c`. From your `make run` earlier, this will automatically close the container.

- Finally, to delete the image and keep your system clean, run `make clean`.




#### Note:

"IMDB Dataset.csv" came directly from the website: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews








### Full Assignment Text From MLOps Class

### Assignment 3 - FastAPI

## Objective: 

In this assignment, you will develop a dedicated API backend. You will wrap your sentiment analysis model (created in assignment 1) in an API using FastAPI. You will then containerize this backend with Docker and prepare it for deployment by pushing it to a GitHub repository.

## Prerequisites:

- You must have Docker installed and running on your machine.

- You must have a GitHub account and Git installed.

- You should start with the sentiment_model.pkl from Assignment 1 and the IMDB Dataset.csv file.

Due Date: 19th July, 2025

## Part 1: Building the FastAPI Application

Your primary task is to create a main.py file that serves your model. The API must provide four distinct endpoints.

### API Endpoints:

1) Health Check (/health)

    - Method: GET

    - Purpose: A simple endpoint to confirm that the API is running.

    - Response: A JSON object, e.g., {"status": "ok"}.

2) Predict Sentiment (/predict)

    - Method: POST

    - Purpose: Takes a text input and returns the predicted sentiment.

    - Request Body: A JSON object with a single key, text, e.g., {"text": "This movie was a masterpiece!"}.

    - Response: A JSON object with the predicted sentiment, e.g., {"sentiment": "positive"}.

3) Predict with Probability (/predict_proba)

    - Method: POST

    - Purpose: Takes a text input and returns the predicted sentiment along with its confidence score.

    - Request Body: Same as /predict.

    - Response: A JSON object with the sentiment and the probability, e.g., {"sentiment": "positive", "probability": 0.95}.

4) Get Training Example (/example)

    - Method: GET

    - Purpose: Returns a random review from the original IMDB training dataset. This is useful for testing the prediction endpoints.

    - Response: A JSON object with a random review, e.g., {"review": "I watched this with my kids and we all loved it."}.

**Tip**: Use Pydantic models to define the structure of your request bodies for robust data validation.

## Part 2: Packaging and Documentation
Once your FastAPI application is working locally, you will package it for distribution.

**Project Structure**: Your final repository should have the following structure:

.

├── .gitignore

├── Dockerfile

├── Makefile

├── README.md

├── main.py

├── requirements.txt

├── sentiment_model.pkl

└── IMDB Dataset.csv
 

The `README.md` should include the following details:

A description of the API and its endpoints.

Instructions on how to build and run the project locally using your `Makefile`.

A link to the auto-generated FastAPI documentation, which will be available at `/docs` once the server is running.

To work with Docker for this assignment, you can read the first few sections (until the section Check It) of this page from FastAPI's documentation: https://fastapi.tiangolo.com/deployment/docker Links to an external site.

Make sure that your APIs are running correctly by downloading Postman Desktop locally and testing with it. This is how I am going to grade your assignment as well.

## Part 3: Submission

1. Create a new public repository on GitHub. (Do not use the ones created for previous assignment)

2. Commit all your project files and push them to your GitHub repository.

3. Submit the URL to your public GitHub repository on this canvas page.