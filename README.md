AI-Powered Cold Email Generator – Job & Client Outreach

A lightweight AI-based tool that helps users create clear and personalized cold emails for job applications, client outreach, or sales communication.
The system uses an LLM backend and custom user inputs to produce polished, ready-to-send messages within seconds.

🔍 What This Project Does

Generates refined outreach emails using AI

Accepts job details, skills, or client information

Produces concise, professional messages tailored to each user

Runs through a simple interactive Streamlit interface

Ensures fast generation with modern LLMs

⚡ Key Highlights

User-friendly interface: No technical knowledge required

Adaptive email tone: Outputs clear and professional emails

Fast API processing: Powered by Groq / LLaMA backend

Beginner-friendly setup: Simple Python environment

Easily customizable: Modify prompts or email style

🧠 How the System Works

User provides input (job role, skills, target company, or client info).

Backend formats a structured prompt.

Prompt is sent to the LLM model using the Groq API.

Model returns a completed email draft.

Email is displayed instantly inside Streamlit.

📂 Project Layout
AI-Powered-Cold-Email-Generator-Job-Client-Outreach
│
├── Notebook/
│   ├── Home.py             # Streamlit UI
│   └── llama_email.py      # LLaMA / Groq email generator
│
├── References/
│   └── overview.pdf        # Project reference material
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── LICENSE                 # MIT License

🛠 Setup & Installation

Clone the repository:

git clone https://github.com/engrsabakhan/AI-Powered-Cold-Email-Generator-Job-Client-Outreach.git
cd AI-Powered-Cold-Email-Generator-Job-Client-Outreach


Install requirements:

pip install -r requirements.txt

▶️ Run the Application

Use Streamlit to launch the interface:

streamlit run Notebook/Home.py

Steps:

Enter job or client details

Provide relevant skills or background

Click Generate Email

Copy your AI-created email and use instantly

🔧 API Configuration

Inside Notebook/llama_email.py, add your Groq API key:

GROQ_API_KEY = "your_api_key_here"

🧰 Built With

Python

Streamlit

Groq API / LLaMA Model

Requests

Custom Prompt Engineering

🚀 Planned Improvements

Multiple email styles (short, formal, casual)

Auto-detection of tone from user preference

Resume or portfolio text extraction

Export email as PDF or Word

Saved email history inside the app

📄 License

This project is released under the MIT License, allowing free use and modification.
