## README.md

### by Alex Holyk

### Description:

This project serves as a brief use of ML for sentiment analysis, as a template or tutorial for applying ML in the streamlit interface via a Docker container.

### Prerequisites
Docker and Python must be installed on the user's computer. Further libraries are listed in requirements.txt, but by following How to Run, these will be added loaded automatically.

### How to clone and run in Docker

- On command line, run: `git clone https://github.com/alexanderholyk/ML_in_Streamlit`

- Switch into the folder: `cd ML_in_Streamlit` or similar

- On command line, run: `make build` to build the image in Docker

- On command line, run: `make run` to run a container. This will show a Local URL; copy and paste this into the brower to load the streamlit app.

- In text box, type a movie review to test. Follow the onscreen instructions to submit it. Then click the button `Analyze` to see the result! You can close the brower window or keep trying new reviews as desired.

- To terminate the program, on command line press `ctrl + c`. From your `make run` earlier, this will automatically close the container.

- Finally, to delete the image and keep your system clean, run `make clean`.

### How to clone and run via a virtual environment

- On command line, run: `git clone https://github.com/alexanderholyk/ML_in_Streamlit`

- Switch into the folder: `cd ML_in_Streamlit` or similar

- Optional: create a virtual environment: `python3 -m venv .venv` and then activate it with `source .venv/bin/activate`

- On command line, run: `pip install -r requirements.txt`

- On command line, run: `streamlit run app.py` This opens a browser window where the app will open.

- In text box, type a movie review to test. Follow the onscreen instructions to submit it. Then click the button `Analyze` to see the result!


#### Note:

"IMDB Dataset.csv" came directly from the website: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews








### Full Assignment Text From MLOps Class

### Assignment 1 - Streamlit App

## Homework Assignment: Building a Sentiment Analysis Web App with Streamlit

Objective: The goal of this assignment is to build a complete, end-to-end machine learning application. You will train a sentiment analysis model on movie review data, save it, and then build an interactive web app with Streamlit that allows a user to input any text and see the predicted sentiment. I have included sufficient hints and comments to assist you with completing this assignment easily. Feel free to email/Discord if you face any confusion.

**Due Date**: Thursday, 26th June. 11.59 pm MT

## Part 1: Data Preparation and Model Training

In this part, you will prepare the data, train a Naive Bayes classifier, and save the trained model pipeline.

#### Step 1: Get the Data

We will use the Large Movie Review Dataset (IMDB). For simplicity, you can use a pre-processed version available on Kaggle.

- Dataset: IMDB Dataset of 50K Movie Reviews

- Download the IMDB Dataset.csv file from the link above and place it in your project folder.

#### Step 2: Create a Training Script

Create a Python script named train_model.py. This script will be responsible for loading the data, training the model, and saving it.

#### Step 3: Load and Preprocess the Data

- Use pandas to load the IMDB Dataset.csv file.

- The dataset has two columns: review and sentiment. The sentiment is already conveniently labeled as positive or negative.

- You will need to split your data into features (the review text) and labels (the sentiment). Let's call them X and y.

#### Step 4: Train the Model

For this task, a combination of TfidfVectorizer and MultinomialNB (Naive Bayes) is a strong and classic baseline. To make the model easy to use in, package them together in a Pipeline.

- Import Pipeline from sklearn.pipeline, TfidfVectorizer from sklearn.feature_extraction.text, and MultinomialNB from sklearn.naive_bayes.

- Create a pipeline that first transforms the text data using TfidfVectorizer and then feeds it to the MultinomialNB classifier.

- Train the pipeline on your entire dataset (X and y). No need to create a train-test split for this assignment

#### Step 5: Save the Model Pipeline

- Once the model is trained, you need to save it to a file so your Streamlit app can use it later.

- Use the joblib library to dump your trained Pipeline object into a file named sentiment_model.pkl.

Your train_model.py script should only be run once to generate the sentiment_model.pkl file.

## Part 2: Building the Streamlit Application

Now for the fun part! You will create a web interface for your model.

#### Step 1: Create the App Script

Create a new Python script named app.py.

#### Step 2: Set up the Basic App Layout

- Import streamlit and joblib.

- Give your application a title, for example: Movie Review Sentiment Analyzer.

- Write a short description of what the app does.

#### Step 3: Load the Saved Model

- Write a function to load sentiment_model.pkl using joblib.load().

- **Crucially, use the @st.cache_data decorator on this function (review Lab 1.5).** This ensures the model is loaded only once when the app starts, which is essential for performance.

#### Step 4: Create the User Input Interface

- Use st.text_area() to create a text box where the user can type or paste a movie review. Give it a descriptive label like "Enter a movie review to analyze:".

- Add a button with st.button() labeled "Analyze".

