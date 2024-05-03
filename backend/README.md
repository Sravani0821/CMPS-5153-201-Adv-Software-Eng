# Backend

## Setup

1. Create a virtual environment

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment

   ```bash
   # For Windows
   .venv\Scripts\activate

   # For Linux
   source .venv/bin/activate
   ```

3. Install the dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Make the migrations

   ```bash
   python manage.py makemigrations
   ```

5. Apply the migrations

   ```bash
   python manage.py migrate
   ```

6. Create a superuser

   ```bash
   python manage.py createsuperuser
   ```

## Run the server

1. Activate the virtual environment

   ```bash
   # For Windows
   .venv\Scripts\activate

   # For Linux
   source .venv/bin/activate
   ```

2. Run the server

   ```bash
   python manage.py runserver
   ```
