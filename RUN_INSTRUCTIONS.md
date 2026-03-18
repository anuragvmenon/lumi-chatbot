# How to Run Lumi: A Mental Health Chatbot

This guide will walk you through the steps to set up and run the Lumi chatbot on your local machine.

## 1. Prerequisites

Before you begin, ensure you have the following installed on your system:

*   **Python 3.8:** This project is compatible with Python 3.8. You can download it from the [official Python website](https://www.python.org/downloads/release/python-380/).

## 2. Setup

Follow these steps to set up your project environment:

### a. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage the project's dependencies. Open a terminal or command prompt in the `Lumi-A-Mental-Health-Chatbot-main` directory and run the following command to create a virtual environment named `.venv`:

```bash
python -m venv .venv
```

### b. Activate the Virtual Environment

Activate the virtual environment. The command to do this will vary depending on your operating system:

*   **Windows:**

    ```bash
    .venv\Scripts\activate
    ```

*   **macOS and Linux:**

    ```bash
    source .venv/bin/activate
    ```

### c. Install Dependencies

With your virtual environment activated, install the required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## 3. Running the Application

To run the chatbot, you will need to open three separate terminals or command prompts in the `Lumi-A-Mental-Health-Chatbot-main` directory and activate the virtual environment in each of them.

### a. Terminal 1: Run the Rasa Actions Server

In the first terminal, run the following command to start the Rasa actions server. This server runs the custom Python code in `actions.py`.

```bash
rasa run actions
```

### b. Terminal 2: Run the Rasa Server

In the second terminal, run the following command to start the Rasa server. This server handles the natural language understanding and dialogue management.

```bash
rasa run --enable-api
```

### c. Terminal 3: Run the Django Web Server

In the third terminal, navigate to the `lumi_web` directory and run the following command to start the Django development server. This server hosts the web interface for the chatbot.

```bash
cd lumi_web
python manage.py runserver
```

## 4. Accessing the Chatbot

Once all three servers are running, you can access the chatbot by opening your web browser and navigating to the following address:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

You should now see the modern and interactive Lumi chatbot interface. You can start a conversation by clicking the "Chat with Lumi" button.
