# Makefile for Dockerized Sentiment Analysis in FastAPI App

# Define variables for the image name and tag
IMAGE_NAME := sentiment_analysis_fastapi

build:
	@echo "Building Docker image: $(IMAGE_NAME)"
	docker build -t $(IMAGE_NAME) .

run:
	@echo "Running Docker container..."
	docker run --rm -p 8000:80 $(IMAGE_NAME)

clean:
	@echo "Removing Docker image: $(IMAGE_NAME)"
	docker rmi $(IMAGE_NAME) || true