#### Step 5: Make Predictions and Display Results

- Write an if block that checks if the "Analyze" button has been pressed.

- Inside the if block:

    1. Get the text from the text area.

    2. Make sure the user has entered some text before trying to make a prediction.

    3. Use your loaded model pipeline's .predict() method on the user's text. Note that the pipeline expects a list or array of documents, so you'll need to pass the input text inside a list (e.g., [user_text]).

    4. The output will be the predicted sentiment ('positive' or 'negative').

    5. Display the result to the user in a clear way. Use st.subheader() or st.write() to show the prediction.

    6. Display the prediction probability using the model's .predict_proba() method.

    - Pro-tip: Make the output more engaging! If the sentiment is positive, you could write "Predicted Sentiment: Positive 👍" and if it's negative, "Predicted Sentiment: Negative 👎".

#### Step 6: Run Your App

Open your terminal in the project directory and run:

streamlit run app.py

Test your app with different reviews to see if it works as expected.

## Submission Guidelines
To receive full grade, you must push all the files on a GitHub repository (make sure it's public or add my email if you want to keep it private: rahimrasool17@gmail.com).

You only have to add the GitHub URL when submitting the assignment. You can work in pairs; however, make sure to submit your work individually in separate accounts and repositories.

Ensure to include the following files:

1. train_model.py (your model training script)

2. app.py (your Streamlit application script)

3. sentiment_model.pkl (the saved model file)

4. A requirements.txt file listing the libraries needed to run your project (e.g., streamlit, pandas, scikit-learn, joblib).

5. A README file with a simple paragraph on how to clone and run your app locally. Preferably, write it in bullet points.


## Bonus Points (Optional)
For extra credit, you can add one or more of the following features:

Display the prediction probability using the model's .predict_proba() method.
Style the output with color. For example, show positive predictions in green and negative predictions in red. (Hint: st.success() and st.error())


### And for the second part, where we add Docker:

#### Homework Assignment: Packaging Your Streamlit App with Docker

Objective: The goal of this assignment is to take the sentiment analysis application you built in Assignment 1 and package it into a standard, reproducible container using Docker. This is a foundational skill for deploying machine learning models in a real-world production environment as mentioned in class. You must have Docker installed and running on your machine for this assignment.

Due Date: Thursday, 3rd July. 11.59 pm MT

#### Tasks & Project Structure

You will create several new files to containerize your application. When you are finished, your project folder should look like this:

.

├── .gitignore

├── Dockerfile

├── Makefile

├── README.md

├── app.py

├── requirements.txt

└── model.pkl
 

**Step 1: Create a .gitignore file**

- This file tells Git which files or folders to ignore.

- Create a .gitignore file and add entries for common Python artifacts (e.g., __pycache__/, .pyc) and any local environment files (e.g., *.env).

**Step 2: Create a Dockerfile**

- This is the blueprint for building your Docker image.

- Your Dockerfile must perform the following steps:

    1. Start from an official Python base image (e.g., python:3.9-slim).

    2. Set a working directory inside the container (e.g., /app).

    3. Copy the requirements.txt file into the container.

    4. Install the Python dependencies using pip.

    5. Copy the rest of your application files (app.py) into the container.

    6. Expose the port that Streamlit runs on (default is 8501).

    7. Define the command (CMD) to run the Streamlit app when the container starts.

**Step 3: Create a Makefile**

- A Makefile simplifies complex Docker commands into simple ones. This is a common practice in many development teams.

- Your Makefile should provide at least three commands:

    - build: This command should build the Docker image and give it a name (e.g., sentiment-app).

    - run: This command should run a container from your image, mapping the container's port to a port on your local machine so you can access the app in your browser.

    - clean: This command should delete the image.

**Step 4: Create a README.md file**

- This is the instruction manual for your project.

- Your README.md must include:

    1. A brief description of the project.

    2. A "Prerequisites" section listing what a user needs to run it (i.e., Docker).

    3. A "How to Run" section with clear, step-by-step instructions on how to use your Makefile to build and run the application. It should tell the user what URL to visit in their browser (e.g., http://localhost:8501).

 

#### Submission Guidelines

To receive full grade, you must push all the files to the GitHub repository you create for Assignment 1 (make sure it's public or add my email if you want to keep it private: rahimrasool17@gmail.com).

You only have to add the GitHub URL when submitting the assignment. This is a solo assignment so you should not pair up for this specific assignment. However, you are not restricted to seek help or get support from each other.

The most important aspect of this assignment is reproducibility. Therefore, before submitting, please test running the app on the container in a new computer or environment to ensure it's working correctly. The bottom-line is that when I clone your repos, I should be able to smoothly run the app with simple make commands and easy-to-follow README.