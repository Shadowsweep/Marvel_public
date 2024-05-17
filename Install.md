# Installation Guide

This guide will help you clone and set up the **Marvelverse** project on your local machine. Follow the steps below to get started.

## Prerequisites

Make sure you have the following installed on your machine:

- Python (version 3.6 or higher)
- Git
- Virtualenv (optional, but recommended)

## Step-by-Step Installation

### 1. Clone the Repository

First, clone the repository to your local machine using Git.

```bash
git clone https://github.com/Shadowsweep/Marvel_public.git
cd Marvel_public
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create a virtual environment to keep your project dependencies isolated.

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install the required dependencies from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Run the database migrations to set up the database schema.

```bash
python manage.py migrate
```

### 5. Run the Development Server

Start the Django development server to see the project in action.

```bash
python manage.py runserver
```

### 6. Open the Project

Open your web browser and go to `http://127.0.0.1:8000` to see the Marvelverse project running locally.



## Enjoy Exploring Marvelverse!

If you encounter any issues or have any questions, feel free to raise an issue on the [GitHub repository](https://github.com/Shadowsweep/Marvel_public).

---

Feel free to explore, enjoy, and share your feedback. Excelsior! 🌟
