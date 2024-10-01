# Gen Z Economy News

![Gen Z Economy News Screenshot](img/screenshot.jpeg)

Welcome to Gen Z Economy News—your go-to spot for market updates, but with a twist! This app grabs the latest market news, 
runs it through some slick web scraping and NLP magic, and serves it up in a fresh, Gen Z style. 
With an easy-to-use web interface, you’ll get all the key market insights, minus the boring jargon.
## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)

## Overview

This project consists of two main components:

1. **generate.py**: A script that scrapes news articles, processes them using a custom NLP model (Groq API), and stores them in a SQLite database.
2. **webpage.py**: A Streamlit application that displays the processed news articles to users in a user-friendly format.

## Features

- **Automated Web Scraping**: Scrapes news articles from an RSS feed.
- **NLP Processing**: Rewrites articles in Gen Z slang using Groq API.
- **Database Integration**: Stores processed articles in a SQLite database.
- **Web Interface**: Displays the articles in a user-friendly web application using Streamlit.

## Installation

To set up and run the project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_name>/src
2. **Install the required dependencies:
   Make sure you have Python installed (preferably Python 3.7 or above). Then, install the dependencies using:
   ```bash
   pip install -r requirements.txt
3. *** Add your Groq API Key:
   In generate.py, replace '******' with your actual Groq API key:
   ```python
   client = Groq(api_key='YOUR_API_KEY')
4. *** Run the code:
  To scrape and process news articles, run:
  To launch the web interface, run:
   ```bash
   python generate.py
   streamlit run webpage.py
  This will open a new tab in your browser displaying the web application.
## Requirements
Ensure you have the following installed:
- **Python 3.7 or higher
- **Groq API key for NLP processing
- **Other dependencies as listed in requirements.txt
## Contributing
Feel free to submit issues or pull requests if you have suggestions for improving the project.
