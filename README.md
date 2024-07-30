# Serverless API

## Overview
The Serverless Movies API is a cloud-based application designed to provide movie information through a set of RESTful API endpoints. The project utilizes Google Cloud Platform (GCP) services, including Cloud Functions, Firestore, and Secret Manager, to create a serverless architecture. Additionally, it integrates OpenAI's API to generate movie summaries.

## Features
- **GetMovies**: Retrieve a list of all movies stored in the database.
- **GetMoviesByYear**: Retrieve a list of movies released in a specified year.
- **GetMovieSummary**: Generate and retrieve an AI-generated summary for a specified movie.

## Technologies Used
- **Google Cloud Platform (GCP)**
  - Cloud Functions
  - Firestore (NoSQL Database)
  - Secret Manager
- **Python**
  - Flask (for handling HTTP requests in cloud functions)
- **OpenAI API** (for generating movie summaries)
- **GitHub** (for version control and project documentation)

## Project Structure

Sure! Here's a sample README.md file for your Serverless Movies API project:

markdown
Copy code
# Serverless Movies API

## Overview
The Serverless Movies API is a cloud-based application designed to provide movie information through a set of RESTful API endpoints. The project utilizes Google Cloud Platform (GCP) services, including Cloud Functions, Firestore, and Secret Manager, to create a serverless architecture. Additionally, it integrates OpenAI's API to generate movie summaries.

## Features
- **GetMovies**: Retrieve a list of all movies stored in the database.
- **GetMoviesByYear**: Retrieve a list of movies released in a specified year.
- **GetMovieSummary**: Generate and retrieve an AI-generated summary for a specified movie.

## Technologies Used
- **Google Cloud Platform (GCP)**
  - Cloud Functions
  - Firestore (NoSQL Database)
  - Secret Manager
- **Python**
  - Flask (for handling HTTP requests in cloud functions)
- **OpenAI API** (for generating movie summaries)
- **GitHub** (for version control and project documentation)

## Project Structure
      serverless-api/
      ├── main.py
      ├── requirements.txt
      ├── README.md
      └── .env

### main.py
Contains the main logic for the API endpoints and the functions to interact with Firestore and OpenAI.

### requirements.txt
Lists the Python dependencies required for the project.

### README.md
Project documentation.

### .env
File for storing environment variables (not included in the repository for security reasons).

## Setup and Deployment

### Prerequisites
- Google Cloud SDK installed and configured.
- Python 3.9 or higher.
- Git installed.
