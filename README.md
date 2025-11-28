# AI-Powered-Cold-Email-Generator-Job-Client-Outreach-
Generate personalized cold emails for job applications, sales, or client pitches — using generative LLMs and user input.
- [Project Overview](#project-overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Acknowledgements](#acknowledgements)


## Project Overview

This project is a simple and effective tool that generates professional cold emails using AI. The Streamlit interface collects user input and the backend uses Groq’s LLaMA 3 model to craft a polished, ready-to-use email.

It helps job seekers, students, and freelancers create clear outreach messages quickly.

---

## Features

Clean, modern homepage

AI-generated cold emails

Skill-based customization

Fast response from Groq API

## How It Works

User enters job details.

A custom prompt is generated.

The prompt is sent to the LLaMA 3 model via Groq API.

AI returns a complete cold email.

Email is shown instantly on screen.

---

## Project Structure

---

<img width="320" height="200" alt="image" src="https://github.com/user-attachments/assets/c5440af2-03f9-45f1-9418-7994567e3f42" />

---

## Installation

**Clone the repo:**

git clone https://github.com/your-username/AI-Cold-Email-Generator.git

cd AI-Cold-Email-Generator

**Install dependencies:**

pip install -r requirements.txt

---

## Usage

Run the application:

streamlit run Notebooks/Home.py

**Steps:**

Open the app in your browser.

Enter job title, company name, and skills.

Click Generate Email.

Copy the generated email and use it anywhere.

---

## Configuration

Set your Groq API key inside llama_email.py:

GROQ_API_KEY = "your_api_key_here"

## Technologies Used

Python

Streamlit

Groq API (LLaMA 3 model)

Requests library

HTML/CSS styling

## Future Enhancements

Automatic resume parsing

Email tone selector

Multi-template email styles

Export email as PDF

Save email history

---

## License

This project is licensed under the MIT License.

You are free to modify and use it with attribution.


## Acknowledgements

Thanks to Groq for their fast API and to Streamlit for making UI development simple.
